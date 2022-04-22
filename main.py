import os
import sqlite3
from flask import *
from werkzeug.utils import secure_filename

app=Flask(__name__)

uploads_dir = os.path.join(app.static_folder, 'image/movie')
app.secret_key='1234567890yuhfsdjbuycgdjkjbsdg'

@app.route('/')
def main():
    con = sqlite3.connect("Movie_Adda.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from movies;")
    rows = cur.fetchall()
    return render_template('home.html',rows=rows)

@app.route('/user_login')
def user_login():
    return render_template('user_login.html')

@app.route('/user_register')
def user_register():
    return render_template("user_register.html")

@app.route('/admin_login')
def admin_login():
    return render_template('admin_login.html')

@app.route('/check_user', methods=['POST'])
def userlogin():
    t=''
    userpassword=''
    username=''
    try:
        email=request.form['user_email']
        with sqlite3.connect('Movie_Adda.db') as con:
            s="select Name,Password from user where Email=?;"
            result=con.execute(s,(email,))
            for row in result:
                username=row[0]
                userpassword=row[1]
            session['user_name']=username
    except Exception as e:
        t=e
    finally:
        password=request.form['user_password']
        if userpassword==password:
            con = sqlite3.connect("Movie_Adda.db")
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("select * from movies;")
            rows = cur.fetchall()
            #return render_template('home.html', rows=rows)
            return render_template('home_logedin.html',rows=rows,username=session['user_name'])
        else:
            return "<h1 align='center'>Invalid credentials</h1>"


@app.route('/user_registered', methods=['POST'])
def user_registered():
    t=''
    try:
        name = request.form['user_name']
        mobile = request.form['user_mobile']
        gender = request.form['gender']
        email = request.form['user_mail']
        dob = request.form['user_dob']
        place = request.form['user_place']
        password = request.form['user_password']
        with sqlite3.connect('Movie_Adda.db') as con:
            cur = con.cursor()
            s = "insert into user (Name,Mobile,Gender,Email,Date_of_Birth,Place,Password) values(?,?,?,?,?,?,?);"
            cur.execute(s, (name, mobile, gender, email, dob, place, password))
    except Exception as e:
        t=e
    finally:
        return redirect('/user_login')

@app.route('/undefined')
def undefined():
    con = sqlite3.connect("Movie_Adda.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from movies;")
    rows = cur.fetchall()
    return render_template('home.html', rows=rows)

@app.route('/theater/undefined')
def undefined2():
    con = sqlite3.connect("Movie_Adda.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from movies;")
    rows = cur.fetchall()
    return render_template('home.html', rows=rows)

@app.route('/theater_registration')
def theater_registration():
    return render_template('theater_registration.html')

@app.route('/go_back')
def go_back():
    return render_template("admin.html")

@app.route('/check_admin',methods=['POST'])
def check_admin():
    session['username']=''
    adminpassword=''
    try:
        name=request.form['user_name']
        session['username']=name
        with sqlite3.connect('Movie_Adda.db') as con:
            s='select Password from theater where Owner_name=?;'
            result=con.execute(s,(name,))
            for row in result:
                adminpassword=row[0]
    except Exception as e:
        return "{}".format(e)
    finally:
        password = request.form['user_password']
        if password=='12345' and name=='admin':
            return render_template('admin.html')
        elif password==adminpassword:
            return render_template('theater.html',username=session['username'])
        else:
            return "<h1 align='center'>Invalid credentials</h1>"


@app.route('/register_theater',methods=['POST'])
def register_theater():
    t=''
    try:
        owner=request.form['owner_name']
        password=request.form['theater_password']
        theater=request.form['theater_name']
        place=request.form['place']
        timing=request.form['timing']
        food=request.form['food']
        nos=request.form['number_of_screen']
        with sqlite3.connect('Movie_Adda.db') as con:
            cur=con.cursor()
            s='insert into theater (Owner_Name,Password,Theater_Name,Place,Timing,Food,Number_Of_Screen) values (?,?,?,?,?,?,?);'
            cur.execute(s,(owner,password,theater,place,timing,food,nos))
    except Exception as e:
        t=e
    finally:
        return redirect('/admin_login')

@app.route('/add_movie_btn')
def add_movie_btn():
    con = sqlite3.connect("Movie_Adda.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from theater;")
    rows = cur.fetchall()
    return render_template('Add_Movie.html',rows=rows)
    #return "{}".format(rows)

@app.route('/add_movie', methods=['POST'])
def add_main():
    t=''
    movie = request.form['movie_name']
    picture = request.files['file']
    picture.save(os.path.join(uploads_dir, secure_filename(movie + ".png")))
    try:
        movie=request.form['movie_name']
        desc=request.form['desc']
        theater=request.form['theater']
        duration=request.form['duration']
        releasedate=request.form['release_date']
        rating=request.form['rating']
        languagesavailable=request.form['languages_available']
        genre=request.form['genre']
        ticketcost=request.form['ticket_cost']
        trailer=request.form['trailer']
        picname = movie + '.png'
        with sqlite3.connect('Movie_Adda.db') as con:
            cur=con.cursor()
            s='insert into movies values (?,?,?,?,?,?,?,?,?,?,?);'
            cur.execute(s,(movie,theater,duration,releasedate,rating,languagesavailable,genre,ticketcost,picname,desc,trailer))
    except Exception as e:
        return "{}".format(e)
    finally:
        return render_template("admin.html")

@app.route('/view_movie')
def view_movie():
    con = sqlite3.connect("Movie_Adda.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from movies;")
    rows = cur.fetchall()
    return render_template('View_movie.html', rows=rows)

@app.route('/delMov/')
def delete_movie():
    row=''
    try:
        moviename=request.args.get('movie')
        with sqlite3.connect("Movie_Adda.db") as con:
            cur = con.cursor()
            s=("delete from movies where Movie_Name=?")
            cur.execute(s,(moviename,))
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("select * from movies;")
            rows = cur.fetchall()
    except Exception as e:
        return '{}'.format(e)
    finally:
        return render_template('View_movie.html', rows=rows)

@app.route("/updMov/")
def update_movie():
    con = sqlite3.connect("Movie_Adda.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from theater;")
    rows = cur.fetchall()
    return render_template("Update_Movie.html",rows=rows)

@app.route("/update_movie",methods=['POST'])
def update_movie_detail():
    row = ''
    movie = request.form['movie_name']
    picture = request.files['file']
    picture.save(os.path.join(uploads_dir, secure_filename(movie + ".png")))
    try:
        movie = request.form['movie_name']
        duration = request.form['duration']
        releasedate = request.form['release_date']
        rating = request.form['rating']
        languagesavailable = request.form['languages_available']
        genre = request.form['genre']
        ticketcost = request.form['ticket_cost']
        desc=request.form['desc']
        picname = movie + '.png'
        with sqlite3.connect('Movie_Adda.db') as con:
            cur = con.cursor()
            s = 'update movies set Movie_Name=? ,Duration=? ,Release_Date=? ,Ratings=? ,Languages_available=? ,Genre=? ,Ticket_cost=?,Image=?,Description=? where Movie_Name=?;'
            cur.execute(s, (movie, duration, releasedate, rating, languagesavailable, genre, ticketcost,picname,desc,movie))
    except Exception as e:
        return "{}".format(e)
    finally:
        return render_template('admin.html')

@app.route('/view_theater')
def view_theater():
    con = sqlite3.connect("Movie_Adda.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from theater;")
    rows = cur.fetchall()
    return render_template("view_theater.html",rows=rows)

@app.route('/delthe/')
def delete_theater():
    row=''
    try:
        id=request.args.get('id')
        with sqlite3.connect("Movie_Adda.db") as con:
            cur = con.cursor()
            s=("delete from theater where ID=?")
            cur.execute(s,(id,))
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("select * from theater;")
            rows = cur.fetchall()
    except Exception as e:
        return '{}'.format(e)
    finally:
        return render_template('View_movie.html', rows=rows)

@app.route('/theater/')
def theater_page():
    session['moviename']=request.args.get('movie')
    con = sqlite3.connect("Movie_Adda.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select theater.Theater_Name,theater.Place,theater.Timing,theater.Number_Of_Screen,movies.Movie_Name from theater inner join movies on theater.Theater_Name=movies.Theater_Name where Movie_name=?;",(session['moviename'],))
    rows = cur.fetchall()
    res=cur.execute("select Image from movies where Movie_Name=?",(session['moviename'],))
    for i in res:
        session['image']=i[0]
    return render_template("theater_page.html", rows=rows,username=session['username'],moviename=session['moviename'],image=session['image'])

@app.route('/seat_page/')
def seat_page():
    session['theatername'] = request.args.get('theater')
    var=''
    session['ticketcost']=''
    with sqlite3.connect('Movie_Adda.db') as con:
        cur=con.cursor()
        res=cur.execute('select Ticket_cost from movies where Movie_Name=? and Theater_Name=? ',(session['moviename'],session['theatername']))
        for row in res:
            var=row[0]
        session['ticketcost']=var
    return render_template('seatView.html',ticket=session['ticketcost'])

@app.route('/view_collection')
def view_collection():
    con = sqlite3.connect("Movie_Adda.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from payment;")
    rows = cur.fetchall()
    return render_template('view_collection.html', rows=rows)

@app.route('/deldet/')
def deldet():
    try:
        name=request.args.get('name')
        with sqlite3.connect("Movie_Adda.db") as con:
            cur = con.cursor()
            s=("delete from payment where Username=?")
            cur.execute(s,(name,))
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("select * from payment;")
            rows = cur.fetchall()
    except Exception as e:
        return '{}'.format(e)
    finally:
        return render_template('view_collection.html', rows=rows)

@app.route('/seat',methods=['POST'])
def seat():
    return render_template('payment_page.html')

@app.route('/go_home')
def go_home():
    con = sqlite3.connect("Movie_Adda.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from movies;")
    rows = cur.fetchall()
    return render_template('home.html', rows=rows)

@app.route('/?')
def go_home2():
    con = sqlite3.connect("Movie_Adda.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from movies;")
    rows = cur.fetchall()
    return render_template('home.html', rows=rows)

@app.route('/success',methods=['POST'])
def success():
    name = session['user_name']
    movie = session['moviename']
    cost = session['ticketcost']
    try:
        with sqlite3.connect('Movie_Adda.db') as con:
            cur=con.cursor()
            s='insert into payment values(?,?,?);'
            cur.execute(s,(name,movie,cost))
    except Exception as e:
        return '{}'.format(e)
    finally:
        return render_template('success.html')

if __name__=='__main__':
    app.run(debug=True)