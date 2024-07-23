def log_in():
    global username, password
    log_username = input("Type username: ")
    log_password = input("Type password: ")
    if log_username == username and log_password == password:
        print("You are successfully logged in!")
    else:
        print("Something went wrong!")


def sign_up():
    global username, password
    username = input("Create username: ")
    password = input("Create password: ")


def check():
    global username, password, q
    if q == 2 and username == "" and password == "":
        print("You cant log in, 'cause you not sign up yet")


# vars

username = ""
password = ""

# code
while True:
    q = input("(1)-Sign up, (2)-Log in: ")
    check()
    if q == "1":
        sign_up()
    elif q == "2":
        log_in()
    quit_q = input("Wanna quit?(Y/N): ")
    if quit_q == "y" or quit_q == "Y":
        quit()
    else:
        input("Return>>>")
