# Hotel Management System

A Python-based, terminal-driven **Hotel Management System developed as my Class 12 school project**. The project was created to apply programming concepts and database management principles to a practical, real-world scenario.

The application simulates essential hotel operations, including customer registration, room bookings, service billing, database management, and final checkout calculations.

> **Project Background:** This was an academic project developed during Class 12. It represents my learning and practical application of Python programming, SQL database concepts, and problem-solving skills at the school level.

---

## Project Objectives

The main objectives of this project were to:

- Apply Python programming concepts to build a practical application.
- Understand how relational databases work.
- Implement database operations using SQL.
- Connect Python application logic with an SQLite database.
- Organize hotel operations into separate functional modules.
- Practise data storage, retrieval, calculations, and record management.

---

## Features

### 1. Guest Management
- Register new customers with their personal and contact details.
- Store customer information in the database.
- Search and retrieve existing customer records.

### 2. Room Booking and Management
- Allocate rooms based on different room categories:
  - Ultra Royal
  - Royal
  - Elite
  - Budget
- Record booking dates and stay durations.
- Calculate room charges based on the selected category and duration.

### 3. Multiple Billing Counters

The system includes separate billing modules for different hotel services.

**Room Billing**
- Room tariff calculations.
- Stay-duration-based charges.

**Restaurant Billing**
- Veg and non-veg food options.
- Restaurant order and billing calculations.

**Gaming Zone Billing**
- Virtual Reality
- Arcade
- Racing
- Escape Room
- Charges based on gaming hours.

**Fashion and Retail Billing**
- Record retail purchases.
- Calculate product quantities and total costs.

### 4. Customer Records and Final Billing
- Retrieve previously stored customer information.
- Generate consolidated bills.
- Calculate the final checkout amount using the different service charges.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.13+ | Application logic and programming |
| SQLite 3 | Relational database management |
| SQL | Database queries and operations |
| IDLE / VS Code | Development environment |

**External dependencies:** The project uses Python's built-in `sqlite3` module, so no separate database driver installation is required.

---

## Repository Structure

```text
Hotel-Management-System/
│
├── Backends/
│   └── db_operations.py
│
├── Database_Docs/
│   ├── database_tables_overview.png
│   ├── customer_details_schema.jpg
│   ├── customer_details_records_part1.jpg
│   ├── customer_details_records_part2.jpg
│   ├── room_rent_schema.jpg
│   ├── room_rent_records.jpg
│   ├── room_bookings_schema.jpg
│   ├── room_bookings_records.jpg
│   ├── restaurant_schema.jpg
│   ├── restaurant_records.jpg
│   ├── gaming_schema.jpg
│   ├── gaming_records.jpg
│   ├── fashion_schema.jpg
│   └── fashion_records.jpg
│
├── Outputs/
│   ├── 01_main_menu.png
│   ├── 02_add_customer.png
│   ├── 03_make_booking.png
│   ├── 04_room_rent_calculation.png
│   ├── 05_restaurant_billing.png
│   ├── 06_gaming_billing.png
│   ├── 07_fashion_billing.png
│   ├── 08_show_total_bill.png
│   ├── 09_search_customer.png
│   └── 10_system_exit.png
│
├── HMS.db
├── main.py
├── Project_Report.pdf
├── LICENSE
└── .gitignore
```

---

## Database Architecture

The application uses an SQLite relational database named `HMS.db`, organized into six tables.

| Table | Description |
|---|---|
| `C_DETAILS` | Stores customer identification and personal details. |
| `ROOM_RENT` | Stores room allocation, room categories, stay information, and rental charges. |
| `ROOM_BOOKINGS` | Maintains booking dates, reservation details, and pricing information. |
| `RESTAURANT` | Stores restaurant orders and calculated food charges. |
| `GAMING` | Records gaming activities, hours, and associated charges. |
| `FASHION` | Stores retail purchases, quantities, and product costs. |

### Database Documentation

The `Database_Docs/` directory contains:
- Database table overview.
- Individual table schemas.
- Sample database records.
- Supporting database structure screenshots.

These documents provide a visual reference for the database design and stored information.

---

## Application Screenshots

The `Outputs/` directory contains screenshots documenting the application's execution flow, including:

1. Main menu.
2. Customer registration.
3. Room booking.
4. Room rent calculation.
5. Restaurant billing.
6. Gaming billing.
7. Fashion billing.
8. Final bill generation.
9. Customer search.
10. System exit.

---

## Installation and Execution

### Prerequisites

- Python 3.x installed.
- Git installed (if cloning the repository).

The application uses Python's built-in SQLite support through `sqlite3`.

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Hotel-Management-System.git
```

### 2. Navigate to the Project Directory

```bash
cd Hotel-Management-System
```

### 3. Run the Application

```bash
python main.py
```

The terminal-based application will start from its main menu.

---

## Skills and Concepts Practised

Developing this project helped me practise and understand several programming and database concepts:

- Python fundamentals and structured programming.
- Functions, conditional statements, loops, and modular code organization.
- SQL queries and relational database concepts.
- SQLite database connectivity using Python.
- Database table creation and record management.
- Data insertion, retrieval, and updating.
- Calculation and billing logic.
- Organizing a multi-module application.
- Testing application workflows and identifying errors.

---

## Academic Project and Acknowledgement

This Hotel Management System was developed as **my Class 12 academic project** as part of my school-level programming and practical learning.

The project was an opportunity to explore how programming and database concepts can be combined to create a functional application. It reflects my learning process, implementation efforts, and understanding of Python and SQL at that stage.

The project is shared on GitHub for educational reference and to document my early programming work.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
