import sys, random

print("Welcome to the random name generator. \n")
print("")

first = ('Richard', 'Robert', 'William', 'Bill', 'Bob', 'Eveline', 'Alice', 
        'Tabby', 'Beth', 'Joe Mike', 'Jager'
)

last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
        'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
        'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
        'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
        'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
        'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
        'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
        'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
        'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
        'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
        'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
        'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
        'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
        'Woolysocks'
)

while True: 
    firstName = random.choice(first)
    
    lastName = random.choice(last)
    
    print("\n\n")
    
    print("{} {}".format(firstName, lastName), file=sys.stderr)
    print("\n\n")
    
    try_again = input("\n\nTry again? (Press Enter else press n to quit)\n ")
    if try_again.lower() == "n":
        break
    
input("\nPress Enter to exit.")