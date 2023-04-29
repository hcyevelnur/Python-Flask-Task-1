from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/introduction/')
def introduction():
    namee = request.args.get('name')
    return render_template('introduction.html', namee=namee) 

@app.route('/about')
def about():
    return render_template('about.html') 

@app.route('/all')
def all():
    our_page = request.args.get('page')
    return render_template(our_page)
