
import re
# Phone number validation
print('-----------Phone number validation---------')
numb = input('Import txt: ')
if len(numb) < 1:
    name = "phone_numbers.txt"

handle = open(name)

for line in handle:
    match = re.findall(r'\(\+380\)[\d]{2}-[\d]{3}-[\d]{2}-[\d]{2}.+', line)
    print(match)

print('----------Find and delete space in string----------')
# Find and delete space in string\
incorrect_content = "Я хочу  бути     програмістом"
print(incorrect_content)
correct_content = re.sub(r" +"," ",incorrect_content)
print(correct_content)

# Extract text from html
print('-----------Extract text from html--------------')

html_file = input('Import html:')
if len(html_file) < 1:
    html_name = "html_t.html"

open_html = open(html_name)
pattern = r'<[^>]+>'
for i in open_html:
    replace_html = re.sub(pattern, '',i)
    print(replace_html)








