import unittest
from zTicket import ZendeskTicket

import requestTickets

class RequestTests(unittest.TestCase):
    """
    Tests the attributes and Methods of Zendesk Tickets

    (Assumes Multiple Tickets on account)
    """

    def test_get_ticket_count(self):
        tCount = requestTickets.getTicketCount()

        self.assertTrue(type(tCount) == int)

        # assume account has at least one ticket
        self.assertTrue(tCount > 0)

    def test_get_page_of_tickets01(self):
        tList = requestTickets.getPageOfTickets(25)

        self.assertTrue(type(tList) == list)
        self.assertTrue(len(tList) > 0) # if tickets on account
        self.assertTrue(type(tList[0]) == ZendeskTicket)

    def test_get_page_of_tickets02(self):
        with self.assertRaises(AssertionError): 
            requestTickets.getPageOfTickets(0)
            requestTickets.getPageOfTickets(101)

    def test_get_page_of_tickets03(self):
        tList = requestTickets.getPageOfTickets(1)

        self.assertTrue(type(tList) == list)
        self.assertTrue(len(tList) > 0) # if tickets on account
        self.assertTrue(type(tList[0]) == ZendeskTicket)

    def test_get_page_of_tickets04(self):
        tList = requestTickets.getPageOfTickets(1)

        self.assertTrue(type(tList) == list)
        self.assertTrue(len(tList) > 0) # if tickets on account
        self.assertTrue(type(tList[0]) == ZendeskTicket)
        

if __name__ == '__main__': 
    unittest.main()