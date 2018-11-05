import sqlite3,time,datetime

import datetime

#conn = sqlite3.connect("MedicareInfo.db")

conn = sqlite3.connect("ClubHouseInfo.db")
cursor = conn.cursor()

#cursor.execute("""CREATE TABLE MedicareInfo(id INTEGER PRIMARY KEY, carriercode text,effectivedate text, endDate text,lastMaintenanceTimeStamp text, memberID text, contractID text,policyID text, recordCreateTimeStamp text,status text,userid text)""")

#cursor.execute("""CREATE TABLE EmployeeInfo(id INTEGER PRIMARY KEY, EmployeeName text,Username text,Employee_Type text,Employement_Type text,DOB text,status text)""")


#cursor.execute("""CREATE TABLE Employee_LoginCred_Info(Username text,Password text)""")

#cursor.execute("drop table EmployeeInfo")


#cursor.execute("""CREATE TABLE MEDICARE_MANUAL_FILE (id INTEGER PRIMARY KEY,FILE_NAME text,LOAD_STATUS text,REMARKS text,INSERT_USERID text)""")

#cursor.execute("""CREATE TABLE MEDICARE_RECORD_DETAILS (id INTEGER PRIMARY KEY,FILE_NAME text,ACTION_IND text,CARRIER_CODE text,POLICY_ID text,CONTRACT_ID text,MEMBER_ID text,END_DT text,STATUS text,REMARK text,INSERT_USERID text)""")

#cursor.execute("INSERT INTO MedicareInfo VALUES (null, 'MED A B', '20130101', '99991231', '20130122101249034571','01','001464494A','20130122101249034554')")

#cursor.execute("INSERT INTO EmployeeInfo VALUES (null, 'DIVYA', 'FULL_TIME', 'Active', 'Admin')")

#cursor.execute("INSERT INTO Employee_LoginCred_Info (Username) VALUES ('nsingh')")

#cursor.execute("update Employee_LoginCred_Info set EmployeeType = 'ADMIN' where Username = 'admin'")
#cursor.execute("ALTER TABLE EmployeeInfo ADD DepartureDate text")
#cursor.execute("""CREATE TABLE Employee_LoginManager(id INTEGER PRIMARY KEY,Username text,Date text,LogIn_Time text, LogOut_Time text,Lunch_Start text,Lunch_Done text, Total_Hrs_FD text,Total_Hrs_EXT text,FTD_HOUR text,FTD_MIN text,STATUS text,LogOut_Clock text,LunchIn_Clock text,LunchOut_Clock text)""")
# LogOut_Clock text
# ,LunchIn_Clock text,LunchOut_Clock text;
#values = 'null'
#print(values)

#cursor.execute("INSERT INTO MedicareInfo (carriercode,effectivedate,endDate,lastMaintenanceTimeStamp,memberID,contractID,policyID,recordCreateTimeStamp) VALUES('MED A B', '20170301', '20180516', '20180516122927081125', '01', '117082131', '002426195A', '20170220140839245609')")
#cursor.execute("delete from EmployeeInfo")
#cursor.execute("delete from Employee_LoginCred_Info")
#cursor.execute("delete from Employee_LoginManager")
#cursor.execute("Drop table MEDICARE_RECORD_DETAILS")

#cursor.execute("Drop table Employee_LoginManager")

#cursor.execute('INSERT INTO Employee_LoginCred_Info (Password) VALUES (test) where Username = ' + str('nsingh'))
conn.commit()

#cursor.execute("select ACTION_IND,CARRIER_CODE,POLICY_ID,CONTRACT_ID,MEMBER_ID from MEDICARE_RECORD_DETAILS")

#cursor.execute("select * from MedicareInfo where status = 'INPROGRESS' and userid = 'nsingh'")

#cursor.execute("select FILE_NAME from MEDICARE_MANUAL_FILE where LOAD_STATUS = 'UPD_SUCCESS' and INSERT_USERID = 'nsingh'")


cursor.execute("select * from Employee_LoginManager") #where date = '29-May-18' AND date = '29-May-18'")
# #cursor.execute("delete from Employee_LoginManager where date = '11-Jun-2018'")
# #conn.commit()
# row = cursor.fetchone()
# #print(row)
# print(row[0])
# newdate = time.strftime('%Y-%d-%m')
# #row = cursor.fetchone()
# print(row[1])
#
# print('logintime : ' + row[3])
# print('logouttime : ' + row[4])
# print('Lunchintime : ' + row[5])
# print('LunchoutTime : ' + row[6])
#
# FMT = '%H:%M'
# #print(newdate)
#
# #tdelta = datetime.datetime.strptime(endtime, FMT) - datetime.datetime.strptime(starttime, FMT)
#
# logtotal = datetime.datetime.strptime(row[4],FMT) - datetime.datetime.strptime(row[3],FMT)
# print(logtotal)
# #checktime = datetime.datetime.strptime(logtotal, '%h:%M')
# #print(checktime)
# convertlogtotal = str(logtotal)
# #logformat = datetime.datetime.strptime(logtotal,FMT)
# part1,part2,part3 = convertlogtotal.split(':')
# #finalvaluelog = part1+":"+part2
# loghour = part1
# logminute = part2
# #print(finalvaluelog)
# lunchtotal = datetime.datetime.strptime(row[6],FMT) - datetime.datetime.strptime(row[5],FMT)
# convertlunchtotal = str(lunchtotal)
# part1,part2,part3 = convertlunchtotal.split(':')
# lunchhour = part1
# Lunchminute = part2
#
# totalhour = int(loghour) + int(lunchhour)
# print( totalhour)
# totalminute = int(logminute) + int(Lunchminute)
# print(totalminute)
# print(str(totalhour) + ' Hour ' + str(totalminute) + ' minute ')
#
# #finalvaluelunch = part1+":"+part2
# #print(finalvaluelunch)
# #NEWFMT = '%H:%M'
# #totalhours = time.strptime(finalvaluelog, NEWFMT) + time.strptime(finalvaluelunch, NEWFMT)
# #print(totalhours)
# #print(newdate)
# #print(row[1])
# #print(cursor.fetchall())