# Waterloo Weather

grabs Waterloo weather from Waterloo Weather Station using Python  
http://weather.uwaterloo.ca/

## Requirements
 - requests
 - BeautifulSoup
 - prettytable

## Using pip

```
pip install requests beautifulsoup4 PrettyTable
```
## Usage
run waterloweather.py  
Example:
```
+-----------------------------------+-------------------------+
|          Waterloo Weather         |   2018-11-28 13:51:51   |
+-----------------------------------+-------------------------+
|       Temperature (current)       |          0.8 C          |
|   Temperature (24 hour max/min)   |      1.0 C /-2.2 C      |
| Precipitation (15 min/1 hr/24 hr) | 0.0 /  0.0   /   0.4 mm |
|    Relative Humidity/Dew Point    |     86.7 % / -1.1 C     |
|  Wind Speed (gust) and Direction  |    6.9 (13.9) km/h N    |
|        Barometric Pressure        |   101.0  kPa   Steady   |
|         Incoming Radiation        |        219.8 W/m2       |
+-----------------------------------+-------------------------+
```


# Waterloo Download
Downloads data from http://weather.uwaterloo.ca/ saves as csv file. Data is available from 1998.

## Requirements
 - Python3

## Usage
```
usage: waterloodownload.py [-h] -f  [-l]

script to download data from Waterloo Weather Station

optional arguments:
  -h, --help         show this help message and exit
  -f , --firstyear   starting year to download
  -l , --lastyear    last year to download
```

