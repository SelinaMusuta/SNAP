# -*- coding: utf-8 -*-

from app import app
from flask import render_template

@app.route('/')
def index():
	return render_template('SNAP.html')

@app.route('/addresses')
def addresses():
	return render_template('addresses.html')


