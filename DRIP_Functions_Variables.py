
# coding: utf-8

# ### As the Dam Removal Information Portal is being overhauled into DRIP 2.0 there are a number of reoccuring variables and functions which are documented here.  This is a work in progress and will continue to grow as the DRIP 2.0 project progresses.

# In[ ]:

#Common variables used in DRIP
arSbItemUrl = 'https://www.sciencebase.gov/catalog/item/5a1d7403e4b09fc93dd7bd9c?format=json'



# In[ ]:

####Functions used in DRIP####
##############################


#Function to process pandas dataframe row into a dictionary
def pandasRowToDict(df, intList, floatList, r):   #df = pandas dataframe, r = index number for row to process
    c = 0 #Start at column index = 0
    cMax = len(df.columns) #Number of columns in df 
    record = {} 
    while c < cMax:
        if df.columns[c] in intList:
            record[(df.columns[c])] = float(df.iloc[r,c])
            c += 1
        else:
            record[(df.columns[c])] = df.iloc[r,c]
            c += 1
        
    return record



#Function that determines newest data url based on sb weblink title (where title = year of data)
def sbNewestData(sbItemUrl):
    import requests
    
    sbAr = requests.get(sbItemUrl).json()
    maxYear = None
    for link in sbAr['webLinks']:
        try:
            if maxYear is None or int(link['title'])>int(maxYear): 
                maxYear = int(link['title'])
                maxYearLink = link['uri']
        except:
            continue
            
    

    print ('Data Year: ' + str(maxYear))
    print ('Data Url: ' + maxYearLink)
    return maxYearLink, maxYear

