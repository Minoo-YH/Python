import json

dataJSON = {
 "name":"John Doe" ,
 'age' :51 ,
 'occupation' : 'carpenter'
}
with open('dataJSON.json','w') as file:
    json.dump(dataJSON, file, indent=4)