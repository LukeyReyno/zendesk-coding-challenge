import unittest
import json

from project.zTicket import ZendeskTicket

# tests constructing the Zendesk Ticket object with a dict
with open("project/data/exampleTID.json", "r") as JSON_FILE:
    tDict = json.load(JSON_FILE)

with open("project/data/exampleTID.json", "r") as JSON_FILE:
    tDict2 = json.load(JSON_FILE)

tDict = tDict['ticket'] # One Ticket JSON
tDict2 = tDict2['ticket']
zT = ZendeskTicket(tDict)
zT2 = ZendeskTicket(tDict2)

# To test invalid dictionary
zT3 = ZendeskTicket({})

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

    def test_ticket_attributes_02(self):
        # tests that the dict entries are all None with improper dict
        self.assertEqual(zT3.id, None)
        self.assertEqual(zT3.description, None)
        self.assertEqual(zT3.requester_id, None)
        self.assertEqual(zT3.subject, None)
        self.assertEqual(zT3.tags, None)
        self.assertEqual(zT3.status, None)
        self.assertNotEqual(zT.date, None)

    def test_ticket_str01(self):
        # tests the string version of Zendesk Ticket
        self.assertEqual(str(zT)[:3], "ID-")

    def test_ticket_str02(self):
        # tests the string version of Zendesk Ticket
        self.assertEqual(str(zT3), "Ticket Has Attribute Errors")

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
        zT2.id = -1
        self.assertNotEqual(zT, zT2)

    def test_ticket_eq03(self):
        ls = []
        #tests tickets equality method
        self.assertNotEqual(zT, ls)

if __name__ == '__main__': 
    unittest.main()