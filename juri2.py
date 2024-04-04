min = int(input("Minimum :"))
max = int (input("Maximum :"))

while True: 
       device_tem = int(input("Device temperature :"))
       if device_tem >= min and device_tem <= max:
             print("Nothing to report")
       elif device_tem == -999:
             break      
       elif device_tem < min or device_tem > max:
              print("Alert!") 
              
    