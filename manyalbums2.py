from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Artist, Album, User

engine = create_engine('sqlite:///musiccollection.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

# Create dummy user
user1 = User(name="Yana Kesala", email="yana.kesala@gmail.com", id = 1)
session.add(user1)
session.commit()

user2 = User(name='Radiant Moxie', email = 'radiant.moxie@gmail.com', id = 2)
session.add(user2)
session.commit()

#Albums for Sting
artist1 = Artist(user_id=1, name = 'Sting', picture = '/static/Sting.jpg')

session.add(artist1)
session.commit()

album1 = Album(name = 'Brand New Day', description = \
	"From AllMusic.com:\
	By the late '90s, Sting had reached a point where he didn't have to prove \
	his worth every time out; \
	he had so ingrained himself in pop culture, he really had the freedom to \
	do whatever he wanted.", 
	year_released = 1999, artist = artist1, picture = '/static/BrandNewDay.jpg',
	user_id = 1)

session.add(album1)
session.commit()

album2 = Album(name = 'The Dream of the Blue Turtles', description = \
	"From AllMusic.com:\
	Sting had a lot to prove on his first post-Police effort, and he proved \
	himself up to the task of \
	establishing a distinctive identity as a solo artist.", 
	year_released = 1985, artist = artist1, 
	picture = '/static/DreamTurtles.jpg', user_id = 1)

session.add(album2)
session.commit()

album3 = Album(name = 'Nothing Like the Sun', description = \
	"From AllMusic.com:\
	If Dream of the Blue Turtles was an unabashedly pretentious affair, it \
	looks positively lighthearted \
	in comparison to Sting's sophomore effort, Nothing Like the Sun, one of \
	the most doggedly serious pop \
	albums ever recorded.", year_released =1987, 
	artist = artist1, picture = '/static/NothingSun.jpg', user_id = 1)

session.add(album3)
session.commit()

#Albums for Gwen Stefani
artist2 = Artist(user_id=2, name = 'Gwen Stefani', picture = '/static/Gwen.jpg')

session.add(artist2)
session.commit()

album1 = Album(name = 'Love.Angel.Music.Baby', description = \
	"From AllMusic.com:\
	In the wake of Gwen Stefani's elevation to diva status in the early 2000s, \
	it's easy to forget that for \
	a brief moment at the start of the millennium it seemed that she and her \
	band, No Doubt, were \
	dangerously close to being pegged as yet another of the one-album alt-rock \
	wonders of the '90s.", \
	year_released = 2004, artist = artist2, picture = '/static/LAMB.jpg',
	user_id = 2)

session.add(album1)
session.commit()

album2 = Album(name = 'The Sweet Escape', description = \
	"From AllMusic.com:\
	Awkward and alluring in equal measures, Gwen Stefani's 2004 solo debut, \
	Love.Angel.Music.Baby., did \
	its job: it made Gwen a bigger star on her own than she was as the lead \
	singer of No Doubt. With that \
	established and her long-desired wish for a baby finally fulfilled, there \
	was no rush for Gwen to get \
	back to her regular gig, so she made another solo album, The Sweet Escape, \
	which expanded on what really\
	sold her debut: her tenuous connections to Californian club culture. There \
	was always a sense of \
	artifice behind the turn-of-the-century makeover that brought Gwen from a \
	ska-punk sweetheart to a \
	dance club queen, but that doesn't mean it didn't work at least on \
	occasion, most spectacularly so on \
	the gloriously dumb marching-band rap of 'Hollaback Girl, the Neptunes \
	production that turned \
	L.A.M.B. into a blockbuster.", year_released = 2006, artist = artist2, user_id = 2,
	picture = '/static/Escape.jpg')

session.add(album2)
session.commit()

#Albums for Fiona Apple
artist3 = Artist(user_id=1, name = 'Fiona Apple', picture = '/static/Fiona.jpg')

session.add(artist3)
session.commit()

album1 = Album(name = 'Tidal', description = 
	"From AllMusic.com:\
	Fiona Apple demonstrates considerable talent on her debut album, Tidal, \
	but it is unformed, \
	unfocused talent.", 
	year_released = 1996, artist = artist3, user_id = 1,
	picture = '/static/Tidal.jpg')

session.add(album1)
session.commit()

album2 = Album(name = 'When the Pawn...', description = 
	"From AllMusic.com:\
	Fiona Apple may have been grouped in with the other female \
	singer/songwriters who dominated the \
	pop charts in 1996 and 1997, but she stood out by virtue of her grand \
	ambitions and considerable \
	musical sophistication.", year_released = 1999, artist = artist3, user_id = 1,
	picture = '/static/Pawn.jpg')

session.add(album2)
session.commit()

album3 = Album(name = 'Extraordinary Machine', description = 
	"From AllMusic.com:\
	To say that the released version of Extraordinary Machine is a marked \
	improvement over \
	the bootlegged version is not to say that it sounds more complete -- \
	after all, the booted \
	Jon Brion productions sounded finished, as evidenced by the two cuts that \
	were retained; the \
	intricate chamber pop of the opening title track and the closing \
	'Waltz (Better Than Fine)' are \
	the only time Brion's productions not only suited, but enhanced Fiona \
	Apple's songs -- but they \
	are both more accessible, and more fully realized, letting Apple's songs \
	breathe in a way they \
	didn't on the original sessions.", year_released = 2005, artist = artist3, user_id = 1,
	picture = '/static/EM.jpg')

session.add(album3)
session.commit()

print 'added albums!'