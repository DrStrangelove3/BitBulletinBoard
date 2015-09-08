#!/usr/bin/env python2.7
import sys, sqlite3, json, collections

conn = sqlite3.connect('BulletinBoard.db')
c = conn.cursor()
rows = c.execute("SELECT * FROM posts ORDER BY (upvotes - downvotes) DESC")
object_list = []
for row in rows:
    #print(row)
    d = collections.OrderedDict()
    d['timestamp'] = row[0]
    d['msgid'] = row[1]
    d['chanAddress'] = row[2]
    d['chanLabel'] = row[3]
    d['poster'] = row[4]
    d['title'] = row[5] #.replace("\'","\\\'").replace("\"","\\\"")
    d['type'] = row[6]
    d['url'] = row[7]
    d['updown'] = row[8]
    d['upvotes'] = row[9]
    d['downvotes'] = row[10]
    object_list.append(d)
conn.close()
json_objects = json.dumps(object_list)
sys.stdout.write("Content-type: application/json\r\n\r\n")
sys.stdout.write("")
sys.stdout.write("{\"posts\":")
sys.stdout.write(json_objects)
sys.stdout.write("}")
