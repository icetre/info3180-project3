"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for
from app.forms import SignupForm, LoginForm, ItemForm
from app.models import User, Item
from app import db
import requests
from bs4 import BeautifulSoup
global curr_user


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/api/user/register', methods=['GET', 'POST'])
def register():
    form = SignupForm(request.form, csrf_enabled=False)
    if  form.validate_on_submit(): #form.validate_on_submit():
        print("validated or post")
        fname = form.fname.data
        lname = form.lname.data
        email = form.email.data
        password = form.pass_conf.data

        user = User(fname, lname, email, password)
        db.session.add(user)
        db.session.commit()
        print("User added")
        return redirect('/')

    print("user not added")
    return render_template('register.html', form = form)

@app.route('/api/user/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        email = form.email.data;
        password = form.password.data;
        user = User.query.filter_by(email = email).first()
        if user:
            if user.password == password: #log them in
                return redirect('/api/user/'+str(user.user_id)+'/wishlist')

    return render_template('login.html', form = form)


@app.route('/api/user/<user_id>/wishlist', methods = ['GET']) #displays items in wishlist
def displayList(user_id):
    user = User.query.filter_by(user_id = user_id).first()
    wishlist = Item.query.filter_by(user_id = user_id).all()
    return render_template('wishlistDisplay.html', user = user, wishlist = wishlist)



@app.route('/api/user/<user_id>/wishlist/add', methods = ['GET','POST'])
def addItem(user_id):
    form = ItemForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        name = form.name.data
        url = form.item_url.data
        description = form.description.data

        if url:
            r = requests.get(url)
            html_content  = r.text
            soup = BeautifulSoup(html_content)
            if "amazon" in url: 
                image_url = soup.find('img',{'id':'miniATF_image'}).get('src')
            elif "ebay" in url:
                image_url = soup.find('img',{'id':'icImg'}).get('src')
            
            print (image_url)

        item = Item(name, description, url,image_url, user_id)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('displayList', user_id = user_id)) 

    return render_template("newItem.html", form = form, user_id = user_id)


@app.route('/api/thumbnail/process', methods = ['GET', 'POST'])










@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")