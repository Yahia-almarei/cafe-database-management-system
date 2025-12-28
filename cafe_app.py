import sqlite3

DB = "cafe.db"

def connect():
    return sqlite3.connect(DB)

def init_db():
    with open("schema.sql") as f:
        sql = f.read()
    conn = connect()
    conn.executescript(sql)
    conn.commit()
    conn.close()

def add_customer():
    name = input("Name: ")
    phone = input("Phone: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO Customer (Name, Phone) VALUES (?, ?)", (name, phone))
    conn.commit()
    conn.close()
    print("Customer added")

def add_menu_item():
    name = input("Item name: ")
    price = float(input("Price: "))
    category = input("Category: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO MenuItem (Name, Price, Category) VALUES (?, ?, ?)",
        (name, price, category)
    )
    conn.commit()
    conn.close()
    print("Menu item added")

def create_order():
    customer_id = int(input("Customer ID: "))
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO CafeOrder (CustomerID, Status) VALUES (?, 'Preparing')",
        (customer_id,)
    )
    conn.commit()
    order_id = cur.lastrowid
    conn.close()
    print("Order created. ID:", order_id)

def add_item_to_order():
    order_id = int(input("Order ID: "))
    item_id = int(input("Item ID: "))
    qty = int(input("Quantity: "))
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO OrderDetail (OrderID, ItemID, Quantity) VALUES (?, ?, ?)",
        (order_id, item_id, qty)
    )
    conn.commit()
    conn.close()
    print("Item added to order (subtotal calculated by trigger)")

def record_payment():
    order_id = int(input("Order ID: "))
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "SELECT SUM(Subtotal) FROM OrderDetail WHERE OrderID = ?",
        (order_id,)
    )
    total = cur.fetchone()[0]
    method = input("Payment method: ")
    cur.execute(
        "INSERT INTO Payment (OrderID, Amount, Method) VALUES (?, ?, ?)",
        (order_id, total, method)
    )
    conn.commit()
    conn.close()
    print("Payment recorded:", total)

def menu():
    print("""
1. Add Customer
2. Add Menu Item
3. Create Order
4. Add Item to Order
5. Record Payment
6. Exit
""")

def main():
    init_db()
    while True:
        menu()
        choice = input("Choose: ")
        if choice == "1":
            add_customer()
        elif choice == "2":
            add_menu_item()
        elif choice == "3":
            create_order()
        elif choice == "4":
            add_item_to_order()
        elif choice == "5":
            record_payment()
        elif choice == "6":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
