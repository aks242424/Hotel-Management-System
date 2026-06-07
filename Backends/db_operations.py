import sqlite3

DB_NAME = "HMS.db"

def get_connection():
    """Establishes an independent relational link to the project SQLite file."""
    return sqlite3.connect(DB_NAME)

def initialize_database():
    """Initializes the SQLite master database structure and relational tables."""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Master Guest Profiles Table (P_NO changed to TEXT)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS C_DETAILS (
            CID TEXT PRIMARY KEY,
            C_NAME TEXT,
            C_ADDRESS TEXT,
            C_AGE INT,
            C_COUNTRY TEXT,
            P_NO TEXT,
            C_EMAIL TEXT
        )
    ''')
    
    # Room Calendar Reservations Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ROOM_BOOKINGS (
            CID TEXT,
            ROOM_CHOICE TEXT,
            START_DATE TEXT,
            END_DATE TEXT,
            TOTAL_PRICE INT,
            FOREIGN KEY(CID) REFERENCES C_DETAILS(CID)
        )
    ''')

    # Active Room Rentals Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ROOM_RENT (
            CID TEXT,
            ROOM_CHOICE TEXT,
            NO_OF_DAYS INT,
            ROOM_NO TEXT,
            ROOM_RENT INT,
            FOREIGN KEY(CID) REFERENCES C_DETAILS(CID)
        )
    ''')
    
    # Food & Cuisine Orders Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS RESTAURANT (
            CID TEXT,
            CUISINE TEXT,
            QUANTITY INT,
            BILL INT,
            FOREIGN KEY(CID) REFERENCES C_DETAILS(CID)
        )
    ''')
    
    # Entertainment & Arcade Logging Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS GAMING (
            CID TEXT,
            GAME_NAME TEXT,
            GAME_TIME INT,
            BILL INT,
            FOREIGN KEY(CID) REFERENCES C_DETAILS(CID)
        )
    ''')
    
    # Apparel Counter Purchases Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS FASHION (
            CID TEXT,
            ITEM_NAME TEXT,
            QUANTITY INT,
            BILL INT,
            FOREIGN KEY(CID) REFERENCES C_DETAILS(CID)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("\nCONGRATULATIONS! Your SQLite database connections have been established!")