"""
    Using get method to get the value of a key in dictionary. 
    If the key is not present, it returns None.
"""

user = {
    'name': 'mohamed',
    'class': 'test123',
    'strength': 79,
    'health': 100
}

x = user['name']
# x = user['dfskljfg'] #Errot ---> KeyError: 'dfskljfg'


x = user.get('name')
x = user.get('fdhfjhsdf') # return None
x = user.get('fdhfjhsdf', 0) # return 0


print(x)