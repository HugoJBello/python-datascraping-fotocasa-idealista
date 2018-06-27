import requests
import sys
from pymongo import MongoClient
from dto.real_state_entry_dto import RealStateEntryDTO

class MongoDBSummaryRecorder:

    def __init__(self, summary_dictionary):
        self.summary_dictionary = summary_dictionary
        self.client = MongoClient('mongodb://freshkore:1234@ds231460.mlab.com:31460/real-state-db')
        self.db = self.client['real-state-db']
    
    def post_data(self):
        summary_collection=self.db.summary
        for summary in self.summary_dictionary.values():
            dto_mongodb=summary.__dict__
            summary_collection.save(dto_mongodb)
