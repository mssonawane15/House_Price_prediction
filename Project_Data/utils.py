import json,requests,os
import config
import pickle
import numpy as np

class HousePricePredictor():
    def __init__(self,size,total_sqft,bath,balcony,location):
        self.size = size
        self.total_sqft = total_sqft
        self.bath = bath
        self.balcony = balcony
        self.location = "location_"+location

    def load_model(self):
        with open(config.Model_File_Path,"rb") as f:
            self.model = pickle.load(f)
                    
    def load_json(self):
        with open(config.Encoded_Data_Path,"r") as f:
            self.json = json.load(f)

    def get_house_price(self):
        self.load_model()
        self.load_json()
        test_array = np.zeros(len(self.json["columns"]))
        location_index = self.json["columns"].index(self.location)
        test_array[0] = self.size
        test_array[1] = self.total_sqft
        test_array[2] = self.bath
        test_array[3] = self.balcony
        test_array[location_index] = 1

    
        price = self.model.predict([test_array])

        return price


    

