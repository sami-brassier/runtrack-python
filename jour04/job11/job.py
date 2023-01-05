L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
produit = 1
for i in range(len(L)):
    if L[i] > 25 and L[i] < 90:
        produit = produit * L[i]