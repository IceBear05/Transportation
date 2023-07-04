# class LoginAndSignUp:
#     def __init__(self):
#         pass
#
#     def Check(self, user, password):
#         File = open("users.txt", "r")
#         for line in File:
#             if len(line) < 3:
#                 continue
#             us, pss = line.split(" ")
#             if user == us and int(password) == int(pss):
#                 return False
#         return True
#
#     def SignUp(self, user, password):
#         if self.Check(user, password):
#             File = open("users.txt", "a")
#             File.writelines([user, " ", password, "\n"])
#             return True
#         else:
#             return False
#
#     def Login(self, user, password):
#         File = open("users.txt", "r")
#         for line in File:
#             if len(line) < 3:
#                 continue
#             us, pss = line.split(" ")
#             if user == us and int(password) == int(pss):
#                 return True
#         return False
#
#
# o = LoginAndSignUp()
# print("------------------------- Welcome ------------------------")
# while True:
#     print("1.[Login] \t\t\t\t2.[SignUp] \t\t\t\t", end='')
#     choice = input("3.[Exit]  :")
#
#     if choice == "1":
#         print("-------------------------- Login -------------------------")
#         user = input("please enter Username: ")
#         password = input("please enter password: ")
#
#         if o.Login(user, password):
#             print("---------------------- Welcome To App ---------------------")
#             break
#         else:
#             print("Username and password are not correct\n")
#             continue
#
#     elif choice == "2":
#         print("------------------------- SignUp ------------------------")
#         user = input("please enter Username: ")
#         password = input("please enter password: ")
#
#         if o.SignUp(user, password):
#             print("-------------- Registration was successful --------------")
#             print("---------------------- Welcome To App ---------------------")
#             break
#         else:
#             print("The user already exists\n")
#             continue
#
#     elif choice == "3":
#         print("------------------------- GoodBye ------------------------")
#         break
#     else:
#         print("-------------------------- ERROR -------------------------")
#         print("Please enter [1 or 2 or 3]")
#         print("----------------------------------------------------------")
#         continue



'''from mysql.connector import connect

db = connect(
            host="localhost",
            user="root",
            password="nz8119209",
            database="transportation"
        )
my_cursor = db.cursor()
my_cursor.execute(f"SELECT * FROM Loading")
for line in my_cursor:
    print(line)'''

def MainMenu():
    print('_______________________management menu_______________________')
    print("1.[boxes]\t\t\t\t2.[containers]\t\t\t\t3.[cars]\n4.[loading]\t\t\t\t5.[send & receive]\t\t\t", end='')
    choice = input("6.[Exit] :")
    return choice
def boxCRUD():
    print('_________________________boxes menu__________________________')
    print('1.[add]\t\t\t\t\t2.[edit]\t\t\t\t\t', end='')
    choice = input('3.[delete] :')
    return choice

def carCRUD():
    print('__________________________cars menu__________________________')
    print('1.[add]\t\t\t\t\t2.[edit]\t\t\t\t\t', end='')
    choice = input('3.[delete] :')
    return choice

def containerCRUD():
    print('________________________containers menu_________________________')
    print('1.[add]\t\t\t\t\t2.[edit]\t\t\t\t\t', end='')
    choice = input('3.[delete] :')
    return choice

def LoadingMenu():
    print("____________________loading menu____________________")
    print('1.[show boxes]\n2.[show containers]\n3.[show cars]\n4.[loading boxes to container]')
    choice = input('5.[connect containers to cars] :')
    return choice

def SendAndReceiveMenu():
    print('____________________send & receive menu____________________')
    print('1.[waiting boxes]')
    choice = input('2.[bill of lading :')
    return choice