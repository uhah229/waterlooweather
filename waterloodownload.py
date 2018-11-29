import urllib.request
import argparse

url = 'http://weather.uwaterloo.ca/download/1998_weather_station_data.csv'

def getData(url):
    file_name = url.split('/')[-1]
    u = urllib.request.urlopen(url)
    f = open(file_name, 'wb')
    meta = u.info()
    file_size = int(meta.get_all("Content-Length")[0])
    print("Downloading: %s Bytes: %s" % (file_name, file_size))

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print(status)

    f.close()

def main(firstyear,lastyear):
    url='http://weather.uwaterloo.ca/download/'
    suffix = '_weather_station_data.csv'
    if lastyear == None:
        lastyear = firstyear
    for i in range(firstyear,lastyear+1):
        yearurl = url + str(i) + suffix
        getData(yearurl)




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=
            'script to download data from Waterloo Weather Station')
    parser.add_argument('-f','--firstyear',type=int,metavar='',required=True,help='starting year to download')
    parser.add_argument('-l', '--lastyear',type=int,metavar='',help='last year to download')
    args = parser.parse_args()

    main(args.firstyear,args.lastyear)
