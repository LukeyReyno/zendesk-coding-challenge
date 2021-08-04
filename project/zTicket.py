import datetime

NEEDED_KEYS = ('id', 'subject', 'description', 'requester_id', 'status', 'tags', 'created_at')

class ZendeskTicket():
    """
    Creates a Zendesk Ticket object provided dictionary data
    """

    def __init__(self, ticketDict: dict):
        self.ticketDict = ticketDict
        self.__dict__ = ticketDict
        self.__fixDict()
        self.__setDate()

    def __str__(self):
        try:
            return f"ID-{self.id:03d}\t\"{self.subject}\" by {self.requester_id} on {self.date}"
        except:
            return "Ticket Has Attribute Errors"

    def __eq__(self, other):
        return type(self) == type(other) and \
            self.id == other.id and self.subject == other.subject and \
            self.date == other.date and self.status == other.status

    def __fixDict(self):
        # Forces keys to exist to prevent AttributeErrors
        for key in NEEDED_KEYS:
            if key not in self.__dict__:
                self.__dict__[key] = None

    def __setDate(self):
        # Date Formatting
        try:
            dateStr = self.created_at.strip('Z')
            date = datetime.datetime.fromisoformat(dateStr)
            self.date = date.strftime("%d %B, %Y at %H:%M:%S")
        except:
            # In case date is formatted incorrectly
            self.date = self.created_at

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
