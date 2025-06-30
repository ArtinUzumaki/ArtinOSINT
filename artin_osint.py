import asyncio
import sys

from utils.tools import print_info, print_good, print_bad
from modules import github, instagram, tiktok, gravatar

SERVICES = {
    "GitHub": github.check,
    "Instagram": instagram.check,
    "TikTok": tiktok.check,
    "Gravatar": gravatar.check,
}

async def main(target):
    print_info(f"\n🔍 جستجو برای: {target}\n")
    tasks = [func(target) for func in SERVICES.values()]
    results = await asyncio.gather(*tasks)

    for (name, _), found in zip(SERVICES.items(), results):
        symbol = "✅ Found" if found else "❌ Not Found"
        print(f"[+] {name:10} => {symbol}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_bad("Usage: python artin_osint.py <email_or_username>")
        sys.exit(1)

    asyncio.run(main(sys.argv[1]))
