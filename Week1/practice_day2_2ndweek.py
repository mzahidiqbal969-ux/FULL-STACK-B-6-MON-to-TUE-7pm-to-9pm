# student_age= 43
# print(student_age)
# print(student_age+5)
# updated_age=student_age+5
# print(updated_age)
# print(student_age-3*4)
# print((student_age-3)*4)
# student_height=5.9
# print(student_height/2)
# updated_student_height=student_height/2
# print(updated_student_height)
# num = 5
# text = "10"

# result = text + str(num)
# print(result)
# num_string = '12'
# num_integer = 23

# print("Data type of num_string before Type Casting:",type(num_string))

# # explicit type conversion
# num_string = int(num_string)

# print("Data type of num_string after Type Casting:",type(num_string))

# num_sum = num_integer + num_string

# print("Sum:",num_sum)
# print("Data type of num_sum:",type(num_sum))
# text2=text+str(num)
# print(text2)
# number = int(input('Enter a number: '))

# if number > 0:
#     print(f'{number} is a positive number.')
#     print('A statement outside the if statement.')
# number = int(input('Enter a number: '))

# if number > 0:
#     print('Positive number')
# else:
#     print('Not a positive number')
# number= -5

# if number>0:
#     print(f"{number} is a positive")
#     if number==0:
#         print(f"{number} is a zero value")
#     else:
#         print(f"{number} is not a zero value")
# else:
#     print("number is the negatine")
# a = [10, 20, "GfG", 40, True]
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# a.append(6)
# print("new value of list: ",a)
# l=[12,14,20,25]
# if len(l)%2 !=0:
#     l.append(0)
#     print(l)
# l = [12, 14, 20, 25,15]

# if len(l) % 2 != 0:
#     l.append(5)

# print(l)
#Given a list, append the sum of all elements to the list.
# list=[1,2,3,2,4]
# list.append(sum(list))
# print(list)
#Given a list of integers, append the maximum value twice
# list1=[1,2,3,2,4,6]
# max_value=max(list1)
# list1.append(max_value)
# list1.append(max_value)
# print(list1)
#l1=[1,2,3,4,5]
#l2=[4,5,6,7,8]
# for num in l2:
#     if num%2==0:
#         l1.append(num)
# print(l1)
# if num >5 and num %2!=0:
# print(l1.append(num))
l1=[1,2,3,4,5]
if l1!=[]:

    l1.append(10)
print(l1)
l2=[2,4,7,8,9]
if len(l2)>3:
    l2.append(20)
    print(l2)
else:
    print("list length is less than 3")
#Append the length of the list to the list
l3=[1,2,3,4,12]
l4=len(l3)
l3.append(l4)
print(l3)
#Append the last element again at the end
s=[2,4,6]
s.append(s[2])
print(s)
s1=[23,34,45,56,49]
s1.insert(2,50)
print(s1)
j=["java","c++"]
j.insert(0,"python")
print(j)
k=[10,20,30]   #insert hundred at the end without using append 
k.insert(len(k),100)
print(k)
#insert the sum of list elements at index0
n=[1,2,3,4]
m=sum(n)
n.insert(0,m)
print(n)
b=[1,2,3,4]
b.extend("ABC")
print(b)
m=[1,2,3,4,5]
m.pop(2)
print(m)
v=[1,2,3,4]
v[2]=10
print(v)
t=(1,2,3,4,5)
print(t)
print(type(t))
print(t[0]) #positive indexing in tuple
print(t[1])
print(t[2])
print(t[3])
#negative indexing in tuple
print(t[-1])
print(t[-2])
for x in t:
    print(x*2,end=" ")
    # Code for concatenating 2 tuples
t1 = (0, 1, 2, 3)
t2 = ('python', 'geek')    
print(t1+t2)
tx = ('python',)*3
print(tx)
x=set()
print(x)
print(type(x))
n = set([0, 1, 2, 3, 4])
print(n)
x1 = set([1, 1, 2, 3])
print(x1)
x2=set((1,2,3,4))
print(x2)
print(set("apple"))
companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']
companies.update(tech_companies)
print(companies)
languages = {'Swift', 'Java', 'Python'}
languages.discard('Java')
print(languages)
nums={1,1,2,2,3,4,5}
unique_nums=set(nums)
print(unique_nums)
dl=[10,20,30,40]
dt=(10,20,30,40)
ds={10,20,30,40}
print(dl)
print(dt)
print(ds)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
  "England": "London"
}
print(country_capitals)
# access the value of keys
print(country_capitals["Germany"])    # Output: Berlin
print(country_capitals["England"])
country_capitals["Italy"] = "Rome"

print(country_capitals)
del country_capitals["Germany"]

print(country_capitals)
counntry_head={"pakistan":"islamabad","india":"delhi"}
print(counntry_head)
counntry_head["bangladesh"]="dhaka"
print(counntry_head)
del counntry_head["india"]
print(counntry_head)