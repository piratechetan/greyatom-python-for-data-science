# --------------
# Code starts here
sum=0
# Create the lists 
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']
# Concatenate both the strings
new_class=class_1+class_2
# Append the list
new_class.append('Peter Warden')

# Print updated list
print(new_class)
# Remove the element from the list
new_class.remove('Carla Gentry')
# Print the list
print(new_class)

# Create the Dictionary
courses={'Math':65,'English':70,'History':80,'French':70,'Science':60}

# Slice the dict and stores  the all subjects marks in variable
sum = 0
for i in courses.values():
    sum = sum + i 


# Store the all the subject in one variable `Total`
total=sum
# Print the total
print(total)
# Insert percentage formula
percentage=total/500*100
# Print the percentage
print(percentage)



# Create the Dictionary
mathematics={'Geoffrey Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Benjio':50,    
  'Hilary Mason':70,'Corinna Cortes':66,'Peter Warden':75}



# Given string
topper=max(mathematics,key=mathematics.get)
print(topper)
split=topper.split()
# Create variable first_name 
first_name=split[0]
print(first_name)
# Create variable Last_name and store last two element in the list
Last_name=split[1]
print(Last_name)
# Concatenate the string
full_name=Last_name+' '+first_name
# print the full_name
# print the name in upper case
certificate_name=full_name.upper()
print(certificate_name)
# Code ends here


