favorite_colors = [
    'red',
    'blue',
    'orange',
    'white',
]
favorite_colors_dict = {
    'a': 'red',
    'b': 'blue',
    'c': 'orange',
    'd': 'white',
    'e': 'black',
}  # dict

# get
print(favorite_colors[0])
print(favorite_colors_dict['b'])
print(favorite_colors_dict.get('b'))

# set
favorite_colors[1] = '파랑'
favorite_colors_dict['c'] = '오랜지'
print(favorite_colors)
print(favorite_colors_dict)
