instructor_dict = {'name': 'dylan', 'class': 'matrix', 'hobby': 'dodgeball'}

# whatever is not included, will remain the same
instructor_dict.update({'name': 'sean', 'class': 'matrix'})

print(instructor_dict)

# pip install flask-cors
# allows any server to work
# then instantiate it in init file