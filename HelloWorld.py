from binance.client import Client

#################
publicKey = "your keys"
secretKey = "here"
#################

c = Client(publicKey,secretKey)

for each in c.get_all_tickers()[:10]:
    print(each["symbol"],each["price"])
    

####Example text output:
    
#ETHBTC 0.08478900
#LTCBTC 0.01659200
#BNBBTC 0.00149050
#NEOBTC 0.00739500
#QTUMETH 0.02317300
#EOSETH 0.01884000
#SNTETH 0.00016512
#BNTETH 0.00661000
#BCCBTC 0.15575900
#GASBTC 0.00288000
