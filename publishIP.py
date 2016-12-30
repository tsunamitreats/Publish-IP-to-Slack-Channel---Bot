import urllib
import json
from slacker import Slacker
import sqlite3

#This program requires you to get a slack API and make a sqlite3 database with the following settings: 
#	Sqlite3, db=ip, table=ip, columns=(name UNIQUE, ip text).

slackAPI = 'yourAPI'
slackRoom = '#yourchannel'

#get live ip
raw = urllib.urlopen('https://wtfismyip.com/json')
data = json.load(raw)
liveip = data['YourFuckingIPAddress']

#Get old IP from DB
conn = sqlite3.connect('ip')
c = conn.cursor()
c.execute("""SELECT ip from ip where name = 'IP'""")
oldipraw = c.fetchone()
oldip = oldipraw[0] #unicode
conn.close()

if liveip != oldip:
	#post message
	slack = Slacker(slackAPI)
	message = ("Your fucking IP: " + liveip)
	slack.chat.post_message(slackRoom, message)
	#Store IP in DB for check later.  
	conn = sqlite3.connect('ip')
	c = conn.cursor()
	c.execute("""UPDATE ip set ip = ? where name = 'IP'""",(liveip,))
	conn.commit()
	conn.close()
