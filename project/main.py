import display

def main():
    mainDisplay = display.Display()

    dInput = str()
    while dInput != 'exit':
        dInput = input("\nUser Input: ")
        mainDisplay.inputManager(dInput)

if __name__ == '__main__':
    main()
