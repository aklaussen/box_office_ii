from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView

from flask.ext.mongoengine.wtf import model_form

from box_office_ii.auth import requires_auth
from box_office_ii.models import Movie

admin = Blueprint('admin', __name__, template_folder='templates')


class List(MethodView):
    decorators = [requires_auth]
    cls = Movie

    def get(self):
        movies = self.cls.objects.all()
        return render_template('admin/list.html', movies=movies)


class Detail(MethodView):

    decorators = [requires_auth]

    def get_context(self, filename=None):
        form_cls = model_form(Movie, field_args={})

        if filename:
            movie = Movie.objects.get_or_404(filename=filename)
            if request.method == 'POST':
                form = form_cls(request.form, inital=movie._data)
            else:
                form = form_cls(obj=movie)
        else:
            movie = Movie()
            form = form_cls(request.form)

        context = {
            "movie": movie,
            "form": form,
            "create": filename is None
        }
        return context

    def get(self, filename):
        context = self.get_context(filename)
        return render_template('admin/detail.html', **context)

    def post(self, filename):
        context = self.get_context(filename)
        form = context.get('form')

        if form.validate():
            movie = context.get('movie')
            form.populate_obj(movie)
            movie.save()

            return redirect(url_for('admin.index'))
        return render_template('admin/detail.html', **context)


# Register the urls
admin.add_url_rule('/admin/', view_func=List.as_view('index'))
admin.add_url_rule('/admin/create/', defaults={'filename': None}, view_func=Detail.as_view('create'))
admin.add_url_rule('/admin/<filename>/', view_func=Detail.as_view('edit'))