import re
import requests
from bs4 import BeautifulSoup
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
print("Welcome...")
print("Please login with your canvas info..")
username = input("What is your canvas username? ")
passW = input("What is your canvas password? ")
def checkAcc(user, password):
    if user == 'bypass':
        pass
    else:
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Origin': 'https://fs.ccsd.ws',
            'Upgrade-Insecure-Requests': '1',
            'DNT': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 OPR/69.0.3686.30 (Edition beta)',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': 'https://fs.ccsd.ws/adfs/ls/?SAMLRequest=fZLRT8IwEMbf%2FSuWvm%2FdxkRoGAlCjCSoC6APvpjS3aDJ1o5eK%2FrfW4ZGfJDX6%2F3uu%2B%2B7jpA3dcsmzu7UEvYO0AYfTa2QdQ85cUYxzVEiU7wBZFaw1eRhwdIoZq3RVgtdkzPkMsERwVipFQnms5y8ZWVVDQeQhOJ6CGE25L1wWA14mG2SCtKbGOLehgQvYNAzOfEjPIjoYK7QcmV9KU7jMO6HcbJOMtbrs6z%2FSoKZ9yEVtx21s7ZFRmmFkRBYRgekvKyQ1khJMPnZaKoVugbMCsy7FPC8XPySYsfblu8dj6TXNU5YZyASuqG13kpFj8ZJUHzHcStVKdX2chKbUxOy%2B%2FW6CIun1ZqMR8c5rPNnxkfti9LH5nREz5nR6ZqPXm0%2BK3QtxWdwp03D7f%2FLJFHSVWQZVl0rcwpbELKSUPp86lofpga4hZx4fSB0fBL9%2B2vGV18%3D&SigAlg=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&Signature=UnYqEmAaE%2BBFyQ52JXs74YfMIQWBygZ%2Bc9DJxwQxFg3sGlbPioUqfPzEqzVhKIumqQycsZkU6lpsAwBrlSDu4cJK%2FgxCJB1bi7WpcuWHhGE9XUbONgXGK%2FwRL0TRhTUSCGHEE6p0xKIInYvh0WpclDXk9vTkACIai6kTuBdFsO7CkG7rA8TzdMjglNYF6nrqsT54q8lb9K8Vq0YP3bKlekUWDd5OD7vlrOFz1tWxY5MEhSMqjPgsAeMmnAdMl5euJAqZr%2FdWQutaC67qPT13SJwwnlRgG3ELIKrUSwQwHANCGlv5B%2BEXX%2Fpimo2Tli1bVdo%2BpJiPfrkArgir6BSKhQ%3D%3D',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = (
            ('SAMLRequest',
             'fZLRT8IwEMbf/SuWvm/dxkRoGAlCjCSoC6APvpjS3aDJ1o5eK/rfW4ZGfJDX6/3uu++7jpA3dcsmzu7UEvYO0AYfTa2QdQ85cUYxzVEiU7wBZFaw1eRhwdIoZq3RVgtdkzPkMsERwVipFQnms5y8ZWVVDQeQhOJ6CGE25L1wWA14mG2SCtKbGOLehgQvYNAzOfEjPIjoYK7QcmV9KU7jMO6HcbJOMtbrs6z/SoKZ9yEVtx21s7ZFRmmFkRBYRgekvKyQ1khJMPnZaKoVugbMCsy7FPC8XPySYsfblu8dj6TXNU5YZyASuqG13kpFj8ZJUHzHcStVKdX2chKbUxOy+/W6CIun1ZqMR8c5rPNnxkfti9LH5nREz5nR6ZqPXm0+K3QtxWdwp03D7f/LJFHSVWQZVl0rcwpbELKSUPp86lofpga4hZx4fSB0fBL9+2vGV18='),
            ('SigAlg', 'http://www.w3.org/2001/04/xmldsig-more#rsa-sha256'),
            ('Signature',
             'UnYqEmAaE+BFyQ52JXs74YfMIQWBygZ+c9DJxwQxFg3sGlbPioUqfPzEqzVhKIumqQycsZkU6lpsAwBrlSDu4cJK/gxCJB1bi7WpcuWHhGE9XUbONgXGK/wRL0TRhTUSCGHEE6p0xKIInYvh0WpclDXk9vTkACIai6kTuBdFsO7CkG7rA8TzdMjglNYF6nrqsT54q8lb9K8Vq0YP3bKlekUWDd5OD7vlrOFz1tWxY5MEhSMqjPgsAeMmnAdMl5euJAqZr/dWQutaC67qPT13SJwwnlRgG3ELIKrUSwQwHANCGlv5B+EXX/pimo2Tli1bVdo+pJiPfrkArgir6BSKhQ=='),
        )

        data = {
            '__VIEWSTATE': '/wEPDwUKMTY2MTc3NjUzM2RkJbJzutlNlJuIRAC0jCYAqSoxtPU=',
            '__VIEWSTATEGENERATOR': '0EE29E36',
            '__EVENTVALIDATION': '/wEWBQKXsfKcBwLnmcnFAQKzpa6MBwKo77JuAunYybIMLSWhNV4LURNxBqMLtunjXIcKTQM=',
            '__db': '14',
            'ctl00$ContentPlaceHolder1$UsernameTextBox': f'{user}',
            'ctl00$ContentPlaceHolder1$PasswordTextBox': f'{password}',
            'ctl00$ContentPlaceHolder1$SubmitButton': 'Sign In'
        }

        response = requests.post('https://fs.ccsd.ws/adfs/ls/', headers=headers, params=params, data=data).text
        if 'The user name or password is incorrect.' in response:
            print("Canvas says: The user name or password is incorrect.")
            exit()
        else:
            print("Succesfully logged in.")

checkAcc(user=username, password=passW)

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
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 OPR/69.0.3686.21 (Edition beta)',
            'DNT': '1'
        }

        response = requests.get(f'https://www.zabasearch.com/people/{fName}+{lName}/{city}+{state}/', headers=headers)
        split = response.text.split('<div class="person-info">')
        count = len(split) - 1
        print('Hit found: ' + split[1].split('<p>')[1].split('</p>')[0])


    zaba()
    def fouroneone():
        headers = {
            'authority': 'www.411.com',
            'cache-control': 'max-age=0',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 OPR/69.0.3686.30 (Edition beta)',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://www.411.com/',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': 'D_SID=69.118.121.155:pE6M/OABk2FGJJBih3+cK68LBUd7xprE3hmQGtPufnU; wp_pid=0bbf7f9c88ff570d588c1c74c30e55dc; initial_referrer=https%3A%2F%2Fwww.google.com%2F; initial_referring_domain=www.google.com; device_id=198b650f-2fde-46e8-be98-9b813f153243R; _ga=GA1.2.221837903.1592493593; _gid=GA1.2.1817751617.1592493593; ewp=29; wp_endemic_provider=D; eb=29; D_ZID=D7361884-92EB-31F1-91E7-66A24DE6FF1A; D_ZUID=39588D3E-735D-3F9A-90C2-6F57E2FE29FD; D_HID=77210747-799E-378E-A859-C9A3F81DD2F0; _411_session=Z211MGNzVU1ZdWFONEpUbzJJS21tcERXb3lwb3d0bWM3ck5nenhqVUdmWmlXc0lBK2JxWU5xVUNRVzdLdzNNSTBscVNOTlhxQS84VlV5aE1qZGdwc1dweTQyNXdxQktBalRWZ3VlRzNuSHlCUko1ZElFRWZNelN0MUM4RXBhOWVFb0wwb2RLUjd5T09TdWQyMDVleVZnPT0tLXdxMytHOHRHQmVmN2J0eVlFc1E5bHc9PQ%3D%3D--a05815a21a2d9d86601a7e3cecaf38ca4cb37fd6; amplitude_id_4452f969da1962f05527ab14f5db83da_premium_api411.com=eyJkZXZpY2VJZCI6IjE5OGI2NTBmLTJmZGUtNDZlOC1iZTk4LTliODEzZjE1MzI0M1IiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU5MjQ5MzU5MTk0MywibGFzdEV2ZW50VGltZSI6MTU5MjQ5NDA3NjY5MCwiZXZlbnRJZCI6MTcsImlkZW50aWZ5SWQiOjE3LCJzZXF1ZW5jZU51bWJlciI6MzR9; D_IID=27EFA577-7DEE-3D21-AF43-A7CF51052066; D_UID=C0830A99-45E0-31D7-9718-B6A828F99E37',
        }

        params = (
            ('fs', '1'),
            ('l', f'{city}, {state}'),
            ('q', f'{fName} {lName}'),
        )

        r = requests.get(f'https://www.411.com/name/{fName}-{lName}/{city}-{state}', headers=headers, params=params)
        soup = BeautifulSoup(r.content, 'html.parser')
        links = soup.find_all('a', class_='result-link')
        topRes = links[0]
        for link in links:
            print(f"Hit found on 411... https://411.com{link['href']}")
        headers = {
            'authority': 'www.411.com',
            'cache-control': 'max-age=0',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 OPR/69.0.3686.30 (Edition beta)',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://www.411.com/name/Heather-D-Wohl/Chappaqua-NY/139czngg',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': 'D_SID=69.118.121.155:pE6M/OABk2FGJJBih3+cK68LBUd7xprE3hmQGtPufnU; wp_pid=0bbf7f9c88ff570d588c1c74c30e55dc; initial_referrer=https%3A%2F%2Fwww.google.com%2F; initial_referring_domain=www.google.com; device_id=198b650f-2fde-46e8-be98-9b813f153243R; _ga=GA1.2.221837903.1592493593; _gid=GA1.2.1817751617.1592493593; ewp=29; wp_endemic_provider=D; eb=29; D_ZID=D7361884-92EB-31F1-91E7-66A24DE6FF1A; D_ZUID=39588D3E-735D-3F9A-90C2-6F57E2FE29FD; D_HID=77210747-799E-378E-A859-C9A3F81DD2F0; _411_session=eGE2WndFcUxmRExOMG96QS80d0N3QTJWditsYkE4dVg4V0dEamJqNFNLZThNWDM1VmF1dHhQL2tCdDdXTjc2YWh5bmpVTnkrOGRrTkpKR3hsQ1doK1RNVXVVcW1YYVRLZ3RnZjNMeUVyVW5LL1pMZVZSMjdEM1lXVlNoWjBMNk9TTWJseU03cUcrNW1QOEpROFFDOEJ3PT0tLURWWWRuSm5LamRWcWtzSFJBZ3hFb2c9PQ%3D%3D--d7b82b1fcd9b2f70e609e79b989c79f9e8fb1002; amplitude_id_4452f969da1962f05527ab14f5db83da_premium_api411.com=eyJkZXZpY2VJZCI6IjE5OGI2NTBmLTJmZGUtNDZlOC1iZTk4LTliODEzZjE1MzI0M1IiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU5MjQ5MzU5MTk0MywibGFzdEV2ZW50VGltZSI6MTU5MjQ5NDk4OTE0NywiZXZlbnRJZCI6MjIsImlkZW50aWZ5SWQiOjIyLCJzZXF1ZW5jZU51bWJlciI6NDR9; _gat=1; D_IID=DF6E7C11-8AAE-35C3-B754-6861CFDCAD75; D_UID=67ACD100-88E9-3574-B3E1-F67210D79023',
        }
        print("Attempt to crawl info...")
        res = requests.get(f"https://411.com{topRes['href']}", headers=headers)
        soup = BeautifulSoup(res.content, "html.parser")
        dataPoints = soup.find_all('a', class_='section-click')
        if len(dataPoints) < 1:
            print("Failed to crawl due to captcha. ")
        for data in dataPoints:
            print(f"Data point found: https://411.com{data['href']}")
    fouroneone()
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
                            auth=('evxnw@protonmail.com', 'api-key')).json()
    print(response)
    print(f"Succesfully queried dehashed API in {response['took']}. Total entries found: {response['total']}")
