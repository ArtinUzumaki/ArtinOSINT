import httpx
from utils.tools import print_info, print_error, print_good, print_bad

async def check(target):
    print_info("Checking TikTok...")
    username = target.split('@')[0]  # فرض می‌کنیم قسمت قبل از @ یوزرنیمه
    url = f"https://www.tiktok.com/@{username}"

    async with httpx.AsyncClient() as client:
        try:
            r = await client.get(url, timeout=10)
            if r.status_code == 200:
                print_good(f"TikTok account found: {url}")
                return True
            else:
                print_bad("TikTok account not found.")
                return False
        except httpx.RequestError as e:
            print_error(f"Error checking TikTok: {e}")
            return False
