import requests
import sys

class ZendeskAPIException(Exception):
    """Used for any issue connecting or receiving information from the Zendesk API"""

def handleExceptions(func):
        def inner(*args, **kwargs):
            try:
                print("Requesting Information from Zendesk...")
                return func(*args, **kwargs)
            except ZendeskAPIException:
                print("Zendesk Connection Error has occurred.\n"
                    "Authorization Error\n" 
                    "Program will now terminate.\n\n", flush=sys.stderr)
                sys.exit(1)
            except (requests.ConnectionError, requests.HTTPError):
                print("Connection Error has occurred.\n"
                    "Check your connection to the Zendesk API and the provided credentials.\n" 
                    "Program will now terminate.\n\n", flush=sys.stderr)
                sys.exit(1)
            except AssertionError:
                raise AssertionError
            except Exception as e:
                print("Unchecked Error has occurred.\n"
                    "Program will now terminate.\n\n", flush=sys.stderr)
                print(e)
                sys.exit(1)
        return inner