def main():
    spacecraft = {"name": "James Webb Space Telescope"}
    spacecraft.update({"distance": 0.01, "orbit": "Sun"})
    print(create_report(spacecraft))


def create_report(spacecraft):
    return f"""
    ========= REPORT =========

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Orbit: {spacecraft.get("orbit", "Unknown")}

    ==========================
    """ 


main()



#def main():
    #spacecraft = {"name": "James Webb Space Telescope"}
    #spacecraft["distance"] = 0.1
    #print(create_report(spacecraft))


#def create_report(spacecraft):
    #return f"""
    #========= REPORT =========

    #Name: {spacecraft["name"]}
    #Distance: {spacecraft.get("distance")} AU

    #==========================
    #""" 


#main()