from ApiCode import app
import unittest

class FlaskTest(unittest.TestCase):

    # Check for response 200 on end points
    def test_1(self):
        tester = app.test_client(self)
        response = tester.get("/getMakes")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)
    def test_2(self):
        tester = app.test_client(self)
        response = tester.get("/getCars")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)
    def test_3(self):
        tester = app.test_client(self)
        response = tester.get("/getCertainCars?priceStart=70000&priceEnd=200000&mileageStart=30000&mileageEnd=70000")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)

    # Check for response 404 if not found 
    def test_4(self):
        tester = app.test_client(self)
        response = tester.get("/abc")
        statuscode = response.status_code
        self.assertEqual(statuscode,404)

    # Checks for the response type
    def test_5(self):
        tester = app.test_client(self)
        response = tester.get("/getMakes")
        contentType = response.content_type
        self.assertEqual(contentType,"application/json")
    def test_6(self):
        tester = app.test_client(self)
        response = tester.get("/getCars")
        contentType = response.content_type
        self.assertEqual(contentType,"application/json")
    def test_7(self):
        tester = app.test_client(self)
        response = tester.get("/getCertainCars?priceStart=70000&priceEnd=200000&mileageStart=30000&mileageEnd=70000")
        contentType = response.content_type
        self.assertEqual(contentType,"application/json")
        

if __name__ == "__main__":
    unittest.main()
