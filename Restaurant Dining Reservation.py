import os
class Reservation:
    def __init__(self, name, date, time, adults, children):
        self.name = name
        self.date = date
        self.time = time
        self.adults = adults
        self.children = children
        self.subtotal = (adults * 500) + (children * 300)

    def to_reservation_file(self):
        return f"{self.name:<25}{self.date:<20}{self.time:<12}{self.adults:<10}{self.children:<10}{self.subtotal}\n"

    @staticmethod
    def from_line(line):
        name = line[0:25].strip()
        date = line[25:45].strip()
        time = line[45:57].strip()
        adults = int(line[57:67].strip())
        children = int(line[67:77].strip())
        return Reservation(name, date, time, adults, children)

class ReservationSystem:
    def __init__(self):
        self.reservations = []
        self.load_reservations()

    def load_reservations(self):
        if os.path.exists("reservations.txt"):
            with open("reservations.txt", "r") as file:
                for line in file:
                    reservation = Reservation.from_line(line)
                    if reservation:
                        self.reservations.append(reservation)

    def save_reservations(self):
        with open("reservations.txt", "w") as add_to_file:
            for reservation in self.reservations:
                add_to_file.write(reservation.to_reservation_file())

    @staticmethod
    def display_menu():
        print("\nRestaurant Reservation System")
        print("System Menu")
        print("a. View all reservations")
        print("b. Make reservation")
        print("c. Delete reservation")
        print("d. Generate report")
        print("e. Exit")

    def view_reservations(self):
        if not self.reservations:
            print("No reservations found.\n")
            return
        print("\n#\t\tDate\t\t\t\tTime\t\tName\t\t\t\t\tAdults\tChildren")
        for idx, res in enumerate(self.reservations, 1):
            #print(f"{idx}\t\t{res.date}\t\t{res.time}\t\t{res.name}\t\t{res.adults}\t\t{res.children}")
            print(f"{idx:<8}{res.date:<20}{res.time:<12}{res.name:<24}{res.adults:<8}{res.children}")

    def make_reservation(self):
        try:
            name = input("Enter Name: ").strip()
            date = input("Enter Date: ").strip()
            time = input("Enter Time: ").strip()
            adults = int(input("Enter No of Adults: "))
            children = int(input("Enter No of Children: "))

            new_reservation = Reservation(name, date, time, adults, children)
            self.reservations.append(new_reservation)
            self.save_reservations()
            print(f"Reservation added for {name}")
        except ValueError as err:
            print(f"Input Error: {err}")

    def delete_reservation(self):
        if not self.reservations:
            print("No reservation found")
            return
        self.view_reservations()
        try:
            reservation_number = int(input("\nEnter reservation number to delete: "))
            if 1 <= reservation_number <= len(self.reservations):
                delete = self.reservations.pop(reservation_number - 1)
                print(f"Reservation for {delete.name} has been deleted.")
                self.save_reservations()
            else:
                print("Invalid reservation number.")
        except ValueError:
            print("Please enter a valid number.")

    def generate_report(self):
        if not self.reservations:
            print("No reservation to report.")
            return
        print("\n" + "-"*96)
        print("\t\t\t\t\t\t\t\t\t\t\tREPORT")
        print("\n#\t\tDate\t\t\t\tTime\t\tName\t\t\t\t\tAdults\tChildren\t\tSubtotal")

        total_adults = 0
        total_kids = 0
        grand_total = 0
        for idx, reservation in enumerate(self.reservations, 1):
            print(f"{idx:<8}{reservation.date:<20}{reservation.time:<12}{reservation.name:<24}{reservation.adults:<8}{reservation.children:<16}{reservation.subtotal:.2f}")
            total_adults += reservation.adults
            total_kids += reservation.children
            grand_total += reservation.subtotal
        print(f"\n\nTotal number of Adults: {total_adults}")
        print(f"Total number of Kids: {total_kids}")
        print(f"Grand Total: {grand_total:.2f}")
        print("-"*96)

    def run(self):
        while True:
            self.display_menu()
            choice = input("\nEnter your choice: ").lower()
            if choice == 'a':
                self.view_reservations()
            elif choice == 'b':
                self.make_reservation()
            elif choice == 'c':
                self.delete_reservation()
            elif choice == 'd':
                self.generate_report()
            elif choice == 'e':
                print("Thank you!")
                break
            else:
                print("Invalid option.")


if __name__ == "__main__":
    ReservationSystem().run()
