import unittest


from credentials import Credentials

class Test_credentials(unittest.TestCase):
    
     
    def setUp(self):
        
        self.new_site = Credentials("Facebook","Stanford1*")
    
    def tearDown(self):

        Credentials.Credentials_list = []
        
    def test_init(self):
        
        '''
        Test if the credentials class has been initialized
        '''
        self.assertEqual(self.new_site.site_name, "Facebook")
        self.assertEqual(self.new_site.site_password, "Stanford1*")
        
    def test_adding_credentials(self):
        '''
        test if a user can add credentials to a certain site
        '''
        
        new_credentails = Credentials.add_credentials()
        self.assertTrue(new_credentails)
        
    def test_saving_credentials(self):
        '''
        test if a user can save credentials of a certain site
        '''
        self.new_site.save_credentials()
        self.assertEqual(len(Credentials.Credentials_list),1)
    def test_display credentials(self):
        self.assertEqual(Credentials.Credentials_list, Credentials.display_credentials)
    
        
if __name__ == "__main__":
    unittest.main()