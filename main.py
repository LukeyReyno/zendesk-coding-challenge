import requests
import json

from zTicket import ZendeskTicket

with open("API_Credentials.json") as credFile:
    API_Creds = json.load(credFile)

url = f"https://{API_Creds['subdomain']}.zendesk.com/api/v2/tickets.json"

def main():
    # curl request example
    request = requests.get(url, auth=(f"{API_Creds['email_address']}/token", API_Creds['api_token']))
    print(request)
    ticketJson = request.json()

    with open("test.json", "w") as outFile:
        json.dump(ticketJson, outFile, indent="  ")

    zT = ZendeskTicket(ticketJson['tickets'][1])
    print(zT.id)

if __name__ == '__main__':
    main()
