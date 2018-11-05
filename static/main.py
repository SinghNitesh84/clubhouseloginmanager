
from flask import Flask, render_template, request, url_for, redirect, flash
from ldap3 import Server, Connection, SIMPLE, SYNC, ALL, SASL, NTLM, Tls, LEVEL,SUBTREE#
from flask_mail import Mail,Message
import requests
#import AuthenticateLDAP
#import FileRead
import Configuration
import os, platform
from Crypto.Cipher import DES

app = Flask(__name__)

@app.route('/MadtownSpace/')
def MadtownSpace():
    return render_template('Homepage.html')
    #return render_template('.html')

@app.route('/Loginform/')
def loginhome():
    return render_template('loginHome.html')
    #return render_template('.html')


@app.route('/MadtownHome/')
def MadtownHome():
    print("#### Read the Configuration #####")
   
    currentfile = open(Configuration.currentfilepath)
    
    currentread = currentfile.read()
    replacedvalue = currentread.replace('%','')
    currentfile.close()
    return render_template("main.html",nameTXT=replacedvalue)

@app.route('/CurrentConfig/<nameTXT>', methods=["GET"])
def ReadFile(nameTXT):
    print("#### Read the Configuration #####")
    currentfile = open(Configuration.currentfilepath)
    currentread = currentfile.read()
    replacedvalue = currentread.replace('%','')
    currentfile.close()
    return render_template("main.html",nameTXT=replacedvalue)

@app.route('/UpdateConfig/',methods=["GET","POST"])
def updateconfig():
    try:

        if request.method == "POST":
            value = request.form['sel1']
            print(value)

            print("#### START THE REPLACEMENT #####")
            originalfile = open(Configuration.CommercialConfpath)
            originalfilegov = open(Configuration.GovernmentConfpath)
            currentfile = open(Configuration.currentfilepath)
            currentread = currentfile.read()
            data = originalfile.read()
            datagov = originalfilegov.read()
            # print("AFTER")
            # print(data.replace(currentr,))
            r = data.replace(currentread, value)
            rg = datagov.replace(currentread, value)
            print("LOADED VARIABLE")
            print(r)
            print(rg)

            print("#### REPLACED THE DATA ###### ")
            replaceoriginalfile = open(Configuration.CommercialConfpath, 'w')
            replaceoriginalfile.write(r)
            replaceoriginalfile.close()
            replaceoriginalfilegov = open(Configuration.GovernmentConfpath, 'w')
            replaceoriginalfilegov.write(rg)
            replaceoriginalfilegov.close()
            replacecurrentfile = open(Configuration.currentfilepath, 'w')
            replacecurrentfile.write(value)
            replacecurrentfile.close()
            originalfile.close()
            originalfilegov.close()
            currentfile.close()
            #print("Before")
            #print(r)

            #return redirect(url_for('homepage'))
            return render_template("header.html")

    except Exception as e:
        flash(e)
        return redirect(url_for('MadtownHome'))

@app.route('/Rebill/', methods=["GET"])
def Rebill():
    return render_template("Rebill.html")


@app.route('/RebillGovernment/')
def RebillGOV():
    try:
        runningfile = open(Configuration.GovernmentStatus)
        runningread = runningfile.read()
        if runningread == "RUNNING":
            return render_template('tryagain.html')
        else:
            sendrequest = requests.get('http://DHP2EEBE9:1001/Test')
            if (sendrequest.status_code == 200):
                #return render_template('/Happy/')
                return redirect(url_for('happy'))
            else:
                return render_template('error.html')
    except Exception as f:
        return render_template('error.html')

@app.route('/Happy/', methods=["GET"])
def happy():
    return render_template('Happy.html')


@app.route('/RebillCommercial/')
def RebillCOMM():
    try:
        runningcomm = open(Configuration.CommercialStatus)
        readcomm = runningcomm.read()
        if readcomm == "RUNNING":
            return render_template('tryagain.html')
        else:
            sendrequest = requests.get('http://DHP2EEBE9:1001/Test')
            if (sendrequest.status_code == 200):
                #return render_template('/Happy/')
                return redirect(url_for('happy'))
            else:
                return render_template('error.html')
    except Exception as t:
        return render_template('error.html')

@app.route('/ValidateUser/', methods=["GET","POST"])
def Authenticateuser():
    try:
        error=None
        if request.method == "POST":
            username = request.form['username']
            password = request.form['password']
            #if AuthenticateLDAP.authenticateuser.userdetails(self=username,Username=username,Password=password) == "SUCCESS":
            #if username == "nsingh":
            #receive request data
            strUin = username
            strP = password
            print(strUin)

            #inspect incoming username and password & perform transformations if needed====
            if strP.startswith("\\\"") and strP.endswith("\\\""):
                strXform = strP
                strXform = strXform[1:]
                strXform = strXform[:-1]
                strP = strXform
            elif strP.startswith('\"') and strP.endswith('\"'):
                strXform = strP
                strXform = strXform[1:]
                strXform = strXform[:-1]
                strP = strXform
            if strUin.startswith('\"') and strUin.endswith('\"'):
                strXform = strUin
                strXform = strXform[1:]
                strXform = strXform[:-1]
                strUin = strXform
            strU = strUin
            strUwDomain = "dhp\\" + strU
            print(strUwDomain)

            #key = platform.node()
            #key = key[0:8]
            #des = DES.new(key, DES.MODE_ECB)
            #with open(Configuration.strCredFilePath, 'rb') as site_file:                
                #strLine = site_file.read()
                #site_file.close()
                #encInput = strLine
                #strPassword = ((str((des.decrypt(encInput))))[2:50]).strip()

            #Bind with LDAPS cred for search operation====================================
            objTLS = Tls(ca_certs_file='/opt/flaskproject/MadtownWebapp/TrustedCertCollection.txt')
            #C:\inetpub\wwwroot\apps\RebillApp\TrustedCertCollection.txt
            objLDAPServer = Server('dhpdc1.dhp.ad.deanhealth.com', use_ssl=False, get_info=ALL) #tls=objTLS)
            #objLDAPServer = Server('dhp.ad.deanhealth.com', use_ssl=false, get_info=ALL)#, tls=objTLS)
            objLDAPConn = Connection(objLDAPServer, user="dhp\\kabldaptest02", password="TurboAgile38!", authentication=NTLM)
            #objLDAPConn = Connection(objLDAPServer, user="dhp\\BIA_MadtnSpaceLDAP", password=strPassword, authentication=NTLM)
            objLDAPConn.bind()
            #print(objLDAPConn.bind())

            #Search to assess group membership=============================================
            strSearchBlock = '(&(objectclass=user)(samaccountname=' + strU + '))'
            objLDAPConn.search('dc=dhp,dc=ad,dc=deanhealth,dc=com', strSearchBlock, attributes = ['sn','objectclass','distinguishedname','memberOf'])
            arrAppGroups = []
            #print(objLDAPConn.entries[0].memberof)
            arrUserMemberOf = objLDAPConn.entries[0].memberof

            boolMemberCriteriaMet = "False"

            #Perform authentication test for source user===================================
            objAuthUserLDAPConn = Connection(objLDAPServer, user=strUwDomain, password=strP, authentication=NTLM)
            print(strUwDomain)

            if not objAuthUserLDAPConn.bind():
                strReplyMsg = 'Invalid Username/Password ! Please check your Credentials and Try Again !!!'
                #print('console troubleshooting message - failed authentication') #if you want to see the result code: objAuthUserLDAPConn.result
                #print('console troubleshooting message - User-Name received: ' + strU)
                #print('console troubleshooting message - User-Password received: ' + strP)
                print(strReplyMsg)
                #return strReplyMsg
                return render_template('loginHome.html',error=strReplyMsg)
                #sys.exit(1)
            else:
                #print('console troubleshooting message - successful authentication')
                for objGroup in sorted(arrUserMemberOf):
                    if "S_AppInformaticaDevUser" in str(arrUserMemberOf):
                        boolMemberCriteriaMet = "True"
                if boolMemberCriteriaMet == "True":
                    strReplyMsg = 'SUCCESS'
                    print(strReplyMsg)
                    #return strReplyMsg
                    return redirect(url_for('MadtownHome'))
                    #sys.exit(0)
                else:
                    strReplyMsg = 'Reply-Message = "failed authorization|successful authentication but not member of security group"'
                    print(strReplyMsg)
                    #return strReplyMsg
                    return render_template('loginHome.html',error=strReplyMsg)
                    #sys.exit(1)
                #return redirect(url_for('MadtownHome'))
                #return render_template("main.html")      
        else:
            error = "Invalid Username/Password ! If you don't have access to this app please REGISTER !"
            strReplyMsg = error
            return render_template('loginHome.html',error=strReplyMsg)
    except Exception as e:
        flash(e)
        error = "Invalid Username/Password ! If you don't have access to this app please REGISTER !"
        return render_template('loginHome.html',error=error)
        #return render_template('error.html')


mail=Mail(app)

app.config['MAIL_SERVER']='exchange.deanhealth.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USERNAME'] = None
app.config['MAIL_PASSWORD'] = None
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = False


mail = Mail(app)

@app.route("/email/" ,methods=['GET','POST'])
def email():

    if request.method == 'POST':
        username = request.form['username']
        print(username)
        message = request.form['message']
        #print(password)
        #print('Username is')
        #print(Authenticateuser.username)
        userid=username+'@deancare.com'

        msg = Message('REBILL WEBAPP Reporting from PRODUCTION!', sender = userid, recipients = ['DL-DHP-BEMadtownInnovators@ssmhc.com'])
        msg.body = message
        mail.send(msg)
        return render_template('HappyError.html')
    else:
        return render_template('error.html')

@app.errorhandler(500)
def internal_error(exception):
    app.logger.exception(exception)
    file_handler = RotatingFileHandler('C:\inetpub\wwwroot\logs.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('microblog startup')
    return render_template('500.html'), 500 

if __name__ == "__main__":
    #app.run(debug=True)
	app.run(host='0.0.0.0',debug=True)
