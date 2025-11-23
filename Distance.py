import math

class Distance:
    def __init__(self):
        pass
    def is_valid_input(self, input_value, min_valid, max_valid):
        try:
            num = float(input_value)
            return min_valid <= num <= max_valid
        except ValueError:
            return False

    def calculate_distance (self, lat1, lon1, lat2, lon2):
        # Convert latitude and longitude from degrees to radians
        lat1 = math.radians(lat1)
        lon1 = math.radians(lon1)
        lat2 = math.radians(lat2)
        lon2 = math.radians(lon2)

        # Compute differences
        dlat = lat2 - lat1
        dlon = lon2 - lon1

        # Haversine formula
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.asin(math.sqrt(a))
        # Radius of Earth in kilometers
        r = 6371
        # Calculate the distance in kilometres
        distance_res = round(r * c, 1)
        return distance_res