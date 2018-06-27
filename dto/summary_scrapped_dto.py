from datetime import datetime

class SummaryScrappedDTO:
    def __init__(self,prize_m2,number_of_items,url_scrapped,obtained_prize_m2):
        self.prize_m2 = prize_m2
        self.number_of_items = number_of_items
        self.url_scrapped = url_scrapped
        self.obtained_prize_m2 = obtained_prize_m2
        self.date = str(datetime.now())
        self.construct_id()

    def construct_id(self):
        self._id = self.date