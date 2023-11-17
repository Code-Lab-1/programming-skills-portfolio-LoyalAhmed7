pets=[]

pet={ 'Animal': 'dog',
      'Name' : 'Bolt',
      'Owner' : 'Ahmed',
      'Food' : 'meat'
    }

pets.append(pet)

pet={ 'Animal': 'cat',
      'Name' : 'Daisy',
      'Owner' : 'Raheem',
      'Food' : 'fish'
    }

pets.append(pet)

for pet in pets:
    print("\nHere is what I know about " + pet['Name'].title())
    for key, value in pet.items():
        print("\t" + key + " : " + value)