#! /usr/bin/python3


# prints out waterloo weather to the command line
import pip

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install',package])



def getWaterlooWeather():
    import requests, bs4
    from prettytable import PrettyTable
    from time import localtime, strftime
    
    Date = strftime("%Y-%m-%d %H:%M:%S", localtime())
    
    
    def align(word, number):
        return "{:>10s}{:>40s}".format(word, number)
    
    res = requests.get('http://weather.uwaterloo.ca/')
    soup = bs4.BeautifulSoup(res.text,"html.parser")
    
    rows = soup.find_all('tr')
    
    FirstWords = []
    SecondWords = []
    t = PrettyTable(['Waterloo Weather',Date])
    for i,row in enumerate(rows):
        EachRow = rows[i].getText()
        EachRow = EachRow.replace(u'\n', '')
        EachRow = EachRow.replace(u'\xb0','')
        EachRow = EachRow.replace(u'\xa0','')
        Splitrow = EachRow.split(":")
    
    
        if bool(Splitrow[0].strip()) == 0:
            continue
        else:
    
            firstword = Splitrow[0]
            firstword = firstword.rstrip()
            secondword = Splitrow[1].lstrip()
            secondword = secondword.rstrip()
            t.add_row([firstword,secondword])
    
    print(t)

def main():
    import_or_install('bs4')
    import_or_install('prettytable')
    getWaterlooWeather()

if __name__ == '__main__':
    main()



