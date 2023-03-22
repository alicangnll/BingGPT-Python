import BingPython as ai
import asyncio

if __name__ == "__main__":
    # Cookies
    # You can get with Cookie Editor
    # - Enter to https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx
    # - Open cookie editor
    # - Write your cookie
    # OR
    # - Export your cookies as Netscape
    # - Write your cookies inside of cookies.txt
    # import cookielib
    # cookies = cookielib.MozillaCookieJar('cookies.txt')
    # cookies.load()
    cookies = {
        'MUID': '',
        'BCP': '',
        'MUIDB': '',
        'USRLOC': '',
        'SRCHD': '',
        'SRCHUID': '',
        'ANON': '',
        'NAP': '',
        'PPLState': '',
        'KievRPSSecAuth': '',
        '_U': '',
        'WLID': '',
        'SUID': '',
        '_EDGE_S': '',
        'WLS': '',
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
