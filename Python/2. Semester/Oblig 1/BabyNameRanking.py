import requests

def getData():
    year = input("Enter the year: ")
    gender = input("Enter the gender: ")
    name = input("Enter the name: ")
    
    url = f"https://liveexample.pearsoncmg.com/data/babynameranking{year}.txt"
    response = requests.get(url)
    response.raise_for_status()
    data = response.text.splitlines()
    
    for line in data:
        parts = line.split()
        rank = parts[0]
        boyName = parts[1]
        boyCount = parts[2]
        girlName = parts[3]
        girlCount = parts[4]

        if gender.lower() == "male":
            if boyName.lower() == name.lower():
                print(f"{name} is ranked {rank} in year {year} with {boyCount} births.")
                return
        elif gender.lower() == "female":
            if girlName.lower() == name.lower():
                print(f"{name} is ranked {rank} in year {year} with {girlCount} births.")
                return
            
        
