#!/usr/bin/python
import sys, sqlite3, json, collections

conn = sqlite3.connect('BulletinBoard.db')
c = conn.cursor()
msgids = c.execute("SELECT msgid FROM posts").fetchall()

for msgid in msgids:
    down = c.execute("SELECT COUNT(*) AS votes FROM votes WHERE parent='" + msgid[0] + "' AND updown='down'").fetchone()
    c.execute("UPDATE posts SET downvotes = '" + str(down[0]) + "' WHERE msgid = '" + msgid[0] + "'")

conn.commit()
conn.close()
