def phoneRecords():
    phoneNumber=list(input("Enter the phone number with two dashes:"))
    if len(phoneNumber)<10:
        print("Please enter a phone number more than 10 digits.")
        phoneRecords()
    elif phoneNumber[3] and phoneNumber[7]!='-':
        print("Please enter the dashes at valid places.")
        phoneRecords()
    else:
        print("The phone number is VALID.")

# __main__

phoneRecords()