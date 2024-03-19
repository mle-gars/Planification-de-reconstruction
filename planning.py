import numpy as np
import pandas as pd

class Planning:

    def __init__(self, csv_path):
        self.networf_df = pd.read_csv(csv_path)

    def prepare_data (self):
        dict_infra =  {}
        list_buildings = []

        return  dict_infra, list_buildings
    
    def run_plannif (self, dict_infra , list_building):
        sorted_infra = []
        sorted_buildings = []

        #algo
        return sorted_infra, sorted_buildings
    
if __name__  == "__main__":
    pass
