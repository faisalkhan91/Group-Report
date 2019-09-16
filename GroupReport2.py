#!/usr/bin/python3

#############################################################################################
#                               Program by Mohammed Faisal Khan                             #
#                               Email: faisalkhan91@outlook.com                             #
#                               Date: 09/15/2019                                            #
#############################################################################################

# Importing system module

import sys

# Function Definitions


def get_file():

    default = ["groups.txt", "users.txt"]
    # groups = input("Please enter name of the file containing user groups: ")
    # users = input("Please enter name of the file containing users: ")

    groups = default[0]
    users = default[1]

    if groups != "groups.txt" or users != "users.txt":
        print("File not recognized. Please enter a user or a group file. Retry program! ")
        exit(1)

    file = open(groups, "r", encoding="utf8")
    file2 = open(users, "r", encoding="utf8")

    content = file.readlines()
    content2 = file2.readlines()

    stripped_content = [s.rstrip() for s in content]
    stripped_content2 = [s.rstrip() for s in content2]

    file.close()
    file2.close()

    return stripped_content, stripped_content2


def process_data(pdata, pdata2):

    group = {}
    guser_id = {}
    user = {}
    primary_group = {}

    for line in pdata:
        tmp_group, tmp_group_id, tmp_guser_id = line.split(':')
        group[tmp_group_id] = tmp_group
        guser_id[tmp_group_id] = tmp_guser_id

    for line in pdata2:
        tmp_user, tmp_user_id, tmp_primary_group = line.split(':')
        user[tmp_user] = tmp_user_id
        primary_group[tmp_user_id] = tmp_primary_group

    return group, guser_id, user, primary_group


#############################################################################################

# Main Program


data, data2 = get_file()
group, guser_id, user, primary_group = process_data(data, data2)
# print(group)
# print(guser_id)
# print(user)
# print(primary_group)

print("### USER ########## USER_ID ########### PRIMARY_GROUP ###########")
for user, user_id in user.items():
    print(user, "                 ", user_id, "              ", group[primary_group[user_id]])

#############################################################################################
#                                       End of Program                                      #
#                                       Copyright 2019                                      #
#############################################################################################
