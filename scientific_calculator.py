import math
class scientific:
    def __init__(self, num1, num2):
        self.num1= num1
        self.num2= num2

    # This function adds two numbers
    def addition(self):
        return (self.num1+self.num2)
    
        # This function subtracts two numbers
    def subtract(self):
         return (self.num1-self.num2)
     
        # This function multiplies two numbers
    def multiply(self):
         return (self.num1*self.num2)
     
        # This function divides two numbers
    def divide(self):
         return (self.num1/self.num2)
        # This function gives the result of raising a number to a power of another number
    def exponent(self):
        return (self.num1**self.num2)
    
class second_scientific:
    def __init__(self, num1):
        self.num1= num1
        # This function gives the logarithmic result of a number
    def log(self):
        return math.log(self.num1)
         # This function gives the cose of a number
    def cos(self):
        return math.cos(self.num1)
        # This function gives the sine of a number
    def sin(self):
        return math.sin(self.num1)
        # This function gives the tangent of a number
    def tan(self):
         return math.tan(self.num1)
   
