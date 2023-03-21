import BingPython as ai
import asyncio

if __name__ == "__main__":
    cookies = {
        'MUID': '',
        'BCP': '',
        'MUIDB': '',
        'USRLOC': '',
        'SRCHD': '',
        'SRCHUID': '',
        'MMCASM': '',
        '_UR': '',
        'MicrosoftApplicationsTelemetryDeviceId': '',
        '_BINGNEWS': '',
        'MSCC': '',
        'ANON': '',
        'NAP': '',
        'ANIMIA': '',
        'ABDEF': '',
        'PPLState': '',
        'KievRPSSecAuth': '',
        '_U': '',
        'WLID': '',
        '_uetsid': '',
        '_uetvid': '',
        'SUID': '',
        '_EDGE_S': '',
        'WLS': '',
        '_HPVN': '',
        '_SS': '',
        '_clck': '',
        '_clsk': '',
        'SRCHUSR': '',
        '_RwBf': '',
        'SRCHHPGUSR': '',
        'ipv6': '',
        }
    
    ask = input("Ask your question : ")
    command = ai.BingPython.sendcom(ai.BingPython.CreateSession(cookies), ask)
    print(asyncio.get_event_loop().run_until_complete(command))