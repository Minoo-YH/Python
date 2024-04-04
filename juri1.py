number = int(input("Give number: "))
counter = 0
while True:
    guess = int(input())
    counter = counter + 1
    if guess < number :
        print("it is more")
        
    elif guess > number : 
        print("it is less")  
         
    elif guess == number :
        print(f'Number of tries needed:\n{counter}'  )
        break
 #       print("Number of tries needed:")
 #       print(counter)
         
    