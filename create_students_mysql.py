import csv
import mysql.connector
import sys

CSV_FILE = "students.csv"

# Get MySQL credentials from command line arguments
if len(sys.argv) != 3:
    print("Usage: python3 create_students_mysql.py <mysql_user> <mysql_password>")
    sys.exit(1)

mysql_user = sys.argv[1]
mysql_password = sys.argv[2]

connection = mysql.connector.connect(
    host="localhost",
    user=mysql_user,
    password=mysql_password
)

cursor = connection.cursor()

with open(CSV_FILE, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        username = row['username']
        password = row['password']
        db_name = f"{username}_db"
        
        print(f"Creating user {username} and database {db_name}...")
        
        # Create database
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}`;")
        
        # Create user
        cursor.execute(f"CREATE USER IF NOT EXISTS '{username}'@'%' IDENTIFIED BY '{password}';")
        
        # Grant privileges
        cursor.execute(f"GRANT ALL PRIVILEGES ON `{db_name}`.* TO '{username}'@'%';")
        
        # Flush privileges
        cursor.execute("FLUSH PRIVILEGES;")

connection.commit()
cursor.close()
connection.close()
print("All students created successfully!")
