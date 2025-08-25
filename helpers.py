from datetime import datetime 

def add_transaction(transactions, transaction_id, amount, category, date=None):
    if date == None or date == "":
        date = datetime.now()
    if isinstance(date, datetime):
        date = date.strftime("%d-%m-%Y")
    else:
        try:
            day, month, year = date.split("-")
            day = day.zfill(2)
            month = month.zfill(2)
            date = f"{day}-{month}-{year}"
        except ValueError:
            print("Invalid date, use the d-m-y format")
            return

    transaction_id += 1
    transactions.append(
        {
            "id": transaction_id,
            "amount": amount,
            "category": category,
            "date": date
        }
    )


def remove_transaction(transactions, index):
    try:
        removed = transactions.pop(index)
        print(f"\nRemoved: {removed}\n")
    except IndexError:
        print("\nInvalid index\n")


def list_transactions(transactions, budget):
    total = 0
    if not transactions:
        print("\nEmpty!\n")
        return
    print("\n")
    for transaction in transactions:
        print(
            f"{transaction["id"]}. [{transaction['date']}, ${transaction['amount']}, - {transaction['category']}]")
        total += transaction["amount"]
    print(
        f"\n You have a budget of {budget}, and have spent {total}. Your remaining total is {budget-total:.1f} \n")
