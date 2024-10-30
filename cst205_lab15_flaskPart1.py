#Task 1 From the fact that the other tasks were done this seems to be already done.

# hello_flask.py
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# create an instance of Flask
app = Flask(__name__)
bootstrap = Bootstrap5(app)
# route decorator binds a function to a URL
#Task2
@app.route('/')
def hello():
  return '<p>Alexey : FIIK</p>'

@app.route('/welcome')
def wc():
    s1 = 'Welcome to my page! '
    s2 = 'Have a nice day!'
    return s1 + s2

@app.route('/azrael')
def t_test():
   return render_template('template1.html')