# Generate band name by combining city and pet name, if you never had a pet, then combine with favourite movie

print('Welcome to the Band Name Generator')

def generate_band_name():
    
    print('What\'s the name of the city you grew up in?')
    city = input()
    print('What\'s your pet\'s name or your favourite movie?')
    petNameOrFavMovie = input()
    
    return print('Your band name could be {} {}'.format(city, petNameOrFavMovie))


generate_band_name()





## References on formatting inputs: 
# https://sahiljain444.medium.com/format-specifiers-in-python-601df860a6a4
# https://www.linisnil.com/articles/practical-guide-to-python-string-format-specifiers/
