import os


def get_old_passwords(password):

   with open('passwords.txt', 'r') as pass_data:
      old_passwords_list = pass_data.read().split()
      old_passwords = ''

      for i in old_passwords_list:
         old_passwords += i + ' '

      return old_passwords + password + ' '



def save_file(password):

   if os.path.exists('passwords.txt') == True:
      old_passwords = get_old_passwords(password)

      with open('passwords.txt', 'w') as pass_file:
         pass_file.write(old_passwords)

   else:

      with open('passwords.txt', 'w') as pass_file:
         pass_file.write(password + ' ')
   
   print('-----------------------------')
   print('your password has been saved succesfully')



