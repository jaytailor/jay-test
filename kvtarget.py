def call(element,limit):
    kv=[{"phraseId": 203177, "criterias": []}]
    
    key_v=[]
    
    if(element=="values"):
        for key in range(1,limit):
            key_v.append({"expressionType": "Text", "keyName": "kv_4096_val", "keyId": 103, "operator": "==", "expressionStrings":["auto"+str(key)], "expressionIds":[key]})
    else:
        for key in range(1,limit):
            key_v.append({"expressionType": "Text", "keyName": "kv_key_"+str(key), "keyId": 0+key, "operator": "==", "expressionStrings":["value_auto"+str(key)], "expressionIds":[key]})
    
    kv[0]["criterias"]=key_v
    
    return kv
  
def call2(limit):
    kv=[]
    
    for key in range(1,limit):
        for key2 in range(1,limit2):
            kv.append({"phraseId": key,"criterias":[{"expressionType": "Text", "keyName": "key_auto_"+str(key), "keyId": 0+key, "operator": "==", "expressionStrings":["auto"+str(key)], "expressionIds":[key]}]})
    
    return kv
    
def kvincall2(element,limit):
    key_values=''
    if(element=="values"):
        for key in range(1,limit):
            if key == limit - 1:
                key_values += 'key_auto_' + str(key) +'='+'auto'+str(key)+ ';'
            else:
                key_values += 'key_auto_' + str(key) +'='+'auto'+str(key)+ ';'
    else:
        key_k=[]
        key_v=[]
        
        for key in range(1,limit):
                key_k.append('key_auto_'+str(key)) #since adserver removes kv therefore adding extra kv here
                key_v.append('auto400'+str(key))
        
        key_values = {}
        for i in range(len(key_k)):
            key_values[key_k[i]] = key_v[i]
    
    return key_values
    
def kvincall(element,limit):
    key_values=''
    if(element=="values"):
        for key in range(1,limit):
            if key == limit - 1:
                key_values += 'auto' + str(key) + ';'
            else:
                key_values += 'auto' + str(key) + ':'
    else:
        key_k=[]
        key_v=[]
        
        for key in range(1,limit):
                key_k.append('kv_key_'+str(key)) #since adserver removes kv therefore adding extra kv here
                key_v.append('value_auto'+str(key))
        
        key_values = {}
        for i in range(len(key_k)):
            key_values[key_k[i]] = key_v[i]
    
    return key_values
    
    
#print call("values",4097)

#print kvincall("values",4097)

#print call2(401)
print kvincall2("values",401)


