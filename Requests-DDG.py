import requests
from bs4 import BeautifulSoup as soup



def requesting_ip():
    HEADERS = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        #'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'en-US,en;q=0.5',
        'Connection':'keep-alive',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0',
    }
    
    url = 'https://www.duckduckgo.com/html?q=my+ip'
    
    if url:
        r = requests.get(url, headers=HEADERS)
        page = soup(r.text, 'html5lib')
        page = str(page).splitlines()
        return page
    elif url_check == False:
        print('< check url >')



def parsing_ip(page):
    for line in page:
        if 'Your IP address is ' in line and ' in <a href="http' in line:
            line = line.replace('Your','\nYour').splitlines()[1]
            line = line.split(' ')
            print(f'{line[0]} {line[1]} {line[2]} {line[3]} {line[4]} ')



def main():
    page = requesting_ip()
    if page:
        parsing_ip(page)

if __name__ == '__main__':
    main()
