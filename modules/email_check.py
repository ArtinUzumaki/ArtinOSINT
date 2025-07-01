import httpx
from utils.tools import print_info, print_good, print_bad

async def check(email):
    print_info("Checking email existence via password reset page...")
    # نمونه سایت برای تست (مثلا Gmail reset page)
    url = "https://accounts.google.com/signin/v2/usernamerecovery"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (compatible)"
    }
    data = {
        "identifier": email,
        "continue": "https://accounts.google.com/signin/recovery"
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(url, headers=headers, data=data, timeout=10)
    
    # چک ساده روی متن پاسخ
    if "Couldn't find your Google Account" in r.text:
        print_bad("Email not found via password reset page.")
        return False
    else:
        print_good("Email found via password reset page.")
        return True
