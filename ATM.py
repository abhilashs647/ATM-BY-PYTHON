#libraries imported
from datetime import date
today = date.today()
#---------------------------------

#global variables
name = "ABHILASH KUMAR SINGH"
total_amount = 500000


#------------------functions----------------------------------
def amount_info():
    global total_amount
    print(f'''
      ----------------------------------------
      - Name : {name}
      - Total Amount : {total_amount}
      - Date : {today}
      ----------------------------------------
      ''')

def withdraw_money():
    name = "ABHILASH KUMAR SINGH"
    withdraw_amount = int(input("Enter desire amount : "))
    
    global total_amount 
    total_amount = total_amount - withdraw_amount
    
    print(f'''
      -----------------
      - Name : {name}
      - Amount :RS {withdraw_amount} 
      - Amount Remaining : RS {total_amount} 
      - Date : {today}
      -----------------
      ''')
      
def sent_money():
    name = "ABHILASH KUMAR SINGH"
    recpient_name = input("Enter name or phone number : ")
    sent_amount = int(input("Enter amount to send : "))
    
    global total_amount 
    total_amount = total_amount - sent_amount
    
    print(f'''
      ----------------------------------------
      - Name : {name}
      - Recpient Name : {recpient_name}
      - Amount :RS {sent_amount} 
      - Amount Remaining :RS {total_amount} 
      - Date : {today}
      ----------------------------------------
      ''')
      
#-------------------ATM Logic ----------------------------

pin_code = int(input("Enter your 4 digit pin code : "))

if pin_code == 3322:
    print(f"Welcome {name} !")
    
    user_choice = input('''
        1 : Enter w for withdraw money
        2 : Enter s for sending money
        3 : Enter a for account information
        4 : Enter q for quit
                        ''')
    
    if user_choice == "w":
        withdraw_money()
    elif user_choice =="s":
        sent_money()
    elif user_choice =="a":
        amount_info()
    elif user_choice =="q":
        print("*** Thank you using our ATM *** ")
    

else:
    print(f''' 
          *******************
               Warning ! 
          Wrong Code Entered 
          Ejecting your card... 
          *******************
          ''')