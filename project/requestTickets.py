import requests
import json
import zExceptions

with open("project/data/API_Credentials.json") as credFile:
    API_Creds = json.load(credFile)

@zExceptions.handleExceptions
def getTicketCount():
    """
    returns an integer value for the number of tickets with the associated account
    """
    url = f"https://{API_Creds['subdomain']}.zendesk.com/api/v2/tickets/count.json"
    request = requests.get(url, headers={"Authorization": f"Bearer {API_Creds['auth_token']}"})
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
        url = f"https://{API_Creds['subdomain']}.zendesk.com/api/v2/tickets.json?page[size]={pageSize}"
    request = requests.get(url, headers={"Authorization": f"Bearer {API_Creds['auth_token']}"})

    checkStatusCode(request.status_code)
    return request.json()

@zExceptions.handleExceptions
def getTicketByID(tID : int):
    """
    returns a single Zendesk Ticket Object specified by ID
    """
    url = f"https://{API_Creds['subdomain']}.zendesk.com/api/v2/tickets/{tID}.json"
    request = requests.get(url, headers={"Authorization": f"Bearer {API_Creds['auth_token']}"})

    checkStatusCode(request.status_code)
    return request.json()

def checkStatusCode(status_code):
    """
    Checks the status code of Request to Zendesk
    """
    # status code for receiving tickets - 200
    if status_code != requests.codes['\o/']:
        raise zExceptions.ZendeskAPIException