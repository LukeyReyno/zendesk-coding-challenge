import datetime

class ZendeskTicket():
    """
    Creates a Zendesk Ticket object provided dictionary data
    """

    def __init__(self, ticketDict):
        self.ticketDict = ticketDict
        self.createAttrFromDict()

    def __str__(self):
        return f"ID-{self.id:03d}\t\"{self.subject}\" by {self.requester_id} on {self.date}"

    def __eq__(self, other):
        return type(self) == type(other) and \
            self.id == other.id and self.subject == other.subject and \
            self.date == other.date and self.status == other.status

    def detailedView(self):
        return f"Ticket #{self.id} - \"{self.subject}\"\n" \
            f"Requested by: {self.requester_id}\nCreated on: {self.date}\n" \
            f"Full Description:\n{self.description}\n\n" \
            f"Status: {self.status}\n"

    def createAttrFromDict(self):
        # Maybe find another way to convert a dict object to attributes
        self.id = self.ticketDict['id']
        self.subject = self.ticketDict['subject']
        self.description = self.ticketDict['description']
        self.requester_id = self.ticketDict['requester_id']
        self.status = self.ticketDict['status']
        
        # Date Formatting
        dateStr = self.ticketDict['created_at'].strip('Z')
        date = datetime.datetime.fromisoformat(dateStr)
        self.date = date.strftime("%d %B, %Y at %H:%M:%S")

