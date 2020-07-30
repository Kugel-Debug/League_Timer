import requests


def requisiçãosummonerv4(regiao, Nome, Key):
    URLsummoner = requests.get(f"https://{regiao}.api.riotgames.com/lol/summoner/v4"
                               f"/summoners/by-name/{Nome}?api_key={Key}").json()
    return URLsummoner

def requisiçãospectator(regiao, summonerId, Key):
    URLspecatator = requests.get(f'https://{regiao}.api.riotgames.com/lol/spectator/v4'
                                 f'/active-games/by-summoner/{summonerId}?api_key={Key}').json()
    return URLspecatator

def requisiçãoversao():
    versao = requests.get('https://ddragon.leagueoflegends.com/api/versions.json').json()[0]
    return versao

def requisiçãokeytochampion():
    datadragon = requests.get('http://ddragon.leagueoflegends.com/cdn/{}/data/en_US/champion.json'.format(requisiçãoversao())).json()

    champions = {}
    for champion in datadragon["data"]:
        key = int(datadragon["data"][champion]["key"])
        champions[key] = champion
    return champions

def championId_to_name(id: int):
    champions = requisiçãokeytochampion()
    return champions[id]


