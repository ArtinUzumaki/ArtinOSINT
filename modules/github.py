# فایل: modules/github.py

import httpx

async def check(target):
    url = f"https://github.com/{target}"
    try:
        r = await httpx.AsyncClient().get(url, timeout=10)
        return r.status_code == 200
    except:
        return False
