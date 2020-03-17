###
# Program sprawdza, czy podane przez
# użytkownika słowo jest palindromem.
###

txt = input("Podaj słowo: ")
txt = txt.upper()

i = 0
j = len(txt)
a = True

while i < j:
    if txt[i] == txt[j-1]:
        i+=1
        j-=1
    else:
        a = False
        break

if a == True:
    print("Podane słowo: \'" + txt + "\' jest palindromem")
else:
    print("Podane słowo: \'" + txt + "\' nie jest palindromem")