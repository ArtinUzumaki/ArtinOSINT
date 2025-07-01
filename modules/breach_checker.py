import httpx
from utils.tools import print_info, print_good, print_error

URL = "https://breachdirectory.tk/api/?func=auto&term={email}"

async def check(email):
    print_info(f"[BreachDirectory] 🔎 Checking for: {email}")

    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/115.0.0.0 Safari/537.36"
            )
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(URL.format(email=email), headers=headers, timeout=10)

        if response.status_code == 200:
            json_data = response.json()
            if json_data.get("success") and json_data.get("result"):
                print_good(f"[BreachDirectory] Found breaches:")
                for item in json_data["result"]:
                    print(f"  └─ {item}")
            else:
                print_error(f"[BreachDirectory] No breaches found.")
        else:
            print_error(f"[BreachDirectory] HTTP Error: {response.status_code}")

    except Exception as e:
        print_error(f"[BreachDirectory] Request error: {e}")
