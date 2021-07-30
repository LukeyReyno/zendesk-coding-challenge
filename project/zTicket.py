class ZendeskTicket():
    """
    Creates a Zendesk Ticket object provided dictionary data
    """

    def __init__(self, ticketDict):
        self.ticketDict = ticketDict
        self.createAttrFromDict()

    def __str__(self):
        return f"Ticket #{self.id}: {self.subject} by {self.requester_id} on {self.date}"

    def __eq__(self, other):
        return type(self) == type(other) and \
            self.id == other.id and self.subject == other.subject and \
            self.date == other.date and self.status == other.status

    def createAttrFromDict(self):
        self.date = self.ticketDict['created_at']
        self.id = self.ticketDict['id']
        self.subject = self.ticketDict['subject']
        self.description = self.ticketDict['description']
        self.requester_id = self.ticketDict['requester_id']
        self.status = self.ticketDict['status']