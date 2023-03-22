import random
import ssl
import uuid
import certifi
import requests
import websockets
import json
import asyncio


class NotAllowedToAccess(Exception):
    pass

class BingPython:
    def CreateSession(cookie):
        header = {
            "authority": "edgeservices.bing.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "max-age=0",
            "sec-ch-ua": '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
            "sec-ch-ua-arch": '"x86"',
            "sec-ch-ua-bitness": '"64"',
            "sec-ch-ua-full-version": '"110.0.1587.69"',
            "sec-ch-ua-full-version-list": '"Chromium";v="110.0.5481.192", "Not A(Brand";v="24.0.0.0", "Microsoft Edge";v="110.0.1587.69"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-model": '""',
            "sec-ch-ua-platform": '"Windows"',
            "sec-ch-ua-platform-version": '"15.0.0"',
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69",
            "x-edge-shopping-flag": "1",
        }
        response = requests.get('https://www.bing.com/turing/conversation/create', cookies=cookie, headers=header)
        return response.text
    
    def ayikla(string):
        string = str(string).lower()
        string = str(string).replace("?", "")
        return str(string)
    
    async def ping(websocket):
        while True:
            await websocket.send('{"message":"PING"}')
            print('--- Connection are under control. Loading... ---')
            await asyncio.sleep(5)

    async def sendcom(loaddata, question):
        # JSON Load
        js1 = json.loads(loaddata)

        # SSL Context
        ssl_context = ssl.create_default_context()
        ssl_context.load_verify_locations(certifi.where())

        # Headers and IP Addresses
        FORWARDED_IP = (f"13.{random.randint(104, 107)}.{random.randint(0, 255)}.{random.randint(0, 255)}")
        HEADERS = {
            "accept": "application/json",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "sec-ch-ua": '"Not_A Brand";v="99", "Microsoft Edge";v="110", "Chromium";v="110"',
            "sec-ch-ua-arch": '"x86"',
            "sec-ch-ua-bitness": '"64"',
            "sec-ch-ua-full-version": '"109.0.1518.78"',
            "sec-ch-ua-full-version-list": '"Chromium";v="110.0.5481.192", "Not A(Brand";v="24.0.0.0", "Microsoft Edge";v="110.0.1587.69"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-model": "",
            "sec-ch-ua-platform": '"Windows"',
            "sec-ch-ua-platform-version": '"15.0.0"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-ms-client-request-id": str(uuid.uuid4()),
            "x-ms-useragent": "azsdk-js-api-client-factory/1.0.0-beta.1 core-rest-pipeline/1.10.0 OS/Win32",
            "Referer": "https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx",
            "Referrer-Policy": "origin-when-cross-origin",
            "x-forwarded-for": FORWARDED_IP,
            }
        if js1["result"]["value"] == "UnauthorizedRequest":
            raise NotAllowedToAccess(js1["result"]["message"])
        else:
            try:
                wsscon = await websockets.connect('wss://sydney.bing.com/sydney/ChatHub', extra_headers=HEADERS, max_size=None, ssl=ssl_context, timeout=9999, close_timeout=9999)
                await wsscon.send('{"protocol":"json","version":1}')
                await wsscon.recv()
                await wsscon.send('{"type":6}')
                await wsscon.recv()
                await wsscon.send('{"arguments":[{"source":"cib","optionsSets":["nlu_direct_response_filter","deepleo","disable_emoji_spoken_text","responsible_ai_policy_235","enablemm","harmonyv3","glpromptv1","cachewriteext","e2ecachewrite","dv3sugg"],"allowedMessageTypes":["Chat","InternalSearchQuery","InternalSearchResult","Disengaged","InternalLoaderMessage","RenderCardRequest","AdsQuery","SemanticSerp","GenerateContentQuery","SearchQuery"],"sliceIds":["creatorv2c","semserpbptf2","perfinstcf","sydperfinput","314sdprc","314sdprc","0310wlthrots0","prod114cf","317glpmtv1","316e2ecache"],"traceId":"6419870a6e6845039712f7e579452595","isStartOfSession":true,"message":{"locale":"tr-TR","market":"tr-TR","region":"TR","location":"lat:47.639557;long:-122.128159;re=1000m;","locationHints":[{"Center":{"Latitude":40,"Longitude":28},"RegionType":2,"SourceType":11},{"country":"Turkey","state":"Bursa","city":"Mudanya","zipcode":"16970","timezoneoffset":3,"countryConfidence":8,"cityConfidence":5,"Center":{"Latitude":40,"Longitude":28},"RegionType":2,"SourceType":1}],"timestamp":"2023-03-21T13:29:34+03:00","author":"user","inputMethod":"Keyboard","text":"' + BingPython.ayikla(question) + '","messageType":"Chat"},"conversationSignature":"' + str(js1["conversationSignature"]) + '","participant":{"id":"' + str(js1["clientId"]) + '"},"conversationId":"' + str(js1["conversationId"]) + '"}],"invocationId":"0","target":"chat","type":4}')
                task = asyncio.create_task(BingPython.ping(wsscon))
            except(websockets.exceptions.ConnectionClosedError):
                return "WebSocket ConnectionClosedError! - TERMINATED!"
            final = False
            while not final:
                try:
                    objects = str(await wsscon.recv()).split("")
                except:
                    final = True
                    try:
                        return "Answer : " + veri
                    except:
                        return "An error occured! Please try again!"
                for obj in objects:
                    if obj is None or obj == "":
                        continue
                    response = json.loads(obj)
                    try:
                        if response["type"] == 1:
                            if response["arguments"][0]["messages"][0]["text"]:
                                if "Searching the web for" in str(response["arguments"][0]["messages"][0]["text"]):
                                    continue
                                else:
                                    if "Generating answers for you..." in str(response["arguments"][0]["messages"][0]["text"]):
                                        continue
                                    else:
                                        lenarray = len(response["arguments"][0]["messages"])
                                        veri = str(response["arguments"][0]["messages"][lenarray-2]["text"])
                        elif response["type"] == 2:
                                final = True
                                if veri == question:
                                    return "An error occured! Please try again!"
                                else:
                                    return "Answer : " + veri
                    except(KeyError):
                        continue