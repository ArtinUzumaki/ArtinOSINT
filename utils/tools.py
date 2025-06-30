def print_info(text):
    print(f"\033[94m[INFO]\033[0m {text}")

def print_good(text):
    print(f"\033[92m[OK]\033[0m   {text}")

def print_bad(text):
    print(f"\033[91m[ERR]\033[0m  {text}")

def print_error(message):
    print(f"\033[91m[-] {message}\033[0m")

def print_success(message):
    print(f"\033[92m[+] {message}\033[0m")
