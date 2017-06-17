import csv, math
station_x_y = {}
compare = 1
def test_under(file_name, x = None, y = None):
    db = {}
    with open(file_name, 'r') as f:
        reader = csv.DictReader(f, delimiter = ';')
        for row in reader:
            y_station = float(row['Долгота в WGS-84'])
            x_station = float(row['Широта в WGS-84'])
            if row['Станция метрополитена'] not in db:
                db[row['Станция метрополитена']] = [x_station, y_station]
    return(db)
#    for k, v in db.items():
#        print(k, v)

def test_ground(file_name, data_base):
    count = {}
    with open(file_name, 'r') as f:
        reader = csv.DictReader(f, delimiter = ';')
        for row in reader:
            x_bus = float(row['Latitude_WGS84'])
            y_bus = float(row['Longitude_WGS84'])
            for k, v in data_base.items():
                if math.fabs(x_bus - v[0]) < 0.008 and math.fabs(y_bus - v[1]) < 0.008:
                    if k in count:
                        count[k] += 1
                    else:
                        count[k] = 1
    return (count)


station_x_y = test_under('data-397-2017-04-21.csv')
station_count = test_ground('data-398-2017-06-05.csv', station_x_y)
for k, v in station_count.items():
    if v > compare:
        compare = v
for k, v in station_count.items():
    if v == compare:
        print(k, v)
