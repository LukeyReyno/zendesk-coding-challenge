import requests
import sys

class ZendeskAPIException(Exception):
    """Used for any issue connecting or receiving information from the Zendesk API"""

def handleRequestExceptions(func):
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
                print("Unchecked Request Error has occurred.\n"
                    "Program will now terminate.\n\n", flush=sys.stderr)
                print(e)
                sys.exit(1)
        return inner

def handleAPICredExceptions(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except KeyError:
                print("JSON parse error has occurred.\n"
                    "Make sure json files use the correct keys"
                    "Program will now terminate.\n\n", flush=sys.stderr)
                sys.exit(1)
            except FileNotFoundError:
                print("API Credential file not found.\n"
                    "Check your provided path to the file.\n" 
                    "Program will now terminate.\n\n", flush=sys.stderr)
                sys.exit(1)
            except Exception as e:
                print("Unchecked API Credentail Error has occurred.\n"
                    "Program will now terminate.\n\n", flush=sys.stderr)
                print(e)
                sys.exit(1)
        return inner