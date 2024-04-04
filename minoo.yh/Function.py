import json
#navigation data
#load convert json to python file and dumps versa. 
   
def wipe():
    confirmation =input("wipe json file ?(yes/no):")
    if confirmation.lower() in ("yes","y"):
        with open ("MN.json","w") as file:
            file.write("")
        print("wiped!")
    else:
        print("can not!")  
        
         

def userInput():
      key = input("Name :")
      value = input("Family:") 
      return key,value 
  # creat and update data  from json file by while loop cuse want to continue ant time.
  #try and except for error
  #.lower for same world not capital or shortness
                
#creat or update in json 
def creat():
  try:  
    while True:
        key, value = userInput()
        try:
            with open("MN.json","r") as file:
                existData= json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            existData = {}
            #update new input of user
            
        existData[key]=value 
            #write update to file   
        with open("MN.json", "w")  as file:
            json.dump(existData, file, indent=4) 
            print("Update Successful.")
        exitInput = input("press 'Enter' to continue or 'no' to Exit:")
        if exitInput.lower() in ("no","n"):
            break
    
  except FileNotFoundError:
       print("Error: json file not found")
  except PermissionError:
       print("Error:denied to write json file ")          
creat() 