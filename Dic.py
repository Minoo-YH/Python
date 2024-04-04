My_daily_food = {
    "sushi" : ["rice", "fish", "wasabi"],
    "salmon soup" :["salmon", "potato", "cream"],
    "pizza" : ["egg", "dough", "cheez"] 
    }
#x = My_daily_food.values()
#y = My_daily_food.keys()
# add more item 
#My_daily_food["price"] = "12$"
#print(x)
#print(y)
#print(My_daily_food["sushi"])
#print(My_daily_food)
my_keys = My_daily_food.keys()
for x in my_keys:
  print(x, end=" ")
print("\n")
my_values = My_daily_food.values()
# [list1], [list2], [list3] 
for i in my_values:
  for x in i :
    print(x, end=" ")
    
  

