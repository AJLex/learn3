import csv, collections


def get_max_station(file_name, ignoring_street):
    cnt = collections.Counter()
    cnt_list = []
    with open(file_name, 'r') as f:
        station_date = list(csv.DictReader(f, delimiter=';')) #помещаем исходный файл в переменную вида - [{}, {}, ...]
    for element in station_date:                      # проходим по улементам переменной station_base
        if element['Street'] != ignoring_street:      # 1 элемент - 1 словарь, если в словаре по ключу Street
            cnt[element['Street']] +=1                #  выдаётся значение - ignoring_street, то не учитываем этот эелемент
    return cnt.most_common(1)                         #  делам подсчёт числа упоминаний улиц и возвращаем самое большое число


if __name__ == '__main__':
    print(get_max_station('data-398-2017-06-05.csv', 'проезд без названия'))
