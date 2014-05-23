# -*- coding: utf-8 -*-

from app import app
from flask import render_template

@app.route('/')
def index():
	title = "Home"
	return render_template('SNAP.html',  title = title)

@app.route('/EBT_Spots')
def addresses():
	title = "EBT Spots"
	return render_template('addresses.html', title = title)

@app.route('/map_view')
def map_view():
	title = "Map View"
	return render_template('map.html', title = title)

@app.route('/EBT_Calculate')
def calculator():
	title = "Calculator"
	return render_template('calculator.html', title = title)


