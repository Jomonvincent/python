#!/usr/bin/env python
# coding: utf-8

# In[3]:


pi=3.14
r= input("enter radius")
area=pi*r*r
print("area is",area)


# In[5]:


r=input("enter radius")
a=int(r)*int(r)*3.14
print("area is",a)


# In[6]:


a= input("enter number ")
b= input("enter number ")
s= int(a)+int(b)
print("sum is",s)
sub= int(a)-int(b)
print("subtraction is",sub)
mul= int(a)*int(b)
print("product is",mul)
div= int(a)/int(b)
print("divison is",div)


# In[7]:


a= input("enter salary ")
h=int(a)*0.10
t=int(a)*0.5
print("hra is",h)
print("tra is",t)


# In[18]:


a= int(input("enter a number"))
if (a%2==0):
    print("its even number")
else:
    print("its odd number")


# In[1]:


a= 5
print(type(a))


# In[ ]:


a= int(input("enter a number 1:"))
b= int(input("enter a number 2:"))
c= int(input("enter a number 3:"))
if (a<b):
    print("a is greater number")
elif:
    print("b is greater number")
else(c<b):
    print("c is greater number")
    
# In[ ]:

# In[ ]:

a= int(input("enter a number 1:"))
b= int(input("enter a number 2:"))
c= int(input("enter a number 3:"))
if (a<b):
    print("a is greater number")
elif:
    print("b is greater number")
else(c<b):
    print("c is greater number")
# In[ ]:


#Generate the pattern
N = int(input("Enter a value for N: "))
for i in range(1, N + 1):
    for j in range(1, i + 1):
        multiple = i * j
        print(multiple, end=" ")  
    print()  


# Print the factors using a while loop
number = int(input("Enter a number to find its factors: "))
divisor = 1
print(f"The factors of {number} are:")
while divisor <= number:
    if number % divisor == 0: 
        print(divisor)  
    divisor += 1  


# Display the GCD
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
while num2 != 0:
    temp = num2
    num2 = num1 % num2
    num1 = temp
gcd = num1
print(f"The GCD of the two numbers is: {gcd}")


# Display the reversed number
number = int(input("Enter a number to reverse: "))
reverse = 0
while number > 0:
    remainder = number % 10  
    reverse = reverse * 10 + remainder  
    number //= 10  
print(f"The reversed number is: {reverse}")



#amstrong
number = int(input("Enter a number to check if it's an Armstrong number: "))
original_number = number
sum_of_powers = 0
num_digits = 0
temp_number = number
while temp_number > 0:
    temp_number //= 10
    num_digits += 1 
temp_number = number
while temp_number > 0:
    digit = temp_number % 10  
    sum_of_powers += digit ** num_digits 
    temp_number //= 10  
if sum_of_powers == original_number:
    print(f"{original_number} is an Armstrong number.")
else:
    print(f"{original_number} is not an Armstrong number.")



# Display the average
n = int(input("Enter the value of n: "))
sum_of_numbers = 0
for i in range(1, n + 1):
    sum_of_numbers += i 
average = sum_of_numbers / n
print(f"The average of the first {n} natural numbers is: {average}")


# Multiplication table up to 10
n = int(input("Enter a number to print its multiplication table: "))
print(f"Multiplication Table of {n}:")
for i in range(1, 11):  
    result = n * i
    print(f"{n} x {i} = {result}")



#sum of the series
n = int(input("Enter the value of n: "))
sum_of_series = 0.0 
for i in range(1, n + 1):
    sum_of_series += i / (i + 1)  
print(f"The sum of the series up to {n} terms is: {sum_of_series:.4f}")


# Print  stars
n = int(input("Enter the number of rows for the upper half of the pattern: "))
for i in range(1, n + 1): 
    for j in range(i):  
        print("*", end=" ")
    print()  
for i in range(n - 1, 0, -1):  
    for j in range(i):  
        print("*", end=" ")
    print()  
