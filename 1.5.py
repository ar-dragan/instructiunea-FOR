a = int(input("Introduceti numar exclusiv de la sfarsitul intervalului "))
summ = 0
ran = range(1,a)

for number in ran:
    if number % 3 == 0 or number % 5 == 0 :  
        summ += number
print(summ)