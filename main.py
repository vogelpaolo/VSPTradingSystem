#!/usr/bin/env python
# -*- coding:utf-8 -*-

#TOUT LE DEVELOPPEMENT SERA FAIT EN PYTHON 3

"""Connection et récupération de données via l'API de ETORO premier test"""
import http.client, urllib.request, urllib.parse, urllib.error, base64

#headers = {
    # Request headers
 #   'Ocp-Apim-Subscription-Key': '{subscription key}',
#}

#params = urllib.parse.urlencode({
#})

#try:
 #   conn = http.client.HTTPSConnection('api.etoro.com')
  #  conn.request("GET", "/Discover/V1/MetaData?%s" % params, "{body}", headers)
   # response = conn.getresponse()
    #data = response.read()
    #print(data)
    #conn.close()
#except Exception as e:
 #   print("[Errno {0}] {1}".format(e.errno, e.strerror))