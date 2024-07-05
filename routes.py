from flask import Flask
from flask import render_template
from flask import url_for, redirect

pages = {'Home' : 'home', 'About' : 'about', 'Contact' : 'contact'}

app = Flask(__name__)

@app.route('/')
def home():

    return render_template('home.html', pages=pages)

@app.route('/about')
def about():

    return render_template('about.html')

@app.route('/contact')
def contact():

    return render_template('contact.html')

if __name__ == "__main__":

    app.run()
