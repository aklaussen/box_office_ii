from functools import wraps
from flask import request, Response
import hashlib


def check_auth(username, password):
	"""This function is called to check if a username / password
	combination is valid.
	"""
	return username=='anna' and hashlib.sha224(password).hexdigest()==(
				'5fba04773b364286693f648f22bf8012f6933a1d719064412121eaf4')


def authenticate():
	"""Sends a 401 response that enables basic auth"""
	return Response(
		'Could not verify your access level for that URL.\n'
		'You have to login with proper creditials', 401, 
		{'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		auth = request.authorization
		if not auth or not check_auth(auth.username, auth.password):
			return authenticate()
		return f(*args, **kwargs)
	return decorated
