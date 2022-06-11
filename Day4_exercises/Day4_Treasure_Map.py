# changing the place of a box with treasure
# the code is not dynamic and errors are not handled
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# needs fixing - code is long can be done in shorter way
# new_position = []
# for a in position:
#     if int(a) <= 3:
#         new_position.append(int(a))
# print(new_position)
#
# if new_position[0] == 1:
#     if new_position[1] == 1:
#         row1[0] = "🤯"
#     elif new_position[1] == 2:
#         row1[1] = "🤯"
#     elif new_position[1] == 3:
#         row1[2] = "🤯"
# if new_position[0] == 2:
#     if new_position[1] == 1:
#         row2[0] = "🤯"
#     elif new_position[1] == 2:
#         row2[1] = "🤯"
#     elif new_position[1] == 3:
#         row2[2] = "🤯"
# if new_position[0] == 3:
#     if new_position[1] == 1:
#         row3[0] = "🤯"
#     elif new_position[1] == 2:
#         row3[1] = "🤯"
#     elif new_position[1] == 3:
#         row3[2] = "🤯"
#

# the shorter version

vertical_position = int(position[0])-1
horizontal_position = int(position[1])-1
map[vertical_position] [horizontal_position] = "🤯"


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")