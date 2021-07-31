import unittest
import sys
import os

cd = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(cd)
sys.path.append(parent)
import requestTickets, zExceptions

class RequestTests(unittest.TestCase):
    """
    Tests the functions that request ticket Jsons

    (Assumes Multiple Tickets on account)
    """

    def test_get_ticket_count(self):
        tCount = requestTickets.getTicketCount()

        self.assertTrue(type(tCount) == int)

        # assume account has at least one ticket
        self.assertTrue(tCount > 0)

    def test_get_page_of_tickets01(self):
        page_size = 25
        tJson = requestTickets.getPageOfTickets(page_size)

        self.assertTrue(type(tJson) == dict)
        self.assertTrue(len(tJson["tickets"]) <= page_size)

    def test_get_page_of_tickets02(self):
        with self.assertRaises(AssertionError): 
            requestTickets.getPageOfTickets(0)

    def test_get_page_of_tickets03(self):
        with self.assertRaises(AssertionError):
            requestTickets.getPageOfTickets(101)

    def test_get_page_of_tickets04(self):
        page_size = 25
        tJson = requestTickets.getPageOfTickets(page_size)

        self.assertTrue(type(tJson) == dict)
        self.assertTrue(len(tJson["tickets"]) <= page_size)

    def test_get_page_of_tickets05(self):
        page_size = 100
        tJson = requestTickets.getPageOfTickets(page_size)

        self.assertTrue(type(tJson) == dict)
        self.assertTrue(len(tJson["tickets"]) <= page_size)

    def test_get_tickets_json(self):
        tJson = requestTickets.getTicketsJSON()

        self.assertTrue(type(tJson) == dict)
        self.assertIsNotNone(tJson["tickets"])

    def test_get_tickets_by_id(self):
        testID = 2 
        tJson = requestTickets.getTicketByID(testID)

        self.assertTrue(type(tJson) == dict)
        self.assertIsNotNone(tJson["ticket"])

    def test_check_status_code(self):
        self.assertIsNone(requestTickets.checkStatusCode(200))

        with self.assertRaises(zExceptions.ZendeskAPIException):
            requestTickets.checkStatusCode(404)

        with self.assertRaises(zExceptions.ZendeskAPIException):
            requestTickets.checkStatusCode(199)

    def test_check_exception_handler01(self):
        @zExceptions.handleExceptions
        def raiseZException():
            raise zExceptions.ZendeskAPIException

        with self.assertRaises(SystemExit):
            raiseZException()

    def test_check_exception_handler02(self):
        @zExceptions.handleExceptions
        def raiseException():
            raise Exception

        with self.assertRaises(SystemExit):
            raiseException()

if __name__ == '__main__': 
    unittest.main()