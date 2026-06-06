def add (a , b):
  return a+b
  
def subtract (a , b):
  	return a-b
  	
def multiply (a , b):
  		return a*b
  		
def divide (a , b):
    if  b == 0:
        return "Cannot divide by zero"
    else:
        return a / b
        
    
print("\n_ _ _Calculator_ _ _")
 	
while True:
 	print ("1. Add")
 	print ("2. Subtract")
 	print ("3. Multiply")
 	print ("4. Divide")
 	print ("5. Exit")

    choice = input ("Enter choice(1-5): ")
    
     if choice = = "5":
    	print("Calculator closed")
        break        
  
    	 num 1 = float (input("Enter first number: "))
    num 2= float (input("Enter second number: "))

    if choice = = "1":
    	print(add(num1, num2))
    	
    elif choice = = "2":
    	print(subtract(num1, num2))  
    	
    elif choice = = "3":
    	print(multiply(num1, num2))
    	
    elif choice = = "4":
    	print(divide(num1, num2))
    		


  		
  		