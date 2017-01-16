import csv

RE_counter = 0
event_counter = 0
new_results = []
duplicates_results = []
manual_check_results = []

# Open Raiser's Edge list and save in memory
with open('RE_list.csv', 'rb') as master:
    master_indices = dict((r[1], i) for i, r in enumerate(csv.reader(master)))
print str(len(master_indices)) + " records in RE list."


# Open event list and compare to RE
with open('rootscamp_list.csv','rb') as rootscamp:
    reader = csv.DictReader(rootscamp)

    for row in reader:
        event_counter +=1
        #if the email address is in master indices:
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


print str(event_counter) + " records checked from event list."