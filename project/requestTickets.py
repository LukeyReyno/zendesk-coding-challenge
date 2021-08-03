import requests
import json
import zExceptions

API_CRED_PATH = "project/data/API_Credentials.json"

class Zendesk_API_Credentials():
    """
    Creates instance of API Credentials for requesting tickets
    OAUTH scope needs 'read' capabilities

    CredFile needs subdomain and oauth token 
    """

    def __init__(self, filePath):
        # requires a valid file path with a specific json key
        with open(filePath) as credFile:
            credDict = json.load(credFile)
        self.subdomain = credDict['subdomain']
        self.token = credDict['auth_token']

client = Zendesk_API_Credentials(API_CRED_PATH)

@zExceptions.handleExceptions
def getTicketCount():
    """
    returns an integer value for the number of tickets with the associated account
    """
    url = f"https://{client.subdomain}.zendesk.com/api/v2/tickets/count.json"
    request = requests.get(url, headers={"Authorization": f"Bearer {client.token}"})
    checkStatusCode(request.status_code)
    countDict = request.json()

    return countDict['count']['value']

@zExceptions.handleExceptions
def getPageOfTickets(pageSize, url=None):
    """
    returns a json-encoded object of a page of Zendesk Tickets from the account
    
    pageSize in range of [1, 100]
    """

    assert(1 <= pageSize <= 100)
    if url == None:
        url = f"https://{client.subdomain}.zendesk.com/api/v2/tickets.json?page[size]={pageSize}"
    request = requests.get(url, headers={"Authorization": f"Bearer {client.token}"})

    checkStatusCode(request.status_code)
    return request.json()

@zExceptions.handleExceptions
def getTicketByID(tID : int):
    """
    returns a single Zendesk Ticket Object specified by ID
    """
    url = f"https://{client.subdomain}.zendesk.com/api/v2/tickets/{tID}.json"
    request = requests.get(url, headers={"Authorization": f"Bearer {client.token}"})

    checkStatusCode(request.status_code)
    return request.json()

def checkStatusCode(status_code):
    """
    Checks the status code of Request to Zendesk
    """
    # status code for receiving tickets - 200
    if status_code != requests.codes['\o/']:
        raise zExceptions.ZendeskAPIException