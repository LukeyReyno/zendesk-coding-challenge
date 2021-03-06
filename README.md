# zendesk-coding-challenge ~ Lucas Reyna
This project is an entry for the Zendesk Student Co-op.

This is used to connect to the Zendesk API and display all the Tickets connected to an account.

All information is displayed in the command line interface (CLI).

Users can scroll through pages and look at individual tickets.

This current build only shows tickets linked to my account on the zcclreyna subdomain.

Users could change ```projects/data/API_Credentials.json``` to fit their OAUTH credentials.

## Instructions

```git clone https://github.com/LukeyReyno/zendesk-coding-challenge.git```

Make the cloned directory the current working directory

```cd zendesk-coding-challenge```

```bash runProgram.sh```

~ Internet Connection required for intended use

Running the program script will start the Zendesk Ticket Reader.
* Users can scroll through the pages by inputting 'up' or 'down'
* 'display' will show the current page's ticket content
* Inputting a valid integer will give more details about a specific ticket
* Use 'exit' to leave the program

## Tests
The Python Coverage library needs to be installed in order to run the testing script

```pip install coverage```

If not already, make the cloned directory the current working directory

```cd zendesk-coding-challenge```

```bash runTests.sh```

This should show every test passing with 100% coverage.


## Notes
* Switched from Email and Token requests to OAUTH token with ['read'] scope for better security
    + Removed Email, Password, and Token access to API, only OAUTH Client (since it can be deleted later)
* Organized project into different folders for better user experience
* Tested on Mac OS X and Linux through several Python 3.8 versions. (Should work on most python 3 distributions)
* The shell scripts expect the cloned directory to be the current working directory
    + This could be modified later
