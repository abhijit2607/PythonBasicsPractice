def add():
    import csv
    f=open("records.csv",'a', newline="\n")
    fieldName=["empid","name","mobile"]
    wr=csv.writer(f)
    wr.writerow(fieldName)
    while True:
        e=int(input("Enter the employee id:"))
        n=input("Enter the name:")
        m=int(input("Enter the mobile number:"))
        wrd=csv.writer(f)
        wrd.writerow([e,n,m])
        a=int(input("1.To add more\n2.Exit"))
        if a==2:
            break
        f.close()
def count():
    import csv
    f=open("records.csv","r")
    rd=csv.reader(f)
    b=list(rd)
    count=len(b)
    print("The number of records in the csv file is",count)
    f.close()

#__main__

add()
count()
    
