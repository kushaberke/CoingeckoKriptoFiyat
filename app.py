    
import requests

symbol = "btc"
response = requests.get("https://api.coingecko.com/api/v3/coins/list?include_platform=true")
coins = response.json()

symbol_to_find = symbol  # Aradığınız "symbol" değeri
for coin in coins:
        try:
            if coin["symbol"] == symbol_to_find:
                coin_id = coin["id"]
                name = coin_id
                break  # İlgili öğe bulundu, döngüyü sonlandırın
        except:
              print("Çok fazla sorgu attınız. Lütfen Bekleyin.")

print(name)

url = "https://api.coingecko.com/api/v3/simple/price?ids="+name+"&vs_currencies=usd&include_market_cap=false&include_24hr_vol=true&include_24hr_change=true&precision=15"
response = requests.get(url)
if response.status_code == 200:
                            data = response.json()
                            price = float(data[name]['usd'])  
                            change = data[name]['usd_24h_change']
                            vol = data[name]['usd_24h_vol']          
else:
    print("Hata")
print(price)
print(change)
print(vol)