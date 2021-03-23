# Python 3.8.5
import cloudscraper
import tweepy

url = 'https://api.bitclout.com'
scraper = coudscraper.create_scraper()
print(scraper.post(url, data = {"PostHashHex":"4f61aaafd26a8f1e6676e29885237a665e7514f4f24dfbf3e7e3d04c321296f5","ReaderPublicKeyBase58Check":"BC1YLi9NmWoASziGZYzhfoKXB6fxyCCRbxTDH5Sep2KCm7rPHTCwx5g","FetchParents":True,"CommentOffset":0,"CommentLimit":20,"AddGlobalFeedBool":False}, headers={'Origin' : 'https://bitclout.com', 'Accept' : 'application/json, text/plain, */*', 'Accept-Encoding' : 'gzip, deflate, br', 'Accept-Language' : 'en-US', 'Connection' : 'keep-alive', 'Content-Length' : '251', 'Content-Type' : 'application/json', 'DNT' : '1', 'Host' : 'api.bitclout.com', 'Sec-GPC' : '1', 'TE' : 'Trailers'}).text)
