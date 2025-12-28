# Cafe Database Management System

## Project Description
This project is a Cafe Database Management System developed as part of a Database course.  
The system manages customers, menu items, orders, and payments using a relational database design.

The project demonstrates database design, SQL usage, triggers, and system integration.



## Technologies Used
- Python 3
- SQLite (Database)
- SQL
- Oracle Live SQL (for PL/SQL objects)



## System Features
- Add and manage customers
- Add and manage menu items
- Create customer orders
- Add items to orders
- Automatically calculate order subtotals using a database trigger
- Record payments for orders



## Database Design
The database includes the following tables:
- Customer
- MenuItem
- CafeOrder
- OrderDetail
- Payment

Relationships are enforced using primary and foreign keys.



## Trigger, Function, Procedure, and Package
- A database trigger is used to automatically calculate the subtotal for each order item.
- Stored procedures, functions, and packages were implemented and tested using Oracle Live SQL to demonstrate PL/SQL concepts required by the course.
- The system logic is implemented in Python and interacts with the SQLite database.



## How to Run the System

1. Make sure Python 3 is installed.
2. Open the project folder in VS Code.
3. Open a terminal in the project directory.
4. Run the system using:
   ```bash
   python cafe_app.py
