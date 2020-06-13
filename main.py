import re
import requests

banner = '''

 #######  #     #  #     #  #     # 
 #        #     #   #   #   ##    # 
 #        #     #    # #    # #   # 
 #####    #     #     #     #  #  # 
 #         #   #     # #    #   # # 
 #          # #     #   #   #    ## 
 #######     #     #     #  #     # 
                                    

'''

print(banner)
print("Welcome to evxn.io's OSINT tool...")

module = input("Please select a module: \n  1. Name & Location Search \n  2. Deep Search \n ")

if module == '1':
    fName = input("What is the first name?(Can be left blank) ")
    lName = input("What is the last name? ")
    city = input("What city? ")
    state = input("What state? ")
    f = open(f"{fName}_{lName}.txt", "a")
    f.write("Started automatic dox on victim...")


    def anywho():
        headers = {
            'Connection': 'keep-alive',
            'DNT': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 OPR/69.0.3686.21 (Edition beta)',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        response = requests.get(f'https://www.anywho.com/people/{fName}-{lName}/{city}-{state}', headers=headers)
        split = response.text.split('<div class="c-people-result__address">')
        count = len(split)
        arrayTotal = count + 1
        looprange = int(arrayTotal) / 2
        if looprange > 1:
            for x in range(int(looprange)):
                print('Hit found: ' + split[int(looprange)].split('</div>')[0])
                f.write('Hit found: ' + split[int(looprange)].split('</div>')[0])

        else:
            print('Unable to find location data from anywho.com...')
            f.write("No hits found on anywho...")


    anywho()


    def fastPeoplSearch():
        headers = {
            'authority': 'www.fastpeoplesearch.com',
            'cache-control': 'max-age=0',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 OPR/69.0.3686.21 (Edition beta)',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://www.fastpeoplesearch.com/',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': '__cfduid=dc7ee81f44bf4d461c39bebdbcb89d47a1590876224; cf_clearance=3a5d2abf518f4fc8a8673dc69fde9057793772ec-1591973093-0-150',
        }

        response = requests.get(f'https://www.fastpeoplesearch.com/name/{fName}-{lName}_{city}-{state}',
                                headers=headers)
        split = response.text.split('data-link="/')
        count = len(split)
        iterations = count - 1
        for x in range(int(iterations)):
            print('Hit found: https://www.fastpeoplesearch.com/' + split[int(x + 1)].split('">')[0])


    fastPeoplSearch()


    def zaba():
        headers = {
            'authority': 'www.google-analytics.com',
            'cache-control': 'max-age=0',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 OPR/69.0.3686.21 (Edition beta)',
            'accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-mode': 'no-cors',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'image',
            'accept-language': 'en-US,en;q=0.9',
            'Referer': 'https://www.zabasearch.com/people/Heather+Wohl/Chappaqua+ny/',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 OPR/69.0.3686.21 (Edition beta)',
            'DNT': '1',
            'referer': 'https://www.zabasearch.com/people/Heather+Wohl/Chappaqua+ny/',
        }

        response = requests.get(f'https://www.zabasearch.com/people/{fName}+{lName}/{city}+{state}/', headers=headers)
        split = response.text.split('<div class="person-info">')
        count = len(split) - 1
        print('Hit found: ' + split[1].split('<p>')[1].split('</p>')[0])


    zaba()
    f.close()
if module == '2':
    query = input("Input your query for search. Options are: email, ip_address, username, password, hashed_password, name, and any other data points. \n")

    headers = {
        'Accept': 'application/json',
    }

    params = (
        ('query', f'"{query}"'),
    )

    response = requests.get('https://api.dehashed.com/search', headers=headers, params=params,
                            auth=('evxnw@protonmail.com', '8e5ccac816ec60d067cf38e510793a3d')).json()
    print(response)
    print(f"Succesfully queried dehashed API in {response['took']}. Total entries found: {response['total']}")
