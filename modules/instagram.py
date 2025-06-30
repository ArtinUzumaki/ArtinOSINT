# فایل: modules/instagram.py

import httpx
from utils.tools import print_info, print_error, print_success, print_bad

async def check(target):
    print_info("Checking Instagram...")
    username = target.split('@')[0]  # فرض می‌کنیم قسمت قبل از @ یوزرنیم باشه
    url = f"https://www.instagram.com/{username}/?__a=1"

    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(url, follow_redirects=True)

        if r.status_code == 200 and "graphql" in r.text:
            print_success(f"Instagram account found: https://instagram.com/{username}")
            return True
        else:
            print_bad("Instagram account not found.")
            return False

    except Exception as e:
        print_error(f"Error checking Instagram: {e}")
        return False
