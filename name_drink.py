import random

drink_names_adj = ["Salty", "Oily", "Cheeky", "Crusty"] 
drink_names_noun = ["Spitoon", "Gunwhale", "Brig", "Poopdeck"] 

def name_drink(drink_names_adj, drink_names_noun):
    new_name = [""]
    for a in drink_names_adj:
        print(random.choice(a))
    """for n in drink_names_noun:
        new_name.append(random.choice(n))
    print(new_name)"""
        

print(name_drink(drink_names_adj, drink_names_noun))