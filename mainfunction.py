import Functions #importing  Functions here for getting add() inside the Functions.py
import json
navoption="""
1.create data
2 wipe data
3.add data
4 exit()"""
def nav():
    
    while True:
        print(navoption)
        option=input("which option you need to choose")
        match option:
            case "1":
                Functions.createjson()
                break
            case "2":
                Functions.wipe_data()
                break
            case "3":
                Functions.add_data()
                break
            case "4":
                print("exiting....")
                exit()
nav()