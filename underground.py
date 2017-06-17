import csv

def get_repear_date(file_name):
    with open(file_name, 'r') as f:
        repear_date = {}
        reader = csv.DictReader(f, delimiter = ';')
        for row in reader:
            if row['Ремонт эскалаторов']:
                if row['Станция метрополитена'] not in repear_date:
                    repear_date[row['Станция метрополитена']] = row['Ремонт эскалаторов']
    for k, v in repear_date.items():
        print('{} - {}'.format(k, v))

get_repear_date('data-397-2017-04-21.csv')
