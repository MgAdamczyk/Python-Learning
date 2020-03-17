###
# Program zamienia podaną temperaturę
# na inną wybraną skalę.
###

x = float(input("Podaj wartość temperatury do przeliczenia: "))
y = input("Wybierz jednostkę podanej temperatury: C (Celsjusz), K (Kelwin) lub F (Fahrenheit): ")
z = input("Wybierz skalę, do której chcesz przeliczyć podaną temperaturę: C (Celsjusz), K (Kelwin) lub F (Fahrenheit): ")

if y == "C" and z == "K":
    temp = x + 273.15
    txt = "Podana temperatura w Kelwinach wynosi: {}"
    print(txt.format(temp))

elif y == "C" and z == "F":
    temp = x*1.8 + 32
    txt = "Podana temperatura w Fahrenheitach wynosi: {}"
    print(txt.format(temp))

elif y == "K" and z == "C":
    temp = x - 273.15
    txt = "Podana temperatura w stopniach Celsjusza wynosi: {}"
    print(txt.format(temp))

elif y == "K" and z == "F":
    temp = x * 1.8 - 459.67
    txt = "Podana temperatura w Fahrenheitach wynosi: {}"
    print(txt.format(temp))

elif y == "F" and z == "C":
    temp = (x - 32)/1.8
    txt = "Podana temperatura w stopniach Celsjusza wynosi: {:.2f}"
    print(txt.format(temp))

elif y == "F" and z == "K":
    temp = (x + 459.67)/1.8
    txt = "Podana temperatura w Kelwinach wynosi: {:.2f}"
    print(txt.format(temp))

elif y == z:
    print("Wybrana do przeliczenia skala jest równa jednostce, w jakiej podano temperaturę")
else:
    print("Wprowadzono niewłaściwe dane")