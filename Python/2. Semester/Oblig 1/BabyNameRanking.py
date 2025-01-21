import requests

def getData():
    while True:
        year = input("Enter the year (2001-2010): ").strip()
        if not year:
            print("Please enter a year.")
        elif not year.isdigit():
            print("Please enter a valid year (digits only).")
        elif int(year) < 2001 or int(year) > 2010:
            print("No data for this year. Please enter a year between 2001 and 2010.")
        else:
            break

    while True:
        gender = input("Enter the gender (male/female): ").strip().lower()
        if gender not in ["male", "female"]:
            print("Please enter either 'male' or 'female'.")
        else:
            break
  
    while True:
        name = input("Enter the name: ").strip()
        if not name.isalpha():
            print("Please enter a valid name (letters only).")
        else:
            break
    
    url = f"https://liveexample.pearsoncmg.com/data/babynameranking{year}.txt"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return
    
    data = response.text.splitlines()
    
    found = False    
    for line in data:
        parts = line.split()
        rank = parts[0]
        boyName = parts[1]
        boyCount = parts[2]
        girlName = parts[3]
        girlCount = parts[4]

        
        if gender == "male" and boyName.lower() == name.lower():
            print(f"{name} is ranked {rank} in year {year} with {boyCount} births.")
            found = True
            break
        elif gender.lower() == "female" and girlName.lower() == name.lower():
            print(f"{name} is ranked {rank} in year {year} with {girlCount} births.")
            found = True
            break
    if not found:             
        print(f"{name} is not ranked in year {year}.")

            
getData()
