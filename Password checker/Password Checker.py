import requests
import hashlib
import sys

def request_api_data(quary_char):
    url = 'https://api.pwnedpasswords.com/range/' + quary_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, ch')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines)
    for h, count in hashes:
        if h == hash_to_check:
            return count
        return 0

def pawned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest
    first_char, tail =  sha1password[:5], sha1password[5:]
    response = request_api_data(first_char)
    return get_password_leaks_count(response, tail)

def main(args):
    for password in args:
        count = pawned_api_check(password)
        if count:
           print(f'{password} was found {count} times... you should')
        else:
            print(f'{password} was not found. carry on!')
    return 'done!' 

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))