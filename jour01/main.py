print(10 + 3)
print(10*3)
print(10+3)
print(10-3)
print(10%3)
print(10/3)
print(10//3)
print("abcdefghijklmnopqrstuvwxyz")
print("zyxwvutsrqponmlkjihgfedcba")

ma_string = "je suis une String"
print(ma_string)

num1 = 3
num2 = 14
print(num1*num2)

ma_chaine = "zzzzezzezze"
lenchaine = len(ma_chaine)-1
value = 0
nombredee = 0
while value <= lenchaine:
  if ma_chaine[value] == "e":
      nombredee=nombredee+1
  value = value + 1
print("Il y a",nombredee,"e dans cette chaine")