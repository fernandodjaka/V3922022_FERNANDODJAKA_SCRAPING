#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests

start_url = "https://proxyway.com/reviews"

def scrape_page(url):
    print("URL: " + url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    get_data(soup)
    next_page_link = soup.find("a", class_="archive-list__block")
    if next_page_link is not None:
        href = next_page_link.get("href")
        scrape_page(href)
    else:
        print("Done")

def get_data(content):
    # Implementasi logika untuk mengambil data dari halaman web
    pass

def main():
    scrape_page(start_url)

if __name__ == "__main__":
    main()


# In[2]:


import requests
from bs4 import BeautifulSoup as bs

URL = 'https://proxyway.com/reviews'

req = requests.get(URL)
soup = bs(req.text, 'html.parser')

titles = soup.find_all('a', attrs={'class': 'archive-list__block'})

print(titles)

print(titles[1].img)


# In[7]:


from bs4 import BeautifulSoup
import requests

start_url = "https://proxyway.com/reviews"

def scrape_page(url):
    print("URL: " + url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    get_data(soup)
    next_page_link = soup.find("a", class_="next")
    if next_page_link is not None:
        href = next_page_link.get("href")
        scrape_page(href)
    else:
        print("Done")

def get_data(content):
    # Implementasi logika untuk mengambil data dari halaman web
    pass

def main():
    scrape_page(start_url)

if __name__ == "__main__":
    main()
    
import csv
import requests
from bs4 import BeautifulSoup as bs

URL = 'https://proxyway.com/reviews'

data = []

for page in range(1, 4):
    print("\n")
    print("Sub Titles Page:", page, "\n")

    req = requests.get(f'{URL}/page/{page}')
    soup = bs(req.text, 'html.parser')

    titles = soup.find_all('h3', class_='archive-list__title')

    for i, title in enumerate(titles):
        print(f"{i+1} {title.text}")
        data.append({
            'Page Number': f'Page {page}',
            'Title Number': f'Title {i+1}',
            'Title Name': title.text
        })

# Menyimpan data ke dalam file CSV
filename = 'proxywaydata.csv'
fieldnames = ['Page Number', 'Title Number', 'Title Name']

with open(filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print("Data telah disimpan ke dalam file, Terima Kasih Untuk Semuanya", filename)


# In[ ]:





# In[ ]:




