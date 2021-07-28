import unittest
import json
import requests

from zTicket import ZendeskTicket

with open("API_Credentials.json") as credFile:
    API_Creds = json.load(credFile)

url = f"https://{API_Creds['subdomain']}.zendesk.com/api/v2/tickets/2.json"

request = requests.get(url, auth=(f"{API_Creds['email_address']}/token", API_Creds['api_token']))

ticketJson = request.json()

with open("test.json", "w") as outFile:
    json.dump(ticketJson, outFile, indent="  ")

zT = ZendeskTicket(ticketJson['ticket'])

#TODO: create class with API_Creds to get tickets

class functionTests(unittest.TestCase):

    def test_skeleton(self):
        self.assertEqual(zT.id, ticketJson['ticket']['id'])

if __name__ == '__main__': 
    unittest.main()