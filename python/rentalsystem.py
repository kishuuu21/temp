class Car:
    def __init__(self, car_id, brand, model, price):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.price = price
        self.is_rented = False
    def __str__(self):
        status = "Rented" if self.is_rented else "Available"
        return f"{self.car_id}: {self.brand} {self.model} - Rs.{self.price} - {status}"
class CarRentalSystem:
    def __init__(self):
        self.cars = []
    def add_car(self, car):
        self.cars.append(car)
    def show_available_cars(self):
        print("\nAvailable Cars:")
        for car in self.cars:
            if not car.is_rented:
                print(car)
    def rent_car(self, car_id):
        for car in self.cars:
            if car.car_id == car_id:
                if car.is_rented:
                    print("Car is already rented.")
                else:
                    car.is_rented = True
                    print(f"You have rented: {car.brand} {car.model}")
                return
        print("Car not found.")
    def return_car(self, car_id):
        for car in self.cars:
            if car.car_id == car_id:
                if car.is_rented:
                    car.is_rented = False
                    print(f"You have returned: {car.brand} {car.model}")
                else:
                    print("This car wasn't rented.")
                return
        print("Car not found.")
def main():
    system = CarRentalSystem()
    system.add_car(Car(1, "Toyota", "Corolla", 3000))
    system.add_car(Car(2, "Honda", "Civic", 2800))
    system.add_car(Car(3, "Land Rover", "Defender", 5000))
    system.add_car(Car(4,"Hundai","i20",2000))
    system.add_car(Car(5,"suzuki","Ertiga",3000))
    while True:
        print("\n=== Car Rental Menu ===")
        print("1. Show available cars")
        print("2. Rent a car")
        print("3. Return a car")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            system.show_available_cars()
        elif choice == "2":
            car_id = int(input("Enter Car ID to rent: "))
            system.rent_car(car_id)
        elif choice == "3":
            car_id = int(input("Enter Car ID to return: "))
            system.return_car(car_id)
        elif choice == "4":
            print("Thanks for using the system!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()