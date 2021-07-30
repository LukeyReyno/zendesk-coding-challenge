import sys
import requestTickets

from zTicket import ZendeskTicket

TICKETS_PER_PAGE = 25

class Display():
    """
    Contains information and methods to display tickets on the command line
    """
    def __init__(self):
        self.__printWelcomeMessage()
        self.totalTickets = requestTickets.getTicketCount()
        self.numPages = (self.totalTickets // TICKETS_PER_PAGE) + 1
        self.currentPageIndex = 0
        self.__createPages()
        self.__initializePageMinMaxID()
        self.__printInformation()

    def __printWelcomeMessage(self):
        print("Welcome to the Zendesk Ticket Viewer\n"
            "Program will now try to collect Ticket data\n"
            "Connecting...\n")

    def __printInformation(self):
        print("Type 'exit' to stop the program")
        print("Type 'help' to show help menu\n")
        print(f"Total Number of Tickets: {self.totalTickets}")
        print(f"Currently on page {self.currentPageIndex + 1} out of {self.numPages}\n")

    def __showInstructions(self):
        print("\n\tType 'exit' to stop the program")
        print("\tType 'help' to show this menu")
        print("\tType 'up' to view next page")
        print("\tType 'down' to view previous page")

    def __loadNewPage(self, newPage):
        """
        Load page with tickets, if not already
        """
        if newPage.isLoaded == False:
            self.pages.append(newPage)
            newPage.loadPage(self.urls[self.currentPageIndex])
            self.urls += [newPage.nextUrl]
            # New Pages can only be accessed by scrolling in order

    def __createPages(self):
        """
        Load first page, and initialize the rest
        """
        self.pages : list[Page] = []
        self.urls = [None]

        newPage = Page(self.currentPageIndex + 1)
        self.__loadNewPage(newPage)

        for pageNum in range(2, self.numPages + 1):
            newPage = Page(pageNum)
            self.pages.append(newPage)
    
    def __initializePageMinMaxID(self):
        count = 0
        for i in range(0, self.numPages):
            self.pages[i].minTicketID = count + 1
            count += TICKETS_PER_PAGE 
            if (count > self.totalTickets):
                count += ((self.totalTickets % TICKETS_PER_PAGE) - TICKETS_PER_PAGE)
            self.pages[i].maxTicketID = count

    def __scrollPage(self, amount):
        self.currentPageIndex += amount
        if not (0 <= self.currentPageIndex < self.numPages):
            self.currentPageIndex -= amount
            print("You can no longer scroll in that direction.\n")
        else:
            self.__loadNewPage(self.pages[self.currentPageIndex])
        print(f"Currently on page {self.currentPageIndex + 1} out of {self.numPages}")

    def inputManager(self, userInput: str):
        # Maybe in future use new Python switch case
        if userInput == "help":
            self.__showInstructions()
        elif userInput == "up":
            self.__scrollPage(1)
        elif userInput == "down":
            self.__scrollPage(-1)
        elif userInput == "exit":
            pass
        else:
            print("That is not a valid input. Type 'help' if necessary.")

    def printAllPageIDs(self):
        # Mostly used for debugging
        for p in self.pages:
            print(f"Min: {p.minTicketID} - Max: {p.maxTicketID}")

class Page():
    """
    Contains a list of Tickets, up to 25
    """
    def __init__(self, pageNumber):
        self.tickets = []
        self.pageNumber = pageNumber
        self.minTicketID = None
        self.maxTicketID = None
        self.isLoaded = False

    def loadPage(self, url):
        # Only loads if tickets aren't already there
        if self.isLoaded == False:
            ticketsJson = requestTickets.getPageOfTickets(TICKETS_PER_PAGE, url)
            for ticketDict in ticketsJson['tickets']:
                self.tickets.append(ZendeskTicket(ticketDict))
            self.numTickets = len(ticketsJson['tickets'])
            self.nextUrl = ticketsJson["links"]["next"]
            self.isLoaded = True
