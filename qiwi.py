from SimpleQIWI import * 
log ='''
   ____ _ __    __ _ _        _              
  /___ (_) / /\ \ (_) |_ ___ | | _____ _ __  
 //  / / \ \/  \/ / | __/ _ \| |/ / _ \ '_ \ 
/ \_/ /| |\  /\  /| | || (_) |   <  __/ | | |
\___,_\|_| \/  \/ |_|\__\___/|_|\_\___|_| |_|
################(Version:2.1)################
|                  Author                   |
|           JTexas   and    Paris302        |
#############################################
'''
print (log)
def user_info():
  global token,api
  token=input('Enter token: ') 
  api = QApi(token=token, phone="") 
  try: 
    print('Balance:',api.balance) 
  except:
    print('Error check')
    return user_info()
user_info()
acc=input('Phone: +')
com=input('Comment: ') 
t=input('Mod id? ')
if t == 'y':
  print (api.full_balance)
  id = input('Id: ')
else:
    id='643'
def pay_info():
  try:
    api.pay(account=acc, amount=input('Pay: '), comment=com, acc_id=id, currency='643') 
  except:
    print('Error pay')
    return pay_info()
pay_info()
print(api.balance)
print('Successfull')
input('Exit')