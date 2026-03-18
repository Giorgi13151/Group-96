number = int(input("Enter Your Number:"))
if number / 2 == 0:
    print('Even')
else:
    print("odd")

temp = int(input("Enter Temp: "))
if temp > 30:
    print("It's Hot")
elif temp > 15 < 30:
    print("Its Warm")
else:
    print("Its Cold")

num = int(input("Enter Your Number: "))
if  num / 2==0:
    print("Positive even")
elif num / 3==0:
    print("Positive Odd")
else:
    print("Negative")


user_number = int(input("Enter Your Number: "))
if user_number / 2==0:
    print("Your Number Is Even")
else:
    print("Odd")

numbers2 = [10,-5,8,0,6,-1,0,3,2,1]
if numbers2 > 0:
    print("Positive")
elif numbers2 < 0:
    print("Negative")
else:
    print("Zero")

fruits = ["apple", "kiwi", "orange", "grape"]

nums = [4, 8, 12, 16, 20]
resulut = nums[0] + nums[-1]
print(resulut)

numbers3 = [1,5,2,6,1,6,2]
print(numbers3)

number5 = [7,9,7,8,11,24,6,5,1,4]
while number5 > 6:
    print(number5)

random = "Giorgi"
for i in random:
    print(i)

name = 'Shop'
resulut = name[0] + name[1] + name[2]
print(resulut)