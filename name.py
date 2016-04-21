import random

drink_names_adj = ["Salty", "Oily", "Cheeky", "Crusty"] 
drink_names_noun = ["Spitoon", "Gunwhale", "Brig", "Poopdeck"] 

def name_drink(drink_names_adj, drink_names_noun):
    return random.choice(drink_names_adj), random.choice(drink_names_noun)
    
        
print("My name is {!s}".format(name_drink(drink_names_adj, drink_names_noun)))
#print("My name is: %s" % name_drink(drink_names_adj, drink_names_noun))

