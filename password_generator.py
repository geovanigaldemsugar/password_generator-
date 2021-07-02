from hashlib import sha512
from random_string import random_string
from save_file import save_file
import os

begin = False
clearconsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

class Error(Exception):
    """ Base class for other exceptions"""


class WrongInput(Error):
    """ raised when there is a wrong input""" 
    pass








while True:

    if begin == False:
        print(''' 
.............     #@@@@@@@@@@@@&&&@&&&%... ..   ... .    .  
...........  *@@@@@@@@@@@@@@@@@@@@@@@&@@@@*........... ,. ..
..........(@@@@@@&@@@@@@@@@@@@@@@&@&@@&&@@@@@/..../@@@@@%%* 
........,@@@@&@@@&&@@&@&@&&@%&@&&&&@@@&&&&@@@@@@/*@@@@@&&@@(
.......%&@@@&&&%&&%&&&&@%&%@&%&%%&%&%%@%%&@@@@@@@@@@@@@&&@@%
......&&&&&&&&%&%&&&%@((*,,,,******/(%%&%&&&@@@@@@@@@@@&&@@@
.....%%&&&&&&&&(**,......,..,,,,,***((%%&&&&&@@@@@@@@@@&&%&@
.....&&&%&#/*,,,......,,,/&@&&&&&/,**/##%@&%&&&@@@@@@@@@&%@@
.....&&&&/**,,,,,,,,*(%@%#////****,*,*((%#&&%///*#%@@@@@@@@@
........#/******,,**/(((((((@@@@/*,,,**//%%@&#(%**/@@@@@@@@@
......../&&@&@&%(/****/(##(*#((,...,,,*/((&&&#%(/(**//&@@%. 
.........#/((**/%%*,,,*/*,,,,,....,,,****(&&%#%#*/*/        
........,/&##,&(///,,,*,,,,,,....,,,,****(##&##%/(/.        
.........,*%***,,,*,,,****/**,,,,,,*******/(%#&@&(*         
.........,/(/,,,,*/*//&&&//***/****,******//####&#*.        
..........,/%*****(###(***,,,,,,***********/(#(#(/(,.       
...........,/#(//*******//////****,*******/(#((#//(*..      
............,*((////(%&#(//,/***********//((//((/*/,*.....  
..............,(*(//////((#(//******///(#(/////(&@@/,.... ..
................(/*.///(/**,**,,**//(%#(//****/((@*.@.......
.................***...//******/(#%%(///*****/(#/@.(.*......
.................***,.....*@&((#((///**///*//(.@*&(*/*... ..
..................,*,.....#@@%((///////////,.@#.@,*# %.,..#.
...................,,,.... /@@%#(((((/.,@/%(&@/#//(.#(,&. (&
.....................,,..(,,@*@//(#/#@(#@(&, @# @/*@,,#(. */
.................../.*(,../,,@/@,#*(@*/%.@.(@,,#/*& *&&(#&@%
.............,((**,&&&*,&/*@/,@/@(#&,@((@*@#*@**& .@#.%,,&&*
........../((/(#%*(%@*& (&,@/&#&,@ #.#&,&/*&.(&*@&&@@&(@#&&&) ''')

        print('----------------------------')
        print('Hello there, im called genna')
        print('----------------------------')
        print('im a password generator')
        begin = True

   
    print('----------------------------')
    try:
        pass_len = int(input('what do you want the length of your password to be, the max is 162:'))

        if pass_len > 162:
            clearconsole()
            print('----------------------------')
            print('password lenght is too long please choose reduce the size')

        elif pass_len == 0:
            clearconsole()
            print('----------------------------')
            print('password length cant be zero please choose a higher number')

        else:
            password = sha512(random_string().encode()).hexdigest()[0:pass_len]
            print('-----------------------------')
            print(f'Your password is: {password}')
            print('-----------------------------')
            pass_should_be_saved = input('Do want your password to be saved (y/n):').lower()
            
            while True:
                try:
                    if pass_should_be_saved == 'y' or pass_should_be_saved == 'yes':
                        print('-----------------------------')
                        for_what_app = input('Which app or website do you want to save it for:')

                        save_file(for_what_app + ': ' + password)
                        break

                    elif pass_should_be_saved == 'n' or pass_should_be_saved == 'no':
                        break

                    else:
                        raise WrongInput

                except WrongInput:
                    clearconsole()
                    print('-----------------------------')
                    pass_should_be_saved =  input('Please enter an valid input either (y/n):')

                
            print('-----------------------------')
            print('Thank you for using genna the password generator')
            break

    except ValueError:
        clearconsole()
        print('-----------------------------')
        print('Please enter an valid input')







    