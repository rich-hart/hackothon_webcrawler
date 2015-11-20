from lxml import html
import requests

url_list = [ 'http://houston.novusagenda.com/agendapublic/MeetingView.aspx?MeetingID=121&MinutesMeetingID=156&doctype=Minutes',
             'http://houston.novusagenda.com/agendapublic/MeetingView.aspx?MeetingID=111&MinutesMeetingID=155&doctype=Minutes',
           ]

page = requests.get('http://houston.novusagenda.com/agendapublic/MeetingView.aspx?MeetingID=121&MinutesMeetingID=156&doctype=Minutes')
tree = html.fromstring(page.content)


############

#from scrapy.linkextractors import LinkExtractor

#links=LinkExtractor(allow_domains='http://houston.novusagenda.com/agendapublic')
