# Adventure Game

user_input = input("Would you like to play ? (Yes / No) ")

if user_input.lower().strip() == 'yes' :
    
    a = input("You reached a crossroad, would you like to go left or right ? ").lower().strip()
    if a == 'left' :
        
        b = input("You encountered Godzilla !, would you like to attack or run ? ").lower().strip()
        if b == 'attack' :
            print('That was not a great idea, you lost !')
        else :yes
            print('good choice, you are safe now.')
            
    elif a == 'right' :
        print('you lost !')
        
    else :
        print('oops..! you fell into godzilla\'s nuclear den !(you\'re dead)')
    
else :
    print('King Kong killed you !(you\'re dead)')