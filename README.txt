Project: Item Catalog  - Yana Kesala
================================
This is a web application of a music collection. You can login with Google Plus or Facebook. When you are authenticated you may add new artists to the collection. Each artist's 'creator' has the ability to edit, delete, or add albums to that artist's discography. You do not have the ability to perform CRUD operations on artists you did not create.

This app was written with Python, SQLAlchemy, and Flask. There are JSON endpoints for artist and album information:

/artists/JSON: get info for all artists
/artists/artist_id/albums/JSON: get info for all albums of a certain artist
/artist/artist_id/albums/album_id/JSON: all info for a specific album

All images for the app are located in the 'static' folder. If you'd like to edit or add an image, please put it in this folder. When providing Image Location, be sure to root the location (example: '/static/Gwen.jpg').


Requirements
-----------------------------------
It's highly recommended that you use a VM to run this project -- that way any changes that you make won't affect your personal machine setup.

1. Install Vagrant (http://vagrantup.com) and VirtualBox (http://www.virtualbox.org) if you have not done so already.
2. Clone the fullstacknanodegreevm repository from GitHub. 


How to Run Project
------------------
1. Launch the Vagrant VM by typing 'vagrant up' in the directory fullstack/vagrant from the
terminal.
2. Run database setup to establish the database ('python database_setup.py')
3. If you'd like to populate the database with some artists and albums, run manyalbums. ('python manyalbums.py')
4. Run the application ('python application.py').
5. Visit http://localhost:8000 locally on your browser. Enjoy!

