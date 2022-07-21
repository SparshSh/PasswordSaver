from datetime import date
def fileForPass():
    today = date.today()
    f = open("PassMngt.txt", "a")
    count  = int(input("How many Passwords you wanna save ?"))
    d1 = today.strftime("%B %d , %Y")
    d = {'Date':  d1}
    for i in range(count):
        username = str(input('Enter the username : '))
        password = input('Enter the password : ')
        d[username] = password
    d = str(d)
    print(d)
    sure = input("Are you sure you want to save ? y/n : ")
    if sure=='y':
        f.write('\n'+d)
    else:
        print("Function terminated !")
    f.close()

fileForPass()

