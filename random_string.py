import random



def random_string ():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ran_str = ''

    str_len = random.randint(1,10)

    for i in range(0, str_len):

        ran_str += random.choice(letters)
        
    return ran_str
    