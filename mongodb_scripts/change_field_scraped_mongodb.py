import unittest
import sys
from pymongo import MongoClient
import hashlib
sys.path.append("..")
from scraper.scraper_selenium_fotocasa import ScraperSeleniumFotocasa


class ChangeIdsMongodb(unittest.TestCase):  

    def testFotocasa(self):
        self.client = MongoClient('mongodb://freshkore:1234@ds231460.mlab.com:31460/real-state-db')
        self.db = self.client['real-state-db']

        scraped_collection=self.db.scrapped
        for scraped_data in scraped_collection.find({}):
            if(not "url_scraped" in scraped_data.keys()):
                print("cleaning " + scraped_data["_id"])
                scraped_data["url_scraped"]=scraped_data["url_scrapped"]
                scraped_data["url_scrapped"]=None
                scraped_collection.save(scraped_data)
        self.assertTrue(True)
if __name__ == '__main__':
	    unittest.main()
