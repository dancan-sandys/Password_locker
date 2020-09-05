import unittest

from credentials import Credentials

class Test_credentials(unittest.TestCase):
    
     
    def setUp(self):
        
        self.new_site = Credentials("Facebook","Stanford1*")
        
    def test_init(self):
        
        '''
        Test if the credentials class has been initialized
        '''
        self.assertEqual(self.new_site.site_name, "Facebook")
        self.assertEqual(self.new_site.site_password, "Stanford1*")
        
    def test_adding_credentials(self):
        new_credentails = Credentials.add_credentials()
        self.assertTrue(new_credentails)
        
        
if __name__ == "__main__":
    unittest.main()