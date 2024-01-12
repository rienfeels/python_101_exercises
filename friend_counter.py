def countFriends(person):
    friends_count = len(person.get('friends', []))
    result = person.copy()
    result['friends_count'] = friends_count
    return result

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

# Function call
result_ramit = countFriends(ramit)

# Display the result
print(result_ramit)
