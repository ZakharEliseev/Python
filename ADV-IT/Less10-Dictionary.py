enemy = {
            'loc_x': 70,
            'loc_y': 50,
            'color': 'green',
            'health': 100,
            'name': 'Vrag'
}
print(enemy)
print('Location X = ' + str(enemy['loc_x']))
print('Location Y = ' + str(enemy['loc_y']))
print('Name is = ' + enemy['name'])
enemy['range'] = 'Admiral'
print(enemy)
del enemy['range']
print(enemy)
enemy['loc_x'] = enemy['loc_x'] + 40
enemy['health'] = enemy['health'] - 30
if enemy['health'] < 80:
    enemy['color'] = 'yellow'
print(enemy)
print(enemy.keys())
print(enemy.values())