#Note! tzdata package must be installed to enable Zoneinfo to work on Windows OS
from zoneinfo import ZoneInfo
from datetime import datetime, timezone

def timecheck():
    #Extracts the current time from each time zone
    pdxtime = datetime.now(ZoneInfo("America/Los_Angeles"))
    nyctime = datetime.now(ZoneInfo("America/New_York"))
    lontime = datetime.now(ZoneInfo("Europe/London"))
    #Extracts the current hour from each timezone and turns it into and integer for arithmatic and logical 
    # comparisons (the strftime() method that extracts the hour turns the time into a string value)
    pdxhour = int(pdxtime.strftime("%H"))
    nychour = int(nyctime.strftime("%H"))
    lonhour = int(lontime.strftime("%H"))
    #Statements prints whether each location is open if the local time is between 9 am. and 5 pm., or closed if it
    # earlier/later than that
    if pdxhour >= 9 and pdxhour < 16:
        print("The Portland HQ is open")
    else:
        print("The Portland HQ is closed")
    if nychour >= 9 and nychour < 16:
        print("The New York branch is open")
    else:
        print("The New York branch is closed")
    if lonhour >= 9 and lonhour < 16:
        print("The London branch is open")
    else:
        print("The London branch is closed")

if __name__ == "__main__":
    timecheck()


