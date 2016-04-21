import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}
ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],           #simple dictionary with key: list[values]
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "splash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

drink_names_adj = ["Salty", "Oily", "Cheeky", "Crusty"] 
drink_names_noun = ["Spitoon", "Gunwhale", "Brig", "Poopdeck"] 

def what_drink(questions):  ### this function asks questions stored as values in the 'questions' dictionary above
    preferences = {}        ### creates new dictionary 'preferences' with Boolean matched to key of 'questions' dictionary
    for d, q in questions.items():
        ques = input(q)
        if ques == 'y' or ques == 'yes':
            preferences[d] = True
        else:
            preferences[d] = False
    return preferences 

def new_drink(preferences):   ###this function 
    drink = []
    for s, t in preferences.items():
        if t == True:
            drink.append(random.choice(ingredients[s]))
        else:
            continue
    return drink
    
def name_drink(drink_names_adj, drink_names_noun):
    x = random.choice(drink_names_adj)
    y = random.choice(drink_names_noun)
    new_name = x + " " + y
    return new_name
    
def main():
    preferences = what_drink(questions)
    drink = new_drink(preferences)
    print("Based on what ye told me, here's what ye be drinkin': 'The {}'".format(name_drink(drink_names_adj, drink_names_noun)))
    for thing in drink:
        print('{}'.format(thing))
    money = input("Arrrg, hope ye be satisfied. How's about another?")
    if money == 'y' or money == 'yes':
        main()
    
    
if __name__ == '__main__':
    main()
    