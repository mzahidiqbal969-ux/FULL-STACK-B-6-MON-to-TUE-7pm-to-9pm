s1="it is winter"
s2="lahore is capital of punjab"
s3="islamabad is the capital of pakistan"
print(s1[6:12:1])
print(s2[0:6:1])
print(s3[0:9:1])
print(s1[-6::])
print(s2[-28:-21:])
print(s3[-36:-28:])
print(len(s1))

for ch in s1:
    print(ch)
for ch in s2:
    print(ch)
for ch in s3:
    print(ch)
print(s1.upper())
print(s1.lower())
print(s1.capitalize())
print(s1.title())
print(s1.swapcase())
long=48.9
print(long)
print(type(long))
location=4
print(location)
print(type(location))
sum=long+location
print(type(sum))
mystring_int="12"
print(type(mystring_int))
print(int(mystring_int))
#Check positive, negative or zero
num=int(input("enter any number: "))
if num>0:
    print("number is positive")
elif num==0:
    print("number is zero")
else:
    print("number is negative")