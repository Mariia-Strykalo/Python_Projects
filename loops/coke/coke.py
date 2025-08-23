def main():
    print("Amount Due: 50")
    due = 50
    coins = [25, 10, 5]

    while due > 0:
        amount = int(input("Insert Coin: "))

        if amount in coins:
            due -= amount
            if due > 0:
                print(f"Amount Due: {due}")
            if due <= 0:
                due_new = abs(due)
                print(f"Change Owed: {due_new}")
                break
        else:
            print(f"Amount Due: {due}")

main()
