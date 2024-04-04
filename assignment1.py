Dicttablelist={
"table1": "random.randrange(1,24)" ,
"table2": "random.randrange(1,24)",
"table3":"random.randrange(1,24)" , 
"table4" : "random.randrange(1,24)" ,
}
while True:
   name = input ("give table name : ").lower()
   if name in Dicttablelist:
    print(Dicttablelist[name])
   else:
    print("Not Found\ntry again.")