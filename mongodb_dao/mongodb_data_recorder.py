import requests
import sys
from pymongo import MongoClient
from dto.real_state_entry_dto import RealStateEntryDTO

class MongoDBDataRecorder:

    def __init__(self, dto_dictionary):
        self.dto_dictionary = dto_dictionary
        self.client = MongoClient('mongodb://freshkore:1234@ds231460.mlab.com:31460/real-state-db')
        self.db = self.client['real-state-db']
    
    def post_data(self):
        scrapped_data_collection=self.db.scrapped
        for key, dto_list in self.dto_dictionary.items():
            print("------- saving data from url " + key)
            for dto in dto_list:
                print("saving " + dto._id)
                dto_mongodb=dto.__dict__
                scrapped_data_collection.save(dto_mongodb)