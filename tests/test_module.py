import unittest
from ppg_pre import ppg2specgram
from ppg_pre import get_ppg_sample
import numpy as np

class TestClass(unittest.TestCase):
    
    
    def SetUp(self):
        pass
        
    def tearDown(self):
        pass
        
    def test_end2end(self):
        self.x = get_ppg_sample()
        self.assertEqual(type(self.x),np.ndarray)
        
        self.x = ppg2specgram(self.x)
        self.assertTrue(len(self.x.shape) == 2)
    
    # def test_1_raise_exception(self):
    #     self.x = ppg2specgram(self.x)
    #     self.assertTrue(len(self.x.shape) == 2)

# def suite():
#     suite = unittest.TestSuite()
#     suite.addTest(TestClass('test_result'))
#     suite.addTest(TestClass('test_raise_exception'))
#     return suite

# if __name__ == '__main__':
#     runner = unittest.TextTestRunner()
#     runner.run(suite())

    
if __name__ == "__main__":
    unittest.main()