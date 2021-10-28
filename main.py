from pprint import pprint
import requests


def keywithmaxval(d):
    v = list(d.values())
    k = list(d.keys())
    result = k[v.index(max(v))]
    return result

def best_superhero(names, criterion):
    superheros = {}
    for name in names:
        url = 'https://superheroapi.com/api/2619421814940190/search/' + name
        response = requests.get(url)
        # pprint(response.json())
        results = response.json()['results']
        # pprint(results[0])
        if results[0].get('name') == name:
            superheros.update({name: int(results[0]['powerstats'][criterion])})
    # print(superheros)
    best_hero_name = keywithmaxval(superheros)
    return best_hero_name



if __name__ == '__main__':
    names = ['Hulk', 'Captain America', 'Thanos']
    print(best_superhero(names, 'intelligence'))