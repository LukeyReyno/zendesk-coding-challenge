import unittest
import json

from project.zTicket import ZendeskTicket, ticketErrorHandler

# tests constructing the Zendesk Ticket object with a dict
with open("project/data/exampleTID.json", "r") as JSON_FILE:
    tDict = json.load(JSON_FILE)

tDict = tDict['ticket'] # One Ticket JSON
zT = ZendeskTicket(tDict)
zT2 = ZendeskTicket(tDict)


class TicketTests(unittest.TestCase):
    """
    Tests the attributes and Methods of Zendesk Tickets

    (Assumes Multiple Tickets on account)
    """
    def test_ticket_attributes_01(self):
        # tests that the dict entries are translated properly
        self.assertEqual(zT.id, tDict['id'])
        self.assertEqual(zT.description, tDict['description'])
        self.assertEqual(zT.requester_id, tDict['requester_id'])
        self.assertEqual(zT.subject, tDict['subject'])
        self.assertEqual(zT.tags, tDict['tags'])
        self.assertEqual(zT.status, tDict['status'])

        # Date attribute gets formatted
        self.assertNotEqual(zT.date, tDict["created_at"])
        self.assertTrue(type(zT.date) == str)
        self.assertTrue("at" in zT.date)

    def test_ticket_str(self):
        # tests the string version of Zendesk Ticket
        self.assertEqual(str(zT)[:3], "ID-")

    def test_ticket_detailed_str(self):
        # makes sure the correct string is returned
        string = zT.detailedView()
        self.assertTrue(type(string) == str)
        self.assertEqual(string[:24], "\n|-|-|-|-|-|-|-|-|-|-|-|")

    def test_ticket_eq01(self):
        #tests tickets equality method
        self.assertEqual(zT, zT2)
    
    def test_ticket_eq02(self):
        #tests tickets equality method
        zT2.id = 8
        self.assertNotEqual(zT, zT2)

    def test_ticket_eq03(self):
        ls = []
        #tests tickets equality method
        self.assertNotEqual(zT, ls)

    def test_error_handler01(self):
        # Tests the error handler with an invalid dict
        zTError = ZendeskTicket({})

        self.assertEqual(zTError.id, None)
        self.assertEqual(zTError.description, None)
        self.assertEqual(zTError.requester_id, None)
        self.assertEqual(zTError.subject, None)
        self.assertEqual(zTError.tags, None)
        self.assertEqual(zTError.status, None)

    def test_error_handler02(self):
        # Tests the error handler with an invalid type
        zTError = ZendeskTicket("invalid")

        self.assertEqual(zTError.id, None)
        self.assertEqual(zTError.description, None)
        self.assertEqual(zTError.requester_id, None)
        self.assertEqual(zTError.subject, None)
        self.assertEqual(zTError.tags, None)
        self.assertEqual(zTError.status, None)

    def test_error_handler03(self):
        # Tests exception handler with specific exceptions
        @ticketErrorHandler
        def raiseException():
            raise Exception

        with self.assertRaises(SystemExit):
            raiseException()

if __name__ == '__main__': 
    unittest.main()