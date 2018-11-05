import sqlite3

import datetime,time



conn = sqlite3.connect("ClubHouseInfo.db")
cursor = conn.cursor()


# cursor.execute("""CREATE TABLE Employee_LoginManager(id INTEGER PRIMARY KEY,Username text,Date text,LogIn_Time text, LogOut_Time text)""")

#newdate = datetime.datetime.strftime('%d-%b-%y')
#endtime = datetime.datetime.strptime('%H:%M')
#starttime = '01:30'
#endtime = '18:30'

starttime = time.strftime('%H:%M')
endtime = time.strftime('%H:%M')

FMT = '%H:%M'
#print(newdate)
print(endtime)
print(starttime)



tdelta = datetime.datetime.strptime(endtime, FMT) - datetime.datetime.strptime(starttime, FMT)

#part1,part2 = str(tdelta).split(':')
#print(part2)





print(tdelta)

alter = str(tdelta)
#print(alter)

part1,part2,part3 = alter.split(':')
#print(part1)

finalvalue = part1 +":"+part2
print(finalvalue)

#finalvalue = time.strptime(tdelta,FMT)


#cursor.execute("select a.id,a.username,b.EmployeeName,a.Date,a.LogIn_Time,a.LogOut_Time,a.Lunch_Start,a.Lunch_Done,a.Total_Hrs_FD,ROUND(SUM(a.FTD_HOUR) + (SUM(a.FTD_MIN)/60.0)) as PERIOD_TIME,a.STATUS  from Employee_LoginManager a,EmployeeInfo b where a.username = b.username and a.STATUS is NOT NULL and a.date BETWEEN '2018-11-02' AND '2018-11-04' group by a.username")
#cursor.execute("select CAST((SUM(FTD_HOUR) + SUM(FTD_MIN))/60 AS VARCHAR(6)) + ':' + CAST((SUM(FTD_HOUR) + SUM(FTD_MIN))%60 AS VARCHAR(20)) as FTD  from Employee_LoginManager where date BETWEEN '2018-11-02' AND '2018-11-03'")
#cursor.execute("select round(34 + 350/60.0) as FTD  from Employee_LoginManager where date BETWEEN '2018-11-02' AND '2018-11-03'")
#cursor.execute("select *  from Employee_LoginManager where date BETWEEN '2018-11-02' AND '2018-11-04' group by username")
#cursor.execute("select * from Employee_LoginManager where date = '" + str(fromdata) + "' AND date = '" + str(enddate) + "'")
#cursor.execute("delete from Employee_LoginManager")
#cursor.execute("select a.id,a.username,b.EmployeeName,a.Date,a.LogIn_Time,a.LogOut_Time,a.Lunch_Start,a.Lunch_Done,a.Total_Hrs_FD,a.Total_Hrs_EXT,a.STATUS  from Employee_LoginManager a,EmployeeInfo b where a.username = b.username and a.STATUS is NOT NULL and a.date BETWEEN '2018-11-02' AND '2018-11-03'")
#cursor.execute("insert INTO EmployeeInfo (EmployeeName,Username,Employee_Type,Employement_Type,DOB,status,Designation,JoinedDate) VALUES ('ClubHouse Tech Admin','admin','ADMIN','FTE','2018-11-04','ACTIVE','ADMINISTRATOR','2018-11-04')")
#cursor.execute("select * from Employee_LoginCred_Info")
#cursor.execute("INSERT INTO Employee_LoginCred_Info (Username,EmployeeType) VALUES ('admin','ADMIN')")
conn.commit()
select_user = ("select * from EmployeeInfo where id = '1'")
cursor.execute(select_user)
value = cursor.fetchone()
username = value[3]
print(username)
#cursor.execute("SELECT sql FROM sqlite_master WHERE tbl_name='EmployeeInfo'")
totalhour = 8
if totalhour == 8:
    STATUS = "OK"
    print(STATUS)
elif totalhour > 8:
    STATUS = "MORE"
    print(STATUS)
elif totalhour < 8:
    STATUS = "Less"
    print(STATUS)


print(cursor.fetchall())