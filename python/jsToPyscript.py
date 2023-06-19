import js
import json

strCodeHTML = js.jsGlobalStrCodeHTML
strCodeRecovery = js.jsGlobalStrCodeRecovery
stringKeys = js.jsGlobalStringKeys

json_array = json.loads(stringKeys)
stringKeys_list = []

for item in json_array:
    store_details = {"id":None, "value":None, "number":None}
    store_details['id'] = item['id']
    store_details['value'] = item['value']
    store_details['number'] = item['number']
    stringKeys_list.append(store_details)

print(stringKeys_list)
print(dir(js))
print(strCodeHTML)
print(strCodeRecovery)
print(stringKeys)
#from js import pruebaVar
#import { pruebaVar } from 'desdeJS'
#print(pruebaVar)
