# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 17:15:16 2016

@author: ahmedmoalim
"""
import json 
import http.client
import datetime
import dateutil.parser as dp

url  = 'challenge.code2040.org' # API URL to connect.
token = json.dumps({'token':'befdeea19c258349d4baebaa94ff93e0'}) # Unique token for API.
headers = {'Content-type': 'application/json'}
httpServer = http.client.HTTPConnection(url)

# Creates a new json key using the strings passed in.
def createKey(key, value):
    return  json.dumps({'token': 'befdeea19c258349d4baebaa94ff93e0', key : value})

# Pulls infromation from the API.
def connect(path, connectkeys):
    httpServer.request('POST', path, connectkeys, headers) 
    connectionStatus = httpServer.getresponse()  
    return connectionStatus.read().decode('utf-8')

# Sends infromation back to the API.
def sendResponse(path, key, value):
    httpServer.request('POST', path, createKey(key, value), headers) 
    return httpServer.getresponse().read()     

# Finds the needle in the haystack.    
def searchHaystack(dictionary, firstIndexName, secondIndexName):
    identifyer = dictionary.get(firstIndexName)
    searchArray = dictionary.get(secondIndexName)
    prefixArray = []
    
    for index in range(len(searchArray)):
        # I believed using a series of if else staments here was better then 
        # Dictionary mapping. Python does not have any switch case staments to my knowledge        
        if(firstIndexName == "needle" and identifyer == searchArray[index]):
            return index
        elif firstIndexName == "prefix" and not (searchArray[index].startswith(identifyer)):    
            prefixArray.append(searchArray[index])            
            
    return prefixArray

# Adds a time interval to a date in ISO 80 format
def addTimeIntervall(date, secs, utcOffset):
    standerdTime = dp.parse(date)    
    return convertToIso(standerdTime + datetime.timedelta(seconds=secs), utcOffset)

#Converts for Standered Date Object to ISO 8601 format
def convertToIso(date, utcOffset):
    date = date.isoformat().split('+')
    return date[0]+ utcOffset 
                 
# STEP 1
try:
    connect('/api/register', createKey('github',
                                       'https://github.com/ahmedm23/CODE2040_CHALLENGE'))   
except http.client.HTTPException:
    print('\n' + "Error in connecting to " + url)
    
# STEP 2
string = connect('/api/reverse', token)
sendResponse('/api/reverse/validate', 'string', string[::-1])

# STEP 3
dictionary = connect('/api/haystack', token)
index = searchHaystack(json.loads(dictionary), "needle", "haystack")
sendResponse('/api/haystack/validate', 'needle', index)

# STEP 4
dictionary = connect('/api/prefix', token)
prefixArray = searchHaystack(json.loads(dictionary), "prefix", "array")
sendResponse('/api/prefix/validate', 'array', prefixArray)

# STEP 5
dictionary = connect('/api/dating', token)
date = json.loads(dictionary).get('datestamp')
utcOffset = date[-1:] 
secs = json.loads(dictionary).get('interval')
newDate = addTimeIntervall(date, secs, utcOffset)
sendResponse('/api/dating/validate', 'datestamp', newDate)