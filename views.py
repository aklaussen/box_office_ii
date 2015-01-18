from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from box_office_ii.models import *

movies = Blueprint('movies', __name__, template_folder='templates')


class ListView(MethodView):

	def get(self):
		movies = Movie.objects.all()
		return render_template('movies/list.html', movies=movies)


class DetailView(MethodView):

	def get(self, filename):
		movie = Movie.objects.get_or_404(filename=filename)
		return render_template('movies/detail.html', movie=movie)


#register the urls
movies.add_url_rule('/', view_func=ListView.as_view('list'))
movies.add_url_rule('/<filename>/', view_func=DetailView.as_view('detail'))
