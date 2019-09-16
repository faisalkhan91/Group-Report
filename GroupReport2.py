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

    group, group_id, guser_id = pdata.split(':')
    user, user_id, primary_group = pdata2.split(':')

    return group, group_id, guser_id, user, user_id, primary_group


#############################################################################################

# Main Program


data, data2 = get_file()
group, group_id, guser_id, user, user_id, primary_group = process_data(data, data2)
print(group, group_id, guser_id, user, user_id, primary_group)



#############################################################################################
#                                       End of Program                                      #
#                                       Copyright 2019                                      #
#############################################################################################
