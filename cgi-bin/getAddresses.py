#!/usr/bin/env python2.7
import sys, json, collections, xmlrpclib

api = xmlrpclib.ServerProxy("http://username:password@127.0.0.1:8442/")
addresses = json.loads(api.listAddresses())['addresses']

object_list = []
for address in addresses:
    if (address['chan'] == 0):
        d = collections.OrderedDict()
        d['address'] = address['address']
        d['label'] = address['label']
        object_list.append(d)

json_objects = json.dumps(object_list)
sys.stdout.write("Content-type: application/json\r\n\r\n")
sys.stdout.write("")
sys.stdout.write("{\"addresses\":")
sys.stdout.write(json_objects)
sys.stdout.write("}")
