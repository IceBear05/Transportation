class LoginAndSignUp:
    def __init__(self):
        pass

    def Check(self, user, password):
        File = open("users.txt", "r")
        for line in File:
            if len(line) == 0:
                continue
            us, pss = line.split(" ")
            if user == us and int(password) == int(pss):
                return False
        return True

    def SignUp(self, user, password):
        if self.Check(user, password):
            File = open("users.txt", "a")
            File.writelines([user, " ", password, "\n"])
            return True
        else:
            return False

    def Login(self, user, password):
        File = open("users.txt", "r")
        for line in File:
            if len(line) == 0:
                continue
            us, pss = line.split(" ")
            if user == us and int(password) == int(pss):
                return True
        return False


o = LoginAndSignUp()
print("------------------------- Welcome ------------------------")
while True:
    print("1.[Login] \t\t\t\t2.[SignUp] \t\t\t\t", end='')
    choice = input("3.[Exit]  :")

    if choice == "1":
        print("-------------------------- Login -------------------------")
        user = input("please enter Username: ")
        password = input("please enter password: ")

        if o.Login(user, password):
            print("---------------------- Welcome To App ---------------------")
            break
        else:
            print("Username and password are not correct\n")
            continue

    elif choice == "2":
        print("------------------------- SignUp ------------------------")
        user = input("please enter Username: ")
        password = input("please enter password: ")

        if o.SignUp(user, password):
            print("-------------- Registration was successful --------------")
            print("---------------------- Welcome To App ---------------------")
            break
        else:
            print("The user already exists\n")
            continue

    elif choice == "3":
        print("------------------------- GoodBye ------------------------")
        break
    else:
        print("-------------------------- ERROR -------------------------")
        print("Please enter [1 or 2 or 3]")
        print("----------------------------------------------------------")
        continue