import matplotlib.pyplot as plt

def plotting(transactions):
    if transactions:
        transaction_data = {}

        for transaction in transactions:
            if transaction["category"] in transaction_data:
                transaction_data[transaction["category"]
                                 ] += transaction["amount"]
            else:
                transaction_data[transaction["category"]
                                 ] = transaction["amount"]

        labels = list(transaction_data.keys())
        values = list(transaction_data.values())

        plt.pie(values, labels=labels, autopct="%1.1f%%")
        plt.legend(title="Spending by category")
        plt.show()
    else:
        print("You have nothing to plot yet!")