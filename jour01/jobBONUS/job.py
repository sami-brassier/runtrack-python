ma_chaine = "zzzzezzezze"
lenchaine = len(ma_chaine)-1
value = 0
nombredee = 0
while value <= lenchaine:
  if ma_chaine[value] == "e":
      nombredee=nombredee+1
  value = value + 1
print("Il y a",nombredee,"e dans cette chaine")