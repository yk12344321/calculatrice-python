def choix():
    x = int(input(" le premier nombre pour l'opération : "))
    y = int(input(" le deuxième nombre pour l'opération : "))
    return x, y
def calculatrice():
    while True:
        try:
            value = int(input("Choisis l'opération : Addition (1), Multiplication (2), Division (3), Soustraction (4), stop(5) : "))
            if value == 5 :
                print ("Arret de la calculatrice")
                break
            elif value in (1,2,3,4):
                if value == 1:
                    nbr1 , nbr2 = choix()
                    print("L'opération : ",nbr1," + ",nbr2," = ",nbr2+nbr1)
                elif value == 2:
                    nbr1 , nbr2 = choix()
                    print("L'opération : ",nbr1," x ",nbr2," = ",nbr1*nbr2)
                elif value == 3:
                    nbr1 , nbr2 = choix()
                    print("L'opération : ",nbr1," / ",nbr2," = ",nbr1/nbr2)
                elif value == 4:
                    nbr1 , nbr2 = choix()
                    print("L'opération : ",nbr1," - ",nbr2," = ",nbr1-nbr2)
            else:
                print("commande non comprise !")
        except ValueError :
            print("entrer un chiffre valide")
calculatrice()
