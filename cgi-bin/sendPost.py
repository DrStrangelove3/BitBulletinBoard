#!/usr/bin/env python2.7
import sys, xmlrpclib, base64, json, os, cgi

form = cgi.FieldStorage()

api = xmlrpclib.ServerProxy("http://username:password@127.0.0.1:8442/")

try:
    json_map = {}
    json_map["type"] = "link"
    json_map["title"] = form['title'].value
    json_map["url"] = form['url'].value
    message = api.sendMessage(form['to'].value, form['from'].value, base64.b64encode("Sent from BitBulletinBoard"), base64.b64encode(json.dumps(json_map)))

except:
    message = "PyBitmessage not running or API is not enabled."

print """\Content-Type: text/html\n
""" + message
