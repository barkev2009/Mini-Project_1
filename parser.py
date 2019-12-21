from bs4 import BeautifulSoup
from urllib.request import urlopen

model_list = []
k = 0
for i in range(43):
    k += 1
    url = "https://www.e-katalog.ru/ek-list.php?katalog_=298&page_={}".format(i)
    html = urlopen(url)
    tables = BeautifulSoup(html.read(), 'html.parser').find_all('table', {'class': 'model-short-block'})
    print('Page {}'.format(k))
    for table in tables:
        model = table.find('td', {'class': 'model-conf-title'}).find('a').attrs['href']
        model_list.append(model)

sub_list = []
for model in model_list:
    url = 'https://www.e-katalog.ru' + model
    html = urlopen(url)
    mod_bs = BeautifulSoup(html.read(), 'html.parser')
    try:
        submodels = mod_bs.find('table', {'class': 'conf-table'}).find_all('a', {'class': 'conf-name'})
        for sub in submodels:
            print(sub.attrs['href'], model, sep=' | ')
            sub_list.append(sub.attrs['href'])
    except AttributeError:
        print(model)
        sub_list.append(model)
