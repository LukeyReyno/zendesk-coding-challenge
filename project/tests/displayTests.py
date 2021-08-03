import unittest
import sys
import os
import json

# Set up path for correct feature implementation
cd = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(cd)
sys.path.append(parent)
import display

PAGE_ONE = "project/data/examplePage1.json"
COUNT_JSON = "project/data/exampleCount.json"

# Used for testing instead of making full requests
def getPageOfTicketsLocal(pageSize, url):
    """
    returns a json-encoded object of a page of Zendesk Tickets locally
    (Mocking the Response)
    
    pageSize in range of [1, 100]
    """

    assert(1 <= pageSize <= 100)
    if (url == None):
        url = PAGE_ONE
    with open(url, "r") as JSON_IN:
        ticketDict = json.load(JSON_IN)
    return ticketDict

def getTicketCountLocal():
    cDict = getPageOfTicketsLocal(1, COUNT_JSON)
    return cDict['count']['value']

display.requestTickets.getPageOfTickets = getPageOfTicketsLocal
display.requestTickets.getTicketCount = getTicketCountLocal

class DisplayTests(unittest.TestCase):
    """
    Tests the attributes and Methods of Display Object
    
    Connects to the Zendesk API
    (Assumes Multiple Tickets on Account)
    """

    def test_create_display(self):
        # tests newly instantiated display
        d = display.Display()

        self.assertTrue(type(d.totalTickets) == int)
        self.assertTrue(d.totalTickets > 0)
        self.assertTrue(type(d.numPages) == int)
        self.assertTrue(d.numPages > 0)
        self.assertTrue(type(d.currentPageIndex) == int)
        self.assertTrue(d.currentPageIndex == 0)

    def test_display_input(self):
        d = display.Display()

        # print functions return none
        self.assertIsNone(d.inputManager('exit'))
        self.assertIsNone(d.inputManager('help'))

        # Initialized Value
        self.assertEqual(d.currentPageIndex, 0)

        # Can't scroll down past page 0
        self.assertIsNone(d.inputManager('down'))
        self.assertEqual(d.currentPageIndex, 0)

        # Tests Display functionality on Current Page
        self.assertIsNone(d.inputManager('display'))

        if (d.numPages > 1):
            # These tests only work with more than 1 page
            self.assertIsNone(d.inputManager('up'))
            self.assertEqual(d.currentPageIndex, 1)

            # Tests Display functionality on New Page
            self.assertIsNone(d.inputManager('display'))

            # Return to Original Page
            self.assertIsNone(d.inputManager('down'))
            self.assertEqual(d.currentPageIndex, 0)
            self.assertIsNone(d.inputManager('display'))

            # This time with 'origin'
            self.assertIsNone(d.inputManager('up'))
            self.assertEqual(d.currentPageIndex, 1)

            # Return to Original Page
            self.assertIsNone(d.inputManager('origin'))
            self.assertEqual(d.currentPageIndex, 0)
        else: # pragma: no cover
            # Only One Page Test
            self.assertIsNone(d.inputManager('up'))
            self.assertEqual(d.currentPageIndex, 0)
        
        # Tests an valid Ticket Num
        self.assertIsNone(d.inputManager('1'))

        # Tests an invalid Ticket Num
        self.assertIsNone(d.inputManager('0'))
        self.assertIsNone(d.inputManager('-1'))

        self.assertIsNone(d.inputManager('non-valid'))
        self.assertIsNone(d.printAllPageIDs())

        self.assertTrue(type(d.urls) == list)

    def test_initialized_page(self):
        p = display.Page(1)

        self.assertEqual(p.tickets, [])
        self.assertEqual(p.pageNumber, 1)
        self.assertIsNone(p.minTicketID)
        self.assertIsNone(p.maxTicketID)
        self.assertFalse(p.isLoaded)

        # Load
        p.loadPage(None)
        self.assertTrue(len(p.tickets) > 0)
        self.assertEqual(p.pageNumber, 1)
        self.assertTrue(type(p.numTickets) == int)
        self.assertTrue(type(p.nextUrl) == str)
        self.assertIsNone(p.minTicketID)
        self.assertIsNone(p.maxTicketID)
        self.assertTrue(p.isLoaded)
        p.loadPage(None)

if __name__ == '__main__': 
    unittest.main()