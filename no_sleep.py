from time import sleep
from datetime import datetime
import re
import requests

'''
    No sleep should keep your sites awake, it does this by pinging your sites like a cron job.
    since the request will be coming from your computer it should fool most anti cron job catchers.
'''


# CONSTANTS / SETTINGS

SITES = [ # you can put all your project urls in this list.
    'https://vapos.onrender.com', # this is one site I setup to test this script, one of my old projects that hosted on render
    'https://the-shadow-realm.vercel.app', # another one of my projects, to test it with a vercel hosted site
    'https://rotbow.github.io/mini-us/' # lastly one from github pages
]

# Is in minutes
INTERVAL = 30





class No_Sleep:
    
    def __get_timestamp(self) -> str:
        """
        The function returns the current timestamp as a string.
        :return: a string representation of the current timestamp, with the format "HH:MM:SS".
        """
        return str(datetime.now()).split(' ')[1].split('.')[0]
    
    def __sleep_for_interval(self) -> int:
        """
        The function sleeps for the specified interval of time. based off the const in mins
        """
        sleep(INTERVAL * 60)
    
    def __get_site_title(self, url) -> str:
        """
        This function extracts the title of a website from a given URL.
        the regex may need to be updated to account for some urls, I didn't stress test this 
        
        :param url: The `url` parameter is a string that represents a website URL
        :return: the title of the website extracted from the given URL.
        """
        pat = r"http[s]?://(www\.)?(.+)(\.com|\.io|\.app)"
        match = re.match(pat, url)
        return match.group(2)
    
    def __init__(self) -> None:
        self.running = True
    
    def main(self) -> None:
        print('====== No Sleep ======\n\n')
        
        print(f'Pinging {len(SITES)} site(s)\nStarting program...')
        while self.running:
            
            for url in SITES:
                req = requests.get(url)
                print(f'    {self.__get_timestamp()}: {self.__get_site_title(url)} - {req.status_code}')
            
            
            self.__sleep_for_interval()
            
        print('shutting down...')
            
            
            
            
            
            
if __name__ == '__main__':
    ns = No_Sleep()
    ns.main()