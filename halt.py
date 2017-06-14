import csv

def get_max_station(file_name):
    station_name_count = {}
    unknown = {}
    compare = 1
    compare_unknown = 1
    with open(file_name, 'r') as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            if row['Street'] in station_name_count:
                station_name_count[row['Street']] += 1
            elif row['Street'] == 'проезд без названия':
                if row['District'] in unknown:
                    unknown[row['District']] += 1
                else:
                    unknown[row['District']] = 1
            else:
                station_name_count[row['Street']] = 1

    for k, v in station_name_count.items():
        if v > compare:
            compare = v
    for k, v in unknown.items():
        if v > compare_unknown:
            compare_unknown = v
    if compare > compare_unknown:
        for k, v in station_name_count.items():
            if v == compare:
                print(k, v)
    else:
        for k, v in unknown.items():
            if v == compare_unknown:
                print(k, v)

get_max_station('data-398-2017-06-05.csv')
