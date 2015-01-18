import datetime
from flask import url_for
from box_office_ii import db


class Movie(db.Document):
	filename = db.StringField(max_length=255, required=True, verbose_name="Filename")
	title = db.StringField(max_length=255, required=True, verbose_name="Title")
	plot = db.StringField(required=True, verbose_name="Plot")
	rating = db.DecimalField(min_value=0.0, max_value=10.0, precision=2, 
							 verbose_name="Rating")
	year = db.IntField(verbose_name="Release Year")
	imdb_id = db.StringField(verbose_name="IMBD ID", max_length=15)
	# genres = db.ListField(db.StringField(max_length=50), verbose_name="Genres")
	poster = db.URLField(verify_exists=True, verbose_name="Poster Link")
	runtime = db.IntField(min_value=0, verbose_name="Runtime (minutes)")
	# actors = db.ListField(db.StringField(max_length=50), verbose_name="Actors")

	def get_absolute_url(self):
		return url_for('movie', kwargs={"title": self.filename})

	def __unicode__(self):
		return self.title

	meta = {
		'allow_inheritance': False,
		'indexes': ['+year', 'title', '+rating']
	}

# class Genre(db.Document):
	
