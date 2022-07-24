import csv


def process_row(row, f):
    result = row[:13]
    test1 = 0

    for i in range(13,25):
        test1 += int(row[i])

    for i in range(25, 31):
        test1 += int(row[i]) * 1.5

    for i in range(31, 39):
        test1 += int(row[i]) * 2

    result.append(str(test1))
    f.write(";".join(result) + "\n")


f = open('results.csv', 'w')

results = []

with open('data.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    reader = [i for i in reader]
    #for i, name in enumerate(reader[0]):
    #    print(i, name)

    for i, row in enumerate(reader):
        if i == 0:
            tmp = row[:13]
            tmp.append("Test1")
            f.write(";".join(tmp) + "\n")
            continue

        process_row(row, f)


f.close()