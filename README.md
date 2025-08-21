# Budget Tracker

A simple command-line Python program to track your expenses and budget.

## Features

- Add transactions with amount, category, and date.
- Remove transactions.
- List all transactions with a running total and remaining budget.
- Plot spending by category using a pie chart.
- Set or update your budget.
- Delete all transaction data.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/triceraz/Budget-Tracker-CLI-Tool
cd Budget-tracker-CLI-Tool
````

2. Create a virtual environment (optional but recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the program:

```bash
python main.py
```

Follow the on-screen menu to add, remove, or view transactions, set your budget, or plot spending.

### Input Format

* Dates should be in `dd-mm-yyyy` format. Press Enter to use today's date.
* Amounts should be numbers (floats or integers).

## Files

* `main.py` — main program.
* `transactions.json` — stores budget and transaction data (auto-generated).
* `requirements.txt` — lists dependencies (e.g., `matplotlib`).

## Dependencies

* Python 3.x
* matplotlib

## Notes

* Transactions are saved to `transactions.json` when exiting the program.
* Deleting all data removes this file completely.
