from selenium import webdriver
import sys

from utils_app.util_summary_builder import UtilsSummaryBuilder
from dto.real_state_entry_dto import RealStateEntryDTO 
from dto.summary_scrapped_dto import SummaryScrappedDTO
import time
import random

#https://www.seleniumhq.org/download/
#14393
#https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

class ScraperSeleniumFotocasa:

    def __init__(self, urls):
        self.urls = urls
        #self.driver = webdriver.Edge()
        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()
        self.data ={}
        self.summaries = {}
    
    def get_data(self):
        for url_from_db in self.urls:
            driver = self.driver
            driver.get(url_from_db) 
            #driver.set_window_position(-4000,0)

            self.get_data_from_page(driver,url_from_db) 
        driver.close()
       

    def get_data_from_page(self,driver,url_from_db):
        print("obtaining data from " + driver.current_url)
        search_result = self.driver.find_elements_by_class_name("sui-CardComposable-secondary")
        
        random_int =8573 + random.randint(-3, 3)
        driver.execute_script("window.scrollTo(0, "+str(random_int) +");")
        time.sleep(random.uniform(0.5,0.9))
        self.parse_search_result_item_and_update_data(search_result,url_from_db)

        print("obtained " + str(len(self.data)) + " entries")
        time.sleep(random.uniform(0.5,1))

        if (self.is_next_page()):
            print("moving to next page in search")
            url=self.driver.find_element_by_xpath("//*[text()='>']").get_attribute("href")
            driver.get(url)
            self.get_data_from_page(driver,url_from_db)
        else: 
            self.get_summary(driver,url_from_db)
            

    def is_next_page(self):
        try:
            controls=self.driver.find_element_by_xpath("//*[text()='>']")
        except:
            return False
        return not controls==None

    def parse_search_result_item_and_update_data(self,info_container_array,url_from_db):
            if(self.data==None): self.data = {}
            if(not url_from_db in self.data.keys()): self.data[url_from_db]=[]

            for home in info_container_array:
                title=home.find_element_by_class_name('re-Card-title').text.strip()
                url_element=home.find_element_by_tag_name('a').get_attribute("href").strip()
                prize=home.find_elements_by_class_name('re-Card-price')[0].text.replace("<span>","").replace("</span>","").replace(" €","").replace("\u20ac","").strip()
                features = home.find_elements_by_class_name('re-Card-feature')
                if(not features == []):
                    rooms=features[0].text.replace(" habs.","").strip()
                else: rooms=""
                
                if(len(features)>1):
                    meters=features[1].text.replace(" m²","").strip()
                else:
                    meters=""
                print(title + ".." + meters + ".." + rooms + "--" + prize)
                dto=RealStateEntryDTO(title,prize,meters,rooms,self.driver.current_url,url_element,url_from_db)
                self.data[url_from_db]=self.data[url_from_db] + [dto]


    def get_summary(self,driver,url_from_db):
        util_summary_builder=UtilsSummaryBuilder(self.data[url_from_db],url_from_db,"")
        util_summary_builder.obtain_summary()
        summary = util_summary_builder.summary
        self.summaries[url_from_db] = summary