# BingGPT - Bing API on Python
You can use BingGPT API on Python!
# Requirements
<ul>
  <li>Python 3.8+</li>
</ul>
<h1>Installation</h1>
<ul>
  <li>pip install -r requirements.txt</li>
  <li>pip install dist/binggpt-0.0.10-py3-none-any.whl</li>
</ul>
<h1>Example</h1>
<pre>
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
</pre>
