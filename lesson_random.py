# іменем модуля називати файли - ЗАБОРОНЕНО!!!, к примеру random.py нельзя, поэтому к названию модуля надо всегда что-то  дописывать, иначе мы не сможем воспользоваться модулем

import random  # random.randrange(5)  обратись к модулю, найди там .randrange(5) и подставляем число, те обычный наш вызов randrange, найди мне файл и дай мне ответ
# import random as r  # r.randrange(5) импортируй мне модуль, как буйто бы он r 
# from random import *  # randrange(5) возьми мне с этого модуля всё, потому что * сказала, что можно пользоваться всеми методами
#### from numpy import *
# from random import randrange, randint  # randrange(5) можем использовать только те модули, которые указали и все
# from random import randrange as rr  # rr(5) мы взяли из модуля только randrange и переименовали его в rr, те мы переименовали только один элемент

comp_choice = random.randint(0,100) #  выдай мне случайное число от 0 до 100
n_count = 0
# user_choice = -1
# while True:
while n_count < 3: # это ограниченная ф-я, те 3 попытки, к примеру 
    try:
        user_choice = int(input("Enter your number: "))
    except ValueError:
        print("Uncorrect number!")
        continue
    else:
        print("Excelent! I remember your number")
    finally:
        n_count += 1
        print(f"Your attempt {n_count}")
        # print(f"Your choice")
        
    # if
    
    if user_choice == comp_choice:
        print("Congratulations")
        break # если было while trye, то обязательно нужен break, и он должен быть под if, когда ты зашли в эту ф-ю, чтобы выйти из цикла
    # elif
    # else
    print("Try again!")
