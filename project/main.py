import display
import requestTickets

from zTicket import ZendeskTicket

def main():

    """
    c = requestTickets.getTicketCount()

    print(c)"""

    mainDisplay = display.Display()

    dInput = input("User Input: ")
    while dInput != 'exit':
        #mainDisplay.printAllPageIDs()
        mainDisplay.inputManager(dInput)
        dInput = input("User Input: ")
        pass

if __name__ == '__main__':
    main()
