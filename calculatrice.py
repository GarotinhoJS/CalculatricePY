def calculatrice():
    print("Options :")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")
    
    choix = input("Choisissez une option (1/2/3/4/5) : ")

    if choix == '5':
        print("Merci d'avoir utilisé la calculatrice. Au revoir!")
        return
    
    num1 = float(input("Entrez le premier nombre : "))
    num2 = float(input("Entrez le deuxième nombre : "))
    
    if choix == '1':
        resultat = num1 + num2
        print("Résultat : ", resultat)
    elif choix == '2':
        resultat = num1 - num2
        print("Résultat : ", resultat)
    elif choix == '3':
        resultat = num1 * num2
        print("Résultat : ", resultat)
    elif choix == '4':
        if num2 != 0:
            resultat = num1 / num2
            print("Résultat : ", resultat)
        else:
            print("Erreur : Division par zéro")
    else:
        print("Option invalide")

    calculatrice()


