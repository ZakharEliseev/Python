import json
filename = 'user_settings.txt'
myfile = open(filename, mode='w', encoding='Latin-1')
player1 = {
    'PlayerName': 'Donald Trupm',
    'Score': 345,
    'awards': ['OR', 'NV', 'NY']
}

player2 = {
    'PlayerName': 'Clinton Hillary',
    'Score': 346,
    'awards': ['WT', 'TX', 'MI']
}

myplayeers = [player1, player2]
#----------------------Save by JSSON------------------

json.dump(myplayeers, myfile)
myfile.close()

#-----Load by JSON------

myfile = open(filename, mode='r', encoding='Latin-1')
json_data = json.load(myfile)
for user in json_data:
    print('Player name is :' + str(user['PlayerName']))
    print('Player score is: ' + str(user['Score']))
    print('Player awards: ' + str(user['awards'][0]))
    print('Player awards: ' + str(user['awards'][1]))
    print('Player awards: ' + str(user['awards'][2]))
    print('---------------------\n\n')