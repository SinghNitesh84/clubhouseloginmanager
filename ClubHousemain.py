import os
from flask import Flask,request,render_template,make_response,session,g
import requests
import json
import sqlite3
import datetime,time
app = Flask(__name__)
app.secret_key = os.urandom(24)
conn = sqlite3.connect("ClubHouseInfo.db")
cursor = conn.cursor()

@app.before_request
def before_request():
    g.user = None
    session.permanent = True
    app.permanent_session_lifetime = datetime.timedelta(minutes=20)
    session.modified = True
    if 'user' in session:
        g.user = session['user']

@app.route('/CLUBHOUSEHOME/')
def home():
    return render_template('clubhousemain.html')


@app.route('/CLUBHOUSELOGIN/')
def login():
    return render_template('CLUBloginHome.html')

@app.route('/ClubHouseAdmin/')
def admin():
    if g.user:
        return render_template('ClubHouseAdminmain.html')
    else:
        error = "Please Login Again ,User Session Not Valid !"
        return render_template('CLUBloginHome.html', error=error)


# @app.route('/ClubHouseselectapp/')
# def app():
#     if request.method == "POST":
#         value = request.form['sel1']
#         print(value)
#         if value == "RegisterNewEmployee":
#             return render_template('CLubHouseAppHome.html')
#         elif value == "ExtractTimeSheet":
#             return render_template('CLubHouseAppHome.html')
#         elif value == "BackupTimeSheet":
#             return render_template('CLubHouseAppHome.html')
#     else:
#         return render_template("error.html")
#     #return render_template('CLubHouseAppHome.html')

@app.route('/registeremp/', methods=["GET","POST"])
def registeremp():
    if g.user:
        if request.method == "POST":
            employmenttype = request.form['sel1']
            employeename = request.form['Name']
            Username = request.form['Username']
            dob = request.form['dob']
            designation = request.form['designation']
            employeetype = request.form['sel2']
            status = 'ACTIVE'
            JoinedDate = time.strftime('%Y-%m-%d')
            data = (employeename, Username, employeetype, employmenttype, dob,status,designation,JoinedDate)
            userdata = (Username,employeetype)
            conn = sqlite3.connect("ClubHouseInfo.db")
            cursor = conn.cursor()
            select_qury = ("select Username from EmployeeInfo where Username = '" + str(Username) + "'")
            cursor.execute(select_qury)
            row = cursor.fetchone()
            if row is None:
                insert_query = 'INSERT INTO EmployeeInfo (EmployeeName,Username,Employee_Type,Employement_Type,DOB,status,Designation,JoinedDate)VALUES' + str(data)
                print(insert_query)
                cursor.execute(insert_query)
                #ins_query = 'INSERT INTO Employee_LoginCred_Info (Username,EmployeeType) VALUES' ('" + str(Username) + "')"
                ins_query = 'INSERT INTO Employee_LoginCred_Info (Username,EmployeeType) VALUES' + str(userdata)
                print(ins_query)
                cursor.execute(ins_query)
                conn.commit()
                error = "Congratulations , Employee registered Successfully !!!"
                return render_template("clubregistersuccess.html", error=error)
            else:
                error = "Username already exist , Please use different Username and try registration again !!!"
                return render_template("clubregistersuccess.html", error=error)
    else:
        error = "Please Login Again ,User Session Not Valid !"
        return render_template('CLUBloginHome.html', error=error)


@app.route('/passwordregister/', methods=["GET","POST"])
def passwordregist():
    if request.method == "POST":
        User = request.form['user']
        passwo = request.form['passwd']
        Cpasswo = request.form['newpasswd']
        print(User)
        conn = sqlite3.connect("ClubHouseInfo.db")
        cursor = conn.cursor()
        if User == '':
            error = "Please enter Username, Username cannot be Empty !!!"
            return render_template("CLUBloginHome.html", error=error)
        elif User is not None:
            cursor.execute("select * from Employee_LoginCred_Info where Username='" + str(User) + "'")
            row = cursor.fetchone()
            print(row)
            if row is None:
                error = "Username doesn't exist, Please check with Administrator !"
                return render_template('CLUBloginHome.html', error=error)
            elif row is not None and passwo == Cpasswo:
                update_stmt = "update Employee_LoginCred_Info set Password = '" + str(passwo) + "' where Username = '" + str(User) + "'"
                print(update_stmt)
                cursor.execute(update_stmt)
                conn.commit()
                error = "Congratulation User Activated Successfully, Please login with New Credentials !!!"
                return render_template("CLUBloginHome.html", error=error)
            else:
                error = "Passwords do not Match, Please try Activating Again !!! / Contact Administrator !!!"
                return render_template("CLUBloginHome.html", error=error)
    #else:
    #    error = "Please Login Again ,User Session Not Valid !"
    #    return render_template('CLUBloginHome.html', error=error)

@app.route('/ValidateUser/', methods=['GET','POST'])
def validateuser():
    error = None
    if request.method == "POST":
        session.pop('user', None)
        username = request.form['username']
        # print(username)
        password = request.form['password']
        conn = sqlite3.connect("ClubHouseInfo.db")
        cursor = conn.cursor()
        cursor.execute("select EmployeeType from Employee_LoginCred_Info where Username='" + str(username) + "' and Password='" + str(password) + "'")
        row = cursor.fetchone()

        if row is None:
            error="Invalid Username/Password ! If you are FirstTime User please REGISTER !"
            return render_template('CLUBloginHome.html', error=error)
        else:
            part1, part2 = str(row).split(',')
            part3, part4 = str(part1).split('(')

            Admin = str(part4).replace("'", "")

            Adminvalue = 'ADMIN'
            if Admin==Adminvalue:
                print("Admin Login")
                session['user'] = request.form['username']
                resp = make_response(render_template("ClubHouseAdminmain.html"))
                resp.set_cookie('userID', username)
                return resp
                #return render_template('ClubHouseAdminmain.html')
            else:
                print("Employee Login")
                session['user'] = request.form['username']
                resp = make_response(render_template("clubattendance.html"))
                resp.set_cookie('userID', username)
                return resp
                #return render_template('clubattendance.html')
    else:
        return render_template('error.html')

@app.route('/CLUBHOUSEATTENDANCE/',methods=['GET','POST'])
def attendance():
    if g.user in session:
        return render_template('clubattendance.html')
    else:
        error = "Please Login Again ,User Session Not Valid !"
        return render_template('CLUBloginHome.html', error=error)
#cursor.execute("select * from Employee_LoginCred_Info")


@app.route('/loginattendance/', methods=['GET','POST'])
def loginattendance():
    #if g.user:
    #newdate = time.strftime('%d-%b-%y')
    newdate = time.strftime('%Y-%m-%d')
    starttime = time.strftime('%H:%M')
    Username = request.cookies.get('userID')
    dummytime = '00:00'
    clock = 'N'
    conn = sqlite3.connect("ClubHouseInfo.db")
    cursor = conn.cursor()
    cursor.execute("select * from Employee_LoginManager where Date = '" + str(newdate) + "' and Username='" + str(Username) + "'")
    row = cursor.fetchone()
    if row is None:
        ldata = (Username,newdate,starttime, starttime,dummytime,dummytime,dummytime,clock,clock,clock)
        logdata = 'INSERT INTO Employee_LoginManager (Username,Date,LogIn_Time,LogOut_Time,Lunch_Start,Lunch_Done,Total_Hrs_FD,LogOut_Clock,LunchIn_Clock,LunchOut_Clock)VALUES' + str(ldata)
        print(logdata)
        cursor.execute(logdata)
        conn.commit()
        error = "Successfully logged In for the Day, Have a Great DAY !!!"
        return render_template("clubloginsuccess.html", error=error)
    else:
        error = "You already recorded your WELCOME - IN time for the Day , Please Contact Administrator Incase of any question."
        return render_template("clubloginsuccess.html", error=error)
    return render_template('error.html')
    #else:
     #   error = "Please Login Again ,User Session Not Valid !"
      #  return render_template('CLUBloginHome.html', error=error)


@app.route('/logoutattendance/', methods=['GET','POST'])
def logoutattendance():
    if g.user:

        #newdate = time.strftime('%d-%b-%y')
        newdate = time.strftime('%Y-%m-%d')
        starttime = time.strftime('%H:%M')
        Username = request.cookies.get('userID')
        dummytime = '00:00'
        conn = sqlite3.connect("ClubHouseInfo.db")
        cursor = conn.cursor()
        cursor.execute("select * from Employee_LoginManager where Date = '" + str(newdate) + "' and Username='" + str(Username) + "'")
        row = cursor.fetchone()
        if row is None:
            # ldata = (Username,newdate,starttime, starttime,dummytime,dummytime,dummytime)
            # logdata = 'INSERT INTO Employee_LoginManager (Username,Date,LogIn_Time,LogOut_Time,Lunch_Start,Lunch_Done,Total_Hours)VALUES' + str(ldata)
            # print(logdata)
            # cursor.execute(logdata)
            # conn.commit()
            error = "ALERT | You have not recorded WELCOME - IN for the day, Please WELCOME - IN first and then try GOODBYE - OUT !!!"
            return render_template("clubloginsuccess.html", error=error)
        else:
            cursor.execute("select LogOut_Clock from Employee_LoginManager where Date = '" + str(newdate) + "' and Username='" + str(Username) + "'")
            row = cursor.fetchone()
            part1, part2 = str(row).split(',')
            part3, part4 = str(part1).split('(')
            print(part4)
            out = str(part4).replace("'", "")
            if out == 'N':
                updatestmt = (" update Employee_LoginManager set LogOut_Time = '" + str(starttime) + "',LogOut_Clock='Y' where Date = '" + str(newdate) + "' and Username='" + str(Username) + "'")
                cursor.execute(updatestmt)
                conn.commit()
                error = "Successfully logged Out for the Day, See you tomorrow !!!"
                return render_template("clubloginsuccess.html", error=error)
            else:
                error = "You already recorded your GOODBYE - OUT time for the Day , Please Contact Administrator Incase of any question."
                return render_template("clubloginsuccess.html", error=error)
    else:
        error = "Please Login Again ,User Session Not Valid !"
        return render_template('CLUBloginHome.html', error=error)


@app.route('/lunchoutattendance/', methods=['GET','POST'])
def lunchoutattendance():
    if g.user:
        #newdate = time.strftime('%d-%b-%y')
        newdate = time.strftime('%Y-%m-%d')
        starttime = time.strftime('%H:%M')
        Username = request.cookies.get('userID')
        dummytime = '00:00'
        conn = sqlite3.connect("ClubHouseInfo.db")
        cursor = conn.cursor()
        cursor.execute("select * from Employee_LoginManager where Date = '" + str(newdate) + "' and Username='" + str(Username) + "'")
        row = cursor.fetchone()
        if row is None:
            # ldata = (Username,newdate,starttime, starttime,starttime,starttime,dummytime)
            # logdata = 'INSERT INTO Employee_LoginManager (Username,Date,LogIn_Time,LogOut_Time,Lunch_Start,Lunch_Done,Total_Hours)VALUES' + str(ldata)
            # print(logdata)
            # cursor.execute(logdata)
            # conn.commit()
            error = "ALERT | You have not recorded WELCOME-IN time for the day, Please LOG - IN first and then try recording Lunch - OUT !!!"
            return render_template("clubloginsuccess.html", error=error)
        elif row is not None:
            cursor.execute("select LunchOut_Clock,LunchIn_Clock from Employee_LoginManager where Date = '" + str(newdate) + "' and Username='" + str(Username) + "'")
            row = cursor.fetchone()
            # part1, part2 = str(row).split(',')
            # part3, part4 = str(part1).split('(')
            # print(part4)
            lunchout = row[0]
            print(lunchout)
            lunchin = row[1]
            print(lunchin)
            if lunchout == 'N':
                updatestmt = (" update Employee_LoginManager set Lunch_Start = '" + str(starttime) + "',LunchOut_Clock = 'Y' where Date = '" + str(newdate) + "' and Username='" + str(Username) + "'")
                cursor.execute(updatestmt)
                conn.commit()
                error = "Successfully logged Out for Lunch break !!!"
                return render_template("clubloginsuccess.html", error=error)
            # elif lunchin == 'N':
            #     error = "ALERT ! You have not recorded Lunch - IN time for the Day , Please record Lunch - IN time and then retry Lunch - OUT"
            #     return render_template("clubloginsuccess.html", error=error)
            else:
                error = "You already recorded your Lunch - START time for the Day , Please Contact Administrator Incase of any question."
                return render_template("clubloginsuccess.html", error=error)
        return render_template('error.html')
    else:
        error = "Please Login Again ,User Session Not Valid !"
        return render_template('CLUBloginHome.html', error=error)


@app.route('/lunchinattendance/', methods=['GET','POST'])
def lunchinattendance():
    if g.user:
        #newdate = time.strftime('%d-%b-%y')
        newdate = time.strftime('%Y-%m-%d')
        starttime = time.strftime('%H:%M')
        #Username = 'dsingh'
        Username = request.cookies.get('userID')
        dummytime = '00:00'
        conn = sqlite3.connect("ClubHouseInfo.db")
        cursor = conn.cursor()
        cursor.execute("select * from Employee_LoginManager where Date = '" + str(newdate) + "' and Username='" + str(Username) + "'")
        row = cursor.fetchone()
        if row is None:
            # ldata = (Username,newdate,starttime, starttime,starttime,starttime,dummytime)
            # logdata = 'INSERT INTO Employee_LoginManager (Username,Date,LogIn_Time,LogOut_Time,Lunch_Start,Lunch_Done,Total_Hours)VALUES' + str(ldata)
            # print(logdata)
            # cursor.execute(logdata)
            # conn.commit()
            error = "ALERT | You have not Logged in for the day, Please LOG - IN first and then try recording Lunch - IN !!!"
            return render_template("clubloginsuccess.html", error=error)
        elif row is not None:
            cursor.execute("select LunchIn_Clock,LunchOut_Clock from Employee_LoginManager where Date = '" + str(newdate) + "' and Username='" + str(Username) + "'")
            row = cursor.fetchone()
            # part1, part2 = str(row).split(',')
            # part3, part4 = str(part1).split('(')
            # print(part4)
            lunchin = row[0]
            lunchout = row[1]
            if lunchin == 'N' and lunchout == 'Y':
                updatestmt = (" update Employee_LoginManager set Lunch_Done = '" + str(starttime) + "',LunchIn_Clock = 'Y' where Date = '" + str(newdate) + "' and Username='" + str(Username) + "'")
                cursor.execute(updatestmt)
                conn.commit()
                error = "Welcome back, Successfully logged In again !!!"
                return render_template("clubloginsuccess.html", error=error)
            elif lunchout == 'N':
                error = "ALERT ! You have not recorded Lunch - START time for the Day , Please record Lunch - START time and then retry Lunch - DONE"
                return render_template("clubloginsuccess.html", error=error)
            else:
                error = "You already recorded your Lunch - DONE time for the Day , Please Contact Administrator Incase of any question."
                return render_template("clubloginsuccess.html", error=error)
        return render_template('error.html')
    else:
        error = "Please Login Again ,User Session Not Valid !"
        return render_template('CLUBloginHome.html', error=error)

@app.route('/extractemp/', methods=["GET","POST"])
def extractemp():
    if g.user:
        if request.method == "POST":
            fromdata = request.form['fromdate']
            enddate = request.form['enddate']
            print(fromdata)
            print(enddate)
            conn = sqlite3.connect("ClubHouseInfo.db")
            cursor = conn.cursor()
            select_qury = ("select * from Employee_LoginManager where date BETWEEN '" + str(fromdata) + "' AND '" + str(enddate) + "' AND STATUS is NULL")
            cursor.execute(select_qury)
            print(select_qury)
            # cursor.execute("delete from Employee_LoginManager where date = '11-Jun-2018'")
            # conn.commit()
            row = cursor.fetchall()
            print(row)
            for i in row:
                # print(row)
                print(i[0])
                recordid = i[0]
                newdate = time.strftime('%Y-%m-%d')
                # row = cursor.fetchone()
                print(i[1])
                print('logintime : ' + i[3])
                print('logouttime : ' + i[4])
                print('Lunchintime : ' + i[5])
                print('LunchoutTime : ' + i[6])
                FMT = '%H:%M'
                print(newdate)
                logtotal = datetime.datetime.strptime(i[4], FMT) - datetime.datetime.strptime(i[3], FMT)
                print(logtotal)
                convertlogtotal = str(logtotal)
                part1, part2, part3 = convertlogtotal.split(':')
                loghour = part1
                logminute = part2
                lunchtotal = datetime.datetime.strptime(i[6], FMT) - datetime.datetime.strptime(i[5], FMT)
                convertlunchtotal = str(lunchtotal)
                part1, part2, part3 = convertlunchtotal.split(':')
                lunchhour = part1
                Lunchminute = part2
                totalhour = int(loghour) + int(lunchhour)
                print(totalhour)
                totalminute = int(logminute) + int(Lunchminute)
                print(totalminute)
                print(str(totalhour) + ' Hour ' + str(totalminute) + ' minute ')
                Total_time_FD = (str(totalhour) + ' Hour ' + str(totalminute) + ' minute ')
                if totalhour == 8:
                    STATUS = "WORKED 8 HOURS"
                    print(STATUS)
                elif totalhour > 8:
                    STATUS = "OVERTIME"
                    print(STATUS)
                elif totalhour < 8:
                    STATUS = "DEFAULTER"
                    print(STATUS)
                updatequery = ("update Employee_LoginManager set Total_Hrs_FD = '" + str(Total_time_FD) + "',FTD_HOUR = '" + str(totalhour) + "',FTD_MIN = '" + str(totalminute) + "',STATUS = '" + str(STATUS) + "' where id ='" + str(recordid) + "'")
                cursor.execute(updatequery)
                conn.commit()
            select_round = ("select username,ROUND(SUM(FTD_HOUR) + (SUM(FTD_MIN)/60.0)) as PERIOD_TIME from Employee_LoginManager where date BETWEEN '" + str(fromdata) + "' AND '" + str(enddate) + "' group by username")
            cursor.execute(select_round)
            print(select_round)
            row = cursor.fetchall()
            print(row)
            for j in row:
                print(j[0])
                print(j[1])
                user = j[0]
                totaltime = j[1]
                updatequery = ("update Employee_LoginManager set Total_Hrs_EXT = '" + str(totaltime) + "' where username ='" + str(user) + "'")
                cursor.execute(updatequery)
                conn.commit()
            #select_qury = ("select a.id,a.username,b.EmployeeName,a.Date,a.LogIn_Time,a.LogOut_Time,a.Lunch_Start,a.Lunch_Done,a.Total_Hrs_FD,ROUND(SUM(a.FTD_HOUR) + (SUM(a.FTD_MIN)/60.0)) as PERIOD_TIME,a.STATUS  from Employee_LoginManager a,EmployeeInfo b where a.username = b.username and a.STATUS is NOT NULL and a.date BETWEEN '" + str(fromdata) + "' AND '" + str(enddate) + "' group by a.username")
            select_qury = ("select a.id,a.username,b.EmployeeName,a.Date,a.LogIn_Time,a.LogOut_Time,a.Lunch_Start,a.Lunch_Done,a.Total_Hrs_FD,a.Total_Hrs_EXT,a.STATUS  from Employee_LoginManager a,EmployeeInfo b where a.username = b.username and a.STATUS is NOT NULL and a.date BETWEEN '" + str(fromdata) + "' AND '" + str(enddate) + "'")
            print(select_qury)
            cursor.execute(select_qury)
            finalrow = cursor.fetchall()
            return render_template("ClubHouseAttenDetails.html", row=finalrow)
    else:
        error = "Please Login Again ,User Session Not Valid !"
        return render_template('CLUBloginHome.html', error=error)

@app.route("/UPDATEEMPLOYEE/")
def UPDATEEMPLOYEE():
    if g.user:
        conn = sqlite3.connect("ClubHouseInfo.db")
        cursor = conn.cursor()
        select_qury = ("select * from EmployeeInfo")
        cursor.execute(select_qury)
        finalrow = cursor.fetchall()
        return render_template("ClubHouseEmployeeDetails.html", row=finalrow)
    else:
        error = "Please Login Again ,User Session Not Valid !"
        return render_template('CLUBloginHome.html', error=error)

@app.route("/terminateempl/<item>")
def terminateempl(item):
    if g.user:
        usertoexit = item
        TerminateDate = time.strftime('%Y-%m-%d')
        conn = sqlite3.connect("ClubHouseInfo.db")
        cursor = conn.cursor()
        select_user = ("select * from EmployeeInfo where id ='" + str(usertoexit) + "'")
        cursor.execute(select_user)
        value = cursor.fetchone()
        #part1, part2 = str(value).split(',')
        # print(part1)
        #part3, part4 = str(part1).split('(')
        username = value[2]
        print(username)
        deletequery = ("delete from Employee_LoginCred_Info where Username = '" + str(username) + "'")
        cursor.execute(deletequery)
        conn.commit()
        updatequery = ("update EmployeeInfo set STATUS = 'INACTIVE',DepartureDate = '" + str(TerminateDate) + "' where id ='" + str(usertoexit) + "'")
        cursor.execute(updatequery)
        conn.commit()
        select_qury = ("select * from EmployeeInfo")
        cursor.execute(select_qury)
        finalrow = cursor.fetchall()
        return render_template("ClubHouseEmployeeDetails.html", row=finalrow)
    else:
        error = "Please Login Again ,User Session Not Valid !"
        return render_template('CLUBloginHome.html', error=error)

@app.route("/activateempl/<item>")
def activateempl(item):
    if g.user:
        usertoexit = item
        JoinedDate = time.strftime('%Y-%m-%d')
        conn = sqlite3.connect("ClubHouseInfo.db")
        cursor = conn.cursor()
        select_user = ("select * from EmployeeInfo where id ='" + str(usertoexit) + "'")
        cursor.execute(select_user)
        value = cursor.fetchone()
        #part1, part2 = str(value).split(',')
        # print(part1)
        #part3, part4 = str(part1).split('(')
        username = value[2]
        employeetype = value[3]
        print(username)
        userdata = (username, employeetype)
        ins_query = 'INSERT INTO Employee_LoginCred_Info (Username,EmployeeType) VALUES' + str(userdata)
        print(ins_query)
        cursor.execute(ins_query)
        conn.commit()
        #TerminateDate = ''
        updatequery = ("update EmployeeInfo set STATUS = 'ACTIVE',DepartureDate='',JoinedDate = '" + str(JoinedDate) + "' where id ='" + str(usertoexit) + "'")
        cursor.execute(updatequery)
        conn.commit()
        select_qury = ("select * from EmployeeInfo")
        cursor.execute(select_qury)
        finalrow = cursor.fetchall()
        return render_template("ClubHouseEmployeeDetails.html", row=finalrow)
    else:
        error = "Please Login Again ,User Session Not Valid !"
        return render_template('CLUBloginHome.html', error=error)


if __name__ == "__main__":
    app.run()