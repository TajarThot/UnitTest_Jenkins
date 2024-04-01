import unittest
import requests

class TestWebsiteConnection(unittest.TestCase):
    
    def test_website_connection(self):
        
      #Enter any website for testing i have entered atg.world for the test
        website_url = 'https://atg.world'
        
        try:
            
          # Attempt to connect to the website
            response = requests.get(website_url)
            
            # Check if the response status code indicates a successful connection
            self.assertTrue(response.status_code // 100 == 2, f"Failed to connect to {website_url}. Status code: {response.status_code}")
            
            # Log statement on successful connection
            print(f"Successfully connected to {website_url}. Status code: {response.status_code}")
        
        except requests.ConnectionError as e:
            # Log statement on connection error
          
            print(f"Failed to connect to {website_url}. Connection error: {e}")
            self.fail(f"Failed to connect to {website_url}. Connection error: {e}")

if __name__ == '__main__':
    unittest.main()
