def main():
    x = input("Hello, friend! ").strip().casefold()
    greeting(x)

def greeting(n):
    if n[:5] == "hello":
        print("$0")
    elif n[:1] == "h":
        print("$20")
    else:
        print("$100")

main()
