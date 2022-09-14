# Pascal, Python 3.10 | Développé le 14 Septembre 2022 sous l'IDE Pycharm
import copy
import random


def mix_list(list_to_mix: list) -> list:
    """
    La fonction mix_list() permet de mélanger une liste

    :param list_to_mix(list): Représente la liste à mélanger
    :return new_list(list): La valeur de retour est une copie de la précédente liste mélangée
    """

    new_list = copy.deepcopy(list_to_mix)  # On crée une copie approfondie de liste_to_mix.

    for i in range(len(new_list) - 1, 0, -1):  # On parcourt la liste de la fin à son début

        rand = random.randint(0, i + 1)  # On génère un entier aléatoire entre 0 et i + 1 pour avoir un intervalle qui
        # va changer à chaque incrémentation de i.

        print("rand = ", rand)

        new_list[rand], new_list[i] = new_list[i], new_list[rand] # On mélange la liste en switchant les index des
        # 2 cotés

    return new_list

if __name__ == '__main__':
    # Test de la fonction mix_list()
    print("------------")
    print(mix_list([0, 1, 2, 3, 4, 5]))
