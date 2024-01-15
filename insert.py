import json

class SATResultsSystem:
    def __init__(self):
        self.data = []

    def insert_data(self):
        name = input("Enter Name: ")
        address = input("Enter Address: ")
        city = input("Enter City: ")
        country = input("Enter Country: ")
        pincode = input("Enter Pincode: ")
        sat_score = float(input("Enter SAT Score: "))
        passed = "Pass" if sat_score > 30 else "Fail"

        record = {
            "Name": name,
            "Address": address,
            "City": city,
            "Country": country,
            "Pincode": pincode,
            "SAT Score": sat_score,
            "Passed": passed
        }

        self.data.append(record)
        print("Data inserted successfully!")

    def view_all_data(self):
        print(json.dumps(self.data, indent=2))

    def get_rank(self, name):
        sorted_data = sorted(self.data, key=lambda x: x["SAT Score"], reverse=True)
        for i, record in enumerate(sorted_data, start=1):
            if record["Name"] == name:
                return f"{name} is ranked #{i} with SAT Score: {record['SAT Score']}"

        return f"{name} not found in the data."

    def update_score(self, name):
        for record in self.data:
            if record["Name"] == name:
                new_score = float(input(f"Enter new SAT Score for {name}: "))
                record["SAT Score"] = new_score
                record["Passed"] = "Pass" if new_score > 30 else "Fail"
                print(f"SAT Score updated successfully for {name}.")
                return

        print(f"{name} not found in the data.")

    def delete_record(self, name):
        for record in self.data:
            if record["Name"] == name:
                self.data.remove(record)
                print(f"Record for {name} deleted successfully.")
                return

        print(f"{name} not found in the data.")

    def save_to_file(self):
        with open("sat_results.json", "w") as file:
            json.dump(self.data, file, indent=2)
        print("Data saved to 'sat_results.json' file.")

def main():
    sat_system = SATResultsSystem()

    while True:
        print("\nMenu:")
        print("1. Insert data")
        print("2. View all data")
        print("3. Get rank")
        print("4. Update score")
        print("5. Delete one record")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            sat_system.insert_data()
        elif choice == "2":
            sat_system.view_all_data()
        elif choice == "3":
            name = input("Enter name to get rank: ")
            print(sat_system.get_rank(name))
        elif choice == "4":
            name = input("Enter name to update score: ")
            sat_system.update_score(name)
        elif choice == "5":
            name = input("Enter name to delete record: ")
            sat_system.delete_record(name)
        elif choice == "6":
            sat_system.save_to_file()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
