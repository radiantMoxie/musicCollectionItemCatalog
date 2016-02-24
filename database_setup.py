from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key = True)
	name = Column(String(250), nullable = False)
	email = Column(String(250), nullable = False)
	picture = Column(String(250))


class Artist(Base):
	__tablename__ = 'artist'

	id = Column(Integer, primary_key = True)
	name = Column(String(250), nullable = False)
	picture = Column(String(250))
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User, cascade = 'delete')

	#Return object data in easily serializable format
	@property
	def serialize(self):
		return {
			'name': self.name,
			'id': self.id,
			'user_id': self.user_id
		}

class Album(Base):
	__tablename__ = 'album'

	id = Column(Integer, primary_key = True)
	name = Column(String(250), nullable = False)
	description = Column(String(1000))
	year_released = Column(Integer)
	picture = Column(String(250))
	artist_id = Column(Integer, ForeignKey('artist.id'))
	artist = relationship(Artist, cascade = 'delete')
	user_id = Column(Integer, ForeignKey ('user.id'))
	user = relationship(User, cascade = 'delete')

	#Return object data in easily serializable format
	@property
	def serialize(self):
		return {
			'name': self.name,
			'id': self.id,
			'description': self.description,
			'year_released': self.year_released,
			'user_id': self.user_id
		}


engine = create_engine('sqlite:///musiccollection.db')

Base.metadata.create_all(engine)