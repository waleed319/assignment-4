#!/usr/bin/env python
# coding: utf-8

# In[8]:


my_dict = {'value1':100,'value2':-54,'value3':247}
print(sum(my_dict.values()))


# In[3]:


list = ["abc", "def", 4, "ghi"] 
for x in list: 
    if type(x) == int: 
        print(x)


# In[4]:


d = {0:10, 1:20}
print(d)
d.update({2:30})
print(d)


# In[5]:


l=[1,2,3,4,5,2,3,4,7,9,5]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        print(i,end=' ')


# In[3]:


d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(y):
  if y in d:
      print('Key is available in dictionary')
  else:
      print('Key is not available in dictionary')
is_key_present(5)
is_key_present(9)


# In[4]:


# Program a simple calculator

# This function is used to adds two numbers
def add(x, y):
    return x + y

# This function is used to subtracts two numbers
def subtract(x, y):
    return x - y

# This function is used to multiplies two numbers
def multiply(x, y):
    return x * y

# This function is used to divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")


# In[ ]:





# In[ ]:




