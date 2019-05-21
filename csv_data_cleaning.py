import csv

list_text = []
list_receivedat = []
list_groupname = []

with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            if( len(row[0]) > 39):

                if (row[0][38:41] == 'and'):
                    text1 = row[0][0:38]
                    text2 = row[0][0:21] + " " + row[0][42:57]
                    list_text.append(text1)
                    list_receivedat.append(row[1])
                    list_groupname.append(row[2])
                    list_text.append(text2)
                    list_receivedat.append(row[1])
                    list_groupname.append(row[2])

            else:
                list_text.append(row[0])
                list_receivedat.append(row[1])
                list_groupname.append(row[2])

        line_count += 1

with open('updated_data.csv', mode='w') as csv_file:
    fieldnames = ['text', 'receivedat', 'groupname']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(0, len(list_text)):
        writer.writerow({'text': list_text[i], 'receivedat':list_receivedat[i], 'groupname' :list_groupname[i] })

print(f'Processed {line_count} lines.')
