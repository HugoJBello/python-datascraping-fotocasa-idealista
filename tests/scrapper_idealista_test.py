import unittest
import sys
sys.path.append("..")
from scraper.scraper_selenium_idealista import ScraperSeleniumIdealista


class TestIdealista(unittest.TestCase):  

    def testIdealista(self):
        test_urls=['https://www.idealista.com/venta-viviendas/galapagar-madrid/con-precio-hasta_300000,chalets,casas-de-pueblo/']
        scrapper = ScraperSeleniumIdealista(test_urls)
        scrapper.get_data()
        print(str(scrapper.summaries[test_urls[0]]))
        self.assertIsNotNone(scrapper.data)

if __name__ == '__main__':
	    unittest.main()
