class CityData:
    def __init__(self, name, outConCount, outCons):
        self.name = name  
        self.outConCount = outConCount  
        self.outCons = outCons  
        self.seen = False  
        self.predecessor = -1  

def parse_file(filename):
    cities = []
    with open(filename, 'r') as file:
        lines = file.readlines()  
        city_count = int(lines[0].strip())  
        for i in range(1, city_count + 1):
            data = lines[i].split()  
            index = int(data[0])  
            name = data[1].strip(',') 
            outConCount = int(data[2])  
            outCons = [int(x) for x in data[3:]]  
            cities.append(CityData(name, outConCount, outCons))  
    return cities 

def find_path(cities, start_name, dest_name):
    start_index = -1
    dest_index = -1
    for i, city in enumerate(cities):
        if city.name.lower() == start_name.lower():  
            start_index = i
        if city.name.lower() == dest_name.lower():  
            dest_index = i

    if start_index == -1:
        print(f"{start_name} is not a valid city. Please re-enter options.")
        return
    if dest_index == -1:
        print(f"{dest_name} is not a valid city. Please re-enter options.")
        return

    stack = [start_index]
    cities[start_index].seen = True  

    while stack:
        current_index = stack.pop()  
        current_city = cities[current_index]
        if current_index == dest_index:
            path = []
            while current_index != -1:
                path.append(cities[current_index].name) 
                current_index = cities[current_index].predecessor 
            print("Path found: " + " -> ".join(path[::-1])) 
            return

        for neighbor in current_city.outCons:
            if not cities[neighbor].seen:
                cities[neighbor].seen = True 
                cities[neighbor].predecessor = current_index  
                stack.append(neighbor)  
    print("No path found between", start_name, "and", dest_name)
if __name__ == "__main__":
    cities = parse_file('pb.txt')  
    start_city = input("Enter the name of the starting city: ").strip()
    dest_city = input("Enter the name of the destination city: ").strip()
    find_path(cities, start_city, dest_city)
