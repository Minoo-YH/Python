import json
from pathlib import Path
listname = [
    {"Name": "Minoo", "Age": 32, "Gender" :"Women"} ,
    {"Name": "Moji", "Age": 39, "Gender":"men"} ,
    {"Name": "Ryan", "Age": 2, "Gender":"boy"} ,        
     {"Name":"Narges", "Age": 26, "Gender":"Women"}
]
data = json.dumps(listname)

print(data)

Path("Listname.json").write_text(data)