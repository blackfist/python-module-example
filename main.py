from services.pastebin import Pastebin
from services.pastie import Pastie
from services.kevpaste import Kevpaste

if __name__ == "__main__":
    # Here we are making a list of all the services for which we want to run code
    # the entries in the list are class names that we imported above
    # e.g. services.pastebin.Pastebin
    services = [
        Pastebin,
        Pastie,
        Kevpaste
    ]

    for svc in services:
        # This loop will go through each of the services listed above
        # and call a new instance of the class.
        # Then it will call the doit() function of that class
        temp = svc()
        print(temp.doit())