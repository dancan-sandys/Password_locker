from user import User
from credentials import Credentials


first_response = int(input("Hello, Respond with  1 to create an account and 2 to login into an existing account"))    

if first_response == 1:
        
    '''
    function to run when the user does not have an account with us
    '''
    
    creating_an_account()  
     
    '''
    first user's response to determine wehter or not he/she has an account
    '''  


elif(first_response == 2):
    
    '''
    function to login if the user already has an account
    '''
    
    entered_username = input("Enter your username")
    
    case_account = User.find_account_by_username(entered_username)
    
    if case_account.password 
    
    
    
    

def creating_an_account():

   
        
    def creating_an_account():   
        new_user = User.generate_user()
        '''
        Creating the user account
        '''
        
        
        
        new_user_username = new_user.user_name
        
        
        
        print(f"Hang on {new_user_username} as we check if your details have been used in our databasse before")
        existing_account = User.find_account_by_username(new_user_username)
        '''
        checking if username already exists
        '''
        try:
            if existing_account.user_name == new_user_username:
                print("The account details you entered are already in use, please log in or try using another username")
        except:
            print("Your account has successfully been created")
        
        new_user.save_user()
        '''
        saving the user's account
        '''