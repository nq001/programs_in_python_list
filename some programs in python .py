# Write a program to reverse each row and each column of a given matrix >>>>


lis = [1,2,3,4,5,6,7,8,9]

lis.reverse()
for i in lis[:]:

    if i == lis[2] or i == lis[5] or i == lis[8]:

        print(f"{i}\n")
    else:
        print(i,end=" ")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# Write a program to print the str,int, float, from a given list = [[2,"a"],[6,3,5,"c"],[2.3,"d"]]


li = [[2,"a"],[6,3,5,"c"],[2.3,"d"]]


for i in li[0:3][0]:

    print(f"the type of index list [0:3][0] is: {type(i)} ")

print(10 * "=")


for j in li[0:3][1]:

    print(f"the type of index list [0:3][1] is: {type(j)} ")

print(10 * "=")


for k in li[0:3][2]:

   print(f"the type of index list [0:3][2] is: {type(k)} ")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# write a program that takes m*n matrix as input from the user and prints the even elements with their corresponding
# row and coulmn numbers

row = []
coulmn = []

for i in range(6):
    m = int(input("Enter the number_m: "))
    row.append(m)

for j in range(6):
    n = int(input("Enter the number_n: "))
    coulmn.append(n)
total = row + coulmn
print("the matrix")

for i in total[:]:

    if i == total[3] or i == total[7] or i == total[11]:

        print(f"{i}\n")
    else:
        print(i,end=" ")
print("="*20)
for k in total:
    if k %2 ==0:
        print(f"this value from matrix is even {k} ")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Write a python program to read a list of numbers from the user and print the largest 
# number in the list

my_list = []

for i in range(10):
    lis = int(input("Enter the number: "))
    my_list.append(lis)
print("="*10)
print(f"the list is : {my_list}\n"
    f"the largest number is: {max(my_list)} ")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Create a list of temperatures in degrees Celsius with the values: 25.2, 16.8, 31.4, 
# 23.9, 28, 22.5, and 19.6, and assign it to a variable called temps_in_celsius. Then, 
# convert all the values from temps_in_celsius into Fahrenheit, and store the 
# converted values in a new list temps_in_fahrenheit. The list temps_in_celsius 
# should remain unchanged. (Note: F = 9/5(C) + 32)

temps_in_celsius = [25.2, 16.8, 31.4, 23.9, 28, 22.5,19.6]
temps_in_fahrenheit = []
for i in temps_in_celsius:
    F = 9/5 * i + 32  # F mean Fahrenheit role
    temps_in_fahrenheit.append(F)
print(f"celsius: {temps_in_celsius} ")
print("="*10)
print(f"fahrenheit: {temps_in_fahrenheit} ")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Write a program that insert numbers to a list then found the square and summation 
# of this numbers.

list = []
squ_list = []
# sum_list = []

for j in range(6):
    num = int(input("Enter the number: "))
    list.append(num)
for k in list:
    n = k ** 2
    squ_list.append(n)

print(f"the origenal list: {list} ")
print(f"the square of this numbers is: {squ_list} ")
print(f"the summation of this nmbers is: {sum(list)} ")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Write a program to get the intersection between two lists   

lis1 = [1,2,3,4,5,6,7]
lis2 = [1,9,10,6,4,11]

intersection = []

for i in lis1:
    if i in lis2:
        intersection.append(i)
print(intersection)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Write a python program to print all the strings from a list.

li=['red',56,'blue','green',3.6]

for i in li[:]:
    if type(i) == str:
        print(i)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Write a python program to read a list from user and remove the duplicate items 
# from the original list

lis = []

for i in range(10):
    num1 = int(input("enter the number:"))
    lis.append(num1)
print("original list")
print(lis)

print("after")
res = set(lis)
print(res)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Read list of items, quantities, and unit price then print all items and 
# related data in tabular form along with invoice total.
# Super market involving using single 2-D array.

lis,lis2,lis3 = [],[],[]
total = 0 
to = 0 # to keep sum value
for i in range(3):

    name = input("enter type of item: ")
    qty = float(input("enter the quantities: "))
    unit_p = float(input("enter unti price: "))

    lis.append(name)
    lis2.append(qty)
    lis3.append(unit_p)

    total = unit_p * qty 
    to = to + total

print("item\t\tqty\t\tunit_price")
print("-"*40)

a = 0
for x in lis[:]:
    print(f"{lis[a]}\t\t{lis2[a]}\t\t{lis3[a]} $ ")
    a += 1

print("-"*40)
print(f"the total: {to} ")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Super market involving using single 2-D array.

liss = [['milk','sugar','tea','water'],[4,2,8,3],[2500,4500,500,400]]

print("item\t\tqty\t\tunit_price")
print('-'*40)

for i in range(1):
    print(f"{liss[0][0]}\t\t{liss[1][0]}\t\t{liss[2][0]}")
    print(f"{liss[0][1]}\t\t{liss[1][1]}\t\t{liss[2][1]}")
    print(f"{liss[0][2]}\t\t{liss[1][2]}\t\t{liss[2][2]}")
    print(f"{liss[0][3]}\t\t{liss[1][3]}\t\t{liss[2][3]}")
    
print('-'*40)