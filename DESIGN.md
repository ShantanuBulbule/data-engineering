Design Choices:
1. Data was loaded using the csv module to read the csv files.
2. The data was processed using a dictionary to store the member information and then was processed to generate the report.
3. A dictionary was used to store the member information to avoid multiple lookups and to improve performance because of its O(1) average time complexity for lookups.
4. The report was generated using print statements and the csv module to write the csv file.
5. The code was written in a way that it can be easily extended to handle more datasets and more complex transformations due to the modular functions.
6. String normalization was used to ensure that the names were compared in a case-insensitive manner. .strip() was used to remove leading and trailing whitespace.
7. Error handling was implemented to skip invalid records and continue processing rather than failing on the first invalid record.

Architecture:
1. Load Data: Read both CSV files and store the data in memory.
2. Validate and Clean Data: Validate the data and clean it if necessary so that it only considers data that has an entry in memberInfo and the first name and last name are not empty.
3. Transform Data: Build the full name from the first name and last name and check if the constructed name matches the paid name.
4. Report and Output: Generate the report and output the results to a CSV file.

Data Quality Issues Found:
1. Missing Names: Some memberInfo records had empty firstname/lastName fields.
2. Oprhaned Records: memberPaidInfo records had a memberId that did not exist in memberInfo.
3. Name Conflicts: memberPaidInfo fullName sometimes differed from the constructed name from memberInfo firstName and lastName.

Validation Rules to abide by:
Rule 1: Only include if memberId exists in both datasets.
Rule 2: memberInfo mush have complete (non-empty) names.
Rule 3: memberPaidInfo fullName must match the constructed name from memberInfo firstName and lastName.

