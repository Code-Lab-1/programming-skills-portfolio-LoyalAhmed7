def describe_city(city, country='Turkey'):
    msg = city.title() + " is in " + country.title() 
    print(msg)
describe_city('Istanbul')
describe_city('Ankara')
describe_city('Lahore' , 'Pakistan')