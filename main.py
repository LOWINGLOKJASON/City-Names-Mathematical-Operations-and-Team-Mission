#****************************************************************
#Name: Wing Lok LO
#Link: https://replit.com/join/vhuhnaggmu-lowinglokjason
#****************************************************************

#############
#Question #1
#############

# Make a my city list with some of the interesting things to see. Pprint a series of statements about these items

city_elements = ['dense', 'high-rise buildings', 'crowded people']

# Print one statement for each item in your list using a fstring. Print the statements using the index position counting from the beginning, the middle, and end of the list.

print(f'Hong Kong is a {city_elements[0]} country with {city_elements[1]} and {city_elements[2]}.')

#############
#Question #2
#############

# Step 1: Make a list of the five people going on the mission (yourself included) 

team_members = ['Bairre', 'Kenta', 'Masego', 'Jana', 'Jason']

# Print out a message to each person letting them know they are going on the mission. Print a statement using len() and an fstring showing how many people are on the mission.

for name in team_members:
  print(f'Hello {name}, we are going to have mission and there are {len(team_members)} members, good luck!')

# Bairre is sick, John will replace Bairre 

team_members[0] = 'John'

# Print new messages to everyone on the team informing them of the mission and is now on the list. Print a statement using len() and an fstring showing how many people are now on the mission inside of a sentence

print(f'{team_members[0]} will replace one of our team members, there are now {len(team_members)} members in our mission.')

# Step 3:  Use insert() to add one celebrity to the beginning and middle of the list.

team_members.insert(0, 'Keanu Reeves')
team_members.insert(3, 'Ryan Reynolds')

# Use append() to add a celebrity to the end of the list.

team_members.append('Sung Kang')

# Print out a message to each person on the list letting them know about the mission. Print a statement using len() and an fstring showing how many people are now on the mission inside of a sentence.

for name in team_members:
  print(f'Hello {name}, we have three more celebrities going to have mission and there are {len(team_members)} members, good luck!')

# First print a message letting everyone know only two people will be able to go on the mission
  
for name in team_members:
  print(f'Hello {name}, unfortunately, our new vessel, the Little Ducky, only has room for two passengers and only two of us can go to the mission.')

# The use the pop() method to remove people one at a time from the list and print a message to them letting them know that they will not be able to attend the mission.

first_out = team_members.pop()
print(f'Sorry {first_out}! we are here to notify that you will not be able to attend the mission due to lack of vessl seats.')

Second_out = team_members.pop()
print(f'Sorry {Second_out}! we are here to notify that you will not be able to attend the mission due to lack of vessl seats.')

Third_out = team_members.pop()
print(f'Sorry {Third_out}! we are here to notify that you will not be able to attend the mission due to lack of vessl seats.')

Fourth_out = team_members.pop()
print(f'Sorry {Fourth_out}! we are here to notify that you will not be able to attend the mission due to lack of vessl seats.')

Fifth_out = team_members.pop()
print(f'Sorry {Fifth_out}! we are here to notify that you will not be able to attend the mission due to lack of vessl seats.')

Sixth_out = team_members.pop()
print(f'Sorry {Sixth_out}! we are here to notify that you will not be able to attend the mission due to lack of vessl seats.')

#Once the list is down to the final two people, print each of them a message letting them know they will be going on the mission. Its OK if you are not among the final two chosen to go on the mission. Print a statement using len() and an fstring showing how many people are now on the mission inside of a sentence.

for name in team_members:
  print(f'Congrats {name}! you have been selected to attend the mission and there are currently {len(team_members)} members on this mission.')

# In a final blow to your already shaky leadership, Priyanka Chopra calls and lets you know that your now downgraded mission has been canceled entirely. Use the del() method to delete everyone from the list and print the list to show it is empty. 

del team_members[0:2]
print(team_members)

# Print a statement using len() and an fstring showing how many people are now on the mission inside of a sentence.

print(f'Now, the member list has {len(team_members)} member.')

#############
#Question #3 
#############

# Think of five places anywhere on earth the event could be held and store them in a list. Print the list as you stored it

places = ['Japan', 'Columbia', 'England', 'Honduras', 'Brasil']
print(places)

# Print the list using sorted() without modifying the original list

print(sorted(places))

# Print the list as you stored it

print(places)

# Print the list using sorted() in reverse alphabetical order without modifying the original list

print(sorted(places, reverse = True))

# Print the list as you stored it

print(places)

# Print the list using reverse()

places.reverse()
print(places)

# Print the list using reverse() a second time to bring it back to its original form

places.reverse()
print(places)

# Print the list using sort() in alphabetical order

places.sort()
print(places)

# Print the list using sort() a second time to print the list in reverse alphabetical order

places.sort(reverse=True)
print(places)

#############
#Question #4
#############

# random package (import random at the top of the script)

import random

# Create five or more lists

colours = ['blue', 'yellow', 'grey', 'black', 'amber']
cars = ['Koesignegg', 'Pagani', 'McLaren', 'Bugatti', 'Hennessey']
places = ['Toronto', 'Manchester', 'Hong Kong', 'Sudbury', 'Brisbane']
foods = ['burrito', 'quesadilla', 'nachos', 'taco', 'fries']
pets = ['cat', 'owl', 'bunny', 'otter', 'gecko']

# write a story that uses random elements from the lists and random numbers using random.choice(list) and random.randint(1,5)

print(f"I love {random.choice(colours + cars + places + foods + pets)} so much and I hope I can live with it at least {random.randint(1, 5)} year(s).")

#############
#Question #5
#############

# Make a list of your student number

student_numbers = ["A", 0, 0, 2, 6, 8, 4, 1, 4]

# write a program that adds the numbers of your student number together using list index positions. Then, using the same list, print out your student number by converting numbers to strings as needed using an fstring.

sid = ''
for i in range(len(student_numbers)):
  sid += str(student_numbers[i])
print(sid) 

#############
#Question #6
#############

# Make a list called meals, and sub-lists with at least three items of foods for breakfast, lunch, and dinner. 

meals = [['oat', 'bread', 'milk'], ['egg', 'pasta', 'tomato'], ['rice', 'chicken', 'vegetable']]

# Print out the first and last item in each sub-list using an index position inside of a sentence using an fstring.

print(f'Breakfest: {meals[0][0]}, {meals[0][2]}; Lunch: {meals[1][0]}, {meals[1][2]}; Dinner: {meals[2][0]}, {meals[2][2]}')