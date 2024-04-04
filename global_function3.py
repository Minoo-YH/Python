x = "I am so powerful"
print(x)

def myfunc(): 
    global x
    x = "I dont need buttery to play"

myfunc()    

print(x)