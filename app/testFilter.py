# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 20:22:13 2022

@author: valle
"""

# pythonモジュール
import cv2
import numpy as np
from PIL import Image

# 自作モジュール
from randomUtil import getRandomString, getHashFromIpAddress
from opencvFilter.Filters.FilterDotArt import FilterDotArt
from opencvFilter.Filters.FilterMosaic import FilterMosaic
from opencvFilter.Filters.FilterSubColor import FilterSubColor
from opencvFilter.Filters.FilterThreshold import FilterThreshold
from opencvFilter.Utils.ResourceIOFunction import *


path = "./testImages/flower.jpg"
testName = "dotArt"

# ドット絵風
if testName == "dotArt":
    filterDP = FilterDotArt(path)
    mozike = 0.05
    colorNum = 10
    name = filterDP.getFilterName()
    filterDP.setMozikeValue(mozike)
    filterDP.setColorNum(colorNum)
    filterDP.makePictureForMember()
#    dst = filterDP.dotArt(img)# ドット絵化
    dstName = filterDP.getFileName()
    cv2.imwrite(filterDP.getFileName(), filterDP.getImage())# 結果を出力
#    dst = makeFabicon(dst, 32, path = filterDP.getFileName())

# モザイク
if testName == "mosaic":
    filterMosaic = FilterMosaic(path)
    name = filterMosaic.getFilterName()
    mosaic = 0.05
    filterMosaic.setMosaicValue(mosaic)
    dst = filterMosaic.executeMosaic(img)
    dstName = filterMosaic.getFileName()
    cv2.imwrite(filterMosaic.getFileName(), img)# 結果を出力

# 減色
if testName == "subColor":
    filterSubColor = FilterSubColor(path)
    colorNum = 9
    filterSubColor.setColorNum(colorNum)
    dst = filterSubColor.subColor(img)
    dstName = filterSubColor.getFileName()
    cv2.imwrite(filterSubColor.getFileName(), img)# 結果を出力

# 二値化
if testName == "threshold":
    filterThreshold = FilterThreshold(path)
    dst = filterThreshold.threshold(img)
    ret, th = filterThreshold.threshold(img)
    cv2.imwrite(filterThreshold.getFileName(), th)# 結果を出力

#何もしない
else:
    None
"""
def outter(func):
    def inner(num):
        try:
            return func(num)
        except ZeroDivisionError:
            print("error has occured!")
            return
    return inner

def oldFunc(num):
    return 5 / num

newFunc = outter(oldFunc)

print(newFunc(0))
"""


    
    
    
    
