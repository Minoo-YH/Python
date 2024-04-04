Dictlist={
"Dog": "canien with for leg" ,
"Cat": "lioncanien with for leg",
"Fish":"Chikencanien with for leg" , 
"pork" : "Sharkcanien with for leg" ,
}
while True:
   name = input ("Search term: ").lower()
   if name in Dictlist:
    print(Dictlist[name])
   else:
    print("Not Found\ntry again.")