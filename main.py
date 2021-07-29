import display

from zTicket import ZendeskTicket

def main():

    mainDisplay = display.Display()

    
    dInput = input("User Input: ")
    while  dInput != 'exit':
        print(dInput)
        mainDisplay.printAllPageIDs()
        dInput = input("User Input: ")
        pass

if __name__ == '__main__':
    main()
