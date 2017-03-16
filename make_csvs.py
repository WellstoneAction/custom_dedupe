import csv

RE_counter = 0
event_counter = 0
new_results = []
duplicates_results = []
manual_check_results = []
master_records = []


'''
RE schema
=========
First Name,Last Name,Email Number,Mobile Number,Preferred Address Lines,Preferred City,Preferred State,Preferred ZIP


Rootscamp schema from Eventbrite
================================
First Name,Last Name,Email,Home Address 1,Home Address 2,Home City,Home State,Home Zip,Home Country,Cell Phone,What are your preferred gender pronouns?,Which pronouns do you prefer?,Are you a first time RootsCamper?,Company,Website,,
'''

# Function for searching by email
def search_master_by_email(email):
    results = []
    for item in master_records:
        if item["Email Number"] == email:
            results.append(item)
    return results


# Open Raiser's Edge list and save in memory
with open('RE_list.csv', 'rb') as master:
    re_reader = csv.DictReader(master)
    for line in re_reader:
        RE_counter += 1
        master_records.append(line)


# Open event list and compare to RE
with open('rootscamp_list.csv','rb') as rootscamp:
    rootscamp_reader = csv.DictReader(rootscamp)

    # Move through each row in the event file and check if the email address is already present. 
    for row in rootscamp_reader:
        event_counter +=1
        matches = search_master_by_email(row["Email"])

        #if the email address is already in Raiser's Edge, add the record to the duplicates csv:
        if len(matches) > 0:
            duplicates_results += matches

        # if the email address is not already in Raiser's Edge
        else:
            pass
            # Check if the first and last name are already in RE

        #    if the row with the email address matched last name or first name:
        #       duplicates_results.append(row)
        #    else:
        #       manual_check_results.append(row)
        #elif the last name is in master indices:
        #    if the row with the matching last name also matches first name:
        #       duplicates_results.append(row)
        #    elif the row with the matching last name also matches state:
        #       manual_check_results.append(row)
        #else:
        #    new_results.append(row)


# Write the CSVs


print "{0} records checked from event list against {1} records in Raiser's Edge.".format(event_counter, RE_counter)