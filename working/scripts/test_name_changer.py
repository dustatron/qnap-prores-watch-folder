import os
import re

test_string = 'a Valid |||||String|123--__.txt'
#
# line = re.sub('[!@#$|?]', '', test_string)
#
#
# space_to_dash = line.replace(' ', '-').lower()
#
# # artistName = ''.join(e for e in line if e.isalnum() or e == '-')
#
#
#
# print(space_to_dash)

# print(bool(re.match("^[A-Za-z0-9_-]*$", test_string)))
# print(bool(re.match("^[A-Za-z0-9_-]*$", 'inv@lid')))


def cleanString(file_name):

    file_name_no_extention = os.path.splitext(file_name)
    remove_bad_characters = re.sub('[!@#$|?]', '', file_name_no_extention[0])
    spaces_to_dashs = remove_bad_characters.replace(' ', '-').lower()

    # needs_cleaning = just_the_name[0]
    # cleaned = "".join(i for i in needs_cleaning if i not in "\/:*?<>|")
    return spaces_to_dashs

print(cleanString(test_string))
