from urllib import request, error, parse
import requests
starter = "http://www.imomoe.ai/player/7786-0-0.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75"
}

req = request.Request("https://ggkkmuup9wuugp6ep8d.exp.bcevod.com/mda-maf0d6dh6tg04g9d/mda-maf0d6dh6tg04g9d.mp4", method="GET", headers=headers)
response = requests.get("https://ggkkmuup9wuugp6ep8d.exp.bcevod.com/mda-maf0d6dh6tg04g9d/mda-maf0d6dh6tg04g9d.mp4", headers=headers)
with open("石纪元" + "。mp4", "wb") as f:
    f.write(response.content)
