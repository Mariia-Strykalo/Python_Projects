def main():
    time = input("What time is it? ")
    time_decimal = convert(time)

    if 7.0 <= time_decimal <= 8.0:
        print("breakfast time")
    elif 12.0 <= time_decimal <= 13.0:
        print("lunch time")
    elif 18.0 <= time_decimal <= 19.0:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + (float(minutes) / 60)

if __name__ == "__main__":
    main()



#def main():
    #time = input("What time is it? ")
    #hours, minutes = time.split(":")
    #convert(hours, minutes)

#def convert(hours, minutes):
    #floatHours = float(hours)
    #decimalMinutes = float(minutes) / 60
    #addTime = round((floatHours + decimalMinutes), 1)

    #if 7.0 <= addTime <= 8.0:
        #answer("breakfast")
    #elif 12.0 <= addTime <= 13.0:
        #answer("lunch")
    #elif 18.0 <= addTime <= 19.0:
        #answer("dinner")

#def answer(mealTime):
    #print(mealTime, "time")

#main()
