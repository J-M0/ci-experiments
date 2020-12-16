import unittest
import hello

class TestHello(unittest.TestCase):
    
    def test_hello(self):
        self.assertEqual(hello.hello_str(), "Hello world")

if __name__ == "__main__":
    unittest.main()
