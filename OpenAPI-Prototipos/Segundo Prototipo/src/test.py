import unittest

class TestAPI(unittest.TestCase):
    URL = "http://127.0.0.1:5000/"

    def test_main(self):
        resp = requests.get(self.URL)
        self.assertEqual(resp.status_code, 200)
        print("Test main completed.")

if __name__ == "__main__":
    tester = TestAPI()
    tester.test_main()
