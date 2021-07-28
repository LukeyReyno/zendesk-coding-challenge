
class ZendeskTicket():
    """
    Creates a Zendesk Ticket object provided dictionary data
    """

    def __init__(self, ticketDict):
        self.ticketDict = ticketDict
        self.createAttrFromDict()

    def createAttrFromDict(self):
        self.id = self.ticketDict['id']