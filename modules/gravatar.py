import hashlib
import httpx
from utils.tools import print_info, print_bad, print_success

async def check(email):
    print_info("Checking Gravatar...")
    email_hash = hashlib.md5(email.lower().encode()).hexdigest()
    url = f"https://www.gravatar.com/avatar/{email_hash}?d=404"
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
    if r.status_code == 200:
        print_success(f"Gravatar found for {email}")
        return True
    else:
        print_bad("Gravatar not found.")
        return False
