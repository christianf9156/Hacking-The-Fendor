import csv
import json

compromised_users = []

# -----------------------------------------
# 1) Reading the Passwords

# Opens file called passwords.csv then closes the file
with open('passwords.csv') as password_file:
  # Saves contents of variable file password_file
  password_csv = csv.DictReader(password_file)
  # Shows which User's passwords are leaked
  for password_row in password_csv:
    compromised_users.append(password_row['Username'])


# Open file in 'w'rite mode to write to the file
with open('compromised_users.txt', 'w') as compromised_users_file:
  # Adding users from list to the txt file
  for compromised_user in compromised_users:
    compromised_users_file.write(compromised_user + "\n")
# -----------------------------------------


# -----------------------------------------
# 2) Notifying the Boss

with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}
  # Turns python dictionary into a json file
  json.dump(boss_message_dict, boss_message)
# -----------------------------------------


# -----------------------------------------
# 3) Scrambling the Password

with open('new_passwords.csv', 'w') as new_passwords_obj:
  slash_null_sig = """ 
_  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""
  new_passwords_obj.write(slash_null_sig)

  