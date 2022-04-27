import unittest
import requests
class ApiTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000/mortality/v.1/"
    MORT_STATE = "{}/mortality-state".format(API_URL)
    MORT_STATE_YEAR = "{}/mortality-state-year".format(API_URL)

    #TEST FOR /mortality-state GET FUNCTION
    def test_1_mortality_state(self): 
        id = 10
        r = requests.get("{}?state={}".format(ApiTest.MORT_STATE, id))
        self.assertEqual(r.status_code, 200)
    
    #TEST FOR /mortality-state-year GET FUNCTION
    def test_2_mortality_state_year(self): 
        state = 10
        year = 2012
        r = requests.get("{}?state={}&year={}".format(ApiTest.MORT_STATE, state, year))
        self.assertEqual(r.status_code, 200)
