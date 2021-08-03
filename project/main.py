import display

def main():
    mainDisplay = display.Display()

    dInput = str()
    while dInput != 'exit':
        # Constantly feed inputs into the display Object
        dInput = input("\nUser Input: ")
        print("~~~~~~~~~~~")
        mainDisplay.inputManager(dInput)

if __name__ == '__main__':
    main()
