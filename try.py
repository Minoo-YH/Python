variableX = input("Givenumber :")


try:
    variableX = int(variableX)
    Result = 2 / variableX
except : zeroDivitionError as e:
      print (f"ERROR {e} ,try again.")
except Exception as e:
      print(f"Error {e}") 
else:
    print(Result)           