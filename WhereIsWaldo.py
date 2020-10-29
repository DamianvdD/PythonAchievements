import random

people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]
random.shuffle(people)

def findWaldo():
    x = 0

    for person in people:
        if(person == 'Waldo'):
            print(person + ' is gevonden!')
            break
        else:
            x += 1

    return x

stoel = findWaldo()

print('Waldo zit op stoel nummer: ' + str(stoel))
