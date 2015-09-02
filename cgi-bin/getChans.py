#!/usr/bin/python
import sys, json, collections, xmlrpclib, sqlite3

api = xmlrpclib.ServerProxy("http://username:password@127.0.0.1:8442/")
addresses = json.loads(api.listAddresses())['addresses']

conn = sqlite3.connect('BulletinBoard.db')
c = conn.cursor()

object_list = []
for address in addresses:
    if (address['chan'] == 1):
        c.execute("UPDATE posts SET chanLabel= '" + address['label'] + "' WHERE chanAddress= '" + address['address'] + "'")
        d = collections.OrderedDict()
        d['address'] = address['address']
        d['label'] = address['label']
        object_list.append(d)
        
conn.commit()
conn.close()

json_objects = json.dumps(object_list)
sys.stdout.write("Content-type: application/json\r\n\r\n")
sys.stdout.write("")
sys.stdout.write("{\"chans\":")
sys.stdout.write(json_objects)
sys.stdout.write("}")