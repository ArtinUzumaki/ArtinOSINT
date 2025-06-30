import httpx
from utils.tools import print_info, print_error, print_good, print_bad

async def check(target):
    print_info("Checking GitHub...")
    username = target.split('@')[0]
    url = f"https://github.com/{username}"
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
    if r.status_code == 200:
        print_good(f"GitHub account found: {url}")
        return True
    else:
        print_bad("GitHub account not found.")
        return False
