import csv


def get_repear_date(file_name):
    repear_date = {}
    with open(file_name, 'r') as f:
        undergr_date = list(csv.DictReader(f, delimiter = ';'))
    for element in undergr_date:
            if element['Ремонт эскалаторов'] and element['Станция метрополитена'] not in repear_date:
                repear_date[element['Станция метрополитена']] = element['Ремонт эскалаторов']
    return repear_date



if __name__ == "__main__":
    repear_date = get_repear_date('data-397-2017-04-21.csv')
    for station_name, date in repear_date.items():
        print ('{} - {}'.format(station_name, date))


{
	'city': 'Москва',
	'title': 'Премия МУЗтв',
	'date': {
		'from': 112312311,
		'to': 112312311,
	},
	'category': 'concert',
	'location': {
		'latitude': 55.31122,
		'longitude': 52.52121,
		'address': 'ул Горбушкина, 35',
	},
	'price_rub': {
		'from': 1000,
		'to': 15000,
	},
	'age_category': '12+',
	'description': '...',
	'rating': 3,  # 1...10
	'url': 'http://...'
}# парсить афишу и получать подобные данные
