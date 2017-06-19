import csv, math, collections


def get_undergr_coords(file_name):
    db = {}
    with open(file_name, 'r') as f:
        undergr_date = list(csv.DictReader(f, delimiter = ';'))
    for element in undergr_date:
        y_station = float(element['Долгота в WGS-84'])
        x_station = float(element['Широта в WGS-84'])
        if element['Станция метрополитена'] not in db:
            db[element['Станция метрополитена']] = (x_station, y_station)
    return db
#    for k, v in db.items():
#        print(k, v)

def get_ground_count(file_name, data_base, radius):
    cnt = collections.Counter()
    with open(file_name, 'r') as f:
        grount_date = list(csv.DictReader(f, delimiter = ';'))
    for element in grount_date:
        x_bus = float(element['Latitude_WGS84'])
        y_bus = float(element['Longitude_WGS84'])
        for staton_name, coords in data_base.items():
            if math.fabs(x_bus - coords[0]) < radius and math.fabs(y_bus - coords[1]) < radius:
                cnt[staton_name] += 1
    return cnt.most_common(1)


if __name__ == '__main__':
    station_x_y = get_undergr_coords('data-397-2017-04-21.csv')
    print(get_ground_count('data-398-2017-06-05.csv', station_x_y, 0.008))
