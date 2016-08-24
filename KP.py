#API- K.E.A.T.O.N Parker
import random, time, datetime

while True:
    def openFileGreetings():
        global greetingsPath, greetingsList, greetings
        greetingsPath = "/home/jasmine/Desktop/K.E.A.T.O.N Parker/greetings/greetings.txt"
        with open(greetingsPath, 'r+') as greetings:
            greetingsList = [line.strip() for line in greetings]

    def intro():
        global userInput, greetings, greetingsPath, greetingsList, line, response
        openFileGreetings()
        response = random.choice(greetingsList)
        print(response)
        return response



    def addNewGreeting():
        protocol = input("Re-Confirm Protocol:\n")
        protocol = protocol.upper()
        newGreetingTriggers = ["PROTOCOL 1", "PROTOCOL ONE", "INITIATE NEW GREETING" ]
        for i in newGreetingTriggers:
            if i in protocol:
                newGreeting = input("Protocol 1 commencing, enter new greeting. \n")
                yesNoValid = input("Enter 'Yes' if '" + newGreeting + "' is the correct new greeting you would like to add to K.E.A.T.O.N?\n")
                yesNoValid = yesNoValid.upper()
                if yesNoValid == "YES":
                    greetings = open(greetingsPath, "a")
                    greetings.write(newGreeting + "\n")
                    print("My greetings list has been updated.")

    def removeOldGreeting():
        global greetings, removeWord, line
        protocol = input("Re-Confirm Protocol:\n")
        protocol = protocol.upper()
        deleteGreetingTriggers = ["PROTOCOL 2", "PROTOCOL TWO", "INITIATE DELETE GREETING"]
        for i in deleteGreetingTriggers:
            if i in protocol:
                greetings = open(greetingsPath, 'r')
                lines = greetings.readlines()
                greetings.close()
                print("Protocol 2 commencing...")
                removePhrase = input("Enter the phrase you would like to remove.\n")
                if removePhrase not in lines:
                    print("Phrase doesn't exist.")
                else:
                    validRemovePhrase = input(
                        "Enter 'Yes' if '" + removePhrase + "' is correct greeting you would like to remove from K.E.A.T.O.N?\n")
                    removePhrase = removePhrase + "\n"
                    validRemovePhrase = validRemovePhrase.upper()
                    if validRemovePhrase == "YES":
                        open(greetingsPath, 'w').close()
                        greetings = open(greetingsPath, 'w')
                        for line in lines:
                            if line != removePhrase:
                                greetings.write(line)

                        greetings.close()
                        print("Phrase successfully removed!")

    def getDate():
        date = datetime.datetime.now().strftime('%A %d %B 20%y')
        day = datetime.datetime.now().strftime('%d')
        day = str(day)
        if day == '1' or day == '21' or day == '31':
            day = day + "st"
        elif day.endswith('2'):
            day = day + "nd"
        elif day.endswith('3'):
            day = day + 'rd'
        elif day.endswith(('4', '5', '6', '7', '8', '9', '0')) or day == '11':
            day = day + 'th'

        dateStr = '%A ' + day + ' %B 20%y'
        print(datetime.datetime.now().strftime(dateStr))


    def decideAction():
        protocol = input()
        protocol = protocol.upper()
        if protocol == "KEATON" or protocol == "PARKER" \
                or protocol == "MR PARKER" or protocol == "PARK" \
                or protocol == "YO KEATZ" or protocol == "HELLO":
            response = intro()
            if response == greetingsList[2]:
                positiveTerms = ["GOOD", "HAPPY", "GREAT", "OKAY", "FINE"]
                userMood = input("")
                userMood = userMood.upper()
                words = userMood.split()
                for i in positiveTerms:
                    if i in words:
                        returnMoodList = ["That's Great!", "Good Good.", "Cool."]
                        response = random.choice(returnMoodList)
                        print(response)
                        greetings.close()
            else:
                greetings.close()
        elif protocol == "EXIT" or "ABORT" or "PROTOCOL 0" or "PROTOCOL ZERO":
            exit()
        elif protocol == "ONE" or protocol == "PROTOCOL 1" or protocol == "PROTOCOL ONE":
            addNewGreeting()
        elif protocol == "TWO" or protocol == "PROTOCOL 2" or protocol == "PROTOCOL TWO":
            removeOldGreeting()
        elif protocol == "THREE" or protocol == "PROTOCOL 3" or protocol == "PROTOCOL THREE":
            getDate()
    decideAction()
#problem: when removing a word you need to get the exact capitilisation correct, if not then it will not work. Find a way to bypass case sensitivity.
