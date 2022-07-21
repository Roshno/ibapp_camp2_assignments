class calculator():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        return self.a / self.b

a = int(input('Enter First number : '))
b = int(input('Enter Second number : '))        
object = calculator(a,b)
while True:
    def calc_menu():
        answer = ('1. Add \n2. Sub \n3. Multiply \n4. Divide \n5. Exit') 
        print(answer)
    calc_menu()
    operation = int(input('Select one of the following operations : ')) 
    if operation == 1:
        print("Result: ",object.add())
    elif operation == 2:
        print("Result: ",object.sub())
    elif operation == 3:
        print("Result: ",object.multiply())    
    elif operation == 4:
        print("Result: ",object.divide())
    elif operation == 5:
        print("Exit")
        exit()
    else:
        print('Invalid option') 
        break       
print()
