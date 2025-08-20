import sys

def main():
    coordinates_tuple = (47.376, -71.115)
    coordinates_list = [47.376, -71.115]
    print(f"{sys.getsizeof(coordinates_tuple)} bytes")
    print(f"{sys.getsizeof(coordinates_list)} bytes")
    

main()



#def main():
    #coordinates = (47.376, -71.115)
    #latitude, longitude = coordinates
    #print(f"latitude: {latitude}")
    #print(f"longitude: {longitude}")


#main()