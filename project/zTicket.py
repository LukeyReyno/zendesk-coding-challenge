import datetime
import sys

def ticketErrorHandler(func):
    """
    catches errors for missing keys
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, TypeError):
            print("Zendesk Ticket Instantiation Error has occurred.\n", flush=sys.stderr)
        except Exception as e:
            print("Unchecked Ticket Error has occurred.\n"
                "Program will now terminate.\n\n", flush=sys.stderr)
            print(e)
            sys.exit(1)
    return inner

class ZendeskTicket():
    """
    Creates a Zendesk Ticket object provided dictionary data
    """

    def __init__(self, ticketDict):
        self.ticketDict = ticketDict
        self.__setAttrToNone()
        self.__createAttrFromDict()

    def __str__(self):
        return f"ID-{self.id:03d}\t\"{self.subject}\" by {self.requester_id} on {self.date}"

    def __eq__(self, other):
        return type(self) == type(other) and \
            self.id == other.id and self.subject == other.subject and \
            self.date == other.date and self.status == other.status

    def __setAttrToNone(self):
        """
        In case an error occurs, remainding attributes will result in None
        """
        self.id = None
        self.subject = None
        self.description = None
        self.requester_id = None
        self.status = None
        self.tags = None
        self.date = None

    @ticketErrorHandler
    def __createAttrFromDict(self):
        """
        creates ticket attributes from dictionary
        """
        # Maybe find another way to convert a dict object to attributes
        self.id = self.ticketDict['id']
        self.subject = self.ticketDict['subject']
        self.description = self.ticketDict['description']
        self.requester_id = self.ticketDict['requester_id']
        self.status = self.ticketDict['status']
        self.tags = self.ticketDict['tags']
        
        # Date Formatting
        dateStr = self.ticketDict['created_at'].strip('Z')
        date = datetime.datetime.fromisoformat(dateStr)
        self.date = date.strftime("%d %B, %Y at %H:%M:%S")

    def detailedView(self):
        """
        returns formatted details on this specific ticket
        """
        return "\n|-|-|-|-|-|-|-|-|-|-|-|\n" \
            f"Ticket #{self.id} - \"{self.subject}\"\n\n" \
            f"Requested by: {self.requester_id}\nCreated on: {self.date}\n" \
            f"Tags: {self.tags}\n\n" \
            f"Full Description:\n{self.description}\n\n" \
            f"Status: {self.status}\n"\
            "|-|-|-|-|-|-|-|-|-|-|-|"
