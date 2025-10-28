from pathlib import Path
import re

file_path = Path('D:/Prabi Thapa/learning/automate')

email_list = []
num_list = []

for file in file_path.glob('*.txt'):
    with open(file, 'r') as fr:
        content = fr.read()
    
    email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    match_email = email_pattern.findall(content)
    
    for email in match_email:
        email_list.append(email)
        
    num_pattern = re.compile(r'(?:98|97)\d{8}')
    match_num = num_pattern.findall(content)
    
    for num in match_num:
        num_list.append(num)

# print(email_list)
# print(num_list)        

file_name = Path('result.txt')
if not file_name.exists():
    with open(file_name, 'w') as cf:
        cf.write('Phone numbers are: \n')
        for numbers in num_list:
            cf.write(f'{numbers}\n')
            
        cf.write('Email address are: \n')
        for email in email_list:
            cf.write(f'{email}\n')
