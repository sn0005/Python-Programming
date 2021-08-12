#Project: Phone Number and Email Address Extractor

import re
from pprint import pprint


phoneRegex = re.compile(r'''(
 (\+\d{2}|\(\d{4}\)|\d{4})?
 (\s|-|\.)?
 (\d{2}|\d{3}|\d{4}|\d{9})
 (\s|-|\.)?
 (\d{3}|\d{4}|\d{5})
 (\s|-|\.)?
 (\d{4}|\d{2}|\d{3})
 )''', re.VERBOSE)

mailRegex = re.compile(r'''(
 [\w\.\+-]+
 @
 [\w\.\+-]+
)''', re.VERBOSE)

ListofEmailandPhoneNumbers = []

path = input('Filepath? ')

def emailandphoneExtractor():
    
    with open(path, 'r') as filename:
     Lines = filename.readlines()
    
     for line in Lines:
        mail_id = mailRegex.search(line)
        phonenum = phoneRegex.search(line)
        if mail_id:
           mail = mail_id.group() 
        else:
           mail = 'NA'
        if phonenum:
           num = phonenum.group()
        else:
           num = 'NA'
        cap = [mail,num]
        if cap[0] == 'NA' and cap[1] == 'NA':
            pass
        else:
            ListofEmailandPhoneNumbers.append(cap)
    print('List of email ids and phone numbers received','\n')
    pprint(ListofEmailandPhoneNumbers)

emailandphoneExtractor()

file = open('F:\py_codes\EmailPhone.txt', 'w+')
pprint(ListofEmailandPhoneNumbers, file)
file.close()

print('-'*50)

def DA():
    Onlyphonenumbers = 0
    Onlyemailids = 0
    Both = 0
    for List in ListofEmailandPhoneNumbers:
        if List[0]=='NA':
         Onlyphonenumbers +=1
        elif List[1]=='NA':
         Onlyemailids +=1
        else:
         Both += 1
         
    print(f'{Both} people given both email id and phone number')
    print(f'{Onlyemailids} people given only email ids')
    print(f'{Onlyphonenumbers} people given only phone number')
    
DA()

#F:\py_codes\project_file.txt