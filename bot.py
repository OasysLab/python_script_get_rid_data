import time
import datetime
import json
import urllib2
while(True):
    print("CheckData At "+str(datetime.datetime.now()))
    data = urllib2.urlopen("http://crflood.com/crflood/boat/get_data_rid.php")
    resp = data.read()
    print(str(resp))
    time.sleep(900)

