import CSV
import mysql.connector

connection = mysql.connector.connect (
  host = "localhost",
  user = "root",
  password = "P@ssw0rd!"
)
cursor = connection.cursor()

with open(CSV_FILE, newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    username = row['username']
    password = row['password']
    db_name = f"{username}_db"

    print (f"Creating user {username} and database {db_name}...")

    cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}`;")
    cursor.execute(f"CREATE USER IF NOT EXISTS '{username}'@'IDENTIFIED BY '(password)';")
    cursor.execute(
