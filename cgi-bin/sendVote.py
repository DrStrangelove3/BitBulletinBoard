#!/usr/bin/python
import xmlrpclib, base64, json, os, cgi

form = cgi.FieldStorage()

api = xmlrpclib.ServerProxy("http://username:password@127.0.0.1:8442/")
json_map = {}
json_map["type"] = "vote"
json_map["updown"] = form['updown'].value
json_map["parent"] = form['parent'].value
message = api.sendMessage(form['to'].value, form['address'].value, base64.b64encode("Sent from BitBulletinBoard"), base64.b64encode(json.dumps(json_map)))

print """\Content-Type: text/html\n
""" + message