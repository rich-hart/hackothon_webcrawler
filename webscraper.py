from lxml import html
import requests

page = requests.get('http://houston.novusagenda.com/agendapublic/MeetingView.aspx?MeetingID=121&MinutesMeetingID=156&doctype=Minutes')
tree = html.fromstring(page.content)

