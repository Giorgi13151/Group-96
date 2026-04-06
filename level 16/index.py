user_word = input("შეიყვანეთ თქვენი სიტყვა")
if user_word == user_word.upper():
    print("ყველა ასო დიდია")
else:
    print("არ არის დიდი ასოები")
    user_word = input("შეიყვანეთ თქვენი სიტყვა")

word = input("შეიყვანეთ სიტყვა")
letter = int(input("შეიყვანეთ ერთი ასო"))
find = word.find(letter)
if find != -1:
    print("ასო წარმატებით მოიძებნა")
else:
    print("ასო არ მოიძებნა")

fruits = ['apple','banana','peach','pineapple']
fruits.append("kiwi")
fruits.append("mango")
fruits.append("pineapple")
print(len(fruits))
