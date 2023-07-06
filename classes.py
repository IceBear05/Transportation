from mysql.connector import connect

db = connect(host="localhost",user="root",password="nz8119209",database="transportation")
my_cursor = db.cursor()


class Cars:
    def __init__(self):
        pass

    def Check(self, car_id):
        my_cursor.execute(f"SELECT car_id FROM car WHERE car_id={car_id};")
        for Id in my_cursor:
            if len(Id) > 0:
                return False
        return True

    def Add(self, car_id, weight_limit, box_type):
        if self.Check(car_id) == True:
            if 0 < box_type < 4:
                my_cursor.execute(f"INSERT INTO car (car_id, weight_limit, box_type) VALUES ({car_id}, {weight_limit}, {box_type});")
                db.commit()
            else:
                print("box_type must be between 1 to 3!")
        else:
            print("This car_id already exists!")

    def Edit(self):
        Id = int(input("please enter car_id: "))
        if self.Check(Id) == False:
            choice = input("Which one do you want to change?(car_id or weight_limit or box_type): ")
            if choice == "car_id":
                new_car_id = int(input("please enter new car_id: "))
                if self.Check(new_car_id) == True:
                    my_cursor.execute(f"UPDATE car SET car_id = {new_car_id} WHERE car_id = {Id};")
                    db.commit()
                else:
                    print("This id already exists!")
            elif choice == "weight_limit":
                new_weight_limit = int(input("please enter new weight_limit: "))
                my_cursor.execute(f"UPDATE car SET weight_limit = {new_weight_limit} WHERE car_id = {Id};")
                db.commit()
            elif choice == "box_type":
                while True:
                    new_box_type = int(input("please enter new box_type(1 to 3): "))
                    if 0 < new_box_type < 4:
                        my_cursor.execute(f"UPDATE car SET box_type = {new_box_type} WHERE car_id = {Id};")
                        db.commit()
                        break
                    else:
                        print("box_type must be between 1 to 3!")
                        continue
        else:
            print("This car_id is not found")

    def Delete(self, car_id):
        if self.Check(car_id) == False:
            my_cursor.execute(f"DELETE FROM car WHERE car_id = {car_id};")
            db.commit()
        else:
            print("This car_id does not exists!")


class Container:
    def __init__(self):
        pass

    def Check(self, container_id):
        my_cursor.execute(f"SELECT container_id FROM container WHERE container_id={container_id};")
        for Id in my_cursor:
            if len(Id) > 0:
                return False
        return True

    def Add(self, container_id, weight_limit, box_type):
        if self.Check(container_id) == True :
            if 0 < box_type <4 :
                my_cursor.execute(f"INSERT INTO container (container_id, weight_limit, box_type) VALUES ({container_id}, {weight_limit}, {box_type});")
                db.commit()
            else:
                print("box_type must be between 1 to 3!")
        else:
            print("This container_id already exists!")

    def Edit(self):
        Id = int(input("please enter container_id: "))
        if self.Check(Id) == False:
            choice = input("Which one do you want to change?(container_id or weight_limit or box_type): ")
            if choice == "container_id":
                new_container_id = int(input("please enter new_id: "))
                if self.Check(new_container_id) == True:
                    my_cursor.execute(f"UPDATE container SET container_id = {new_container_id} WHERE container_id = {Id};")
                    db.commit()
                else:
                    print("This id already exists!")
            elif choice == "weight_limit":
                new_weight_limit = int(input("please enter new weight_limit: "))
                my_cursor.execute(f"UPDATE container SET weight_limit = {new_weight_limit} WHERE container_id = {Id};")
                db.commit()
            elif choice == "box_type":
                while True:
                    new_box_type = int(input("please enter new box_type: "))
                    if 0 < new_box_type < 4:
                        my_cursor.execute(f"UPDATE container SET box_type = {new_box_type} WHERE container_id = {Id};")
                        db.commit()
                        break
                    else:
                        print("box_type must be between 1 to 3!")
                        continue
        else:
            print("This car_id is not found")

    def Delete(self, container_id):
        if self.Check(container_id) == False:
            my_cursor.execute(f"DELETE FROM container WHERE container_id = {container_id};")
            db.commit()
        else:
            print("This container_id does not exists!")


class Box:
    def __init__(self):
        pass

    def Check(self, box_id):
        my_cursor.execute(f"SELECT box_id FROM box WHERE box_id = {box_id};")
        for Id in my_cursor:
            if len(Id) > 0:
                return False
        return True

    def Add(self, box_id, weight, origin, destination, box_type):
        if self.Check(box_id) == True:
            if 0 < box_type < 4:
                my_cursor.execute(f"INSERT INTO box (box_id, weight, origin, destination, box_type) VALUES ({box_id}, {weight},{origin},{destination},{box_type};")
                db.commit()
            else:
                print("box_type must be between 1 to 3!")
        else:
            print("this box_id already exists!")

    def Edit(self):
        Id = int(input("please enter box_id: "))
        if self.Check(Id) == False:
            choice = input("Which one do you want to change?(box_id / weight / origin/ destination / box_type)")
            if choice == "box_id":
                new_box_id = int(input("please enter new box_id: "))
                if self.Check(new_box_id) == True:
                    my_cursor.execute(f"UPDATE box SET box_id = {new_box_id} WHERE box_id = {Id};")
                    db.commit()
                else:
                    print("This id already exists!")
            elif choice == "weight":
                new_weight_limit = int(input("please enter new weight: "))
                my_cursor.execute(f"UPDATE box SET weight = {new_weight_limit} WHERE box_id = {Id};")
                db.commit()
            elif choice == "box_type":
                while True:
                    new_box_type = int(input("please enter new box_type: "))
                    if 0 < new_box_type < 4:
                        my_cursor.execute(f"UPDATE box SET box_type = {new_box_type} WHERE box_id = {Id};")
                        db.commit()
                        break
                    else:
                        print("box_type must be between 1 to 3!")
                        continue
            elif choice == "origin":
                new_origin = input("please enter new origin: ")
                my_cursor.execute(f"UPDATE box SET origin = {new_origin} WHERE box_id = {Id};")
                db.commit()
            elif choice == "destination":
                new_destination = input("please enter new destination: ")
                my_cursor.execute(f"UPDATE box SET destination = {new_destination} WHERE box_id = {Id};")
                db.commit()
        else:
            print("This car_id is not found")

    def Delete(self, box_id):
        if self.Check(box_id) == False:
            my_cursor.execute(f"DELETE FROM box WHERE box_id = {box_id};")
            db.commit()
        else:
            print("This box_id does not exists")


class Loading:
    def __init__(self):
        pass

    def Show_Box(self):
        my_cursor.execute("SELECT * FROM box;")
        for line in my_cursor:
            print(f"box_id:{line[0]}\tweight:{line[1]}\torigin:{line[2]}\tdestination:{line[3]}\tbox_type:{line[4]}")

    def Show_Container(self):
        my_cursor.execute("SELECT * FROM container;")
        for line in my_cursor:
            print(f"container_id:{line[0]}\tweight_limit:{line[1]}\tbox_type:{line[2]}")

    def Show_Car(self):
        my_cursor.execute("SELECT * FROM car;")
        for line in my_cursor:
            print(f"car_id:{line[0]}\tweight_limit:{line[1]}\tbox_type:{line[2]}")

    def Loading_Package_Container(self):
        pass

    def Loading_Package_Car(self):
        pass

