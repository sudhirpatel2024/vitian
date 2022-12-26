from logging import CRITICAL
from flask import Flask, render_template, url_for, flash, session, redirect, jsonify  , request 
import datetime  
import mysql.connector  
from flask_sqlalchemy import SQLAlchemy  
from flask_mail import Mail, Message  
import smtplib  
import requests  
import random  
from werkzeug.security import generate_password_hash, check_password_hash  
from flask_login import LoginManager, UserMixin, login_required, login_required, logout_user, current_user,login_user  
from sqlalchemy import func  
from threading import Thread  
import os  
import datetime  
from werkzeug.utils import secure_filename  
import os  
from pathlib import Path  
import uuid  
from flask_mysqldb import MySQL  
import requests
import json
import itertools
app = Flask(__name__)
app.secret_key = "dfmesawqf83ru8934t348"



AWS_SERVER = False
if AWS_SERVER:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ALDSonrent1@localhost/vit'
    app.config['MYSQL_HOST'] = "localhost"
    app.config['MYSQL_USER'] = "root"
    app.config['MYSQL_PASSWORD'] = "ALDSonrent1"
    app.config['MYSQL_DB'] = "vit"
    app.config['MYSQL_CURSORCLASS'] = "DictCursor"
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/vit'
    app.config['MYSQL_HOST'] = "localhost"
    app.config['MYSQL_USER'] = "root"
    app.config['MYSQL_PASSWORD'] = ""
    app.config['MYSQL_DB'] = "vit"
    app.config['MYSQL_CURSORCLASS'] = "DictCursor"

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    event_name = db.Column(db.String(255), nullable=False)
    ondate = db.Column(db.String(255), nullable=True)
    event_cond_by = db.Column(db.String(255), nullable=True)
    mode = db.Column(db.String(255), nullable=True)
    event_cat = db.Column(db.String(255), nullable=True)
    support = db.Column(db.String(255), nullable=True)
    link = db.Column(db.String(255), nullable=False)
    about = db.Column(db.String(255), nullable=False)
    photosUrl = db.Column(db.String(255), nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    followers = db.Column(db.Integer, nullable=False)
    views = db.Column(db.Integer, nullable=False)
    html_filename = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.String(255), nullable=True)
    member_id = db.Column(db.String(255), nullable=True)
    rating = db.Column(db.String(255), nullable=True)


class Clubs(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    club_name = db.Column(db.String(255), nullable=True)
    club_school = db.Column(db.String(255), nullable=True)
    club_category = db.Column(db.String(255), nullable=True)
    date_created = db.Column(db.String(255), nullable=True)
    club_opening_date = db.Column(db.String(255), nullable=True)
    club_images = db.Column(db.String(255), nullable=True)
    club_head_id = db.Column(db.String(255), nullable=True)
    link = db.Column(db.String(255), nullable=False)
    html_filename = db.Column(db.String(255), nullable=True)
    members = db.Column(db.Integer, nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    followers = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    faculty_coordinator_id = db.Column(db.Integer, nullable=False)
    member_id = db.Column(db.Integer, nullable=False)
    event_id = db.Column(db.Integer, nullable=False)

class Like_data(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(255), nullable=False)
    events = db.Column(db.String(255), nullable=False)
    clubs = db.Column(db.String(255), nullable=False)
    post = db.Column(db.String(255), nullable=False)
    blog = db.Column(db.String(255), nullable=False)


class Profiles(UserMixin, db.Model):

    # id,name,email,password,date
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_key = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255),unique_key = True, nullable=False)
    propicurl = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255),unique_key = True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    bio = db.Column(db.Text(), nullable=False)
    reputation = db.Column(db.Integer, nullable=False)
    level = db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.String(50), nullable=False)
    last_edit_date = db.Column(db.String(50), nullable=False)
    followers = db.Column(db.Integer, nullable=False)
    views = db.Column(db.Integer, nullable=False)
    isfaculty = db.Column(db.Integer, nullable=False)
    ismoderator = db.Column(db.Integer, nullable=False)
    branch = db.Column(db.Integer, nullable=False)
    posts = db.Column(db.Integer, nullable=False)
    blogs = db.Column(db.Integer, nullable=False)



class Website_visitors(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    ip_address = db.Column(db.String(255), nullable=True)
    state = db.Column(db.String(255), nullable=True)
    country = db.Column(db.String(255), nullable=True)
    date = db.Column(db.String(255), nullable=True)






class Follow_data(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(255), nullable=False)
    events = db.Column(db.String(255), nullable=False)
    clubs = db.Column(db.String(255), nullable=False)
    users = db.Column(db.String(255), nullable=False)



class Paper(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    paper_name = db.Column(db.String(255), nullable=False)
    paper_course = db.Column(db.String(255), nullable=False)
    paper_cc = db.Column(db.String(255), nullable=False)
    paper_sem = db.Column(db.String(255), nullable=False)
    paper_year = db.Column(db.String(255), nullable=False)
    paper_faculty = db.Column(db.String(255), nullable=False)
    paper_link = db.Column(db.String(255), nullable=False)
    paper_sol_link = db.Column(db.String(255), nullable=True)
    paper_sol_by_username = db.Column(db.String(255), nullable=True)
    date_added = db.Column(db.String(255), nullable=True)



@login_manager.user_loader
def load_user(user_id):
    return Profiles.query.get(int(user_id))



@app.route("/unique_visit", methods = ["GET","POST"])
def unique_visit():
    if request.method == "POST":
        ip = str(request.form.get('ip'))
        ip = json.loads(ip)
        ip = str(ip["ip"])
        info = (getting_ip(f"{ip}"))
        # view = Website_visitors(ip_address = ip,country = info["data"]["location"]["country"]['alpha3'],state = info["data"]["location"]["region"]["name"],date = datetime.datetime.now())
        view = Website_visitors(ip_address = "0.0.0.",country = "IND",state = "NA",date = datetime.datetime.now())
        db.session.add(view)
        db.session.commit()
        
    return "SUCCESS"
























def getting_ip(row):
    """This function calls the api and return the response"""
    url = f"https://api.ipbase.com/v2/info?apikey=idfEJs8hwZXCnuu75DlhJYOzdBhBHzKYcGWdH8w6&language=en&ip={row}"       # getting records from getting ip address
    headers = {
        'accept': "application/json",
        'content-type': "application/json"
        }
    response = requests.request("GET", url, headers=headers)
    respond = json.loads(response.text)
    return respond


@app.context_processor
def user_name():
    if current_user.is_authenticated:
        user_name = Profiles.query.filter_by(email=current_user.email).first().name.partition(' ')[0]
        user = Profiles.query.filter_by(email=current_user.email).first()
        my_profile_username = user.username
    else:
        user_name = "User"
        user_name = "User"
        my_profile_username = "oops"
    return dict(user_name=user_name,my_profile_username=my_profile_username)


@app.route("/")
def index():
    clubs = Clubs.query.all()
    events = Events.query.all()
    res = len(clubs) + len(events)
    profiles = Profiles.query.all()
    website_visitors = len(Website_visitors.query.all())
    users = len(Profiles.query.order_by(func.random()).all())
    return render_template("0home.html" , clubs = clubs , events = events , res = res , users = users , wv  = website_visitors , peoples = profiles)


@app.route("/addclub" , methods = ["GET" , "POST"])
# @login_required
def addclub():
    permission_email = ["sudhir.kumar2020@vitbhopal.ac.in","dhananjay.arne2020@vitbhopal.ac.in"]
    if current_user.email in permission_email:
    # if True:
        if request.method == "POST":

            clubcat = request.form.get("clubcat")
            name = request.form.get("name")
            club_short_des = request.form.get("club_short_des")
            memberscount = request.form.get("memberscount")
            school = request.form.get("school")
            opendate = request.form.get("opendate")
            repuser = request.form.get("repuser").lower()
            images = request.files.getlist("images")
            link = request.form.get("link")
            html = request.files["html"]
            htmlf_name = secure_filename(html.filename)
           # html.save(os.path.join(f"/var/www/dj/dj/templates/clubs/", htmlf_name))
            html.save(os.path.join(f"C:/Users/Sudhir Kumar Patel/PycharmProjects/vitwale/templates/clubs/", htmlf_name))
            key1 = uuid.uuid4()
            htmlf1_name = f"R{key1}{htmlf_name}"

            # os.rename(f"/var/www/dj/dj/templates/clubs/{htmlf_name}",
            #                         f"/var/www/dj/dj/templates/clubs/{htmlf1_name}")

            os.rename(f"C:/Users/Sudhir Kumar Patel/PycharmProjects/vitwale/templates/clubs/{htmlf_name}",
                                    f"C:/Users/Sudhir Kumar Patel/PycharmProjects/vitwale/templates/clubs/{htmlf1_name}")
            if str(images) == "[<FileStorage: '' ('application/octet-stream')>]":
                    images_file = []
            else:
                    try:
                        images_file = []
                        f1 = request.files.getlist("images")
                        for f in f1:
                            key = uuid.uuid1()
                            image1_name_user = secure_filename(f.filename)
                            #f.save(os.path.join(f"/var/www/dj/dj/static/website_images/clubs_images/", image1_name_user))
                            f.save(os.path.join(f"/var/www/dj/dj/static/website_images/clubs_images/", image1_name_user))
                            image1_name = f"R{key}{image1_name_user}"
                            os.rename(f"/var/www/dj/dj/static/website_images/clubs_images/{image1_name_user}",
                                    f"/var/www/dj/dj/static/website_images/clubs_images/{image1_name}")
                            images_file.append(image1_name)
                    except Exception as e:
                        print(f"ERROR OCCURED \n{e}")
                        images_file = []

            print(name,clubcat,memberscount,school,opendate,repuser,images,html)

            flash('Succesfully Published Club On VITWALE.')
            newclub = Clubs(club_name = name , club_school = school , club_category = clubcat , members = memberscount , views =  0, likes = 0 , followers = 0 , club_opening_date = opendate , html_filename =  htmlf1_name , club_images = str(images_file) , date_created = datetime.datetime.now() , link = link, club_head_id = "",rating = "4",faculty_coordinator_id = "",member_id = "", event_id = "")
            db.session.add(newclub)
            userep = Profiles.query.filter_by(username  = repuser).first()
            userep.reputation = int(userep.reputation) + 25
            db.session.commit()
            db.session.commit()
            return redirect(url_for('club_view' , clubfname = htmlf1_name))
        return render_template("clubform.html")
    else:
        return render_template("getout.html")

@app.route("/club/<string:clubfname>")
def club_view(clubfname):
    club = Clubs.query.filter_by(html_filename = clubfname).first()
    date_now  = datetime.datetime.now()
    return render_template(f"clubs/{clubfname}", club  = club , date_now = date_now)

@app.route("/addevent" , methods = ["GET" , "POST"])
@login_required
def addevent():
    permission_email = ["sudhir.kumar2020@vitbhopal.ac.in","dhananjay.arne2020@vitbhopal.ac.in"]
    if current_user.email in permission_email:
        if request.method == "POST":
            eventcat = request.form.get("eventcat")
            name = request.form.get("name")
            event_short_des = request.form.get("event_short_des")
            opendate = request.form.get("opendate")
            repuser = request.form.get("repuser").lower()
            mode = request.form.get("mode")
            images = request.files.getlist("images")
            link = request.form.get("link")
            html = request.files["html"]
            htmlf_name = secure_filename(html.filename)
            html.save(os.path.join(f"/var/www/dj/dj/templates/events/", htmlf_name))
            key1 = uuid.uuid4()
            htmlf1_name = f"R{key1}{htmlf_name}"
            os.rename(f"/var/www/dj/dj/templates/events/{htmlf_name}",
                                    f"/var/www/dj/dj/templates/events/{htmlf1_name}")
            if str(images) == "[<FileStorage: '' ('application/octet-stream')>]":
                    images_file = []
            else:
                    try:
                        images_file = []
                        f1 = request.files.getlist("images")
                        for f in f1:
                            key = uuid.uuid1()
                            image1_name_user = secure_filename(f.filename)
                            f.save(os.path.join(f"/var/www/dj/dj/static/website_images/events_images/", image1_name_user))
                            image1_name = f"R{key}{image1_name_user}"
                            os.rename(f"/var/www/dj/dj/static/website_images/events_images/{image1_name_user}",
                                    f"/var/www/dj/dj/static/website_images/events_images/{image1_name}")
                            images_file.append(image1_name)
                    except Exception as e:
                        print(f"ERROR OCCURED \n{e}")
                        images_file = []

            flash('Succesfully Published Event On VITWALE.')
            newevent = Events(event_name = name , event_cat = eventcat ,  views =  0, likes = 0 , followers = 0 , ondate = opendate , html_filename =  htmlf1_name,about = event_short_des , photosUrl = str(images_file) , date_created = datetime.datetime.now() , link = link, rating = "4",support = "",member_id = "", event_cond_by = "", mode = mode)
            db.session.add(newevent)
            db.session.commit()
            userep = Profiles.query.filter_by(username  = repuser).first()
            userep.reputation = int(userep.reputation) + 25
            db.session.commit()
            return redirect(url_for('event_view' , eventfname = htmlf1_name))
        return render_template("eventform.html")
    else:
        return render_template("getout.html")

@app.route("/event/<string:eventfname>")
def event_view(eventfname):
    event = Events.query.filter_by(html_filename = eventfname).first()
    date_now  = datetime.datetime.now()
    return render_template(f"events/{eventfname}", event  = event , date_now = date_now)





@app.route("/save_profile", methods=["POST", "GET"])
def save_profile():
    if request.method == "POST":
        name = request.form.get("name")
        branch  = request.form.get("branch")
      
        bio  = request.form.get("bio")
        user = Profiles.query.filter_by(email=current_user.email).first()
        user.name = name
        user.branch = branch
      
        user.bio = bio
        db.session.commit()
    return redirect(url_for("bprofile"))



def username_generator(full_name):
    g_username = []
    username = ''
    names  = full_name.split(" ")
    for name in names:
        if not Profiles.query.filter_by(username  = name).first():
            g_username.append(name.lower())
    if not Profiles.query.filter_by(username  = full_name.replace(" ","")).first():
        g_username.append(full_name.lower().replace(" ","")) 
    for num in range(1):
        names.append(str(num))
        username_list  = list(itertools.permutations(names))
        for one_item in username_list:
            username = ''
            for one_word in one_item:
                username = username+one_word
            if check_availabilty(username.lower()):
                g_username.append(username.lower())
    return g_username[:5]

def check_availabilty(username):
    if Profiles.query.filter_by(username = username).first():
        return False
    else: 
        return True

@app.route("/bprofile")
@login_required
def bprofile():
    user = Profiles.query.filter_by(email=current_user.email).first()
    return redirect(url_for('profile',profile_username = user.username))



@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

    
@app.route("/login", methods = ["GET","POST"])
def login():
    try:
        if current_user.is_authenticated:
            print("CUURENT USER IS ALREADY LOGGED IN ")
            return redirect(url_for('bprofile'))
        else:
            print("CUURENT USER IS ALREADY NOT LOGGED IN ")
            if request.method == "POST":
                name = request.form.get("name")
                email = request.form.get("email")
                propic = request.form.get("propic")
                password = request.form.get("pass")
                print("USER DATA RECIEVED")
                print(name)
                print(email)
                print(propic)
                print(password)
                register = Profiles.query.filter_by(email = email).first()
                print("CHECKING REGISTER")
                print(register)
                if register:
                    if(register.password == password):

                        print("LOGGING USER IN")
                        user_account = Profiles.query.filter_by(email=email).first()

                        login_user(user_account, remember=True)
                        flash('Welcome Back to VITWale.')
                        return redirect(url_for('bprofile'))
                    else:
                        flash('Incorrect Password')
                        return redirect(url_for('bprofile'))
                else:
                    print("SETTING UP NEW USER NAME")
                    avail_username = username_generator(name)
                    session["login_user_info"] = [name,email,propic,password,avail_username]
                    return redirect(url_for('set_username'))
    except Exception as e:
        print("ERROR OCCURED")
        print(e)
    return render_template("2login.html")




@app.route("/set_username", methods = ["GET" , "POST"])
def set_username():
    suggest_username = str(session.get("login_user_info")[4])[1:-1]

    if request.method == "POST":
        username  = request.form.get("username").lower()
        if Profiles.query.filter_by(username = username).first():
            flash("Username Already Taken")
            return redirect(url_for('set_username'))
        else:
            user_info = session.get("login_user_info")
            # newuser = Profiles(name = user_info[0] , email = user_info[1] , propicurl = user_info[2] , password = generate_password_hash(user_info[3] , method = "sha256") , username = username,bio = "A verified VITwale.",level  = "Beginner",reputation = 0,followers = 0,views = 0,date_created = datetime.datetime.now() , last_edit_date = datetime.datetime.now(),isfaculty = 0, ismoderator = 0, branch = "" , posts = "", blogs = "", user_key = str(uuid.uuid1()))
            newuser = Profiles(name = user_info[0] , email = user_info[1] , propicurl = user_info[2] , password = user_info[3] , username = username,bio = "A verified VITwale.",level  = "Beginner",reputation = 0,followers = 0,views = 0,date_created = datetime.datetime.now() , last_edit_date = datetime.datetime.now(),isfaculty = 0, ismoderator = 0, branch = "" , posts = "", blogs = "", user_key = str(uuid.uuid1()))
            db.session.add(newuser)
            db.session.commit()
            
            strTable = '''
        {% extends "club_def.html" %}
            {% block seo %}
            <!DOCTYPE html>
            <html lang="en">

            <head>

                <!-- META ============================================= -->
                <meta charset="utf-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="keywords" content="'''+ username +","+ user_info[0]  + ","+ user_info[0].upper() +","+"VIT WALE" +'''"/>
                <meta name="author" content="VIT WALE"/>


                <!-- DESCRIPTION -->
                <meta name="description" content="'''+ "Check out the profile of " + username + " on VIT WALE Community. Follow " + username + " On VITWALE"+'''"/>

                <!-- OG -->
                <meta property="og:title" content="'''+ username +'''"/>
                <meta property="og:description" content="'''+ "Check out the profile of " + username + " on VIT WALE Community. Follow " + username + " On VITWALE"+'''"/>

                <!-- FAVICONS ICON ============================================= -->
                <link rel="icon" href="{{user.propicurl}}"/>
                <link rel="shortcut icon" type="image/x-icon" href="{{user.propicurl}}"/>

                <!-- PAGE TITLE HERE ============================================= -->
                <title>'''+ username + " On VITWale"+'''</title>

                <!-- MOBILE SPECIFIC ============================================= -->
                <meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="google-signin-client_id" content="897661527969-cqpqlh62u214odr8751i1iq3g6a71std.apps.googleusercontent.com">
<script src="https://apis.google.com/js/platform.js" async defer></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>   





            {% endblock %}
    
        


            {% block body %}
          
            <!-- Content -->
            <div class="page-content bg-white">
                <!-- inner page banner -->

                <!-- Breadcrumb row -->
                <div class="breadcrumb-row">
                    <div class="container">
                        <ul class="list-inline">
                            <li><a href="{{url_for('index')}}">Home</a></li>
                            <li>Profile</li>
                        </ul>
                    </div>
                </div>
                <!-- Breadcrumb row END -->
                <!-- inner page banner END -->
                <div class="content-block">
                    <div style="padding-top: 50px;" ></div>
                    <div class="container">
                        {% if owner %}
                    <h4>Share Your Profile </h4>
                    {% else %}
                    <h4>Share This Profile </h4>
                    {% endif %}
                        <h6> <div class="sharethis-inline-share-buttons"></div></h6>

                        {% if owner %}

                        <a href="{{url_for('logout')}}" onclick="signOut();" style="float: right; bottom: 0;  "  class="btn btn-danger">Logout</a>


                        {% endif %}

                </div>
                    <!-- About Us -->
                    <div class="section-area section-sp1">
                        <div class="container">

                            <div class="row">
                                <div class="col-lg-3 col-md-4 col-sm-12 m-b30">
                                    <div class="profile-bx text-center">
                                        <div class="user-profile-thumb">
                                            <img src="{{user.propicurl}}"
                                                alt=""/>
                                        </div>
                                        <div class="profile-info">
                                        {% if owner %}
                                        {% else %}
                                        {% if current_user.is_authenticated %}
                                        {% if followed %}
                                        <span><button id="followbtn"   class="btn btn-success">Following</button></span>
                                        {% else %}
                                        <span><button id="followbtn"   class="btn btn-success">Follow</button></span>
                                        {% endif %}
                                        {% else %}
                                        <span><button onclick="alert('Please Login To Follow This User');"  class="btn btn-success">Follow</button></span>
                                        {% endif %}
                                        {% endif %}
                                            <div class="mb-3"></div>
                                            <h4>{{user.name}}</h4>
                                            <span>{{user.level}}</span><br>
                                            <span>@{{user.username}}</span><br>
                                            <span style="color: black;">{{user.followers}} Followers , {{user.reputation}} Repu</span>


                                        </div>
                                       
                                        <div class="profile-tabnav">
                                            <ul class="nav nav-tabs">

                                                <li class="nav-item">

                                                    <a class="nav-link active" data-toggle="tab" href="#courses"><i
                                                            class="fa fa-th"></i>
                                                        {% if owner %}
                                                        My Posts & Blogs

                                                            {% else %}

                                                            User's Posts & Blogs
                                                            {% endif %}
                                                        </a>
                                                </li>
                                                <li class="nav-item">
                                                    {% if owner %}
                                                    <a class="nav-link" data-toggle="tab" href="#edit-profile"><i
                                                            class="fa fa-pencil-square-o"></i>

                                                            Edit Profile

                                                        </a>

                                                            {% else %}
                                                            <a class="nav-link" data-toggle="tab" href="#edit-profile"><i
                                                                class="fa fa-user"></i>

                                                                Profile

                                                            </a>
                                                            {% endif %}


                                                </li>

                                                {% if owner %}
                                        
                                                <li class="nav-item">
                                                
                                                    <a class="nav-link" onclick="alert('This Feature Will Coming Soon!');"><i
                                                            class="fa fa-plus"></i>Create Post Or Blog</a>
                                                
                                                </li>

                                                {% endif %}

                                            </ul>
                                        </div>
                                    </div>
                                </div>

                                <div class="col-lg-9 col-md-8 col-sm-12 m-b30">
                                    <div class="profile-content-bx">
                                        <div class="tab-content">
                                            <div class="tab-pane active" id="courses">
                                                <div class="profile-head">
                                    
                                                    <h3>Posts & Blogs</h3>
                                                    
                                                    <div class="feature-filters style1 ml-auto">
                                                        <ul class="filters" data-toggle="buttons">
                                                            {% if user.posts != ""  or user.blogs != ""  %}
                                                    
                                                            <li data-filter="" class="btn active">
                                                                <input type="radio">
                                                                <a href="#"><span>All</span></a> 
                                                            </li>
                                                            {% if user.posts != "" %}
                                                            <li data-filter="publish" class="btn">
                                                                <input type="radio">
                                                                <a href="#"><span>Posts</span></a> 
                                                            </li>
                                                            {% endif %}
                                                            {% if user.blogs != "" %}
                                                            <li data-filter="pending" class="btn">
                                                                <input type="radio">
                                                                <a href="#"><span>Blogs</span></a> 
                                                            </li>
                                                        {% endif %}
                                                        {% else %}
                                                        NO POSTS YET
                                                            {% endif %}
                                                        </ul>
                                                    </div>
                                                </div>
                                            
                                                <div class="courses-filter">
                                                    <div class="clearfix">
                                                        <ul id="masonry" class="ttr-gallery-listing magnific-image row">

                                                            {% for post in user_post %}
                                                            <li class="action-card col-xl-4 col-lg-6 col-md-12 col-sm-6 publish">
                                                                <div class="cours-bx">
                                                                    <div class="action-box">
                                                                        <img src="static/website_images/posts/{{post.image}}" alt="">
                                                                    </div>
                                                                    <div class="info-bx text-center">
                                                                        <h6><a href="#">{{user_post.about}}</a></h6>
                                                                    </div>
                                                            
                                                                </div>
                                                            </li>
                                                            {% endfor %}
                                                    {% for blog in user_blog %}
                                                            <li class="action-card col-xl-4 col-lg-6 col-md-12 col-sm-6 pending">
                                                                <div class="cours-bx">
                                                                    <div class="action-box">
                                                                        <img src="static/website_images/blog_images/{{blog.thumbnail}}" alt="">
                                                                        <a href="#" class="btn">Read More</a>
                                                                    </div>
                                                                    <div class="info-bx text-center">
                                                                        <h5><a href="#">{{blog.heading}}</a></h5>
                                                                        <span>{{blog.date}}</span>
                                                                    </div>
                                                            
                                                                </div>
                                                            </li>
                                                            {% endfor %}
                                                
                                                        
                                    
                                                        </ul>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="tab-pane" id="del-account">
                                                <div class="profile-head">
                                                    <h3>Delete Your Account</h3>
                                                </div>
                                                <form class="edit-profile" action="/pro_feedback" method="post">
                                                    <div class="">
                                                        <div class="form-group row">
                                                            <div class="col-12 col-sm-9 col-md-9 col-lg-10 ml-auto">
                                                                <h2 style="color: red;">Danger Zone</h2>
                                                            </div>
                                                        </div>
                                                        {% if ads|length != 0 %}
                                                        <div class="form-group row">
                                                            <div class="col-12 col-sm-9 col-md-9 col-lg-10 ml-auto">
                                                                <h3>You have <span style="color: blue;">{{views}} +</span> views on Your ADs
                                                                </h3>
                                                            </div>
                                                        </div>
                                                        {% endif %}
                                                        <div class="form-group row">
                                                            <div class="col-12 col-sm-9 col-md-9 col-lg-10 ml-auto">
                                                                <h3>Your Will <span style="color: blue;">Loose All Your Data</span> & You Won't Able To Recover Your Account.
                                                                </h3>
                                                            </div>
                                                        </div>

                                                        <div class="form-group row">
                                                            <div class="col-12 col-sm-9 col-md-9 col-lg-10 ml-auto">
                                                                <h3>Have any issue?, Share with us!</h3>
                                                                <div class="form-group row">
                                                                    <label class="col-12 col-sm-3 col-md-3 col-lg-2 col-form-label">Write
                                                                        Issue Here!</label><br>
                                                                    <div class="col-12 col-sm-9 col-md-9 col-lg-7">
                                                                        <textarea class="form-control" id="body" name="body"
                                                                                cols="30" rows="10"></textarea>

                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                        <div class="">
                                                            <div class="">
                                                                <div class="row">
                                                                    <div class="col-12 col-sm-3 col-md-3 col-lg-2">
                                                                    </div>
                                                                    <div class="col-12 col-sm-9 col-md-9 col-lg-7">
                                                                        <button type="submit" class="btn"><i
                                                                                class="fa fa-share"></i> Send
                                                                        </button>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                        <div class="seperator"></div>
                                                        <div class="m-form__seperator m-form__seperator--dashed m-form__seperator--space-2x"></div>
                                                        <br>
                                                        <br>
                                                        <br>

                                                        <div class="form-group row">
                                                            <div class="col-12 col-sm-9 col-md-9 col-lg-10 ml-auto">
                                                                <h6>Deleting your account will delete all your data from VITwale
                                                                    Website and you won't able to recover your data.</h6>
                                                            </div>
                                                        </div>
                                                        <div class="seperator"></div>


                                                        <div class="m-form__seperator m-form__seperator--dashed m-form__seperator--space-2x"></div>

                                                    </div>
                                                    <div class="">
                                                        <div class="">
                                                            <div class="row">
                                                                <div class="col-12 col-sm-3 col-md-3 col-lg-2">
                                                                </div>
                                                                <div class="col-12 col-sm-9 col-md-9 col-lg-7">
                                                                    <button type="reset" class="btn-danger" data-toggle="modal"
                                                                            data-target="#DelModalCenter">Delete
                                                                    </button>


                                                                    <!-- Modal -->
                                                                    <div class="modal fade" id="exampleModalCenter" tabindex="-1"
                                                                        role="dialog" aria-labelledby="exampleModalCenterTitle"
                                                                        aria-hidden="true">
                                                                        <div class="modal-dialog modal-dialog-centered"
                                                                            role="document">
                                                                            <div class="modal-content">
                                                                                <div class="modal-header">
                                                                                    <h5 class="modal-title"
                                                                                        id="exampleModalLongTitle">Confirmation</h5>
                                                                                    <button type="button" class="close"
                                                                                            data-dismiss="modal" aria-label="Close">
                                                                                        <span aria-hidden="true">&times;</span>
                                                                                    </button>
                                                                                </div>
                                                                                <div class="modal-body">
                                                                                    <h5>Are you sure to delete your account</h5>
                                                                                </div>
                                                                                <div class="modal-footer">
                                                                                    <button type="button" class="btn btn-secondary"
                                                                                            data-dismiss="modal">No
                                                                                    </button>
                                                                                    <button type="button" class="btn btn-primary">
                                                                                        Yes
                                                                                    </button>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                    <button type="reset" class="btn-success">Cancel</button>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </form>
                                            </div>
                                            <div class="tab-pane" id="edit-profile">
                                                <div class="profile-head">
                                                    {% if owner %}
                                                    <h3>Edit Profile</h3>
                                                    {% else %}
                                                    <h3>Profile Detail</h3>
                                                    {% endif %}
                                                </div>
                                                <form class="edit-profile" action="/save_profile" method="post">
                                                    <div class="">
                                                        <div class="form-group row">
                                                            <div class="col-12 col-sm-9 col-md-9 col-lg-10 ml-auto">
                                                                <h3>1. Personal Details</h3>
                                                            </div>
                                                        </div>
                                                        <div class="form-group row">
                                                            <label for="name_div" class="col-12 col-sm-3 col-md-3 col-lg-2 col-form-label">Full
                                                                Name</label>

                                                            <div class="col-12 col-sm-9 col-md-9 col-lg-7" name="name_div">
                                                                {% if owner %}
                                                                <input class="form-control" name="name" type="text"
                                                                    value="{{user.name}}">
                                                                    {% else %}
                                                                    <input class="form-control" name="name" type="text"
                                                                    value="{{user.name}}" readonly>
                                                                    {% endif %}
                                                            </div></div>



                                                            <div class="form-group row">
                                                            <label class="col-12 col-sm-3 col-md-3 col-lg-2 col-form-label" for="username_div">
                                                                VITwale Username</label>

                                                                <div class="col-12 col-sm-9 col-md-9 col-lg-7" name="username_div">
                                                                    {% if owner %}
                                                                    <input class="form-control" name="name" type="text"
                                                                        value="{{user.username}}" readonly>
                                                                        {% else %}
                                                                        <input class="form-control" name="name" type="text"
                                                                        value="{{user.username}}" readonly>
                                                                        {% endif %}
                                                                </div>
                                                        </div>

                                                        <div class="seperator"></div>

                                                        <div class="form-group row">
                                                            <div class="col-12 col-sm-9 col-md-9 col-lg-10 ml-auto">
                                                                <h3>2. Other Details</h3>
                                                            </div>
                                                        </div>
                                                        <div class="form-group row">
                                                            <label class="col-12 col-sm-3 col-md-3 col-lg-2 col-form-label">Email
                                                                Address</label>
                                                            <div class="col-12 col-sm-9 col-md-9 col-lg-7">
                                                                <input class="form-control" type="email" value="{{user.email}}"
                                                                    readonly>
                                                                    {% if owner %}
                                                                <small>You cannot change your email address.</small>
                                                                {% endif %}
                                                            </div>
                                                        </div>

                                                   



                                                        <div class="form-group row">
                                                            <label class="col-12 col-sm-3 col-md-3 col-lg-2 col-form-label">Branch</label>
                                                            <div class="col-12 col-sm-9 col-md-9 col-lg-7">
                                                            
                                                                    {% if owner %}
                                                                    <input class="form-control" name="branch" type="text" value="{{user.branch}}"
                                                                    >
                                                            
                                                                {% else %}
                                                                <input class="form-control" name="branch" type="text" readonly value="{{user.branch}}"
                                                                >
                                                                {% endif %}
                                                            </div>
                                                        </div>



                                                        <div class="form-group row">
                                                            <label class="col-12 col-sm-3 col-md-3 col-lg-2 col-form-label">Bio</label>
                                                            <div class="col-12 col-sm-9 col-md-9 col-lg-7">
                                                            
                                                                    {% if owner %}
                                                                    <textarea class="form-control" name="bio">{{user.bio}}</textarea>
                                                                
                                                                {% else %}
                                                                <textarea class="form-control" name="bio" readonly>{{user.bio}}</textarea>
                                                                {% endif %}
                                                            </div>
                                                        </div>


                
                                                        <!-- <div class="form-group row">
                                                            <label class="col-12 col-sm-3 col-md-3 col-lg-2 col-form-label">Phone
                                                                Number:</label>
                                                            <div class="col-12 col-sm-9 col-md-9 col-lg-7">
                                                                {% if not user.phone_no %}
                                                                {% if owner %}
                                                                <input class="form-control" type="tel" id="phone" name="phone"
                                                                    placeholder="Not Given Yet" pattern=".{10,}" min="1111111111" max="9999999999">
                                                                {% else %}
                                                                <input class="form-control" type="tel" id="phone" name="phone"  readonly
                                                                    placeholder="Not Given Yet" pattern=".{10,}" min="1111111111" max="9999999999">
                                                                {% endif %}
                                                                {% else %}
                                                                {% if owner %}
                                                                <input class="form-control" type="tel" id="phone" name="phone"
                                                                    placeholder="Enter your phone no." value="{{user.phone_no}}" pattern=".{10,}" min="1111111111" max="9999999999">
                                                                    {% else %}
                                                                    <input class="form-control" type="tel" id="phone" name="phone" readonly
                                                                    placeholder="Enter your phone no." value="{{user.phone_no}}" pattern=".{10,}" min="1111111111" max="9999999999">
                                                                    {% endif %}
                                                                {% endif %}
                                                            </div>
                                                        </div> -->

                                                        <div class="m-form__seperator m-form__seperator--dashed m-form__seperator--space-2x"></div>

                                                    </div>
                                                    <div class="">
                                                        <div class="">
                                                            <div class="row">
                                                                <div class="col-12 col-sm-3 col-md-3 col-lg-2">
                                                                </div>
                                                                {% if owner %}
                                                                <div class="col-12 col-sm-9 col-md-9 col-lg-7">

                                                                    <button type="submit" class="btn">Save changes</button>

                                                                    <button type="reset" class="btn-secondry">Cancel</button>
                                                                </div>
                                                                {% endif %}
                                                            </div>
                                                        </div>
                                                    </div>
                                                </form>
                                            </div>
                                    
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- contact area END -->
            </div>








            <div class="modal fade" id="DelModalCenter" tabindex="-1" role="dialog" aria-labelledby="DelModalCenterTitle"
                aria-hidden="true">
                <div class="modal-dialog modal-dialog-centered" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="DelModalLongTitle">Confirmation </h5>
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                <span aria-hidden="true">&times;</span>
                            </button>
                        </div>
                        <div class="modal-body">
                            <input type="email" name="cmail" id="cmail" onkeyup="check();" class="form-control"
                                placeholder="Re-enter your email address">
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-dismiss="modal">No</button>
                            <form action="/delete_account" method="post">      
                                <button type="submit" onclick="signOut();" class="btn btn-danger" id="delbtn" disabled>Delete My Account</button>


                            </form>
                        </div>
                    </div>
                </div>
            </div>

<a href="{{url_for('logout')}}" id="logout_a" hidden></a>

<script src="https://apis.google.com/js/platform.js?onload=onLoad" async defer></script>
            <script>

                $(document).ready(function(){
            $("#followbtn").click(function(e){
                id = "{{user.id}}";

                $.ajax({
                    method:"post",
                    url:"/followuser",
                    // data:{backendname:valueName}
                    data:{id:id},
                    success:function(res){
                        if(document.getElementById("followbtn").innerHTML == 'Follow'){
                            document.getElementById("followbtn").innerHTML = 'Following';
                            }else{
                                document.getElementById("followbtn").innerHTML = 'Follow';

                            }

                        }
                    })
                });
            })
            </script> 
            <!-- Content END-->
            <!-- Footer ==== -->
            {% endblock %}

            


                    

                    
                    '''

            # hs = open(f"/var/www/dj/dj/templates/profiles/{username}.html", 'w')
            hs = open(f"C:/Users/Sudhir Kumar Patel/PycharmProjects/vitwale/templates/profiles/{username}.html", 'w')
            hs.write(strTable)
            user_account = Profiles.query.filter_by(email=user_info[1]).first()
            login_user(user_account, remember=True)
            entry_follow = Follow_data(email = current_user.email, events = "[]" , clubs = "[]" , users = "[]")
            entry_like = Like_data(email = current_user.email, events = "[]" , clubs = "[]" , post = "[]",blog = "[]")
            db.session.add(entry_like)
            db.session.commit()
            db.session.add(entry_follow)
            db.session.commit()
            flash("WELCOME TO VITWALE Community.")
            return redirect(url_for('profile',profile_username = username))
    return render_template("3username.html" , suggest_username = suggest_username)


@app.route("/followuser", methods=["POST", "GET"])

@login_required
def followuser():
    following_user_id = request.form.get("id")
    following_user_idIcode = f'{following_user_id}'
    usermail = current_user.email
    user_follow_data = Follow_data.query.filter_by(email=usermail).first()
    following = Profiles.query.filter_by(id = following_user_id).first()
    currentUser = Profiles.query.filter_by(email  = current_user.email).first()
    user_follow_list = str(user_follow_data.users).replace("'" , "").strip('][').split(', ')
    print(currentUser.reputation)
    if(user_follow_data.users == '[]'):
        final = f"['{following_user_id}']"
        following.followers = str(int(following.followers) + 1)
        user_follow_data.users  = str(final)
        currentUser.reputation = (int(currentUser.reputation) + 5)
        following.reputation = (int(following.reputation) + 5)
    elif(following_user_idIcode in user_follow_list):
        final = str(user_follow_data.users).replace("'","").strip('][').split(', ')
     
        print(final)
        print(following_user_id)
        following.followers = str(int(following.followers) - 1)
        final.remove(f'{following_user_id}')
        currentUser.reputation = (int(currentUser.reputation) - 5)
        following.reputation = (int(following.reputation) - 5)


        user_follow_data.users  = str(final).replace('"', "")
    else:
        final = str(user_follow_data.users).strip('][').split(', ')
        final.append(f"{following_user_id}")
        following.followers = str(int(following.followers) + 1)
        currentUser.reputation = (int(currentUser.reputation) + 5)
        following.reputation = (int(following.reputation) + 5)
        user_follow_data.users  = str(final).replace('"', "")

    db.session.commit()
    return f"Followed ACTION SUCCESS CODE 232 "



@app.route("/pro_feedback", methods=["GET", "POST"])
@login_required
def feedback():
    response = request.form.get("body")
    mail_thread = Thread(target=our_email_sender,args=(our_email, "Feedback From Registered User", response))
    mail_thread.start()
    flash("Thank you for your valuable feedback.")
    return redirect(url_for("bprofile"))


our_email = "aldsonrent1@gmail.com"
our_pwd = "onrent1isnowDJstartup"

def our_email_sender(to, subject, body):
    with app.app_context():
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (our_email, to, subject, body)
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(our_email, our_pwd)
            server.sendmail(our_email, to, message)
            server.close()
        except Exception as e:
            print("failed to send mail")
            print(e)


@app.route("/profile/<string:profile_username>")
def profile(profile_username):
    user = Profiles.query.filter_by(username = profile_username).first()
    owner = False
    followed = False
    if current_user.is_authenticated:
        visitor = Profiles.query.filter_by(email = current_user.email).first()
        if visitor.username == profile_username:
            owner = True
        else:
            owner = False
            
            visitor_follow_list = Follow_data.query.filter_by(email = current_user.email).first()
            follow_list = str(visitor_follow_list.users).strip('][').split(', ')
            print("FOLLOW LIST IS HERE")
            print(follow_list)
            userId  = f"'{user.id}'"
            print(userId)
            if userId in follow_list:
                followed = True
                print("FOLLOWING")
            else:
                print("NOT FOLLOWING")
    else:
        owner == False
    
    account_email = user.email
    return render_template(f"profiles/{user.username}.html",followed  = followed, user=user,profile_username = profile_username,owner = owner)





@app.route("/analytics/c119f6ff-4e4d-4bc5-bc01-921497391c0c")
@login_required
def analytics():
    return render_template("analytics.html")

@app.route("/check_user_avail" , methods = ['GET','POST'])
def check_user_avail():
    if request.method == "POST":
        username = request.form.get("username")
        if Profiles.query.filter_by(username  =  username).first():
            return "False"
        else:
            return "True"
    return "Checking"


    id = db.Column(db.Integer, primary_key=True, nullable=False)
    paper_name = db.Column(db.String(255), nullable=False)
    paper_course = db.Column(db.String(255), nullable=False)
    paper_cc = db.Column(db.String(255), nullable=False)
    paper_sem = db.Column(db.String(255), nullable=False)
    paper_year = db.Column(db.String(255), nullable=False)
    paper_faculty = db.Column(db.String(255), nullable=False)
    paper_link = db.Column(db.String(255), nullable=False)
    paper_sol_link = db.Column(db.String(255), nullable=True)
    paper_sol_by_username = db.Column(db.String(255), nullable=True)
    date_added = db.Column(db.String(255), nullable=True)


@app.route("/addpaper" , methods = ['GET' , 'POST'])
# @login_required
def addpaper():
    permission_email = ["sudhir.kumar2020@vitbhopal.ac.in","dhananjay.arne2020@vitbhopal.ac.in"]
    
    if current_user.email in permission_email:
        if request.method == "POST":
            paper_name = request.form.get("name")
            paper_course = request.form.get("course")
            paper_cc = request.form.get("cc")
            paper_sem = request.form.get("sem")
            paper_year = request.form.get("year")
            paper_faculty = request.form.get("fac")
            paper_link = request.form.get("pap_googled_link")
            paper_sol_link = request.form.get("pap_sol_googled_link")
            paper_sol_by_username = request.form.get("soluser")
            creditUser  = request.form.get("repuser")
            print("hello")
            print(creditUser)
            userep = Profiles.query.filter_by(username  = creditUser).first()
            userep.reputation = int(userep.reputation) + 10
            db.session.commit()
            newpaper = Paper(paper_name = paper_name , paper_course = paper_course, paper_cc = paper_cc , paper_sem = paper_sem , paper_year = paper_year , paper_faculty = paper_faculty , paper_link  = paper_link ,paper_sol_link = paper_sol_link, paper_sol_by_username = paper_sol_by_username, date_added = datetime.datetime.now() )
            db.session.add(newpaper)
            db.session.commit()
            flash("PAPER DETAILS ADDED SUCCESSFULLY")
            return redirect(url_for('paper'))
            
        return render_template("addpaper.html")
    else:
        return render_template("getout.html")

@app.route("/papers")
@login_required
def paper():

    papers = Paper.query.all()
    return render_template("papers.html" , papers = papers)

    
if __name__ == "__main__":
    app.run(debug = True)