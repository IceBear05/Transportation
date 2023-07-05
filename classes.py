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
                return True
        return False

    def Add(self, car_id, weight_limit, box_type):
        my_cursor.execute(f"INSERT INTO car (car_id, weight_limit, box_type) VALUES ({car_id}, {weight_limit}, {box_type});")
        db.commit()

    def Edit(self, car_id=0, weight_limit=0, box_type=0):
        if car_id > 0:
            last_id = int(input("please enter last car_id: "))
            my_cursor.execute(f"UPDATE car SET car_id = {car_id} WHERE car_id = {last_id};")
            db.commit()
        elif weight_limit > 0:
            last_limit = int(input("please enter last weight_limit: "))
            my_cursor.execute(f"UPDATE car SET weight_limit = {weight_limit} WHERE weight_limit = {last_limit};")
            db.commit()
        elif box_type > 0:
            last_type = int(input("please enter last box_type: "))
            my_cursor.execute(f"UPDATE car SET box_type = {box_type} WHERE box_type = {last_type};")
            db.commit()

    def Delete(self, car_id):
        if self.Check(car_id):
            my_cursor.execute(f"DELETE FROM car WHERE car_id = {car_id};")
            db.commit()
        else:
            print("car_id not found")

# ob = Cars()
# # choice = input("Enter(car_id or weight_limit or box_type): ")
# # if choice == "car_id":
# #     car_id = int(input("please enter new car_id: "))
# #     ob.Edit(car_id=car_id)
# # elif choice == "weight_limit":
# #     weight_limit = int(input("please enter new weight_limit: "))
# #     ob.Edit(weight_limit=weight_limit)
# # elif choice == "box_type":
# #     box_type = int(input("please enter new box_type: "))
# #     ob.Edit(box_type=box_type)

# ob.Delete(int(input("please enter car_id: ")))



class Container:
    def __init__(self):
        pass

    def Check(self, container_id):
        my_cursor.execute(f"SELECT container_id FROM container WHERE container_id={container_id};")
        for Id in my_cursor:
            if len(Id) > 0:
                return True
        return False

    def Add(self, container_id, weight_limit, box_type):
        my_cursor.execute(f"INSERT INTO container (container_id, weight_limit, box_type) VALUES ({container_id}, {weight_limit}, {box_type});")
        db.commit()

    def Edit(self, container_id=0, weight_limit=0, box_type=0):
        if container_id > 0:
            last_id = int(input("please enter last container_id: "))
            my_cursor.execute(f"UPDATE container SET container_id = {container_id} WHERE container_id = {last_id};")
            db.commit()
        elif weight_limit > 0:
            last_limit = int(input("please enter last weight_limit: "))
            my_cursor.execute(f"UPDATE container SET weight_limit = {weight_limit} WHERE weight_limit = {last_limit};")
            db.commit()
        elif box_type > 0:
            last_type = int(input("please enter last box_type: "))
            my_cursor.execute(f"UPDATE container SET box_type = {box_type} WHERE box_type = {last_type};")
            db.commit()

    def Delete(self, container_id):
        if self.Check(container_id):
            my_cursor.execute(f"DELETE FROM container WHERE container_id = {container_id};")
            db.commit()
        else:
            print("container_id not found")



class Box:
    def __init__(self):
        pass

    def Check(self, box_id):
        my_cursor.execute(f"SELECT box_id FROM box WHERE box_id = {box_id};")
        for Id in my_cursor:
            if len(Id) > 0:
                return True
        return False

    def Add(self, box_id, weight, origin, destination, box_type):
        my_cursor.execute(f"INSERET INTO box (box_id, weight, origin, destination, box_type) VALUES ({box_id}, {weight},{origin},{destination},{box_type};")
        db.commit()

    def Edit(self, box_id = 0, weight = 0, origin='', destination='', box_type = 0):
        if box_id > 0 :
            last_id = int(input("please enter last box_id: "))
            my_cursor.execute(f"UPDATE box SET box_id = {box_id} WHERE box_id = {last_id};")
            db.commit()
        elif weight > 0 :
            last_weight = int(input("please enter last weight: "))
            my_cursor.execute(f"UPDATE box SET weight = {weight} WHERE weight = {last_weight};")
            db.commit()
        elif box_type > 0:
            last_type = int(input("please enter last box_type: "))
            my_cursor.execute(f"UPDATE box SET box_type = {box_type} WHERE box_type = {last_type};")
            db.commit()

    def Delete(self, box_id):
        if self.Check(box_id):
            my_cursor.execute(f"DELETE FROM box WHERE box_id = {box_id};")
            db.commit()
        else:
            print("box_id not found")

