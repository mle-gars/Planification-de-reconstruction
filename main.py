import numpy as np
import pandas as pd

class PrepData :

    pass


class Infra :

    def __init__(self, infra_id, infra_type, length, nb_houses):
        pass

    def repair_infra(self, ):
        pass
        
    def get_infra_difficulty (self, ):
        pass
        
    def __radd__(self, other_infra, ):
        pass


''' métrique par difficultés : infra intacte = diff NULL, infra damaged = diff FULL 
nécessaire '''

    

class House :

    def __init__(self, id_building, list_infras):
        pass

    def get_building_difficulty(self, ):
        pass
        
    def __lt__(self, ):
        pass
        

    
''' métrique par difficultés : somme des difficultés permettant de raccorder le House)'''