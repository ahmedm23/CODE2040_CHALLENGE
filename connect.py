# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 17:15:16 2016

@author: ahmedmoalim
"""
import json 
import http.client

url  = 'challenge.code2040.org' 
httpServer = http.client.HTTPConnection(url)
keys = json.dumps({'token': 'befdeea19c258349d4baebaa94ff93e0',             
                   'github': 'https://github.com/ahmedm23/CODE2040_CHALLENGE'})               
headers = {'Content-type': 'application/json'}


def connect():
    httpServer = http.client.HTTPConnection(url)

    headers = {'Content-type': 'application/json'}
    httpServer.request('POST', '/api/register', keys, headers) 
    connectionStatus = httpServer.getresponse()  
    return connectionStatus
    
def getString(path, token):
    httpServer.request('POST', path, json.dumps({'token':token}), headers) 
    conn = httpServer.getresponse()
    string = conn.read().decode('utf-8')   
    print(string)    
    return string
    
    
def sendString(path, token, string)     :
    httpServer.request('POST', path, json.dumps({'token':token, 'string' : string}), headers) 
    
    
connect    
string = getString('/api/reverse', 'befdeea19c258349d4baebaa94ff93e0')
sendString('/api/reverse/validate', 'befdeea19c258349d4baebaa94ff93e0', string[::-1])