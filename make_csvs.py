import csv

RE_counter = 0
event_counter = 0
new_results = []
duplicates_results = []
manual_check_results = []
master_records = []
totalmatches = 0


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
        if item["Email Number"].lower() == email.lower():
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

        

        if len(matches) > 0: #if the email address is already in RE
            totalmatches += len(matches)
            duplicates_results += matches
        else: # if the email address is not already in Raiser's Edge
            new_results.append(row)

    print totalmatches, len(new_results)

# Write the new records CSV
with open('new_records.csv', 'w') as csvfile:
    fieldnames = ['First Name','Last Name','Email Number','Mobile Number','Preferred Address Lines','Preferred City','Preferred State','Preferred ZIP']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for n in new_results:
        writer.writerow({'First Name': n['First Name'], 'Last Name': n['Last Name'], 'Email Number': n['Email'], 'Mobile Number': n['Cell Phone'], 'Preferred Address Lines': n['Home Address 1'] + n['Home Address 2'], 'Preferred City': n['Home City'], 'Preferred State': n['Home State'], 'Preferred ZIP': n['Home Zip'] })

print "{0} records checked from event list against {1} records in Raiser's Edge.".format(event_counter, RE_counter)