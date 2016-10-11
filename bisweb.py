from bs4 import BeautifulSoup
from urllib2 import urlopen
import pandas as pd
import re

def bisweb_batch(df, bbl='bbl'):

    def get_bin(df):

        # assign BBL information
        boro = df['bbl'].astype(str)[:1]
        block = df['bbl'].astype(str)[1:6]
        lot = df['bbl'].astype(str)[6:10]

        # create URL to scrape
        URL = 'http://a810-bisweb.nyc.gov/bisweb/PropertyProfileOverviewServlet?boro='+str(boro)+'&block='+str(block)+'&lot='+str(lot)+'&go3=+GO+&requestid=0'

        # cook up some soup
        soup = BeautifulSoup(urlopen(URL), 'html.parser')

        # if the BBL does not exist (by checking for a specific string that only shows up on the search page), return nothing
        if soup.findAll(text=re.compile('DOB Building Information Search'), limit=1) != []:
            return

        # if the BBL does exist, look for the BIN and return it
        try:
            return soup.findAll(text=re.compile('BIN#'), limit=1)[0].encode('utf-8')[8:15]

        # in the event that the BIS Web site took too long to load, recursively query it again
        except:
            return get_bin(df)

    # apply function on entire DataFrame
    df[['bisweb_bin']] = df.apply(get_bin, axis=1).apply(pd.Series)

    # return completed DataFrame
    return df
