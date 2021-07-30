import unittest
import sys
import os

cd = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(cd)
sys.path.append(parent)

from zTicket import ZendeskTicket

# tests constructing the Zendesk Ticket object with a dict
tDict = {
            "id": 1,
            "description": "this is a description",
            "requester_id": 1901028593545,
            "subject": "this is a subject",
            "status": "open",
            "created_at": "2021-07-27T23:20:25Z",
            "not_important": 5
        }
zT = ZendeskTicket(tDict)
zT2 = ZendeskTicket(tDict)


class TicketTests(unittest.TestCase):
    """
    Tests the attributes and Methods of Zendesk Tickets

    (Assumes Multiple Tickets on account)
    """

    def test_ticket_attributes_01(self):
        self.assertEqual(zT.id, tDict['id'])
        self.assertEqual(zT.description, tDict['description'])
        self.assertEqual(zT.requester_id, tDict['requester_id'])
        self.assertEqual(zT.subject, tDict['subject'])

    def test_ticket_str(self):
        # tests the string version of Zendesk Ticket
        self.assertEqual(str(zT)[:8], "Ticket #")

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

if __name__ == '__main__': 
    unittest.main()