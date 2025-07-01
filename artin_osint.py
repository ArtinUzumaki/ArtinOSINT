#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import asyncio
from modules import github, instagram, tiktok, gravatar, email_check, scylla_checker
from utils.tools import print_info, print_good, print_bad

SERVICES = {
    "GitHub": github.check,
    "Instagram": instagram.check,
    "TikTok": tiktok.check,
    "Gravatar": gravatar.check,
    "EmailReset": email_check.check,
    "Scylla.sh": scylla_checker.check,  # همین‌جا async check اضافه شد
}

async def main(target: str):
    print_info("///")
    print_info("___        __  __       ")
    print_info("  / _ | ___  / /_/ /____ __")
    print_info(" / __ |/ _ \\/ __/ __/ -_) _ \\")
    print_info("/_/ |_/_//_/\\__/\\__/\\__/_//_/")
    print_info("")
    print_info("       A R T I N   O S I N T")
    print_info("")
    print_info(f"🔍 Searching for: {target}\n")

    # آماده‌سازی همه coroutineها
    tasks = [func(target) for func in SERVICES.values()]
    # return_exceptions=True تا اگر یکی خطا داد بقیه ادامه بدن
    results = await asyncio.gather(*tasks, return_exceptions=True)

    print()
    for (name, _), result in zip(SERVICES.items(), results):
        # اگر exception یا False باشه Not Found
        if isinstance(result, Exception) or not result:
            print_bad(f"[+] {name:<12} => ❌ Not Found")
        else:
            print_good(f"[+] {name:<12} => ✅ Found")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_bad("Usage: python artin_osint.py email@example.com")
        sys.exit(1)

    email = sys.argv[1]
    try:
        asyncio.run(main(email))
    except KeyboardInterrupt:
        print_bad("\n[!] Exited by user")
        sys.exit(0)
