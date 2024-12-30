import pandas as pd 
import playsound as ps
import time as tm

secondsPassed = 0
while True:
    d = pd.read_csv("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.csv")
    reqDF = d[['place', 'mag']]
    containsCountry = reqDF.place.str.contains('Solomon Islands')
    dfOfCountry = reqDF[containsCountry]
    dfOfSEQ = dfOfCountry[dfOfCountry['mag']>4.8]
    rowsInDfSEQ = dfOfSEQ.shape[0]

    if rowsInDfSEQ>0:
        print('Earthquake Occured') 
        ps.playsound('mixkit-sci-fi-ship-siren-alert-1653.wav')
        secondsPassed +=6
    else:
        print('No Earthquake Occured')

    print(f"Monitoring For {secondsPassed} Sec\nPress Crtl+C to Stop\n")
    tm.sleep(60)
    secondsPassed +=60

    # print(rowsInDfSEQ)
