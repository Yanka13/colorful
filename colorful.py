def is_colorful(number):

    # Typage du nombre = None
    if type(number) != int:
        return None

    # Chiffres = colorful
    if 0 <= number < 10:
        return True

    # Chiffres négatifs =  pas colorful
    if number < 0:
        return False

    # Doublon = pas colorful
    list_numbers = [int(n) for n in str(number)]
    if len(list_numbers) != len(list(set(list_numbers))):
        return False

    # 0 ou 1 dans le nombre = pas colorful
    if "0" in str(number) or "1" in str(number):
        return False

    # SINON - dans tous les autres cas :
    # -> 1. Mettre toutes ses parties contigues dans une liste
    # -> 2. Calculer le produit de toutes ces parties contigues
    # -> 3. Vérifier que tous les produits sont uniques

    #print(list_numbers)
    all_products = list_numbers.copy()
    for width in range(2, len(list_numbers)+ 1 ):

        for i in range(0, len(list_numbers)- width + 1):
            slice = list_numbers[i: i+width]
            #print(slice)
            # 2. Calculer les produits de toutes les parties contigues
            result = 1
            for digit in slice:
                result *= digit
            #print(result)
            # 3. vérifier si les produits sont uniques
            if result in list_numbers:
                return False
            all_products.append(result)
            #print(all_products)
    # vérifier si tous les produits sont uniques
    if len(all_products) != len(list(set(all_products))):
        return False
    print(f"Wow, {number} is colorful!")
    return True

print(is_colorful(32975))

# - taille 1
#[3,2,9,7,5]

# - taille 2
# 32 - number_list[0:2]
# 29 - number_list[1:3]
# 97 - number_list[2:4]
# 75 - number_list[3:5]

# - taille 3
# 329 - number_list[0:3]
# 297 - number_list[1:4]
# 975 - number_list[2:5]

# - taille 4
# 3297 - number_list[0:4]
# 2975 - number_list[1:5]

# - taille 5
# 32975 - number_list[0:5]
