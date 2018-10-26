tags=['App', 'Website', 'Web app']

ziel=['app', 'website', 'web_app']

temp=[]

for tag in tags:
    new_tag = tag.replace(" ", '_', -1)
    temp.append(new_tag)

for tag in temp:
    print('new_tag: ', tag)
    