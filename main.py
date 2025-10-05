import json
import os

from plotting import plotting
from helpers import add_transaction, remove_transaction, list_transactions

try:
    with open("transactions.json", "r") as f:
        data = (
            json.load(f)
            if os.path.getsize("transactions.json") > 0
            else {"budget": 0, "transactions": []}
        )
        transactions = data["transactions"]
        budget = data["budget"] if "budget" in data else 0
except FileNotFoundError:
    transactions = []
    budget = 0


def main():
    global transactions, budget
    if budget == 0:
        print("Please set a budget before you start: ")
        budget = float(input())

    while True:
        print(
            "Please choose your option (type the number):\n 1. Add transcation: \n 2. Remove transaction:  \n 3. List transactions: \n 4. Plotting \n 5. Exit/Save \n 6. Delete all data \n 7. Set new budget"
        )
        option = input()
        if option == "1":
            print("\n")
            try:
                amount = float(input("How much?: "))
            except ValueError:
                print("Enter a valid number")
                continue
            category = input("What category?: ")
            date = input("Which date? (press enter for today): ")
            add_transaction(transactions, amount, category, date)
            print("\n")

        elif option == "2":
            try:
                txn_id = int(input("Which transaction id would you like to delete?: "))
            except ValueError:
                print("Enter a valid number")
                continue
            remove_transaction(transactions, txn_id)

        elif option == "3":
            list_transactions(transactions, budget)

        elif option == "4":
            plotting(transactions)

        elif option == "5":
            with open("transactions.json", "w") as f:
                json.dump({"budget": budget, "transactions": transactions}, f, indent=4)
            break

        elif option == "6":
            transactions = []
            budget = 0
            try:
                os.remove("transactions.json")
            except Exception:
                pass

        elif option == "7":
            budget = float(input("Set a new budget amount: "))


if __name__ == "__main__":
    main()
