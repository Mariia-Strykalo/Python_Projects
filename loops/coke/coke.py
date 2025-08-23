#option 1
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


#option 2
def main():
    coins = []              
    total_sum = 0           
    price = 50              

    print(f"Amount Due: {price}")

    while total_sum < price:
        amount = int(input("Insert Coin: "))
        if amount in [25, 10, 5]:
            coins.append(amount)
            total_sum = sum(coins)   
            if total_sum < price:
                print(f"Amount Due: {price - total_sum}")
        else:
            print(f"Amount Due: {price - total_sum}")

    print(f"Change Owed: {total_sum - price}")


main()

