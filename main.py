import matplotlib.pyplot as plt
import json
import os
from datetime import datetime



try:
    with open("transactions.json", "r") as f:
        data = json.load(f) if os.path.getsize("transactions.json") > 0 else {"budget": 0, "transactions": []}
        transactions = data["transactions"]
        transaction_id = transactions[-1]["id"] if transactions else 0
        budget = data["budget"] if "budget" in data else 0
except FileNotFoundError:
    transactions = []
    transaction_id = 0
    budget = 0

def main():
    global transactions, transaction_id, budget
    while True:
        print("Please choose your option (type the number):\n 1. Add transcation: \n 2. Remove transaction:  \n 3. List transactions: \n 4. Plotting \n 5. Exit \n 6. Delete all data \n 7. Set new budget" )
        option = input()
        if option == "1":
            print("\n")
            add_transaction(float(input("How much?: ")), input("What category?: "), input("Which date? (press enter for today): "))
            print("\n")

        elif option == "2":
            index = int(input("Which number would you like to delete?: "))
            remove_transaction(index-1)
    
        elif option == "3":
            list_transactions()

        elif option == "4":
            plotting()
        
        elif option == "5":
            with open("transactions.json", "w") as f:
                json.dump({"budget": budget, "transactions": transactions}, f, indent=4) 
            break

        elif option == "6":
            transactions = []
            transaction_id = 0
            try:
                os.remove("transactions.json")
            except Exception:
                pass
        
        elif option == "7":
            budget = float(input("Set a new budget amount: "))


def add_transaction(amount, category, date=None):
    if date == None or date == "":
        date = datetime.now()
    if isinstance(date, datetime):
        date = date.strftime("%d-%m-%Y")
    real_date = verify_date(date)
    if real_date:
        global transaction_id
        transaction_id += 1
        transactions.append(
            {
            "id": transaction_id,
            "amount": amount, 
            "category": category, 
            "date":date
            }
            )
    
def verify_date(date):
    try:
        datetime.strptime(date, "%d-%m-%Y")
        return True
    except ValueError:
        print("Invalid date, use the d-m-y format")
        return False
    

def remove_transaction(index):
    try:
        removed = transactions.pop(index)
        print(f"\nRemoved: {removed}\n")
    except IndexError:
        print("\nInvalid index\n")

def list_transactions():
    total = 0
    if not transactions:
        print("\nEmpty!\n")
        return
    print("\n")
    for transaction in transactions:
        print(f"{transaction["id"]}. [{transaction['date']}, ${transaction['amount']}, - {transaction['category']}]")
        total += transaction["amount"]
    print(f"\n You have a budget of {budget}, and have spent {total}. Your remaining total is {budget-total} \n")
        


def plotting():
    transaction_data = {}

    for transaction in transactions:
        if transaction["category"] in transaction_data:
            transaction_data[transaction["category"]] += transaction["amount"]
        else:
            transaction_data[transaction["category"]] = transaction["amount"]

    labels = list(transaction_data.keys())
    values = list(transaction_data.values())

    plt.pie(values, labels=labels)
    plt.legend(title="Spending by category")
    plt.show()


if __name__ == "__main__":
    main()