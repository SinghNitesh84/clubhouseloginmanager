import paramiko, os
from lib import EnvDetails,ConfigValues
import re

nbytes = 4096
#ParmFilepath = ConfigValues.ParmFlileLoc + ConfigValues.ParmFileName
InfoloadSetupFile = ConfigValues.homepath + ConfigValues.InfoloadFileName
client = paramiko.Transport((EnvDetails.hostname, 22))
client.connect(username=EnvDetails.hostname_username, password=EnvDetails.hostname_Password)


session = client.open_channel(kind='session')
sftp = paramiko.SFTPClient.from_transport(client)
# try :
#     sftp.remove(ParmFilepath)
# except IOError as err:
#     print(err)
# sftp.put(ConfigValues.ParmFileName,ParmFilepath)
# sftp.chmod(ParmFilepath, 0o777)
# try :
#     sftp.remove(InfoloadSetupFile)
# except IOError as err:
#     print(err)
# sftp.put(ConfigValues.InfoloadFileName,InfoloadSetupFile)
# sftp.chmod(InfoloadSetupFile, 0o777)
sftp.close()

stdout_data = []
stderr_data = []
session.exec_command(ConfigValues.run_wf)
while True:
    if session.recv_ready():
        stdout_data.append(session.recv(nbytes))
    if session.recv_stderr_ready():
        stderr_data.append(session.recv_stderr(nbytes))
    if session.exit_status_ready():
        break
session.close()
client.close()
exit_sts_cd = session.recv_exit_status()
#for a in stdout_data:
#    print(str(a,"utf-8"))

try:
    if exit_sts_cd!= 0:
        raise ValueError('Error on workflow execution')
except ValueError as err:
    print(err)
#return exit_sts_cd
