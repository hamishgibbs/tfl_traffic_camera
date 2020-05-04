#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 12:09:02 2020

@author: hamishgibbs
"""

import sys
import requests as r
import json
import pandas as pd
from count_vehicles import count_vehicles


_args = ['code', '/Users/hamishgibbs/Documents/Covid-19/tfl_cam_mobility/tmp', '/Users/hamishgibbs/Documents/Covid-19/tfl_cam_mobility/output/output.csv']
#%%

#88c2a948
#cf17f707c8da5abcbaa0f041b3ac0572

json_data = r.get('https://api.tfl.gov.uk/Place/Type/JamCam/?app_id=88c2a948&app_key=cf17f707c8da5abcbaa0f041b3ac0572')

json_data = json.loads(json_data.text)


cam_urls = [json_data[i]['additionalProperties'][1]['value'] for i in range(0, len(json_data))]

#%%
def main(_args):
    
    try:
        vehicle_count_prev = pd.read_csv(_args[2], index_col = 0)
    except:
        pass
    
    vehicle_count = pd.DataFrame([count_vehicles(url, _args[1]) for url in cam_urls])
    
    try:
        vehicle_count = pd.concat([vehicle_count_prev, vehicle_count]).reset_index()
    except:
        pass
    
    vehicle_count.to_csv( _args[2])
    
    print('Success.')

#%%
if __name__ == "__main__":
    
    main(_args)
