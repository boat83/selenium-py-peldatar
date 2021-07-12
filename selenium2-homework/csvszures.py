import csv

with open("table_in.csv", "r", encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for line in reader:
        with open("table_new.txt", "a", encoding='utf-8') as f:
            name = line[0]
            email = line[1]
            f.write(f'{email},{name}\n')




