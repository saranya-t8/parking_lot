class ParkingSystem:
    def __init__(self):
        self.level_a = {i: None for i in range(1,20)}
        self.level_b = {i: None for i in range(21, 40)}

    def assign_parking_space(self, vehicle_number):
        for level, spots in [("A", self.level_a), ("B", self.level_b)]:
            for spot, occupied_vehicle in spots.items():
                if occupied_vehicle is None:
                    spots[spot] = vehicle_number
                    return {"level": level, "spot": spot}

    def retrieve_parking_spot(self, vehicle_number):
        for level, spots in [("A", self.level_a), ("B", self.level_b)]:
            for spot, occupied_vehicle in spots.items():
                if occupied_vehicle == vehicle_number:
                    return {"level": level, "spot": spot}

    def unpark_vehicle(self, vehicle_number):
        for spots in [self.level_a,self.level_b]:
            for spot, occupied_vehicle in spots.items():
                if occupied_vehicle == vehicle_number:
                    spots[spot] = None
                    return {"level": "A" if spot < 21 else "B", "spot": spot}

    def retrieve_nearest_parking_location(self, unparked_spot):
        level, spot = unparked_spot["level"], unparked_spot["spot"]
        next_spot = spot
        while next_spot <= 20 or (next_spot > 20 and next_spot <= 40):
            next_spot += 1
            if next_spot <= 20 and self.level_a[next_spot] is None:
                return {"level": "A", "spot": next_spot}
            elif next_spot > 20 and self.level_b[next_spot] is None:
                return {"level": "B", "spot": next_spot}
            return None


if __name__ == "__main__":

    print("Welcome to XYZ Parking Management System")
    obj = ParkingSystem()
    option = ""
    while option != "Q":

        print("Please Select An Option:\n"
              "P - Park Vehicle\n"
              "U - Un-Park Vechicle\n"
              "V - View Parked Spot\n"
              "Q - Quit Application\n")

        option = input("Enter your option >")

        if option == "P":
            print("Entered option is P ---> Park Vehicle")
            vehicle_number = input("Enter the vechicle number to park : ")
            print("Parked Spot : " + str(obj.assign_parking_space(vehicle_number)))
        if option == "U":
            print("Entered option is E ---> Un-park vehicle")
            vehicle_number = input("Enter the vechicle number to unpark : ")
            unparked_spot = obj.unpark_vehicle(vehicle_number)
            print("Un-Parked Spot : " + str(unparked_spot))
            print("Nearest spot : " +str(obj.retrieve_nearest_parking_location(unparked_spot)))
        if option == "V":
            print("Entered option is V ---> View vehicle parked spot")
            vehicle_number = input("Enter the vechicle number to view spot : ")
            print("Parked Spot : "+str(obj.retrieve_parking_spot(vehicle_number)))
        if option == "Q":
            print("Entered option is Q ---> Qutting application \nThank you for using XYZ Parking managament system")




