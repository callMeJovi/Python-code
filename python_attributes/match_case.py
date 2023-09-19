"""
match...case
"""
status = 404
match status:
    case 200:
        print('Access to website is successful')
    case 404:
        print("website doesn't exist")
    case 500:
        print("Error")
    case _:
        print('other issues')


p1 = ('zs', 23, 'Monsieur')
p2 = ('zoey', 25, 'Madame')
p3 = ('max', 12, 'Madamosielle')
p4 = ('gaga', 53, 'Monsieur')


def test(person):
    match person:
        case (name, _, 'Monsieur'):  # age is indifferent so replaced by "_"
            print(f'{name} is Monsieur')
        case (name, _, 'Madamosielle'):  # name is indifferent so replaced by "_"
            print(f'{name} is Madamosielle')
        case (name, age, 'Madame'):
            print(f'{name} is {age} and is Madame')
        case (name, age, _,):  # gender is indifferent
            print(f'{name} is {age}')

        case _:
            print('not match')


test(p1)
test(p2)
test(p3)
test(p4)
