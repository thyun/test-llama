import requests
from bs4 import BeautifulSoup, SoupStrainer

class RecursiveURLLoader:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password

    def load_url(self, url):
        response = requests.get(url, auth=(self.username, self.password))
        if response.status_code == 200:
            return response.content
        else:
            raise Exception("Failed to load URL: {}".format(url))

    def load_all_urls(self):
        urls = [self.base_url]
        while urls:
            url = urls.pop()
            content = self.load_url(url)
            result = content.decode('utf-8')
            print(result)
            for new_url in self.extract_new_urls(content):
                urls.append(new_url)
        return urls

    def extract_new_urls(self, content):
        # This is a placeholder method that should be implemented by subclasses
        pass

class ImageURLLoader(RecursiveURLLoader):
    def extract_new_urls(self, content):
        soup = BeautifulSoup(content, "html.parser")
        image_tags = soup.find_all("img")
        image_urls = []
        for image_tag in image_tags:
            image_urls.append(image_tag["src"])
        return image_urls

class LinkURLLoader(RecursiveURLLoader):
    def extract_new_urls(self, content):
        soup = BeautifulSoup(content, "html.parser")
        link_tags = soup.find_all("a")
        link_urls = []
#        print(link_tags)
#        for link_tag in link_tags:
#            link_urls.append(link_tag["href"])
        return link_urls

# from rloader import LinkURLLoader
#loader = LinkURLLoader("http://wiki.skplanet.com/pages/viewpage.action?pageId=295656385", "1001291", "xxxx")
#loader.load_all_urls()

