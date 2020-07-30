import requests
import Apilol04
# Aqui eu coloco a key q eu consigo no site da riot dev
Key = 'RGAPI-6b0fed70-427a-4982-879f-6416ba7d6cb1'
regiao = 'BR1'

def aplicativo(Nome):

    try:
        jsonsummoner = Apilol04.requisiçãosummonerv4(regiao, Nome, Key)
        # apartir daqui eu consigo acessar o conteudo do json como um dicionario na variavel
        Level = jsonsummoner['summonerLevel']
        summonerId = jsonsummoner['id']
        ContaID = jsonsummoner['accountId']

    except:
        print('jogador não encontrado')

    else:
        try:
            jsonspectator = Apilol04.requisiçãospectator(regiao, summonerId, Key)['participants']


            def requisiçãocampeoespartida():
                Championmatch = []

                for playerfinder in range(0, 10):
                    playerIdfinder = (jsonspectator[playerfinder]["summonerId"])
                    if playerIdfinder == summonerId:
                        playerposition = playerfinder

                if playerposition < 5:
                    for p in range(5, 10):
                        Championmatch.append(jsonspectator[p]['championId'])
                else:
                    for p in range(0, 5):
                        Championmatch.append(jsonspectator[p]['championId'])
                return Championmatch


            Championmatch = requisiçãocampeoespartida()

            def championskeysmatchtoname():
                championname = []
                for keytoname in range(len(Championmatch)):
                    championname.append(Apilol04.championId_to_name(Championmatch[keytoname]))
                return championname

            print(championskeysmatchtoname())

            def appspell():

                spells = {21: "SummonerBarrier", 1: 'SummonerBoost', 14: 'SummonerDot',
                          3: 'SummonerExhaust', 4: 'SummonerFlash', 6: 'SummonerHaste',
                          7: 'SummonerHeal', 13: 'SummonerMana', 30: 'SummonerPoroRecall',
                          31: 'SummonerPoroThrow', 11: 'SummonerSmite', 39: 'SummonerSnowURFSnowball_Mark',
                          32: 'SummonerSnowball', 12: 'SummonerTeleport'}

                def spellId_to_name(id: int):
                    spellfromkey = spells
                    return spellfromkey[id]

                jsonspectator = Apilol04.requisiçãospectator(regiao, summonerId, Key)['participants']

                def requisiçãospellpartida():
                    spell1 = []

                    for playerfinder in range(0, 10):
                        playerIdfinder = (jsonspectator[playerfinder]["summonerId"])
                        if playerIdfinder == summonerId:
                            playerposition = playerfinder

                    if playerposition < 5:
                        for p in range(5, 10):
                            spell1.append(jsonspectator[p]["spell1Id"])
                            spell1.append(jsonspectator[p]["spell2Id"])
                    else:
                        for p in range(0, 5):
                            spell1.append(jsonspectator[p]["spell1Id"])
                            spell1.append(jsonspectator[p]["spell2Id"])

                    return spell1

                spellspartida = requisiçãospellpartida()

                def spellkeysmatchtoname():
                    spells = []
                    for keytoname in range(len(spellspartida)):
                        spells.append(spellId_to_name(spellspartida[keytoname]))
                    return spells

                return spellkeysmatchtoname()

            spells21 = appspell()
            def spelltime5():
                versao = requests.get('https://ddragon.leagueoflegends.com/api/versions.json').json()[0]
                cdsspells = []
                for quant in range(0, 10):
                    spellCD = requests.get(
                        f'http://ddragon.leagueoflegends.com/cdn/{versao}/data/en_US/summoner.json').json()
                    cdsspells.append(spellCD['data'][spells21[quant]]['cooldown'])

                return cdsspells





            return championskeysmatchtoname(), spells21, spelltime5()
        except:
            print('O jogador não esta em uma partida ativa')

