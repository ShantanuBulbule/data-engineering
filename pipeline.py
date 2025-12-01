import csv
from pathlib import Path

#Loads the csv file and returns the data as a list of dictionaries
def load_csv(filepath):
    data = []
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        # maps the column names 
        for row in reader:
            data.append(row)
    return data

memberinfo = load_csv('data/input/memberinfo.csv')
memberPaidInfo = load_csv('data/input/memberpaidinfo.csv')

#Checks if the first name and last name are not empty
def is_full_name(row):
    return bool(row['firstName']) and bool(row['lastName'])

#Builds the full name from the first name and last name
def build_full_name(row):
    return f"{row['firstName'].strip()} {row['lastName'].strip()}"

#Checks if the constructed name matches the paid name
def names_match(constructed_name, paid_name):
    constructed_normalized = constructed_name.lower().strip()
    paid_normalized = paid_name.lower().strip()
    return constructed_normalized == paid_normalized

#Processes the records by first checking if the memberId exists in the memberinfo
#Then checks if the first name and last name are not empty
#Then checks if the constructed name matches the paid name
def process_records(memberinfo, memberPaidInfo):
    memberinfoDict = {row['memberId']: row for row in memberinfo}
    valid_records = []
    for paid in memberPaidInfo:
        memberId = paid['memberId']
    
        if memberId not in memberinfoDict:
            continue
        infoRow = memberinfoDict[memberId]

        if not is_full_name(infoRow):
            continue
        constructedName = build_full_name(infoRow)
        paidName = paid['fullName'].strip()
        if paidName:
            if not names_match(constructedName, paidName):
                continue
        valid_records.append({
            'memberId': memberId,
            'fullName': constructedName,
            'paidAmount': paid['paidAmount']
        })
    return valid_records

#Generates the report by printing the total records, highest amount paid, and highest paid member information
def generate_report(valid_records):
    print("Records Summary:")
    if len(valid_records) == 0:
        print("No valid records found.")
        return
    print("="*60)
    print(f"Total records: {len(valid_records)}")
    print(f"Highest amount paid: {max(float(record['paidAmount']) for record in valid_records)}")
    print("\n" + "="*60)
    print("Highest paid member information:")
    highestPaidMember = max(valid_records, key=lambda record: float(record['paidAmount']))
    print("Member ID: " + highestPaidMember['memberId'])
    print("Name: " + highestPaidMember['fullName'])
    print("Paid Amount: " + highestPaidMember['paidAmount'])
    print("\n" + "="*60)
    print(f"Total amount paid: {sum(float(record['paidAmount']) for record in valid_records)}")
    print("="*60)


#Generates the csv file by writing the valid records to the csv file
def generate_csv(valid_records):
    with open('data/output/cleaned_members.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['memberId', 'fullName', 'paidAmount'])
        writer.writeheader()
        writer.writerows(valid_records)

#Generates the report and csv file
generate_report(process_records(memberinfo, memberPaidInfo))
generate_csv(process_records(memberinfo, memberPaidInfo))
