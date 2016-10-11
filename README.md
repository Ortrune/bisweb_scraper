# BIS Web Scraper

**bisweb.py** is a simple script that scrapes the NYC Department of Buildings (DOB) online Building Information System (BIS Web), and returns Buildings Identification Numbers (BINs) from an inputted Pandas DataFrame containing BBLs.

The reason one might want to use this script rather than the Geoclient API is that BIS Web returns BINs for "transitional" buildings, whereas as far as I can tell, there is no easy way in Python to batch query the Geoclient API for transitional BINs. (Curiously, however, the Department of City Planning (DCP) returns transitional BINs on its Geographic Online Address Translator (GOAT)).

I should note that BIS Web is a notoriously unreliable site, and can occasionally take some time to load its content. While this scraper should usually run quite quickly, there will be some times where you might have to wait a few minutes depending on the size of your DataFrame.

I should also note that while this script only returns BINs, it can easily be modified to return anything displayed on the BIS Web front-end.

This script requires the BeautifulSoup package, which you can install with `pip install bs4`

**bisweb_example.ipynb** shows an example of how to use the **bisweb.py** script.
