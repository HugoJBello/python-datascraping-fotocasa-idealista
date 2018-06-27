import sys
from dto.summary_scrapped_dto import SummaryScrappedDTO

class UtilsSummaryBuilder:

    def __init__(self, data, scrapped_url, scrapped_prize):
        self.data = data
        self.scrapped_url = scrapped_url
        self.scrapped_prize=scrapped_prize
        self.number_of_items=0
        self.mean_prize_m2=0
        self.summary = None

    def obtain_summary(self):
        self.calculate_mean_prize_m2_and_number_items()
        if (self.scrapped_prize=="" or self.scrapped_prize==None):
            self.scrapped_prize=self.mean_prize_m2
        self.summary=SummaryScrappedDTO(self.scrapped_prize,self.number_of_items,self.scrapped_url,self.mean_prize_m2)

    
    def calculate_mean_prize_m2_and_number_items(self):
        count = 0
        sum_prize = 0
        for dto in self.data:
            if(self.scrapped_url in dto.url_first_page):
                prize_m2=self.calculate_prize_m2(dto)
                if (not prize_m2== None):
                    count = count + 1
                    sum_prize = sum_prize + float(prize_m2)
        self.number_of_items=count
        
        if (not count == 0):
            self.mean_prize_m2= sum_prize/count
        else:
             self.mean_prize_m2= 0

    def calculate_prize_m2(self,real_state_entry_dto):
        is_prized =not ((real_state_entry_dto.prize=="") or (real_state_entry_dto.prize==None))
        has_meters = not ((real_state_entry_dto.meters=="") or (real_state_entry_dto.prize==None))
        if (is_prized and has_meters):
            return float(real_state_entry_dto.prize.replace(".",""))/float(real_state_entry_dto.meters.replace(".",""))
        else:
            return None

