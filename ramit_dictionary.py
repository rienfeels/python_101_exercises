ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movies', 'tennis'],
    'friends': [
        {
        'name': 'Jasmine',
        'email': 'jasmine@yahoo.com',
        'interests': ['photography', 'tennis']
        },
        {
        'name': 'Jan',
        'email': 'jan@hotmail.com',
        'interests': ['movies', 'tv']
        }
    ]
}

print(ramit['email'])

print(ramit['interests'][0])

for friend in ramit['friends']: 
    if friend['name'] == "Jasmine": 
        print(friend ['email'])
        
for friend in ramit['friends']:
    if friend['name'] == "Jan":
        print(friend ['interests'][1])