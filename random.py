import random
GenNum=random.randint(0, 10)
number=int(input("Угадай число"))
if number > GenNum:
    print ("Введенное число больше загаданного")
elif number < GenNum:
    print ("Введенное число меньше загаданного")
else: print (GenNum==number)


