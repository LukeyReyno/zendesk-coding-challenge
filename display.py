import requestTickets

from zTicket import ZendeskTicket

TICKETS_PER_PAGE = 25

class Display():
    """
    Contains information and methods to display tickets on the command line
    """
    def __init__(self):
        self.totalTickets = requestTickets.getTicketCount()
        self.numPages = (self.totalTickets // TICKETS_PER_PAGE) + 1
        self.currentPageIndex = 0
        self.__createPages()
        self.__printWelcomeMessage()

    def __printWelcomeMessage(self):
        print("Welcome to the Zendesk Ticket Viewer\nType 'exit' to stop the program")
        print(f"Total Number of Tickets: {self.totalTickets}")
        print(f"Currently on page {self.currentPageIndex + 1} out of {self.numPages}")

    def __createPages(self):
        self.pages = []
        currentUrl = None
        for pageNum in range(1, self.numPages + 1):
            currentPage = Page(pageNum, currentUrl)
            self.pages.append(currentPage)
            currentUrl = currentPage.nextUrl

    def printAllPageIDs(self):
        for p in self.pages:
            print(f"Min: {p.minTicketID} - Max: {p.maxTicketID}")

class Page():
    """
    Contains a list of Tickets, up to 25
    """
    def __init__(self, pageNumber, url):
        self.tickets = []
        self.pageNumber = pageNumber

        ticketsJson = requestTickets.getPageOfTickets(TICKETS_PER_PAGE, url)
        for ticketDict in ticketsJson['tickets']:
            self.tickets.append(ZendeskTicket(ticketDict))
        
        self.numTickets = len(ticketsJson['tickets'])
        self.__maxTicketID()
        self.__minTicketID()
        self.nextUrl = ticketsJson["links"]["next"]

    def __maxTicketID(self):
        if (self.numTickets > 0):
            self.maxTicketID = self.tickets[-1].id
        else:
            self.maxTicketID = None

    def __minTicketID(self):
        if (self.numTickets > 0):
            self.minTicketID = self.tickets[0].id
        else:
            self.minTicketID = None
