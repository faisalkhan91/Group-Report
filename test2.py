#!/usr/bin/python3

#############################################################################################
#                               Program by Mohammed Faisal Khan                             #
#                               00598949                                                    #
#                               mkhan8@unh.newhaven.edu                                     #
#############################################################################################

import sys

# Function Definitions


def get_file(filename=""):

    if not filename:
        filename = input("Please enter name of data file: ")
#    elif filename != "users.txt" or "groups.txt" :
#        filename = input("File not recognized. Please enter a user and a group file: ")

    file = open(filename, "r", encoding="utf8")
    data = file.readlines()
    file.close()

    return data


def separate(p2data, p2count):

    if p2count == 2:
            group, group_id, guser_id = p2data.split(':')
            guser_id = str(guser_id.split('\n\,n'))
            return group, group_id, guser_id

    elif p2count == 1:
        user, user_id, primary_group = p2data.split(':')
        return user, user_id, primary_group


def process_data(pdata, pcount):

    user_dict = {}
    group_dict = {}

    if pcount == 1:
        user, user_id, primary_group = separate(pdata, pcount)
        user_dict[user_id] = user
        return user_dict, user_id, primary_group

    elif pcount == 2:
        group, group_id, guser_id = separate(pdata, pcount)
        group_dict[group_id] = group
        return group_dict, group_id, guser_id


def get_primary(primary_group, group_dict):
    primary_dict = {}
    for primary in primary_group :
        temp = group_dict.get(primary)
        primary_dict[primary] = temp
        print(primary_dict[primary])

    return list(primary_dict)


def get_secondary(group_dict, guser_id):
    secondary_dict = {}

    for group in guser_id:
        try:
            secondary_dict[group] = group_dict[group]
            print(secondary_dict[group])
        except:
            print("Some Error")

    return list(secondary_dict)


#############################################################################################

# Main Program

count = 0

user_dict2 = {}
user_id2 = []
primary_group2 = []
group_dict2 = {}
group_id2 = []
guser_id2 = []

print("###USER##########PRIMARY###########SECONDARY###########")

files = [1, 2]

for file in files:
    data = get_file(sys.argv[file])
    count += 1

    for line in data:
        if count == 1:
            user_dict, user_id, primary_group = process_data(line, count)
            user_dict2.update(user_dict)
            user_id2.append(user_id)
            primary_group2.append(user_id)
        else:
            group_dict, group_id, guser_id = process_data(line, count)
            group_dict2.update(group_dict)
            group_id2.append(group_id)
            guser_id2.append(guser_id)

#primary = get_primary(primary_group2, group_dict2)
#secondary = get_secondary(group_dict2, guser_id2)

for user_id, user in user_dict2.items():
    try:
        print("User: ", user_dict2[user_id], "   Primary: ", group_dict2[user_id], "   Secondary: ", guser_id2[int(user_id)])
    except:
        print("User: ", user_dict2[user_id], "   Primary:    Key Error ", "   Secondary:    Key Error ")

#############################################################################################
#                                       End of Program                                      #
#############################################################################################
