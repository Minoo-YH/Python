variableX = input("Data please?:")


try:
    variableX = int(variableX)
    Result = variableX * variableX
    print(Result)
except Exception :
    print("Error")  
else:
    print("Finished")      
