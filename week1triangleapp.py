# Week 1 mid-week Triangle Web App built off original template
# Name: Christopher Van Schyndel

import flask, flask.views
import os
app = flask.Flask(__name__)

app.secret_key = "bagels"

def is_triangle(a, b, c):
	if a > b + c or b > a + c or c > a + b:
		return 'no, a triangle is not possible.'
	else:
		return 'yes, a triangle is possible.'

def stickinput(a, b, c):
	if a.isdigit() == False or b.isdigit() == False or c.isdigit() == False:
		return 'None'
	else:
		a = int(a)
		b = int(b)
		c = int(c)
		return is_triangle(a, b, c)

class View(flask.views.MethodView):
	def get(self):
		return flask.render_template('index.html')
	
	def post(self):
		result = 'With the sides given: '
		result += str((flask.request.form['expressionA'])) + ', '
		result += str((flask.request.form['expressionB'])) + ', and '
		result += str((flask.request.form['expressionC'])) + '. '
		a = str((flask.request.form['expressionA']))
		b = str((flask.request.form['expressionB']))
		c = str((flask.request.form['expressionC']))
		trianglechecked = stickinput(a, b, c)
		result += 'Then ' + trianglechecked
		if a.isdigit() == True and b.isdigit() == True and c.isdigit() == True:
			flask.flash(result)
		return self.get()


app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET', 'POST'])

app.debug = True
app.run()