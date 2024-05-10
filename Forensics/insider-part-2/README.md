# Insider (Part 2)

Category: Forensics

Author: ljx1608

Flag: `sctf{n00b_h4ck3r_8e7dd87d}`

## Description

Our employee John from Hacking Pros has been acting suspiciously lately. We managed to get a memory dump of his computer. We think he has been trying to make contact with a malicious server. Investigate this server, though we have received intelligence reports that it is no longer active, so you may need to time travel... Good luck!

## Distribution
https://drive.google.com/file/d/11Ue988l0ujsCc1Vt7fLH-vAtjWO-PwTQ/view?usp=sharing

## Solution

Since the challenge invovles a volatile memory dump, we first use Volatility 2 to find the appropriate profile using `volatility -f JOHN-PC-20240307-103240.raw imageinfo`. Then, using the appropriate profile, we try `volatility -f JOHN-PC-20240307-103240.raw --profile Win7SP1x86 consoles` to see what was ran on the console:

```
...

C:\Users\John>wget --no-cache --spider http://swift-prepared-vastly.ngrok-free.app
SYSTEM_WGETRC = c:/progra~1/wget/etc/wgetrc
syswgetrc = C:\Program Files\GnuWin32/etc/wgetrc
Spider mode enabled. Check if remote file exists.
--2024-03-07 10:29:54--  http://swift-prepared-vastly.ngrok-free.app/
Resolving swift-prepared-vastly.ngrok-free.app... 18.141.129.246, 52.220.121.212, 18.139.9.214, ...
Connecting to swift-prepared-vastly.ngrok-free.app|18.141.129.246|:80... connected.
HTTP request sent, awaiting response... 307 Temporary Redirect
Location: https://swift-prepared-vastly.ngrok-free.app/ [following]
Spider mode enabled. Check if remote file exists.
--2024-03-07 10:29:55--  https://swift-prepared-vastly.ngrok-free.app/
Connecting to swift-prepared-vastly.ngrok-free.app|18.141.129.246|:443... connected.
OpenSSL: error:1407742E:SSL routines:SSL23_GET_SERVER_HELLO:tlsv1 alert protocol version
Unable to establish SSL connection.

C:\Users\John>wget --no-cache --spider http://swift-prepared-vastly.ngrok-free.app
SYSTEM_WGETRC = c:/progra~1/wget/etc/wgetrc
syswgetrc = C:\Program Files\GnuWin32/etc/wgetrc
Spider mode enabled. Check if remote file exists.
--2024-03-07 10:31:36--  http://swift-prepared-vastly.ngrok-free.app/
Resolving swift-prepared-vastly.ngrok-free.app... 18.136.148.247, 18.141.129.246, 18.139.9.214, ...
Connecting to swift-prepared-vastly.ngrok-free.app|18.136.148.247|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 228 [text/html]
Remote file exists and could contain further links,
but recursion is disabled -- not retrieving.

...

```

If we visit [http://swift-prepared-vastly.ngrok-free.app/](http://swift-prepared-vastly.ngrok-free.app/), we get an error page. However, if we were to "time travel" back in time using the Wayback Machine, we find a page at [https://web.archive.org/web/20240307024039/http://swift-prepared-vastly.ngrok-free.app/](https://web.archive.org/web/20240307024039/http://swift-prepared-vastly.ngrok-free.app/), with a directory listing that links to [/flag.txt](https://web.archive.org/web/20240307024136/http://swift-prepared-vastly.ngrok-free.app/flag.txt).
