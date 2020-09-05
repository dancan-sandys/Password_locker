class Credentials:
    '''
    A class to store and generate credentials for the user's accounts
    '''
    
    Credentials_list = []
    '''
    A list to store the credentials
    '''
    
    def __init__(self, site, password):
        
        '''
        initialize the Credentials class
        '''
            
        self.site_name = site
        self.site_password = password
    
    # def add_credentials():
        
    #     '''
    #     a function to add the credentials
    #     '''
        
    #     new_credentials = Credentials(input('Enter the site you would like to secure'), input('Enter the site password'))
    #     return new_credentials
    
    
    def save_credentials():
        
        '''
        a function to save the credentials
        '''
        new_credentials = Credentials.add_credentials()
        
        Credentials.Credentials_list.append(new_credentials)
    
    @classmethod
    def find_credentials(cls):
        
        search_credential = input('Enter the site whose passowrd you would like to search')
        
        for site in Credentials.Credentials_list:
            if site.site_name == search_credential:
                print(f'Your {site.site_name} password is {site.site_password}')
                return site.site_password
            
            
            else:
                print('The site you entered does not exist in our data base. You can add it below.')
                
                
Credentials.save_credentials()
Credentials.find_credentials()
    
    