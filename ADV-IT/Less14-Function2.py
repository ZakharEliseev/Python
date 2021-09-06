def create_record(name, telephone, address):
    """Create record"""
    record = {
        'name': name,
        'phone': telephone,
        'address': address
    }
    return record


user1 = create_record('Vasya', '+790222222', 'Tunissia')
user2 = create_record('Petya', '+793333333', 'Munissia')
print(user1, user2)


def give_awarrd(medal, *persons):
    '''Give Medals to persons'''
    for person in persons:
        print('Tovarish ' + person.title() + ' Nagrazdaetsa medalyu  '  + medal)


give_awarrd('Za Berlin', 'vasa' , 'peta')
give_awarrd('Za London', 'peta', 'alex', 'Baala')