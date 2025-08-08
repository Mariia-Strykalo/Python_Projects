def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")

def main():
    pregunta = input("¿Dime algo? ")
    print(convert(pregunta))

main()
