# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 17:15:16 2016

@author: ahmedmoalim
"""
import json 
import http.client

url  = 'challenge.code2040.org' 
httpServer = http.client.HTTPConnection(url)
token = 'befdeea19c258349d4baebaa94ff93e0'
keys = json.dumps({'token': token,             
                   'github': 'https://github.com/ahmedm23/CODE2040_CHALLENGE'})               
headers = {'Content-type': 'application/json'}
httpServer = http.client.HTTPConnection(url)

def connect (path, requestKey):
    httpServer.request('POST', path, requestKey, headers) 
    return httpServer.getresponse()  
    
def getString(path, requestKey): 
    conn = connect(path, requestKey)   
    string = conn.read().decode('utf-8')   
    return string   
    
def getNeedle(path, requestKey):
    conn = connect(path, requestKey) 
    dict = conn.read().decode('utf-8')
    print (dict)

connect('/api/register', keys)   
string = getString('/api/reverse', json.dumps({'token':token}))
connect('/api/reverse/validate', json.dumps({'token':token, 'string' : string[::-1]}))
getNeedle('/api/haystack', token)