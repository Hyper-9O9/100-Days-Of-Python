travel_log = [
{
    "country": "France",
    "visits": 12,
    "cities_visited": ["Paris", "Dijon", "Lille"]
},
{
    "country": "Germany",
    "visits": 5,
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"]

},
]

def add_new_country(country, visits, city_visited):
    new_country = {}
    new_country["country"] =  country
    new_country["visits"] = visits
    new_country["cities_visited"] = city_visited

    travel_log.append(new_country)
    print(travel_log)

add_new_country(country = "Russia", visits = 2, city_visited = ["Moscow", "Saint Petersburg"])