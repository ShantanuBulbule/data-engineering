import csv
from pathlib import Path

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
#print(memberinfo)
#print(memberPaidInfo)

def is_full_name(row):
    return bool(row['firstName']) and bool(row['lastName'])

def build_full_name(row):
    return f"{row['firstName'].strip()} {row['lastName'].strip()}"

def names_match(constructed_name, paid_name):
    constructed_normalized = constructed_name.lower().strip()
    paid_normalized = paid_name.lower().strip()
    return constructed_normalized == paid_normalized

#memberinfo = list(filter(is_full_name, memberinfo))
#print(memberinfo)


#memberinfo = list(map(build_full_name, memberinfo))
#print(memberinfo)
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

#print(process_records(memberinfo, memberPaidInfo))