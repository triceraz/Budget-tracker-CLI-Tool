from datetime import datetime
from typing import Optional, List, Dict


def _format_date(date: Optional[str] = None) -> Optional[str]:
    """Normalize date to dd-mm-YYYY. If empty, use today. Returns None if invalid."""
    if date is None or date == "":
        return datetime.now().strftime("%d-%m-%Y")
    if isinstance(date, datetime):
        return date.strftime("%d-%m-%Y")
    try:
        day, month, year = str(date).split("-")
        day = day.zfill(2)
        month = month.zfill(2)
        return f"{day}-{month}-{year}"
    except Exception:
        print("Invalid date, use the d-m-y format")
        return None


def add_transaction(transactions: List[Dict], amount: float, category: str, date: Optional[str] = None) -> Optional[Dict]:
    """Append a transaction with an auto-incremented id. Returns the created tx or None on failure."""
    date_str = _format_date(date)
    if date_str is None:
        return None

    new_id = max((t.get("id", 0) for t in transactions), default=0) + 1
    tx = {"id": new_id, "amount": amount, "category": category, "date": date_str}
    transactions.append(tx)
    return tx


def remove_transaction(transactions: List[Dict], txn_id: int) -> bool:
    """Remove a transaction by its id. Returns True if removed, False otherwise."""
    for i, t in enumerate(transactions):
        if t.get("id") == txn_id:
            removed = transactions.pop(i)
            print(f"\nRemoved: {removed}\n")
            return True
    print("\nInvalid transaction id\n")
    return False


def list_transactions(transactions: List[Dict], budget: float) -> None:
    total = 0.0
    if not transactions:
        print("\nEmpty!\n")
        return
    print("\n")
    for transaction in transactions:
        print(
            f"{transaction['id']}. [{transaction['date']}, ${transaction['amount']}, - {transaction['category']}]"
        )
        total += float(transaction.get("amount", 0))
    print(
        f"\n You have a budget of {budget}, and have spent {total}. Your remaining total is {budget-total:.1f} \n"
    )
