# Welcome the user
print("Welcome to the Simple Calculator")

# Operators
# While loop for operators
while (operator := input('''\nPlease select the operator you wish to use : 

+ 

- 

* 

/ 

'r' to read files
"exit" to stop  : \n''')) != "exit":

# Command operators
 commands =  ["+","-","*","/","r",]
 if operator in commands:
    
    try:
        # Operator to read files
        if operator == 'r':

         # Ask user to enter the name of the file they want to read from.
         user_input = input("Enter the name of a file you want to read: ")

         # Open file for reading
         my_file = open(user_input + ".txt")

         # Read equations in the file
         information = my_file.readlines()
         print(information)

         # Continue calculator after reading equations
         continue

        # '+' to add
        if operator == "+":

         # Ask user to enter two numbers they wish to calculate
         int1 = input("Enter first number you wish to calculate: ")
         int2 = input("Enter second number you wish to calculate with the first number: ")

         # Add num1 with num2 (Addition)
         result = int(int1) + int(int2)

         # Result for Equation
         print(result)
         
         # Write the equation and result in the numbers text file
         with open('equations.txt' , 'a')as num_result:
                num_result.write(f"{int1} + {int2} = {result}\n")
                
                #Let user know where the equation is saved on
                print("You equation is saved on the equations.txt file!")
         
         # '-' for Subtraction
        if operator == "-":

           # Ask user to enter two numbers they wish to calculate
          int1 = input("Enter first number you wish to calculate: ")
          int2 = input("Enter second number you wish to calculate with the first number: ")

          # Subtract num1 with num2 (Subtraction)
          result = int(int1) - int(int2)

          # Result for Equation
          print(result)

          # Write the equation and result in the numbers text file
          with open('equations.txt' , 'a')as num_result:
                num_result.write(f"{int1} - {int2} = {result}\n")

                #Let user know where the equation is saved on
                print("You equation is saved on the equations.txt file!")

        # '*' for Multiplication
        if operator == "*":
            
          # Ask user to enter two numbers they wish to calculate
          int1 = input("Enter first number you wish to calculate: ")
          int2 = input("Enter second number you wish to calculate with the first number: ")

          # Multiply num1 with num2 (Multiplication)
          result = int(int1) * int(int2)

          # Result for Equation
          print(result)

          # Write the equation and result in the numbers text file
          with open('equations.txt' , 'a')as num_result:
                num_result.write(f"{int1} * {int2} = {result}\n")
                
                #Let user know where the equation is saved on
                print("You equation is saved on the equations.txt file!")

        # '/' for division
        if operator == "/":
          
          # Ask user to enter two numbers they wish to calculate
          int1 = input("Enter first number you wish to calculate: ")
          int2 = input("Enter second number you wish to calculate with the first number: ")
          
          # Divide num1 with num2 (Division)
          result = int(int1) / int(int2)

          # Result for Equation
          print(result)

          # Write the equation and result in the numbers text file
          with open('equations.txt' , 'a')as num_result:
                num_result.write(f"{int1} / {int2} = {result}\n")

                #Let user know where the equation is saved on
                print("You equation is saved on the equations.txt file!")

    # Defensive programming if file not found
    except FileNotFoundError:
        print("your text file could not be found")
        print("\ntry again")

    # Defensive programming if user tries to divide by zero.
    except ZeroDivisionError:
        print("you cannot divide by zero please please try again")
        print("\nTry again")
        continue

    # Defensive programming if a number is not entered.    
    except ValueError as ERROR:
        print('invalid  input , please enter a valid number') 
        print("\n Try again")
        continue
 else:
      # If you enter an operator thats not valid
    print("The operator you entered is not valid")


# Print statement for once user has completed using the calculator.
# Let the user know where the equations are saved.    
print("Thank you for using the Simple Calculator,your equations are saved in the equations.txt file!")

#Note code reviewer
#The name of the file is equations.txt

