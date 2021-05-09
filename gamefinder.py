import requests
import json
from igdb.wrapper import IGDBWrapper
from datetime import datetime
from pytz import timezone

r = requests.post('https://id.twitch.tv/oauth2/token', params={
    'grant_type':'client_credentials',
    'client_id' : 'YOUR_CLIENT_ID',
    'client_secret': 'YOUR_CLIENT_SECRET'
})

token = r.json()['access_token']

wrapper = IGDBWrapper("YOUR_CLIENT_SECRET", token)
print('1 Procurar informações de um jogo')
print('2 Quais os top 10 jogos com maior rating em determinado ano?')
print('3 Quais os 10 piores jogos de determinado ano?')
a=int(input())
if(a==1):
    print('Insira o nome do jogo: ')
    nome=str(input())
    array = wrapper.api_request(
                'games',
                'fields *, platforms;search "'+nome+'"; where category = 0; limit 50;'
            )
    resultado = json.loads(array)
    i=0
    while(i<len(resultado)):
        print('Nome do jogo: ', resultado[i]['name'])
        j=0
        if 'first_release_date' in resultado[i]:
            data = datetime.fromtimestamp(resultado[i]['first_release_date'], tz = timezone("Europe/London"))
            exib = str(data.day)+'/'+str(data.month)+'/'+str(data.year)
            print('Data de lançamento: ', exib)
        if 'total_rating' in resultado[i]:
            print('Nota: ', resultado[i]['total_rating'])
        print('Categorias: ')
        if 'genres' in resultado[i]:
            t=len(resultado[i]['genres'])
            while(j<t):
                arrayy = wrapper.api_request(
                                'genres',
                                'fields name;where id='+str(resultado[i]['genres'][j])+';'
                            )
                resultadoo = json.loads(arrayy)
                print('  ', resultadoo[0]['name'])
                j=j+1
        k=0
        print('Plataformas: ')
        if 'platforms' in resultado[i]:
            t=len(resultado[i]['platforms'])
            while(k<t):
                arrayyy = wrapper.api_request(
                                'platforms',
                                'fields name;where id='+str(resultado[i]['platforms'][k])+';'
                            )
                resultadooo = json.loads(arrayyy)
                print('  ', resultadooo[0]['name'])
                k=k+1
        i=1+i
        print('-----------------------')
    
if(a==2):
    print('Qual ano voce deseja consultar?')
    ano=int(input())
    array = wrapper.api_request(
                'games',
                'fields *; sort total_rating desc; where release_dates.y = '+str(ano)+' & total_rating_count!=0;'
            )
    resultado = json.loads(array)
    i=0
    while(i<10):
        print('Nome do '+str(i+1)+'° jogo com maior rating: ', resultado[i]['name'])
        i=1+i
if(a==3):
    print('Qual ano voce deseja consultar?')
    ano=int(input())
    array = wrapper.api_request(
                'games',
                'fields *; sort total_rating asc; where release_dates.y = '+str(ano)+' & total_rating_count!=0;'
            )
    resultado = json.loads(array)
    i=0
    while(i<10):
        print('Nome do '+str(i+1)+'° jogo com menor rating: ', resultado[i]['name'])
        i=1+i
    