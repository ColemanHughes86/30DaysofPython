
text = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print(text)

text = 'Coding' + ' ' + 'For' + ' ' + 'All'
print(text)


company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[7:])

sub_string = 'Coding'
print(company.index(sub_string))
print(company.replace('Coding', 'Python'))
company2 = 'Python For Everyone'
print(company2.replace('Everyone', 'All'))
print(company.split('  '))
print('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(','))
print(company[0])
print(company[-1])
print(company[10])
acronym = "".join(word[0].upper() for word in company.split())
print(acronym)
print(company.index('C'))
print(company.index('F'))
print(company.rfind('l'))
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
print(sentence.rindex('because'))
print(sentence[0:31] + sentence[55:])
print(company.startswith('Coding'))
print(company.endswith('Coding'))
print(' # '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))
print('I am enjoying this challienge \nI just wonder what is next.')
print("Name\tAge\tCountry\tCity\nColeman\t15\tAmerica\tLawrenceburg")
radius = 10
area = 3.14 * radius **2 
print(f"The area of a circle with the radius {radius} is {area} meters squared.")
a = 8
b = 6
print(f'{a}+{b} = {a+b}')
print(f'{a}-{b} = {a-b}')
print(f'{a}*{b} = {a*b}')
print(f'{a}/{b} = {a/b}')
print(f'{a}%{b} = {a%b}')
print(f'{a}//{b} = {a//b}')
print(f'{a}**{b} = {a**b}')