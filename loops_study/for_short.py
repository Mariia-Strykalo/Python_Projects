def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]
    for name in names:
        print(write_letter(name, "Princess Peach"))

def write_letter(receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        Dear {receiver},

        You are cordially invited to a ball at 
        Peach's Castle this evening, 7 PM.

        Sincerelly,
        {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """

main()



#def main():
    #names = ["Mario", "Luigi", "Daisy", "Yoshi"]
    #for i in range(len(names)):
        #print(write_letter(names[i], "Princess Peach"))

#def write_letter(receiver, sender):
    #return f"""
    #+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        #Dear {receiver},

        #You are cordially invited to a ball at 
        #Peach's Castle this evening, 7 PM.

        #Sincerelly,
        #{sender}
    #+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    #"""

#main()