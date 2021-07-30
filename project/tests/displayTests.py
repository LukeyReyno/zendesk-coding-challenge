import unittest
import sys
import os

cd = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(cd)
sys.path.append(parent)
import display

class DisplayTests(unittest.TestCase):
    """
    Tests the attributes and Methods of Display Object
    
    Connects to the Zendesk API
    (Assumes Multiple Tickets on Account)
    """

    def test_create_display(self):
        d = display.Display()

        self.assertTrue(type(d.totalTickets) == int)
        self.assertTrue(d.totalTickets > 0)
        self.assertTrue(type(d.numPages) == int)
        self.assertTrue(d.numPages > 0)
        self.assertTrue(type(d.currentPageIndex) == int)
        self.assertTrue(d.currentPageIndex == 0)

if __name__ == '__main__': 
    unittest.main()