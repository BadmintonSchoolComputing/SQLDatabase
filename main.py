import sqlite3


def output_results(rows):
  print(rows)




#Create a connection to the database called aquarium.db
connection = sqlite3.connect("aquarium.db")
cursor = connection.cursor()

# Create a database table called 'fish'
cursor.execute("CREATE TABLE fish (name TEXT, species TEXT, tank_number INTEGER)")


#Create some data by inserting rows into the database
cursor.execute("INSERT INTO fish VALUES ('Sammy', 'shark', 1)")
cursor.execute("INSERT INTO fish VALUES ('Jamie', 'cuttlefish', 7)")
cursor.execute("INSERT INTO fish VALUES ('Jack', 'clownfish', 7)")
#TASK1 TODO Create some more data for 5 other fish with names and species and tank numbers
#....


#TASK2 TODO Add a new field to the 'fish' called 'predator'. This will have the values of 'Y' or 'N' to indicate if the fish is a predator (might be important when deciding which tanks to put the fish in!!) 


## Run a query to select all the fish from the table and print out the results

rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
output_results(rows)


## Run a query to select all the fish from the table that have a name starting with 'J'
#TASK 3 TODO uncomment the following the code to it can be executed. Modify it to seach using different criteria 
#rows = cursor.execute(
#    "SELECT name, species, tank_number FROM fish WHERE name like 'Ja%'").fetchall()
#output_results(rows)



 
# Run a query to search for all fish with a name inputed by the user
#TASK 4 TODO - uncomment the following the code to it can be executed
#target_fish_name = input("Enter a name to search for (Use % for wilcard):")
#rows = cursor.execute(
#    "SELECT name, species, tank_number FROM fish WHERE name like ?",
#    (target_fish_name,),
#).fetchall()
#output_results(rows)

#TASK 5 Do something similar to ask the user for a tank number and print out all the fish in that tank



#TASK 6 - Modify the function at the top called output_results to use the following code to format the results in a nicer way. 
#for row in rows:
#    print(f"Name: {row[0]} Species:{row[1]} Tank number:{row[2]}")




