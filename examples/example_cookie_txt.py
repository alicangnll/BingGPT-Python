import BingPython as ai
import asyncio
try:
    import cookielib
except:
    import http.cookiejar
    cookielib = http.cookiejar

if __name__ == "__main__":
    # Cookies
    # You can get with Cookie Editor
    # - Enter to https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx
    # - Open cookie editor
    # - Export your cookies as Netscape
    # - Write your cookies inside of cookies.txt

    # import cookielib
    # cookies = cookielib.MozillaCookieJar('cookies.txt')
    # cookies.load()
    cookies = cookielib.MozillaCookieJar('cookie.txt')
    cookies.load()
    ask = input("Ask your question : ")
    command = ai.BingPython.sendcom_sydney(ai.BingPython.CreateSession(cookies), ask)
    print(asyncio.get_event_loop().run_until_complete(command))
