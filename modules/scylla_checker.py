# modules/scylla_checker.py

import requests
from bs4 import BeautifulSoup
from utils.tools import print_info, print_good, print_bad
import asyncio

def _sync_check(email: str) -> bool:
    """
    این قسمت به‌صورت همزمان (synchronous) اجرا می‌شود.
    اگر داده‌ای پیدا کند True برمی‌گرداند، وگرنه False.
    """
    try:
        print_info(f"[Scylla.sh] 🔎 Checking for: {email}")

        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; ArtinOSINT/1.0)"
        }
        search_url = f"https://scylla.sh/search?q={email}"
        resp = requests.get(search_url, headers=headers, timeout=15)
        resp.raise_for_status()

        soup = BeautifulSoup(resp.text, 'html.parser')
        table = soup.find("table")
        if not table:
            print_info("[Scylla.sh] No breach data found.")
            return False

        rows = table.find_all("tr")[1:]  # skip header
        if not rows:
            print_info("[Scylla.sh] No breach data found.")
            return False

        print_good(f"[Scylla.sh] Leak(s) found for {email}:")
        for row in rows[:5]:  # نمایش تا ۵ مورد اول
            cols = [td.text.strip() for td in row.find_all("td")]
            print(f"    └─ {' | '.join(cols)}")
        return True

    except requests.RequestException as e:
        print_bad(f"[Scylla.sh] Request error: {e}")
        return False
    except Exception as e:
        print_bad(f"[Scylla.sh] Unexpected error: {e}")
        return False

async def check(email: str) -> bool:
    """
    این تابع async، منطق synchronous رو در یک Thread جدا اجرا می‌کند.
    """
    return await asyncio.to_thread(_sync_check, email)
