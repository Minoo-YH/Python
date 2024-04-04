import json

def createjson():
    data={
        "name":"Sruthi",
        "age":37,
        "job":None
    }
    #using dump function ,changing python object in to the json object
    with open("datajson.json","w")as file:
        json.dump(data,file,indent=4) #here datajson.json created ,it can be viewed in same folder 
    print("file created")
    print(data)


def input_data():
    print("here we are going to add data in to the file")
    x=input("please enter  the key")
    y=input("please enter value")
    return x, y
def add_data():
    try:
        key,value=input_data()
        try:
            with open("datajson.json", "r") as read_file:
                newdata=json.load(read_file)
        except(FileNotFoundError,json.JSONDecodeError):
            newdata={}
        newdata[key]=value
        with open("datajson.json","w")as file:
            json.dump(newdata,file,indent=4)
            print("added data")
        print(newdata)

    except Exception as e:
        print(f"Error: {e}")
   

def wipe_data():
    print("here you are going to wipe the data")
    confirm=input("are you sure to wipe it yes/no")
    if confirm.lower()in ("yes","y"):
        with open("datajson.json","w")as file:
            file.write("")
            print("json file is wiped")
    else:print("wipe aborted")