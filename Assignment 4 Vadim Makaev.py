# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:34:15 2024

@author: vadim
@assignment 4
"""
#%% Ex 1
def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    else:
        return False
    print(is_prime(1))  
print(is_prime(5)) 
print(is_prime(6))  
print(is_prime(11)) 
#%% Ex 3
A = {c: round((c * 9 / 5) + 32, 1) for c in range(0, 36)}
print(A) #Converted tempreture 
#%% Ex 4
def convert_temp(degrees, cnv_type='ftoc'):
    if not isinstance(degrees, (int, float)):
        return -2
    if cnv_type == 'ftoc':
        return round((degrees - 32) * 5 / 9, 1)
    elif cnv_type == 'ctof':
        return round((degrees * 9 / 5) + 32, 1)
    else:
        return -1

# Test
print(convert_temp(100))               
print(convert_temp(100, cnv_type='ftoc'))  
print(convert_temp('100', 'ftoc'))         
print(convert_temp(31, 'ctof'))            
print(convert_temp(31, 'blah'))
#%% Ex 5
def sort_by_selected_key(dicts, keyname):
    return sorted(dicts, key=lambda x: x[keyname])

# Example
employees = [{'name': 'John', 'age': 28, 'years': 2.5},
    {'name': 'Lisa', 'age': 24, 'years': 3.1},
    {'name': 'Ella', 'age': 31, 'years': 2.9}]

# Sort by name
sorted_by_name = sort_by_selected_key(employees, 'name')
print(sorted_by_name)

# Sort by age
sorted_by_age = sort_by_selected_key(employees, 'age')
print(sorted_by_age)

# Sort by years
sorted_by_years = sort_by_selected_key(employees, 'years')
print(sorted_by_years)
#%% Ex 6
# 1)The attributes of the class Fish are 'first_name' and 'last_name'.

# 2)The methods of the class Fish are '__init__', 'swim', and 'swim_backwards'.

# 3)The parent class is 'Fish'.

# 4)The child class is 'BlueTang'.

# 5)In OOP terms, the code in line 14 is instantiating an object 'obj' of the class 'Fish' with 'Tropical' as the 'first_name' and the default 'last_name' ("Fish").

# 6)Line 15 is calling the 'swim' method on the 'obj' instance of the Fish class, which outputs "The fish is swimming" due to the 'print' statement inside the 'swim' method.
# Line 20 is instantiating an object 'Dory' of the class 'BlueTang' with 'Dory' as the 'first_name' and 'DeGeneres' as the 'last_name' by using the __init__ constructor inherited from the 'Fish' class.

# 7)The code on line 21 functions as a result of the principle of inheritance in object-oriented programming (OOP). The 'BlueTang' class is a derived class of the 'Fish' class and it acquires the methods of the parent class. Thus, despite the absence of an explicitly specified 'swim()' method in the 'BlueTang' class, the 'Dory' object can nevertheless utilize the 'swim()' method defined in its parent 'Fish' class, resulting in the output "The fish is swimming".


