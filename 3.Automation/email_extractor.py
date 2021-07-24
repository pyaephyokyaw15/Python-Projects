'''

Email Extractor
================
- This script extract email and phone from a long text.

Instruction
============
- First, you copy the text on the web on clipboard.
- Then, run the script.
- The script will extract email from the text and copy on clip board 
    automatically.
- You can paste the result wherever you want.


'''
# pip install pyperclip

import pyperclip
import re


# Create email regex.
emailRegex = re.compile('''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    )''', re.VERBOSE)

# get text on clip board
text = str(pyperclip.paste())

# create emial lists
emails= []


for email in emailRegex.findall(text):
    emails.append(email)

# Copy results to the clipboard.
if len(emails) > 0:
    pyperclip.copy('\n'.join(emails))
    print('Copied to clipboard:')
    print('\n'.join(emails))
else:
    print('No email addresses found.')
