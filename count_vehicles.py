#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 14:46:45 2020

@author: hamishgibbs
"""

import requests as r
import cv2
from cvlib import detect_common_objects
from datetime import datetime
import os

def count_vehicles(url, tmp_dir):
    
    im_fn = tmp_dir + '/' + url.split('/')[-1]
    
    with open(im_fn, 'wb') as f:
        f.write(r.get(url, headers={'Cache-Control': 'no-cache', 'Pragma': 'no-cache'}).content)
    
    im = cv2.imread(im_fn)
    
    bbox, label, conf = detect_common_objects(im)
    
    
    os.remove(im_fn)
    
    return({'camera': str('C' + '.'.join(url.split('/')[-1].split('.')[:-1])), 
     'car':label.count('car'), 
     'bus':label.count('bus'), 
     'truck':label.count('truck'), 
     'date_time':datetime.timestamp(datetime.now())})