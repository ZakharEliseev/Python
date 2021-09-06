import json
from random import randint
str_json = '''
{
"response": {
    "count": 6,
        "items": [{
            "first_name": "Анастасия",
            "id": 14239825,
            "last_name": "Архипова",
            "can_access_closed": false
        
    }, {
            "first_name": "Елена",
            "id": 631137325,
            "last_name": "Светлакова",
            "can_access_closed": true
            
        }]
    }
}
'''
print(type(str_json))
data = json.loads(str_json)
print(type(data))
for item in  data['response']['items']:
#    print(item['first_name'], item['last_name'])
    del item['id']
    item['likes'] = randint(100, 200)
    item['a'] = None
print(data['response']['items'])

new_json = json.dumps(data, indent=2)
print(new_json)

print(json.loads(new_json))

