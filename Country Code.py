country_code = {
    'India' : '0091',
    'Australi' : '0025',
    'Nerpal' : '00977',
    'Bangladesh' : '00880',
}

print("Country Code for India: ")
print(country_code.get('India', 'Not Found'))

print("Country Code for Bangaldesh: ")
print(country_code.get('Bangladesh', 'Not Found'))

print("Country Code for Japan: ")
print(country_code.get('Japan', 'Not Found'))