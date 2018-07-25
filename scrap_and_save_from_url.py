from scraper.scraper_selenium_idealista import ScraperSeleniumIdealista
from scraper.scraper_selenium_fotocasa import ScraperSeleniumFotocasa

from mongodb_dao.mongodb_data_recorder import MongoDBDataRecorder
from mongodb_dao.mongodb_config_grabber import MongoConfigGrabber
from mongodb_dao.mongodb_summary_recorder import MongoDBSummaryRecorder

class ScrapAndSaveFromURL():
    def main(self):
        urls=['https://www.idealista.com/venta-viviendas/galapagar-madrid/con-precio-hasta_300000,chalets,casas-de-pueblo/']

        scraper_idealista = ScraperSeleniumIdealista(urls)
        scraper_idealista.get_data()
        data_idealista = scraper_idealista.data
        summary_dictionary_idealista = scraper_idealista.summaries

        mongodb_data_recorder = MongoDBDataRecorder(data_idealista)
        mongodb_data_recorder.post_data()

        mongodb_summary_recorder_idealista = MongoDBSummaryRecorder(summary_dictionary_idealista)
        mongodb_summary_recorder_idealista.post_data()

if __name__ == '__main__':
    ScrapAndSaveFromURL().main()
