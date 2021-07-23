'''

DNA

- This script identifies a person based on their DNA.

- It is also the assignment project of CS50x(2020).

- Project Details:
    https://cs50.harvard.edu/x/2021/psets/6/dna/

- Run from terminal with three arguements.
    Example: python dna.py data.csv sequence.txt
    
'''


import csv
from sys import argv

# make sure that three command line input
if len(argv) != 3:
    print('Usage: python dna.py data.csv sequence.txt')
    exit(1)
    
# open DNA file(.txt) and store in DNA
with open(argv[2]) as txt_file:
    DNA = txt_file.read()
    
 

# open persons' DNA(.csv) and take first row ( name of STRs) and store in srts 
# So, use csv.reader()  instead of csv.dictReader()
# To remove name and take only STRs , pop(0)

with open(argv[1]) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            srts = row
            srts.pop(0)
            break

# initialize dict to store STRs
sequences = {}   

# assign dictionary key and values according to SRTs
for srt in srts:
    sequences[srt] = 0

# print result sequence
# print(sequences)

# iterate through each STR and take the longest count in each STR
for STR in sequences:

    max_count = 0
    temp = 0
    l = len(STR)

    for i in range(len(DNA)):
        
        # if found STR
        if DNA[i: i + l] == STR:
            temp = 1
            
            # Once found STR , check the next sequence 
            while DNA[i-l : i] == DNA[i : i+l]:

                # to find max STR chain, temporarily store in temp
                temp +=1
                i += l

            # finding max_count
            if temp > max_count:
                max_count = temp
            
            # reset temp 
            temp = 0
        
    # assigni max_count to dictionary
    sequences[STR] = str(max_count)

# printing sequences ( dictionary )
# print(sequences)


# Comparing with STR of each person in csv file
with open(argv[1]) as csvfile:

    # To read csv and get dictionary type , use csv.DictReader
    persons = csv.DictReader(csvfile)

    # iterate each person
    for person in persons:

        # To compare two dictionary , name must be removed.
        # So copy the originary dictionary 
        # If use '=' , it may effect original dictionary    
        person_without_name = person.copy()
        # removing name
        person_without_name.pop('name')
        # Comparing dictionary
        if sequences == person_without_name:
            # if exact STRs is found, print name and exit the program
            print(person['name'])
            exit(0)
    
    # if not found in persons ( .csv )
    print('No match')


        
      




