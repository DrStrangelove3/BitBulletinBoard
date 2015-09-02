#!/usr/bin/env python
import cgi, json, os, xmlrpclib, base64
import cgitb; cgitb.enable()

try: # Windows needs stdio set for binary mode.
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass

form = cgi.FieldStorage()

# A nested FieldStorage instance holds the file
fileitem = form['file']

# Test if the file was uploaded
if fileitem.filename:
   
    # strip leading path from file name to avoid directory traversal attacks
    fn = os.path.basename(fileitem.filename)

    encoded_string = base64.b64encode(fileitem.file.read())
    api = xmlrpclib.ServerProxy("http://username:password@127.0.0.1:8442/")

    try:
        json_map = {}
        json_map["type"] = "image"
        json_map["title"] = form['title'].value
        json_map["img"] = encoded_string
        message = api.sendMessage(form['to'].value, form['from'].value, base64.b64encode("Sent from BitBulletinBoard"), base64.b64encode(json.dumps(json_map)))
        #message = api.sendMessage(form['to'].value, form['from'].value, base64.b64encode("Sent from BitBulletinBoard"), base64.b64encode("{\"type\":\"image\", \"title\":\"" + form['title'].value.replace("\\","\\\\").replace("\'","\"").replace("\"","\\\"") + "\",\"img\":\"" + encoded_string + "\"}"))
    except:
        message = "PyBitmessage not running or API is not enabled."
   
else:
    message = 'No file to uploaded'
   
print """\Content-Type: text/html\n
""" + message
