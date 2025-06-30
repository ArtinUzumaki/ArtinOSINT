import asyncio
import sys
import httpx
from utils.tools import print_info, print_good, print_bad

def print_banner(target):
    banner = r"""
 ___        __  __       
/ _ | ___  / /_/ /____ __
/ __ |/ _ \/ __/ __/ -_) _ \
/_/ |_/_//_/\__/\__/\__/_//_/

       A R T I N   OSINT

🔍 Searching for: {}
""".format(target)
    print(banner)


async def check_github(target):
    print_info("Checking GitHub...")
    username = target.split('@')[0]
    url = f"https://github.com/{username}"
    async with httpx.AsyncClient() as client:
        try:
            r = await client.get(url, timeout=10)
            if r.status_code == 200:
                return True, url
        except Exception:
            pass
    return False, None


async def check_instagram(target):
    print_info("Checking Instagram...")
    username = target.split('@')[0]
    url = f"https://instagram.com/{username}"
    async with httpx.AsyncClient() as client:
        try:
            r = await client.get(url, timeout=10)
            if r.status_code == 200:
                return True, url
        except Exception:
            pass
    return False, None


async def check_tiktok(target):
    print_info("Checking TikTok...")
    username = target.split('@')[0]
    url = f"https://www.tiktok.com/@{username}"
    async with httpx.AsyncClient() as client:
        try:
            r = await client.get(url, timeout=10)
            if r.status_code == 200:
                return True, url
        except Exception:
            pass
    return False, None


async def check_gravatar(target):
    print_info("Checking Gravatar...")
    import hashlib
    email_hash = hashlib.md5(target.strip().lower().encode()).hexdigest()
    url = f"https://www.gravatar.com/avatar/{email_hash}?d=404"
    async with httpx.AsyncClient() as client:
        try:
            r = await client.get(url, timeout=10)
            if r.status_code == 200:
                return True, url
        except Exception:
            pass
    return False, None


async def main(target):
    print_banner(target)

    checks = {
        "GitHub": check_github,
        "Instagram": check_instagram,
        "TikTok": check_tiktok,
        "Gravatar": check_gravatar,
    }

    tasks = [func(target) for func in checks.values()]
    results = await asyncio.gather(*tasks)

    for (service, _), (found, url) in zip(checks.items(), results):
        symbol = "✅ Found!" if found else "❌ Not Found"
        extra = f" → {url}" if found else ""
        print(f"[+] {service:<12} => {symbol}{extra}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python artin_osint.py <email>")
        sys.exit(1)
    asyncio.run(main(sys.argv[1]))
