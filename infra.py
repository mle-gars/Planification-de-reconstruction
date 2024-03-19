import numpy as np
import  pandas as pd


class Infra :

    def __init__(self, infra_id, infra_type, length, nb_houses):
        self.infra_id = infra_id
        self.infra_type = infra_type
        self.length = length
        self.nb_houses = nb_houses

    def repair_infra(self):
        self.infra_type = "infra_intacte"
        
    def get_infra_difficulty (self):
        return 0 if self.infra_type == "infra_intacte" else self.length / self.nb_houses
        # if self.infra_type == "infra_intacte":
        #     return 0
        # else:
        #     return self.length / self.nb_houses
        
    def __radd__(self, other_object):
        return self.get_infra_difficulty + other_object


''' métrique par difficultés : infra intacte = diff NULL, infra damaged = diff FULL 
nécessaire '''