import random
GenNum=random.randint(0, 10)
print (GenNum)
number=int(input("Угадай число"))
while number > GenNum:
    continue
    print ("Введенное число больше загаданного")
    if number < GenNum:
        continue
        print ("Введенное число меньше загаданного")
        break
else: 
    print (GenNum==number)
