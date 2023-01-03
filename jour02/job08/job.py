def fonction_parametre(type,saison):
  if type == "fruit" and saison == "hiver":
    print("orange, mandarine et kiwi")
  elif type == "fruit" and saison == "ete":
    print("Poire, fraise, cassis")
  elif type == "legume" and saison == "hiver":
    print("carotte, topinambour, endive")
  elif type == "legume" and saison == "ete":
    print("artichaut, aubergine,navet")

fonction_parametre("fruit","hiver")
fonction_parametre("fruit","ete")
fonction_parametre("legume","hiver")
fonction_parametre("legume","ete")