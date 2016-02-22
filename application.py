from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Artist, Album, User
from flask import session as login_session
import random, string

# Imports for OAuth Validation
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

# Connect to Database and create database session
engine = create_engine('sqlite:///musiccollection.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

CLIENT_ID = json.loads(
	open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Music Collection App"


# Create anti-forgery state token
@app.route('/login')
def showLogin():
	state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
	login_session['state'] = state
	# return "The current session state is %s" % login_session['state']
	return render_template('login.html', STATE=state)

##### Start Google Plus Connect and Disconect Code #####

# Google connect code
@app.route('/gconnect', methods=['POST'])
def gconnect():
	# Validate state token
	if request.args.get('state') != login_session['state']:
		response = make_response(json.dumps('Invalid state parameter.'), 401)
		response.headers['Content-Type'] = 'application/json'
		return response
	# Obtain authorization code
	code = request.data

	try:
		# Upgrade the authorization code into a credentials object
		oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
		oauth_flow.redirect_uri = 'postmessage'
		credentials = oauth_flow.step2_exchange(code)
	except FlowExchangeError:
		response = make_response(
		json.dumps('Failed to upgrade the authorization code.'), 401)
		response.headers['Content-Type'] = 'application/json'
		return response

	# Check that the access token is valid.
	access_token = credentials.access_token
	url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
		% access_token)
	h = httplib2.Http()
	result = json.loads(h.request(url, 'GET')[1])
	# If there was an error in the access token info, abort.
	if result.get('error') is not None:
		response = make_response(json.dumps(result.get('error')), 500)
		response.headers['Content-Type'] = 'application/json'

	# Verify that the access token is used for the intended user.
	gplus_id = credentials.id_token['sub']
	if result['user_id'] != gplus_id:
		response = make_response(
		json.dumps("Token's user ID doesn't match given user ID."), 401)
		response.headers['Content-Type'] = 'application/json'
		return response

	# Verify that the access token is valid for this app.
	if result['issued_to'] != CLIENT_ID:
		response = make_response(
		json.dumps("Token's client ID does not match app's."), 401)
		print "Token's client ID does not match app's."
		response.headers['Content-Type'] = 'application/json'
		return response

	stored_credentials = login_session.get('credentials')
	stored_gplus_id = login_session.get('gplus_id')
	if stored_credentials is not None and gplus_id == stored_gplus_id:
		response = make_response(json.dumps('Current user is already connected.'), 200)
		response.headers['Content-Type'] = 'application/json'
		return response

	# Store the access token in the session for later use.
	login_session['credentials'] = credentials.access_token
	login_session['gplus_id'] = gplus_id

	# Get user info
	userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
	params = {'access_token': credentials.access_token, 'alt': 'json'}
	answer = requests.get(userinfo_url, params=params)

	data = answer.json()

	login_session['username'] = data['name']
	login_session['picture'] = data['picture']
	login_session['email'] = data['email']
	# ADD PROVIDER TO LOGIN SESSION
	login_session['provider'] = 'google'

	# see if user exists, if it doesn't make a new one
	user_id = getUserID(data["email"])
	if not user_id:
		user_id = createUser(login_session)
	login_session['user_id'] = user_id

	output = ''
	output += '<h1>Welcome, '
	output += login_session['username']
	output += '!</h1>'
	output += '<img src="'
	output += login_session['picture']
	output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
	flash("You are now logged in as %s" % login_session['username'])
	print "done!"
	return output

# User Helper Functions

def createUser(login_session):
	newUser = User(name=login_session['username'], email=login_session[
		'email'], picture=login_session['picture'])
	session.add(newUser)
	session.commit()
	user = session.query(User).filter_by(email=login_session['email']).one()
	return user.id


def getUserInfo(user_id):
	user = session.query(User).filter_by(id=user_id).one()
	return user


def getUserID(email):
	try:
		user = session.query(User).filter_by(email=email).one()
		return user.id
	except:
		return None

# Google Plus Diconnect Code
@app.route('/gdisconnect')
def gdisconnect():
	# Only disconnect a connected user
	credentials = login_session.get('credentials.to_json()')
	print credentials
	if credentials is None:
		response = make_response(
			json.dumps('Current user not connected.'), 401)
		response.headers['Content-Type'] = 'application/json'
		return response
	access_token = credentials.access_token
	url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
	h = httplib2.Http()
	result = h.request(url, 'GET')[0]
	if result['status'] != '200':
		# If given token was invalid
		response = make_response(
		json.dumps('Failed to revoke token for given user.', 400))
		response.headers['Content-Type'] = 'application/json'
		return response

##### End Google Plus Connect and Disconnect Code #####

##### Facebook Connect and Disconnect Code #####
@app.route('/fbconnect', methods=['POST'])
def fbconnect():
	if request.args.get('state') != login_session['state']:
		response = make_response(json.dumps('Invalid state parameter.'), 401)
		response.headers['Content-Type'] = 'application/json'
		return response
	access_token = request.data
	print "access token received %s " % access_token

	app_id = json.loads(open('fb_client_secrets.json', 'r').read())[
		'web']['app_id']
	app_secret = json.loads(
		open('fb_client_secrets.json', 'r').read())['web']['app_secret']
	url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=%s&client_secret=%s&fb_exchange_token=%s' % (
		app_id, app_secret, access_token)
	h = httplib2.Http()
	result = h.request(url, 'GET')[1]

	# Use token to get user info from API
	userinfo_url = "https://graph.facebook.com/v2.4/me"
	# strip expire tag from access token
	token = result.split("&")[0]


	url = 'https://graph.facebook.com/v2.4/me?%s&fields=name,id,email' % token
	h = httplib2.Http()
	result = h.request(url, 'GET')[1]
	# print "url sent for API access:%s"% url
	# print "API JSON result: %s" % result
	data = json.loads(result)
	login_session['provider'] = 'facebook'
	login_session['username'] = data["name"]
	login_session['email'] = data["email"]
	login_session['facebook_id'] = data["id"]

	# The token must be stored in the login_session in order to properly logout, let's strip out the information before the equals sign in our token
	stored_token = token.split("=")[1]
	login_session['access_token'] = stored_token

	# Get user picture
	url = 'https://graph.facebook.com/v2.4/me/picture?%s&redirect=0&height=200&width=200' % token
	h = httplib2.Http()
	result = h.request(url, 'GET')[1]
	data = json.loads(result)

	login_session['picture'] = data["data"]["url"]

	# see if user exists
	user_id = getUserID(login_session['email'])
	if not user_id:
		user_id = createUser(login_session)
	login_session['user_id'] = user_id

	output = ''
	output += '<h1>Welcome, '
	output += login_session['username']

	output += '!</h1>'
	output += '<img src="'
	output += login_session['picture']
	output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '

	flash("You are now logged in as %s." % login_session['username'])
	return output


@app.route('/fbdisconnect')
def fbdisconnect():
	facebook_id = login_session['facebook_id']
	# The access token must me included to successfully logout
	access_token = login_session['access_token']
	url = 'https://graph.facebook.com/%s/permissions?access_token=%s' % (facebook_id,access_token)
	h = httplib2.Http()
	result = h.request(url, 'DELETE')[1]
	return "You have been logged out."

##### End FB Connect and Disconnect Code #####

# Disconnect based on provider
@app.route('/disconnect')
def disconnect():
	if 'provider' in login_session:
		if login_session['provider'] == 'google':
			gdisconnect()
			del login_session['gplus_id']
			del login_session['credentials']
		if login_session['provider'] == 'facebook':
			fbdisconnect()
			del login_session['facebook_id']
		del login_session['username']
		del login_session['email']
		del login_session['picture']
		del login_session['user_id']
		del login_session['provider']
		flash("You have successfully been logged out.")
		return redirect(url_for('showAllArtists'))
	else:
		flash("You were not logged in!")
		return redirect(url_for('showAllArtists'))

# JSON APIs to view Artist Information
@app.route('/artists/JSON')
def showAllArtistsJSON():
	artists = session.query(Artist).all()
	return jsonify(artists = [artist.serialize for artist in artists])

@app.route('/artists/<int:artist_id>/albums/JSON')
def showAlbumsJSON(artist_id):
	artist = session.query(Artist).filter_by(id = artist_id).one()
	albums = session.query(Album).filter_by(artist_id = artist_id).all()
	return jsonify(albums = [album.serialize for album in albums])

@app.route('/artists/<int:artist_id>/albums/<int:album_id>/JSON')
def showAlbumInfoJSON(artist_id, album_id):
	album = session.query(Album).filter_by(id = album_id).one()
	return jsonify(album = album.serialize)

# Show all artists
@app.route('/')
@app.route('/artists')
def showAllArtists():
	artists = session.query(Artist).order_by(asc(Artist.name))
	if 'username' not in login_session:
		return render_template('publicartists.html', artists = artists)
	return render_template('artists.html', artists = artists)

# Add a New Artist
@app.route('/artists/new', methods = ['GET', 'POST'])
def addNewArtist():
	if 'username' not in login_session:
		return redirect('/login')
	if request.method == 'POST':
		newArtist = Artist(name = request.form['name'], picture = request.form['picture'],
			user_id = login_session['user_id'])
		session.add(newArtist)
		session.commit()
		flash('New Artist %s Successfully Created' % newArtist.name)
		return redirect(url_for('showAllArtists'))
	return render_template('newartist.html')

# Show an Artist's Albums
@app.route('/artists/<int:artist_id>/albums')
@app.route('/artists/<int:artist_id>/')
def showAlbums(artist_id):
	artist = session.query(Artist).filter_by(id = artist_id).one()
	creator = getUserInfo(artist.user_id)
	albums = session.query(Album).filter_by(artist_id = artist_id).order_by(asc(Album.year_released)).all()
	if 'username' not in login_session or creator.id != login_session['user_id']:
		return render_template('publicalbums.html', artist = artist, albums = albums, creator = creator)
	return render_template('albums.html', artist = artist, albums = albums, creator = creator)

# Edit an Artist
@app.route('/artists/<int:artist_id>/edit', methods = ['GET', 'POST'])
def editArtist(artist_id):
	artistToEdit = session.query(Artist).filter_by(id = artist_id).one()
	if 'username' not in login_session:
		return redirect('/login')
	if artistToEdit.user_id != login_session['user_id']:
		return "<script>function myFunction() {alert('You are not authorized to edit this artist. \
			Please add your own artist in order to edit.');}</script><body onload='myFunction()''>"
	if request.method == 'POST':
		if request.form['name']:
			artistToEdit.name = request.form['name']
		if request.form['picture']:
			artistToEdit.picture = request.form['picture']
		flash('%s Successfully Edited' % artistToEdit.name)
		return redirect(url_for('showAllArtists'))
	return render_template('editartist.html', artist = artistToEdit)

# Delete an Artist
@app.route('/artists/<int:artist_id>/delete', methods = ['GET', 'POST'])
def deleteArtist(artist_id):
	artistToDelete = session.query(Artist).filter_by(id = artist_id).one()
	if 'username' not in login_session:
		return redirect('/login')
	if artistToDelete.user_id != login_session['user_id']:
		return "<script>function myFunction() {alert('You are not authorized to delete this artist. \
		Please add your own artist in order to delete.');}</script><body onload='myFunction()''>"
	if request.method == 'POST':
		session.delete(artistToDelete)
		session.commit()
		flash('%s Successfully Deleted' % artistToDelete.name)
		return redirect(url_for('showAllArtists'))
	return render_template('deleteartist.html', artist = artistToDelete)

# Show Detailed Album Info
@app.route('/artists/<int:artist_id>/albums/<int:album_id>/info')
def showAlbumInfo(artist_id, album_id):
	artist = session.query(Artist).filter_by(id=artist_id).one()
	creator = getUserInfo(artist.user_id)
	album = session.query(Album).filter_by(id=album_id).one()
	if 'username' not in login_session or creator.id != login_session['user_id']:
		return render_template('publicalbuminfo.html', artist = artist, album = album)
	return render_template('albuminfo.html', artist = artist, album = album)

# Add a New Album
@app.route('/artists/<int:artist_id>/albums/new', methods = ['GET', 'POST'])
def addNewAlbum(artist_id):
	if 'username' not in login_session:
		return redirect('/login')
	artist = session.query(Artist).filter_by(id=artist_id).one()
	if artist.user_id != login_session['user_id']:
		return "<script>function myFunction() {alert('You are not authorized to add albums to this artist. \
			Please add your own artist in order to add albums.');}</script><body onload='myFunction()''>"
	if request.method == 'POST':
		newAlbum = Album(name = request.form['name'], description = request.form['description'], 
			year_released = request.form['year_released'], artist_id = artist.id,
			user_id = login_session['user_id'])
		session.add(newAlbum)
		session.commit()
		flash('New Album %s Successfully Added to %s' % (newAlbum.name, artist.name))
		return redirect(url_for('showAlbums', artist_id = artist.id))
	return render_template('newalbum.html', artist= artist)

# Edit an Album
@app.route('/artists/<int:artist_id>/albums/<int:album_id>/edit', methods = ['GET', 'POST'])
def editAlbum(artist_id, album_id):
	albumToEdit = session.query(Album).filter_by(id = album_id).one()
	if 'username' not in login_session:
		return redirect('/login')
	if albumToEdit.user_id != login_session['user_id']:
		return "<script>function myFunction() {alert('You are not authorized to edit albums of this artist. \
			Please add your own artist in order to edit albums.');}</script><body onload='myFunction()''>"
	if request.method == 'POST':
		if request.form['name']:
			albumToEdit.name = request.form['name']
		if request.form['description']:
			albumToEdit.description = request.form['description']
		if request.form['year_released']:
			albumToEdit.year_released = request.form['year_released']
		if request.form['picture']:
			albumToEdit.picture = request.form['picture']
		session.add(albumToEdit)
		session.commit()
		flash('%s Sucessfully Edited' % albumToEdit.name)
		return redirect(url_for('showAlbums', artist_id = artist_id))
	else:
		return render_template('editalbum.html', artist_id = artist_id, album = albumToEdit)

# Delete an Album
@app.route('/artists/<int:artist_id>/albums/<int:album_id>/delete', methods = ['GET', 'POST'])
def deleteAlbum(artist_id, album_id):
	albumToDelete = session.query(Album).filter_by(id = album_id).one()
	if 'username' not in login_session:
		return redirect('/login')
	if albumToDelete.user_id != login_session['user_id']:
		return "<script>function myFunction() {alert('You are not authorized to delete albums of this artist. \
			Please add your own artist in order to delete albums.');}</script><body onload='myFunction()''>"
	if request.method == 'POST':
		session.delete(albumToDelete)
		session.commit()
		flash('%s Successfully Deleted' % albumToDelete.name)
		return redirect(url_for('showAlbums', artist_id = artist_id))
	return render_template('deletealbum.html', artist_id = artist_id, album = albumToDelete)


if __name__ == '__main__':
	app.secret_key = 'super_secret_key'
	app.debug = True
	app.run(host = '0.0.0.0', port = 8000)