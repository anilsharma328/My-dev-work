
import requests
response=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

binfo=response.json()
print(type(binfo))

print( "*" *30)
print("Date As of :" ,binfo['time']['updated'])

print( "1 Bitcoin = $" ,binfo['bpi']['USD']['rate'],' GBP==>',binfo['bpi']['GBP']['rate'] ,' EUR==>',binfo['bpi']['EUR']['rate'])


#print( "1 Bitcoin = £" ,binfo['bpi']['GBP']['rate'])

#print( "1 Bitcoin = Euro" ,binfo['bpi']['EUR']['rate'])
print( "\nDisclaimer:",binfo['disclaimer'])
print( "*" *30)
