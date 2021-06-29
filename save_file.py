


def save_file(password):

    with  open('password.txt', 'w') as pass_file:
       pass_file.write(password + ' ')

    print('Password saved succesfully')