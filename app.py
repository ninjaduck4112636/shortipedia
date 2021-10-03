''' Author: Devaiah'''

from flask import Flask, render_template, url_for, request
import requests
import re
import copy
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contributions.db'

# db = SQLAlchemy(app)

# class Contributions(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), default='Anonymous')
#     amount = db.Column(db.Integer)
#     date_payed = db.Column(db.DateTime,default=datetime.utcnow)

#     def __repr__(self):
#         return 'Name: {}\tAmount: {}\tDate: {}'.format(self.name,self.amount,self.date_payed)

searchUrl = 'https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search=';
contentUrl = 'https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exlimit=max&explaintext&exintro&titles=';

@app.route('/')
def home():
    return render_template('search.html')
    

@app.route('/search', methods=['POST'])
def home_form():
    search = request.form['search']
    content = requests.get(searchUrl+search).json()
    new_content = []
    for value in content[1]:
        value = value.replace(' ','_')
        new_content.append(value)
    return render_template('search_content.html',contentUrl=contentUrl,content=content,text_link=zip(content[1],content[3],new_content))
    
@app.route('/short_content')
def short_content():
    ikey = request.args.get('ikey')
    title_key = request.args.get('title_key')
    content = requests.get(contentUrl+ikey).json()
    dynamic_keys_list = list(content["query"]["pages"].keys())
    dynamic_keys = dynamic_keys_list[0]
    short_content = content["query"]["pages"]["{}".format(dynamic_keys)]["extract"]
    return render_template('short_content.html',short_content=short_content,title_key=title_key)
    
@app.route('/about')
def about():
    return render_template('about.html')    

@app.route('/donate')
def donate():
    return render_template('donate.html')      
    
@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')    
    
@app.route('/thanks')
def thanks():
    return render_template('thanks.html')        

@app.route('/contributions')
def contributions():
    return render_template('contributions.html')      

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')           
    
if __name__ == "__main__":
    app.run()	    