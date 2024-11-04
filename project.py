class Drivers:
    def __init__(self,worker_id,worker_name,worker_city):
        self.worker_id = worker_id
        self.worker_name = worker_name
        self.worker_city = worker_city

class Cities:
    
    def show_cities(self):
        print(sorted(cities,reverse=True))





cities = ["Jbeil","Akkar","Beirut","Saida","Zahle"]
drivers = [Drivers("001", "Max Verstappen", "Akkar"), Drivers("002", "Charles Leclerc", "Saida"), Drivers("003", "Lando Norris", "Jbeil")]
next_id = 4

class DriverManager:
        
    def add_driver(self):
        global next_id
        name = input("Driver's name: ").strip().title()
        city = input("Driver's city: ").strip().title()

        for i in name:
            if not i.isalpha() and i != " ":
                print("Names must be all letters")
                return

        for i in city:
            if not i.isalpha() and i != " ":
                print("Names must be all letters")
                return
                
        if len(name) <= 1 and len(city) <= 1:
            print("invalid name and city, please try again")
            return
        elif len(name) <= 1:
            print("Invalid name please try again")
            return
        elif len(city) <= 1:
            print("Invalid city, please try again")
            return
            
        existing_cities = {driver.worker_city for driver in drivers}
        if city not in existing_cities:
            addto_database = input("this city isn't available want to add it to the database(y/n)? ").strip().lower()

            if addto_database == "y":
                driver =  Drivers(worker_id = f"{next_id:003}", worker_name = name, worker_city = city)
                drivers.append(driver)
                if city not in cities:
                    cities.append(city)
                next_id +=1
                print("Driver added")
            else:
                print("No changes made")
                return
        else:
            driver =  Drivers(worker_id = f"{next_id:003}", worker_name = name, worker_city = city)
            drivers.append(driver)
            if city not in cities:
                cities.append(city)
            next_id +=1
            print("Driver added")

                   
        

    def view_drivers(self):
        for driver in drivers:
            print(f"ID{driver.worker_id}", driver.worker_name, driver.worker_city)

    def check_similar_drivers(self):
        similar_cities = {}
        for driver in drivers:
            city = driver.worker_city

            if city in similar_cities:
                similar_cities[city].append(driver)
            else:
                similar_cities[city] = []
                similar_cities[city].append(driver)
                
        for city, driver_list in similar_cities.items():
            print(f"\n{city}: ")
            for driver in driver_list:
                print(f"ID{driver.worker_id}, Name: {driver.worker_name}")

city = {
    "Akkar":["Jbeil"],
    "Jbeil":["Akkar", "Beirut"],
    "Beirut":["Jbeil"],
    "Saida":["Zahle"],
    "Zahle":["Saida"],
}
 
def dfs(current_city, city, visited):
    visited.add(current_city)
    for neighbor in city.get(current_city, []):
        if neighbor not in visited:
            dfs(neighbor, city, visited)
                
def reachable_cities(start_city):
    visited = set()
    dfs(start_city, city, visited)   
    reachable = visited - {start_city}
    if reachable:
        print(f"Cities reachable from {start_city}:")
        for i in reachable:
            print(i)
    else:
        print(f"No cities reachable from this city")
    
def can_reach(start_city, target_city, city, visited):
    if start_city == target_city:
        return True
    visited.add(start_city)

    for neighbor in city.get(start_city, []):
        if neighbor not in visited:
            if can_reach(neighbor, target_city, city, visited):
                return True
    return False



def drivers_delivering_to_city(target_city, drivers):
    delivering_drivers = []
    for driver in drivers:
        start_city = driver.worker_city
        visited = set()
        if can_reach(start_city, target_city, city, visited):
            delivering_drivers.append(driver.worker_name)
    if delivering_drivers:
        print(f"Drivers delivering {target_city}")
        for i in delivering_drivers:
            print(i)
    else:
        print("There are no drivers delivering to this city")
            

def main_menu():
    while True:
        print("Hello! Please enter")
        print("1. To go to the drivers' menu")
        print("2. To go to the cities' menu")
        print("3. To exit the system")
        
        option = input("option: ")
            
        if option == "1":
            option_one()
        elif option == "2":
            option_two()    
        elif option == "3":
            print("--Exiting--")
            return
        else:
            print("Invalid option, please try again")
            continue
def option_one():
    d = DriverManager()
    print("1. To view all the drivers")
    print("2. To add a driver")
    print("3. Check similar drivers")
    print("4. To go back to the main menu")
    while True:
           
        option = input("option: ")

        if option == "1":
            d.view_drivers()
        elif option == "2":
            d.add_driver()
        elif option == "3":
            d.check_similar_drivers()
        elif option == "4":
           break
        else:
            print("Invalid option, please try again")
            continue
def option_two():
    c = Cities()
    print("1. Show cities")
    print("2. Search city")
    print("3. Print neighboring cities")
    print("4. Print Drivers delivering to city")
    print("5. To go back to the main menu")
    while True:
        option = input("option: ")

        if option == "1":
            c.show_cities()

        elif option == "2":
            result = False
            letter = input("search: ").strip().lower()
            for city in cities:
                if letter in city.lower():
                    print(city)
                    result = True
            if result == False:
                print("No city found")

        elif option == "3":
            city = input("City: ").strip().title()
            if city in cities:
                reachable_cities(city)
            else:
                print("City not found please try again")
            
        elif option == "4":
            target_city = input("City: ").strip().title()
            drivers_delivering_to_city(target_city, drivers)
        
        elif option == "5":
            return
        else:
            print("Invalid option please try again")
            
        
        


            
            
            

            
        

    

main_menu()
            
        
            
            


    


