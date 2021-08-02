import json
import unittest
import unittest.mock
import requests
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

    @unittest.mock.patch('requests.get')
    def test_get_ticket_count(self, mocked_get):
        mocked_get.return_value = unittest.mock.Mock(status_code=200, 
            json=lambda : {"count": {"value": 102, "refreshed_at": "2021-08-02T18:07:17+00:00"}})

        tCount = requestTickets.getTicketCount()

        self.assertTrue(type(tCount) == int)

        # assume account has at least one ticket
        self.assertTrue(tCount > 0)

    @unittest.mock.patch('requests.get')
    def test_get_page_of_tickets01(self, mocked_get):
        with open("project/data/examplePage1.json", "r") as JSON_FILE:
            mockDict = json.load(JSON_FILE)
            mocked_get.return_value = unittest.mock.Mock(status_code=200, json=lambda : mockDict)
        page_size = 25
        tJson = requestTickets.getPageOfTickets(page_size)

        self.assertTrue(type(tJson) == dict)
        self.assertTrue(len(tJson["tickets"]) <= page_size)

    @unittest.mock.patch('requests.get')
    def test_get_page_of_tickets02(self, mocked_get):
        with open("project/data/examplePage2.json", "r") as JSON_FILE:
            mockDict = json.load(JSON_FILE)
            mocked_get.return_value = unittest.mock.Mock(status_code=200, json=lambda : mockDict)
        page_size = 25
        tJson = requestTickets.getPageOfTickets(page_size, "project/data/examplePage2.json")

        self.assertTrue(type(tJson) == dict)
        self.assertTrue(len(tJson["tickets"]) <= page_size)

    def test_get_page_of_tickets03(self):
        with self.assertRaises(AssertionError): 
            requestTickets.getPageOfTickets(0)

    def test_get_page_of_tickets04(self):
        with self.assertRaises(AssertionError):
            requestTickets.getPageOfTickets(101)

    @unittest.mock.patch('requests.get')
    def test_get_page_of_tickets05(self, mocked_get):
        with open("project/data/example100Ticket.json", "r") as JSON_FILE:
            mockDict = json.load(JSON_FILE)
            mocked_get.return_value = unittest.mock.Mock(status_code=200, json=lambda : mockDict)
        page_size = 100
        tJson = requestTickets.getPageOfTickets(page_size)

        self.assertTrue(type(tJson) == dict)
        self.assertTrue(len(tJson["tickets"]) <= page_size)

    @unittest.mock.patch('requests.get')
    def test_get_tickets_by_id(self, mocked_get):
        with open("project/data/exampleTID.json", "r") as JSON_FILE:
            mockDict = json.load(JSON_FILE)
            mocked_get.return_value = unittest.mock.Mock(status_code=200, json=lambda : mockDict)
        testID = 2 
        tJson = requestTickets.getTicketByID(testID)

        self.assertTrue(type(tJson) == dict)
        self.assertIsNotNone(tJson["ticket"])
        self.assertIsNotNone(tJson["ticket"]["created_at"])
        self.assertIsNotNone(tJson["ticket"]["id"])

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
        def raiseConnectionException():
            raise requests.ConnectionError

        with self.assertRaises(SystemExit):
            raiseConnectionException()

    def test_check_exception_handler03(self):
        @zExceptions.handleExceptions
        def raiseException():
            raise Exception

        with self.assertRaises(SystemExit):
            raiseException()

if __name__ == '__main__': 
    unittest.main()