print("Генератор паролей!")
import random
alnm='abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
password=""
l=int(input("Длина пароля-> "))
print("Длина = ",l)
for x in list(range(0,l)):
  password+=alnm[random.randint(0,(len(alnm)-1))]
print("\nТвой пароль - ",password)
