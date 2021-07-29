import requests
import json

from zTicket import ZendeskTicket

with open("API_Credentials.json") as credFile:
    API_Creds = json.load(credFile)

def getTicketCount():
    """
    returns an integer value for the number of tickets with the associated account
    """
    url = f"https://{API_Creds['subdomain']}.zendesk.com/api/v2/tickets/count.json"
    request = requests.get(url, headers={"Authorization": f"Bearer {API_Creds['auth_token']}"})
    checkStatusCode(request.status_code)
    countDict = request.json()

    return countDict['count']['value']

def getPageOfTickets(pageSize, url=None):
    """
    returns a json-encoded object of a page of Zendesk Tickets from the account
    
    pageSize in range of [1, 100]
    """
    ticketList : list[ZendeskTicket] = []
    assert(1 <= pageSize <= 100)
    if url == None:
        url = f"https://{API_Creds['subdomain']}.zendesk.com/api/v2/tickets.json?page[size]={pageSize}"
    request = requests.get(url, headers={"Authorization": f"Bearer {API_Creds['auth_token']}"})

    checkStatusCode(request.status_code)
    return request.json()

def getTicketsJSON():
    """
    returns the JSON for requesting all tickets in the account
    """
    url = f"https://{API_Creds['subdomain']}.zendesk.com/api/v2/tickets.json"
    request = requests.get(url, headers={"Authorization": f"Bearer {API_Creds['auth_token']}"})

    checkStatusCode(request.status_code)
    return request.json()

def getTicketByID(tID : int):
    """
    returns a single Zendesk Ticket Object specified by ID
    """
    url = f"https://{API_Creds['subdomain']}.zendesk.com/api/v2/tickets/{tID}.json"
    request = requests.get(url, headers={"Authorization": f"Bearer {API_Creds['auth_token']}"})

    checkStatusCode(request.status_code)
    ticketJson = request.json()

    return ZendeskTicket(ticketJson['ticket'])

def checkStatusCode(status_code):
    if status_code != 200:
        raise requests.HTTPError
