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
    preferences = {}        ### creates new dictionary 'preferences' with Boolean mapped to key of 'questions' dictionary
    for d, q in questions.items(): 
        ques = input(q)                     ###based on user input and stored as ques
        if ques == 'y' or ques == 'yes':    ###
            preferences[d] = True
        else:
            preferences[d] = False
    return preferences 

def new_drink(preferences):   ###this function creates a drink from ingredient lists located in "ingredients" dictionary
    drink = []                ###it's checking Boolean values in dictionary created in what_drink function
    for s, t in preferences.items():  
        if t == True:
            drink.append(random.choice(ingredients[s])) ###adds item from dictionary to new list called 'drinks' if boolean == True
        else:
            continue
    return drink
    
def name_drink(drink_names_adj, drink_names_noun):  ###this function takes lists above as arguments 
    x = random.choice(drink_names_adj)              ###randomly selects item from list
    y = random.choice(drink_names_noun)             ###repeats for noun list
    new_name = x + " " + y                          ###local variable that stores the drink name and creates concatenated string with a space
    return new_name
    
def main():
    drinking = True
    while drinking:
        preferences = what_drink(questions)             ###calls first function
        drink = new_drink(preferences)
        print("Based on what ye told me, here's what ye be drinkin': 'The {}'".format(name_drink(drink_names_adj, drink_names_noun)))
        for thing in drink:
            print('{}'.format(thing))
        money = input("Arrrg, hope ye be satisfied. How's about another?")
        if money == 'n' or money == 'no':
            drinking = False ###escapes while loop if condition true
        #main()
        ####called main function using recursion
        ###not considered good programming practice when handling large data sets or many imputs
        ###stacking functions can overload memory
        ###while loop will prevent this overload
    
if __name__ == '__main__':
    main()
    