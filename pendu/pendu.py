import random
f = open("dico_france.txt",encoding="ISO-8859-1")
a = f.read()
b = a.split()

solution = random.choice(b)

print(solution)

level = input("Choisis ton niveau de difficulté (débutant, intermédiaire, expert : ")

if level == "débutant" :
    hp = 10
if level == "intermédiaire" :
    hp = 7
if level == "expert" :
    hp = 4

affichage = ""
lettres_trouvees = ""

for l in solution:
  affichage = affichage + "_ "

print(">> Bienvenue dans le pendu <<")

while hp > 0:
  print("\nMot à deviner : ", affichage)
  proposition = input("proposez une lettre : ")[0:1].lower()

  if proposition in solution:
      lettres_trouvees = lettres_trouvees + proposition
      print("-> Bien vu!")
  else:
    hp = hp - 1
    print("-> Nope\n")
    if hp ==0:
        print(" ==========Y= ")
    if hp<=1:
        print(" ||/       |  ")
    if hp<=2:
        print(" ||        0  ")
    if hp<=3:
        print(" ||       /|\ ")
    if hp<=4:
        print(" ||       /|  ")
    if hp<=5:                    
        print("/||           ")
    if hp<=6:
        print("==============\n")

  affichage = ""
  for x in solution:
      if x in lettres_trouvees:
          affichage += x + " "
      else:
          affichage += "_ "

  if "_" not in affichage:
      print(">>> Gagné! <<<")
      break
     
print("\n    * Fin de la partie *    ")