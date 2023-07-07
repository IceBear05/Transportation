from mysql.connector import connect
import json

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

    def Add(self, car_id, weight_limit, car_type):
        if self.Check(car_id) == True:
            if 0 < car_type < 3:
                my_cursor.execute(f"INSERT INTO car (car_id, weight_limit, car_type) VALUES ({car_id}, {weight_limit}, {car_type});")
                db.commit()
            else:
                print("car_type must be 1.[simple] or 2.[container]!")
        else:
            print("This car_id already exists!")

    def Edit(self):
        Id = int(input("please enter car_id: "))
        if self.Check(Id) == False:
            choice = input("Which one do you want to change?(car_id or weight_limit or car_type): ")
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
            elif choice == "car_type":
                while True:
                    new_car_type = int(input("please enter new car_type(1.[simple]\t2.[container]: "))
                    if 0 < new_car_type < 3:
                        my_cursor.execute(f"UPDATE car SET car_type = {new_car_type} WHERE car_id = {Id};")
                        db.commit()
                        break
                    else:
                        print("car_type must be 1.[simple] or 2.[container]!")
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

    def Add(self, container_id, weight_limit, container_type):
        if self.Check(container_id) == True :
            if 0 < container_type < 3 :
                my_cursor.execute(f"INSERT INTO container (container_id, weight_limit, container_type) VALUES ({container_id}, {weight_limit}, {container_type});")
                db.commit()
            else:
                print("container_type must be 1.[breakable] or 2.[cold]!")
        else:
            print("This container_id already exists!")

    def Edit(self):
        Id = int(input("please enter container_id: "))
        if self.Check(Id) == False:
            choice = input("Which one do you want to change?(container_id or weight_limit or container_type): ")
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
            elif choice == "container_type":
                while True:
                    new_container_type = int(input("please enter new container_type(1.[breakable]\t2.[cold]): "))
                    if 0 < new_container_type < 3:
                        my_cursor.execute(f"UPDATE container SET container_type = {new_container_type} WHERE container_id = {Id};")
                        db.commit()
                        break
                    else:
                        print("container_type must be 1.[breakable] or 2.[cold]!")
                        continue
        else:
            print("This container_id is not found")

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
                my_cursor.execute(f"INSERT INTO box (box_id, weight, origin, destination, box_type) VALUES ({box_id}, {weight},'{origin}','{destination}',{box_type});")
                db.commit()
            else:
                print("box_type must be 1.[simple]\t2.[breakable]\t3.[cold]: !")
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
                    new_box_type = int(input("please enter new box_type(1.[simple]\t2.[breakable]\t3.[cold]): "))
                    if 0 < new_box_type < 4:
                        my_cursor.execute(f"UPDATE box SET box_type = {new_box_type} WHERE box_id = {Id};")
                        db.commit()
                        break
                    else:
                        print("box_type must be 1.[simple] or 2.[breakable] or 3.[cold]!")
                        continue
            elif choice == "origin":
                new_origin = input("please enter new origin: ")
                my_cursor.execute(f"UPDATE box SET origin = '{new_origin}' WHERE box_id = {Id};")
                db.commit()
            elif choice == "destination":
                new_destination = input("please enter new destination: ")
                my_cursor.execute(f"UPDATE box SET destination = '{new_destination}' WHERE box_id = {Id};")
                db.commit()
        else:
            print("This box_id is not found")

    def Delete(self, box_id):
        if self.Check(box_id) == False:
            my_cursor.execute(f"DELETE FROM box WHERE box_id = {box_id};")
            db.commit()
        else:
            print("This box_id does not exists")


class Loading(Container):
    containersId_packages = []
    containersId_cars = []

    def __init__(self):
        super().__init__()

    def Show_Packages(self):
        my_cursor.execute("SELECT * FROM box;")
        for line in my_cursor:
            print(f"box_id:{line[0]}\tweight:{line[1]}\torigin:{line[2]}\tdestination:{line[3]}\tbox_type:{line[4]}")

    def Show_Containers(self):
        my_cursor.execute("SELECT * FROM container;")
        for line in my_cursor:
            print(f"container_id:{line[0]}\tweight_limit:{line[1]}\tcontainer_type:{line[2]}")

    def Show_Cars(self):
        my_cursor.execute("SELECT * FROM car;")
        for line in my_cursor:
            print(f"car_id:{line[0]}\tweight_limit:{line[1]}\tcar_type:{line[2]}")

    def Loading_Package_Container(self):
        Dic = {}
        Containers_type_1 = False
        Containers_type_2 = False
        container_id = int(input("please enter container_id: "))
        if Container.Check(self, container_id) == False:
            Loading.containersId_packages.append(container_id)
            my_cursor.execute(f"SELECT * FROM container WHERE container_id={container_id};")
            for line in my_cursor:
                if line[2] == 1:
                    Containers_type_1 = True
                elif line[2] == 2:
                    Containers_type_2 = True
        else:
            print("This container_id is not found")

        if Containers_type_1:
            Dic[container_id] = []
            my_cursor.execute(f"SELECT * FROM box WHERE box_type={2};")
            for line in my_cursor:
                print(line)
                ques = input("do you want to add this box?(yes or no) ")
                if ques == "yes":
                    Dic[container_id].append(line)
                    my_cursor.execute(f"DELETE FROM box WHERE box_id = {line[0]};")
                    db.commit()
                else:
                    continue
        elif Containers_type_2:
            Dic[container_id] = []
            my_cursor.execute(f"SELECT * FROM box WHERE box_type={3};")
            for line in my_cursor:
                print(line)
                ques = input("do you want to add this box?(yes or no) ")
                if ques == "yes":
                    Dic[container_id].append(line)
                    my_cursor.execute(f"DELETE FROM box WHERE box_id = {line[0]};")
                    db.commit()
                else:
                    continue
        if len(Dic[container_id]) > 0:
            with open("LoadingContainer.json", "w") as json_file:
                json.dump(Dic, json_file)
        else:
            print("There is no data to add")

    def Loading_Package_Car(self):
        Dic = {}
        Containers_type_1 = False
        Containers_type_2 = False
        container_id = int(input("please enter container_id: "))
        if Container.Check(self, container_id) == False:
            Loading.containersId_cars.append(container_id)
            my_cursor.execute(f"SELECT * FROM container WHERE container_id={container_id};")
            for line in my_cursor:
                if line[2] == 1:
                    Containers_type_1 = True
                elif line[2] == 2:
                    Containers_type_2 = True
        else:
            print("This container_id is not found")

        if Containers_type_1:
            Dic[container_id] = []
            my_cursor.execute(f"SELECT * FROM car WHERE car_type={2};")
            for line in my_cursor:
                print(line)
                ques = input("do you want to add this box?(yes or no) ")
                if ques == "yes":
                    Dic[container_id].append(line)
                else:
                    continue
        elif Containers_type_2:
            Dic[container_id] = []
            my_cursor.execute(f"SELECT * FROM car WHERE car_type={2};")
            for line in my_cursor:
                print(line)
                ques = input("do you want to add this box?(yes or no) ")
                if ques == "yes":
                    Dic[container_id].append(line)
                else:
                    continue

        if len(Dic.values()) > 0:
            for ID in Dic.keys():
                my_cursor.execute(f"DELETE FROM container WHERE container_id = {ID};")
                db.commit()
            with open("LoadingCar.json", "w") as json_file:
                json.dump(Dic, json_file)
        else:
            print("There is no data to add")

    def package_to_car(self):
        pass


class SendAndReceiveMenu():
    CarsPackagesContainers = []

    def __init__(self):
        pass

    def Show_Waiting(self):
        CarsPackagesContainers = []
        with open("LoadingContainer.json") as json_file:
            data = json.load(json_file)
            CarsPackagesContainers.append(data)

            for line in data:
                number = line
                for Package in data[line]:
                    print(f"box: {number}  |  id: {Package[0]} -- weight: {Package[1]} -- origin: {Package[2]} -- destination: {Package[3]} -- box_type: {Package[4]}")

        with open("LoadingCar.json") as json_file:
            data = json.load(json_file)
            CarsPackagesContainers.append(data)

        with open("List.json", "w") as json_file:
            json.dump(CarsPackagesContainers, json_file)

    def BillOfLading(self):
        with open("List.json") as json_file:
            CarsPackagesContainers = json.load(json_file)

        with open("LoadingCar.json") as json_file:
            data = json.load(json_file)
            for line in data:
                number = line
                for car in data[line]:
                    print(f"car: {number}  |  id: {car[0]} -- weight_limit: {car[1]} -- car_type: {car[2]}")

        if len(CarsPackagesContainers) > 0:
            with open("warehouse.json", "w") as json_file:
                json.dump(CarsPackagesContainers, json_file)
                print("\n\nResult : ---------- Saved ---------")
        else:
            print("There is no data to add")
