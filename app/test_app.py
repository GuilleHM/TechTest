import app, unittest, os

# Directory for saving images
img_dir = "static/image/" 

class MyTestCase(unittest.TestCase):

    # TEST SETUP
    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    # TESTS
    def test_home_exists(self):
        """
        Test home url exists (correct status code)
        """
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_blue_image_exists_or_not(self):
        """
        Test image named 'blue' exist or not
        """
        response = self.app.get('/image/blue')
        if len(os.listdir(img_dir)):
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'blue image', response.data)
        else:
            self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()