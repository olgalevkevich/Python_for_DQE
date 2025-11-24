from DBConnection import DBConnection
from Distance import Distance
if __name__ == "__main__":
    db_name = 'FINAL_DB.db'
    table_name = 'COORDINATES'
    column_names = ["CITY", "LATITUDE", "LONGITUDE"]  # values for column names
    column_types = ["TEXT", "REAL", "REAL"]  # values for column types
    data_insert = []
    valid_lat = [-90, 90]
    valid_lon = [-180,180]
    coordinates = DBConnection(table_name, column_names, column_types, data_insert, db_name)
    distance_ins = Distance()
    coordinates.create_table()
    city = []
    city.append(input("Enter first city name: ").strip())
    city.append(input("Enter second city name: ").strip())
    coord_city = []
    lat = []
    lon = []
    for i in range(len(city)):
        coord_city.append(coordinates.select_data(city[i])) # select data from COORDINATES table for specified cities
        if coord_city[i] == None: # If the coordinates for the specified city are missing, enter them.
            print(f"Coordinates for {city[i]} not found.")
            while True:
                inp_lat = input(f"Enter latitude for {city[i]}: ")
                try:
                    lat[i] = inp_lat
                except IndexError:
                    lat.append(inp_lat)
                if distance_ins.is_valid_input(lat[i], valid_lat[0], valid_lat[1]) == False:
                    print(f'Entered latitude {lat[i]} is invalid. Try to enter again.')
                else:
                    break
            while True:
                inp_lon = input(f"Enter longitude for {city[i]}: ")
                try:
                    lon[i] = inp_lon
                except IndexError:
                    lon.append(inp_lon)
                if distance_ins.is_valid_input(lon[i], valid_lon[0], valid_lon[1]) == False:
                    print(f'Entered longitude {lon[i]} is invalid. Try to enter again.')
                else:
                    break
            data_insert_city = [city[i], float(lat[i]), float(lon[i])] # data to inser in COORDINATES table
            coordinates_city = DBConnection (table_name, column_names, column_types, data_insert_city, db_name)
            coordinates_city.insert_data() # insert the row into COORDINATES table
            coord_city[i] = coordinates_city.select_data(city[i])  # select data from COORDINATES table for specified cities
        try:
            lat[i] = coord_city[i][1]
            lon[i] = coord_city[i][2]
        except IndexError:
            lat.append(coord_city[i][1])
            lon.append(coord_city[i][2])
    distance = distance_ins.calculate_distance(lat[0], lon[0], lat[1], lon[1]) # calculate the distance between specified cities
    print(f"Distance between {city[0]} and {city[1]}: {distance} km")