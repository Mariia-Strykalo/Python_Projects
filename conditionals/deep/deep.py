question = input("What is the answer to the Great Question? ").strip().casefold()

match question:
    case "42" | "forty two" | "forty-two":
        print("Yes")
    case _:
        print("No")
