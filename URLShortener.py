import pyshorteners

long_url = input("Enter the URL to shorten: ")

type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)
while True:
    is_vip = input("Are You VIP?(Y/N) ").upper()
    if is_vip == 'Y':
        premium = input("What is going to be your custom URL? ")
        a = list(short_url)
        new_url = ''.join(a)
        b = new_url.rsplit("/", 1)
        b.pop(1)
        b.append("/")
        b.append(premium)
        url_start = ''.join(b)
        print("The Shortened URL is: " + url_start)
        valid = input("Is this URL valid?(Y/N) ").upper()
        if valid == 'Y':
            break
        elif valid == 'N':
            continue
        else:
            print("Please answer valid options (Y/N)")
            continue
    elif is_vip == 'N':
        print("The Shortened URL is: " + short_url)
        valid = input("Is this URL valid?(Y/N) ").upper()
        if valid == 'Y':
            break
        elif valid == 'N':
            continue
        else:
            print("Please answer valid options (Y/N)")
            continue
    else:
        print("Please answer valid options (Y/N)")
        continue
