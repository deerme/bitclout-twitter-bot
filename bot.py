# Python 3.8.5
import cloudscraper
import tweepy

url = 'https://api.bitclout.com/get-profiles'

headerDict = {  
'POST' : '/get-profiles HTTP/2',
'Host' : 'api.bitclout.com',
'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language' : 'en',
'Accept-Encoding' : 'gzip, deflate, br',
'Content-Type' : 'application/json',
'Content-Length' : '293',
'Origin' : 'null',
'DNT' : '1',
'Connection' : 'keep-alive',
'Cookie' : '__cf_bm=85b791d813fbf25e32d374b7fc9f898bfb481402-1616493203-1800-ASGuxncuiSIASC3/1hZBS9sjFDIEyuP1C2B77Tbg6MnYBa/vBXtRa13la5z8Uy0cmr1wVaDacaDyU7zNramd68Q=',
'Upgrade-Insecure-Requests' : '1',
'Sec-GPC' : '1',
'Cache-Control' : 'max-age=0',
'TE' : 'Trailers'
}

dataDict = {
"PublicKeyBase58Check":"",
"Username":"diamondhands",
"UsernamePrefix":"",
"Description":"",
"OrderBy":"newest_last_post",
"NumToFetch":1,
"ReaderPublicKeyBase58Check":"BC1YLi9NmWoASziGZYzhfoKXB6fxyCCRbxTDH5Sep2KCm7rPHTCwx5g",
"ModerationType":"",
"FetchUsersThatHODL":True,
"AddGlobalFeedBool":False
}

scraper = cloudscraper.create_scraper()
print(scraper.post(url, data = dataDict, headers = headerDict).text)
