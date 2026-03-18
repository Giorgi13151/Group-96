num = int(input("Enter Your Number"))
if num > 0:
  print("positive")
elif num < 0:
  print("negative")
else:
   print("zero")

password = "python123"
user_password = input("Enter Your Password : ")
while user_password != password:
  print("your Password is incorect Try Again")
else:
  print("You entered correct password")

fruits=["banana","apple","orange", "mango","cherry"]
print(fruits[1][2][4])