# Project: Item Catalog  - Yana Kesala
* Part of Udacity's Full Stack Web Developer Nanodegree

## Section 0: Intro
This is a web application of a music collection. You can login with Google Plus or Facebook. When you are authenticated you may add new artists to the collection. Each artist's 'creator' has the ability to edit, delete, or add albums to that artist's discography. You do not have the ability to perform CRUD operations on artists you did not create.

## Section 1: Set Up Environment
It's highly recommended that you use a VM to run this project -- that way any changes that you make won't affect your personal machine setup.

1. Install Vagrant (http://vagrantup.com) and VirtualBox (http://www.virtualbox.org).
2. Clone the fullstacknanodegreevm repository from Udacity's page on GitHub (https://github.com/udacity/fullstack-nanodegree-vm).
3. Launch the Vagrant VM by typing `vagrant up` in the directory fullstack/vagrant from the terminal. 
4. Sign into the VM by typing `vagrant ssh` in the directory fullstack/vagrant from the terminal.
5. To end the connection to the VM type `exit`.
6. To shut down the VM while still saving your work, type `vagrant halt`.

## Section 2: Requirements
* Flask == 0.10.1
* Python == 2.7
* SQLAlchemy == 0.8.4 
* HTTPLib2 == 0.9.2
* Oauth2client == 2.0.0
* Requests == 2.2.1

These are included in a separate file called "requirements.txt". Install using `pip install -r requirements.txt`.

## Section 3: Installation
Clone the repo by typing `git clone https://github.com/radiantMoxie/musicCollectionItemCatalog.git` into the terminal.

## Section 4: Set Up
1. Run database setup to establish the database (`python database_setup.py`)
2. If you'd like to populate the database with some artists and albums, run manyalbums. (`python manyalbums.py`)

## Section 5: How to run
1. Run the application (`python application.py`).
2. Visit http://localhost:8000 locally on your browser. Enjoy!

## Section 6: Usage
This is a web application of a music collection. You can login with Google Plus or Facebook. When you are authenticated you may add new artists to the collection. Each artist's 'creator' has the ability to edit, delete, or add albums to that artist's discography. You do not have the ability to perform CRUD operations on artists you did not create.

This app was written with Python, SQLAlchemy, and Flask. There are JSON endpoints for artist and album information:

/artists/JSON: get info for all artists
/artists/artist_id/albums/JSON: get info for all albums of a certain artist
/artist/artist_id/albums/album_id/JSON: all info for a specific album

All images for the app are located in the 'static' folder. If you'd like to edit or add an image, please put it in this folder. When providing Image Location, be sure to root the location (example: '/static/Gwen.jpg').


