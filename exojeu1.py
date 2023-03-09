jeux0 = [" " for _ in range(9)]  # crée un tableau de 9 caractères espaces " "


def afficherjeux0(p, gagnant=None):
    print(" " + p[0] + " | " + p[1] + " | " + p[2] + " ")
    print("---------")
    print(" " + p[3] + " | " + p[4] + " | " + p[5] + " ")
    print("---------")
    print(" " + p[6] + " | " + p[7] + " | " + p[8] + " ")
    if gagnant:
        print("""* Partie terminée : le joueur {0} a gagné. *""".format(gagnant))


def morpion():
    joueur = "X"
    tour = 0

    while True:
        afficherjeux0(jeux0)
        print("> Tour du joueur " + joueur + ". Entrez un nombre de 1 à 9.")

        move = int(input()) - 1  # notre tableau est de 0 à 8, donc on retire 1

        if jeux0[move] == " ":
            jeux0[move] = joueur
            tour += 1
        else:
            print("! Case déjà occupée, choisissez-en une autre.")
            continue 

        if jeux0[0] == jeux0[1] == jeux0[2] != " " \
        or jeux0[3] == jeux0[4] ==jeux0[5] != " " \
        or jeux0[6] == jeux0[7] == jeux0[8] != " " \
        or jeux0[0] == jeux0[3] == jeux0[6] != " " \
        or jeux0[1] == jeux0[4] == jeux0[7] != " " \
        or jeux0[2] == jeux0[5] == jeux0[8] != " " \
        or jeux0[0] == jeux0[4] == jeux0[8] != " " \
        or jeux0[2] ==jeux0[4] == jeux0[6] != " ":
            afficherjeux0(jeux0, joueur)
            break

        if tour == 9:
            print("valid")
            break

        joueur = "0" if joueur == "x" else "x"  # on change de joueur


if __name__ == "__main__":
    morpion()