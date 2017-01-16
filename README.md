Custome Dedupe
==============

Used to customize de-duplication when merging event registration lists into Raiser's Edge

Makes use of the standard Python csv module and DictReader to compare two CSVs.

Inputs:
- CSV from event file (see script comments for field names )
- Master CSV from Raiser's Edge with: First Name, Last Name, Email Number, Preferred Address, and Preferred Zip

Outputs:
- One csv file with new person records
- One csv file with duplicate people (for adding attendance data to existing records in RE)
- One csv file with potential duplicates for manual checking
