class User:
    '''
    class to create a new user
    '''
    
    users_list = []    
    
    def __init__(self,fname,lname,usname,psword):
        self.first_name = fname
        self.last_name = lname
        self.user_name = usname
        self.password = psword
        
    def save_user(self):
        User.users_list.append(self)
    