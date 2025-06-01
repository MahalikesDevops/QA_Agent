import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

#to extract the text from each url that is sent as input usung beautiful soup
def extract_text_from_url(url):
    try:
        response = requests.get(url, timeout=30)
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all(['p', 'li', 'h1', 'h2', 'h3'])
        return "\n".join([p.get_text(strip=True) for p in paragraphs])
    except Exception as e:
        print(f"[!] Failed to fetch {url}: {e}")
        return ""

#to find the internal link present in the baseurl's soup
def find_internal_links(base_url, soup):
    base_domain = urlparse(base_url).netloc
    internal_links = set()
    for link in soup.find_all('a', href=True):
        href = link['href']
        full_url = urljoin(base_url, href)
        if urlparse(full_url).netloc == base_domain:
            internal_links.add(full_url)
    return list(internal_links)

# creates a list of links to be visited and runs the loop to extract data from all the links
def crawl_site_with_links(base_url, max_pages=50):
    #uncomment the below statement if you want to be nitified when it starts crawling
    #print(f"[+] Crawling base page: {base_url}")
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    visited = set()
    to_visit = [base_url] + find_internal_links(base_url, soup)
    all_texts = []

    for url in to_visit[:max_pages]:
        if url not in visited:
            #uncomment the below statement to see what are all the urls that are being crawled
            #print(f"  -> Crawling: {url}")
            text = extract_text_from_url(url)
            if text:
                all_texts.append((url, text))
            visited.add(url)
            time.sleep(1)

    return all_texts
