###
# Program sprawdza, czy podany rok
# jest rokiem przestępnym.
###

x = int(input("Podaj rok, który chcesz sprawdzić: "))

if x%4 == 0 and x%100 != 0 or x%400 == 0:
    print("Podany rok jest rokiem przestępnym")
else:
    print("Podany rok nie jest rokiem przestępnym")