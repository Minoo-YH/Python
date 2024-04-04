import json
from pathlib import Path

products =[
{"Id" :1, "Tittle":"Iphone","price":2000},
{"Id" :2, "Tittle":"Ipad","price":4000},
{"Id" :3, "Tittle":"Iwatch","price":1000}
]
 
data = json.dumps(products)
 
print(data)

Path("products.json").write_text(data)