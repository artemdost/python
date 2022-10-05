name = input("Введите имя: ")
fam = input("Введите фамилию: ")
date = int(input("Введите год рождения: "))
print(name,fam,date, sep='_')
name, fam = fam, name
date = 2004 + 60
print(name,fam,date, sep='_')

