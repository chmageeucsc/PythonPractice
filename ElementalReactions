# define Python user-defined exceptions
class InvalidEntry(Exception):
    "Raised when there are more than 3 inputs"
    pass

# input up to 3 elements
while True:
    try:
        print('All elemental possibilities: \n\npyro\tgeo\ndendro\tanemo\nhydro\tcryo\nelectro\n')
        input_string = input('Enter up to 3 elements of a list separated by space: \n')
        input_string = input_string.lower()
        user_list = input_string.split()
        print('\nPossible reactions:\n')
        if len(user_list) > 3:
            raise InvalidEntry
        break
    except InvalidEntry:
        print("Please enter no more than 3 elements...\n")  
        continue

if ('anemo' in user_list and ('pyro' or 'hydro' or 'cryo' or 'electro' in user_list)):
    if 'pyro' in user_list:
        print('anemo + pyro: pyro swirl')
    if 'hydro' in user_list:
        print('anemo + hydro: hydro swirl')
    if 'cryo' in user_list:
        print('anemo + cryo: cryo swirl')
    if 'electro' in user_list:
        print('anemo + electro: electro swirl')

if ('geo' in user_list and ('pyro' or 'hydro' or 'cryo' or 'electro' in user_list)):
    if 'pyro' in user_list:
        print('geo + pyro: pyro crystalization')
    if 'hydro' in user_list:
        print('geo + hydro: hydro crystalization')
    if 'cryo' in user_list:
        print('geo + cryo: cryo crystalization')
    if 'electro' in user_list:
        print('geo + electro: electro crystalization')

if ('dendro' in user_list):
    if ('pyro' in user_list):
        print('dendro + pyro: burning')
    if ('electro' in user_list):
        print('dendro + electro: quicken, aggravate, and spread')
    if ('hydro' in user_list):
        print('dendro + hydro: bloom')
        if ('electro' in user_list):
            print('dendro + hydro + electro: hyperbloom')
        if ('pyro' in user_list):
            print('dendro + hydro + pyro: burgeon')
    

if ('pyro' in user_list):
    if ('hydro' in user_list):
        print('pyro + hydro: vaporize')
    if('electro' in user_list):
        print("pyro + electro: overload")
    if ('cryo' in user_list):
        print('pyro + cryo: melt and reverse melt')

if ('hydro' in user_list):
    if ('electro' in user_list):
        print('hydro + electro: electro-charged')
    if('cryo' in user_list):
        print('hydro + cryo: frozen and shatter')
        
if ('cryo' in user_list):
    if ('electro' in user_list):
        print('cryo + electro: superconduct')

print('')
