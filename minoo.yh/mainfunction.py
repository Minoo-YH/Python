#function to handdle navigation option            
import Function
import json
NavTex ="""
1:wipe
2:creat
3:Exit
"""

def NavOption():
    while True:
        print(NavTex)
        userInput = input("Enter one:")
        match userInput:
            case "1" :
                Function.wipe()
            case "2" :
                Function.creat()
            case "3" :
                print("shutting down..")
                exit()   
                                 
 # start with creat file as hear            
NavOption()                     


 

    
      