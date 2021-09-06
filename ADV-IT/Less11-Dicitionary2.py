enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Vrag',
    'awards': 'Za stalina',
    'image': ['im1.jpg', 'im2.jpg', 'im3.jpg']
}

all_enemies = []

for x in range(0, 10):  # Variant dobavleniya 3
    all_enemies.append(enemy.copy())  # vicv 1 stroku


for ene in all_enemies:  # vivod v stolbec
    print(ene)
print('_______________')
all_enemies[1]['health'] += 30
all_enemies[2]['name'] = 'ololo'
all_enemies[3]['loc_x'] += 10
for ene in all_enemies:  # vivod v stolbec
    print(ene)
# all_enemies = [] #Variant dobavleniya 1
# all_enemies.append(enemy)
# all_enemies.append(enemy)
# all_enemies.append(enemy)
# print(all_enemies)
# print('_______________')
# all_enemies = [enemy, enemy, enemy]  #Variant dobavleniya 2
# print(all_enemies)
print('_______________')
