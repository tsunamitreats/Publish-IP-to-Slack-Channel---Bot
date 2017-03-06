import subprocess
import sqlite3
from slacker import Slacker

#This program requires you to get a slack API and make a sqlite3 database with the following settings:
#       Sqlite3, db=iplocal, table=ip, columns=(name UNIQUE, ip text).
#	Then write a record IP: c.execute("INSERT INTO ip VALUES ('name','12345')")
# I know I reverence hard location.  Things were breaking with my local cron, so I did this quick workaround.  

slackAPI = 'slackAPI'
slackRoom = '#slackRoom'

#Get live - all local network interfaces.  This won't work on Windows.
liveip = subprocess.check_output(['/home/pi/slackPrivateIP/privateIP.sh'], shell=True)

#Get old local IPs from DB
conn = sqlite3.connect('/home/pi/slackPrivateIP/localip')
c = conn.cursor()
c.execute("""SELECT ip from ip where name = 'name'""")
oldipraw = c.fetchone()
oldip = oldipraw[0] #unicode
conn.close()

if liveip != oldip:
    #post message
    slack = Slacker(slackAPI)
    liveip = str(liveip)
    message = ("Your LOCAL IPs: " + liveip)
    slack.chat.post_message(slackRoom, message)
    #Store IP in DB for check later.
    conn = sqlite3.connect('/home/pi/slackPrivateIP/localip')
    c = conn.cursor()
    c.execute("""UPDATE ip set ip = ? where name = 'name'""",(liveip,))
    conn.commit()
    conn.close()
