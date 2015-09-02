#!/usr/bin/python
import sqlite3, json, xmlrpclib, time, base64, imghdr


def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError, e:
    return False
  return True


conn = sqlite3.connect('BulletinBoard.db')
c = conn.cursor()

#Initiate the tables if they don't exist
c.execute("CREATE TABLE IF NOT EXISTS posts(timestamp REAL, msgid TEXT, chanAddress TEXT, chanLabel TEXT, poster TEXT, title TEXT, type TEXT, url TEXT, updown TEXT, upvotes INTEGER DEFAULT 0, downvotes INTEGER DEFAULT 0)")
c.execute("CREATE TABLE IF NOT EXISTS votes(timestamp REAL, voter TEXT, parent TEXT, updown TEXT)")

#Get all messages from pyBitmessage
api = xmlrpclib.ServerProxy("http://username:password@127.0.0.1:8442/")
inbox = json.loads(api.getAllInboxMessages())

#Get the chans to find the messages to delete
allAddresses = json.loads(api.listAddresses())['addresses']
chans = []
addresses = []
for address in allAddresses:
    if (address['chan'] == 1):
        chans.append(address['address'])
    else:
        addresses.append(address['address'])
        

for message in inbox['inboxMessages']:
    try:
        messageID = message['msgid']
        payloadJSON = json.loads(base64.b64decode(message['message']).decode('UTF-8'))
            
        if payloadJSON['type'] == 'link' and not c.execute("SELECT * FROM posts WHERE msgid = ? LIMIT 1", (messageID, )).fetchone():
            output = c.execute("""INSERT INTO posts(timestamp, msgid, chanAddress, poster, title, type, url) VALUES(?, ?, ?, ?, ?, ?, ?)""", (str(time.time()), messageID, message['toAddress'], message['fromAddress'], payloadJSON['title'], payloadJSON['type'], payloadJSON['url']))
            conn.commit()
            
        elif payloadJSON['type'] == 'vote' and not c.execute("SELECT * FROM votes WHERE voter = ? AND parent = ? LIMIT 1", (message['fromAddress'], payloadJSON['parent'])).fetchone():
            c.execute("INSERT INTO votes(timestamp, voter, parent, updown) VALUES(?, ?, ?, ?)", (str(time.time()), message['fromAddress'], payloadJSON['parent'], payloadJSON['updown']))
            if message['fromAddress'] in addresses:
                c.execute("UPDATE posts SET updown= ? WHERE msgid= ?", (payloadJSON['updown'], payloadJSON['parent']))
            conn.commit()
            
        elif payloadJSON['type'] == 'image' and not c.execute("SELECT * FROM posts WHERE msgid = ? LIMIT 1", (messageID, )).fetchone():
            imageData = payloadJSON['img'].decode('base64')
            imageFormat = imghdr.what('filename', imageData);
            open("files/" + messageID + "." + imageFormat, 'wb').write(imageData)
            c.execute("INSERT INTO posts(timestamp, msgid, chanAddress, poster, title, type, url) VALUES(?, ?, ?, ?, ?, 'image', ?)", (str(time.time()), messageID, message['toAddress'], message['fromAddress'], payloadJSON['title'], "files/" + messageID + "." + imageFormat))
            conn.commit()

    except ValueError, e:
        print("Warning: Not valid JSON, skipped!")
    
    #Delete unneeded messages
    if message['toAddress'] in chans and is_json(base64.b64decode(message['message']).decode('UTF-8')):
        api.trashMessage(message['msgid'])