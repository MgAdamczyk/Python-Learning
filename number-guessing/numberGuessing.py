###
# Program ma za zadanie wylosować liczbę,
# a użytkownik ma ją zgadnąć.
###

import random

print("Program losuje liczbę z zakresu 1-100...")
x = random.randint(1,100)

#Podgląd wylosowanej liczby
# print(x)

print("A teraz zgadnij wylosowaną liczbę :)")

while True:
    a = int(input("Wpisz swoją liczbę: "))
    if x == a:
        print("Zgadłeś wylosowaną liczbę, która wynosi: " + str(x))
        break
    elif x > a:
        print("Zbyt mała liczba")
    else:
        print("Zbyt duża liczba")