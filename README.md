# Hotel Management System

A robust, terminal-based Hotel Management application developed in Python and integrated with a relational SQL database. This system streamlines front-desk hotel operations ranging from customer onboarding to final check-out billing counter calculations.

---

## 🚀 Features
* **Guest Onboarding:** Easily add and register new customer profiles with complete contact details.
* **Room Bookings & Renting:** Allocate specific room classes (Ultra Royal, Royal, Elite, Budget) and dynamically track stay durations.
* **Integrated Billing Counters:** Automatically calculates costs across separate hotel amenities:
  * Room Tariff / Stay Duration Charges
  * Restaurant & Cuisine Orders (Veg / Non-Veg combos)
  * Gaming Zone Hours (Virtual Reality, Arcade, Racing, Escape Room)
  * Fashion/Retail Counter Purchases
* **Database Inquiries:** Instantly query historical guest profiles and generate consolidated final check-out invoices.

---

## 🛠️ Tech Stack
* **Language:** Python 3.13+
* **Database Engine:** SQLite 3 (`HMS.db`)
* **Development Environment:** IDLE / VS Code

---

## 📁 Repository Structure

<pre><code>Hotel-Management-System/
│
├── Backends/                  # Core Python modules and application logic scripts
│   └── db_operations.py
│
├── Database_Docs/             # Architectural database blueprints & data records
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
├── Outputs/                   # Step-by-step sequential CLI application walkthroughs
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
├── HMS.db                     # Active relational SQLite database file
├── main.py                    # Main application execution entry point
├── Project_Report.pdf         # Comprehensive final project documentation report
├── LICENSE                    # Project distribution license (MIT)
└── .gitignore                 # Spec file ensuring local tracking exclusions</code></pre>

---

## 📊 Database Architecture

The application implements a relational database schema structured across 6 interlinked tables inside HMS.db:

1. **C_DETAILS (Master Table):** Tracks core customer identification attributes (CID as Primary Key), home address profiles, age metrics, and personal communication paths.
2. **ROOM_RENT:** Holds active real-time operational entries for assigned customer room configurations, stay tracking, and running price structures.
3. **ROOM_BOOKINGS:** Manages analytical date-wise guest calendars containing historical reservation ranges (START_DATE, END_DATE) and gross pricing evaluations.
4. **RESTAURANT:** Stores active dinner/meal ordering entries, table quantities, and calculated item totals.
5. **GAMING:** Handles recreational zone hours logging, virtual category counters, and microtransaction billing values.
6. **FASHION:** Logs physical retail shopping logs, apparel counter quantities, and total product costs.

*Note: Visual structural layouts, structural rules, data constraints, and mock table entries are fully detailed inside the `/Database_Docs` folder.*

---

## 💻 How to Setup and Run

### Prerequisites
Ensure you have Python 3.x installed on your workstation. The core database stack utilizes Python's native sqlite3 driver, meaning zero external database installation packages are mandatory.

### Execution Instructions

1. **Clone the repository to your desktop machine:**
<pre><code>git clone https://github.com/YOUR_USERNAME/Hotel-Management-System.git</code></pre>

2. **Navigate into the cloned root project directory:**
<pre><code>cd Hotel-Management-System</code></pre>

3. **Execute the primary script interface entry point:**
<pre><code>python main.py</code></pre>

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for open-source usage and compliance details.