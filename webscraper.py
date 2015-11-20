from lxml import html
import requests

import sqlite3 as lite

url = 'http://houston.novusagenda.com/agendapublic/MeetingView.aspx?MeetingID=121&MinutesMeetingID=156&doctype=Minutes'

page = requests.get(url)

content = "this is web content"  #unicode(page.content)

tree = html.fromstring(page.content)



con = lite.connect('website.db')

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Webdata(Url TEXT, Content TEXT)")
    cur.execute("INSERT INTO Webdata VALUES( ?, ?)",(url,content))  
