from prettytable import *

# creating a table obj
table = PrettyTable()

# creating column
table.add_column("POKEMON", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("TYPE", ["Electric", "Water", "Fire"])
# changing the alignment to left
table.align = 'l'

# printing the table
print(table)
