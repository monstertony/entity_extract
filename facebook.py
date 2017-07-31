__author__ = 'xyang'

import urllib2

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}
url = 'https://www.facebook.com/1277788352283578'
req = urllib2.Request(url, headers=headers)
content = urllib2.urlopen(req)
print req
