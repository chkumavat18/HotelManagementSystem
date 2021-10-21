from logging import fatal
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.ext.automap import automap_base


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///c:\\users\\user\\desktop\\minor_project_db\\userDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Base = automap_base()
Base.prepare(db.engine, reflect=True)
General = Base.classes.general_login_details
Guest = Base.classes.guest_login
Staff = Base.classes.staff_login
Room = Base.classes.room_book

@app.route('/')
def hms():
    return render_template('hms.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')

@app.route('/proceed', methods=["POST"])
def proceed():
    
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    address = request.form.get("address")
    aadhar = request.form.get("aadhar")
    phone = request.form.get("phone")
    bed_type = request.form.get("b_t")
    acc = request.form.get("acc")
    add = request.form.get("add")
    c_i = request.form.get("c_i")
    c_o = request.form.get("c_o")
    pay_opt = request.form.get("pay_opt")
    pay_gate = request.form.get("pay_gate")
    
    if first_name != '' and last_name != '' and address != '' and aadhar is not None and phone != '' and bed_type != '' and acc != '' and add != '' and c_i != '' and c_o != '':
        room =  Room(First_Name=first_name, Last_Name=last_name, Address=address, Aadhar_No=aadhar, Phone=phone, Bed_Type=bed_type, Accommod=acc, Add_Accommod=add, Check_In=c_i, Check_Out=c_o, Pay_Opt=pay_opt, Pay_Gate=pay_gate)
        db.session.add(room)
        db.session.commit()

        return redirect('/booking')


@app.route('/catering')
def catering():
    return render_template('catering.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')    

@app.route('/directory')
def directory():
    return render_template('directory.html')       

@app.route('/event')
def event():
    return render_template('event.html')   

@app.route('/forget')
def forget():
    return render_template('forget.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/GAMEBOOK')
def GAMEBOOK():
    return render_template('GAMEBOOK.html') 

@app.route('/gservice')
def gservice():
    return render_template('gservice.html')  

@app.route('/guest')
def guest():
    return render_template('guest.html')
           
@app.route('/guestroom')
def guestroom():
    return render_template('guestroom.html')   

@app.route('/login')
def login():
    #guest = Guest.query.all()
    return render_template('login.html')

@app.route('/login1')
def login1():
    return render_template('login1.html')

@app.route('/manager')
def manager():
    return render_template('manager.html')

@app.route('/manager1')
def manager1():
    return render_template('manager1.html')

@app.route('/meetinghall')
def meetinghall():
    return render_template('meetinghall.html')

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/create', methods=["POST"])
def create():
    
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    aadhar = request.form.get("aadhar")
    phone = request.form.get("phone")
    account_type = request.form.get("a_t")
    
    if first_name != '' and last_name != '' and aadhar is not None and phone != '' and account_type != '':
        gen_log =  General(First_Name=first_name, Last_Name=last_name, Aadhar_No=aadhar, Phone=phone, A_T=account_type)
        db.session.add(gen_log)
        db.session.commit()

        if account_type == 'GUEST':
            return redirect('/login')

        else:
            return redirect('/login1')
    
@app.route('/partyhal')
def partyhal():
    return render_template('partyhal.html')

@app.route('/pool')
def pool():
    return render_template('pool.html')

@app.route('/reception')
def reception():
    return render_template('reception.html')  

@app.route('/renew')
def renew():
    return render_template('renew.html')   

@app.route('/room')
def room():
    return render_template('room.html')

@app.route('/rservice')
def rservice():
    return render_template('rservice.html')      

@app.route('/staff')
def staff():
    return render_template('staff.html')

@app.route('/trans')
def trans():
    return render_template('trans.html') 

@app.route('/TRY')
def TRY():
    return render_template('TRY.html')

@app.route('/VISIT')
def VISIT():
    return render_template('VISIT.html') 

@app.route('/wedding_hall')
def wedding_hall():
    return render_template('wedding_hall.html')



    

if __name__=="__main__":
    app.run(debug=True)    
