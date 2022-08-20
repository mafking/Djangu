import billboard
from datetime import date
import json


def get_all_years():
    return [i for i in range(1958,date.today().year + 1)]



def get_months(year):
     months=[]
     for i in range(1,13):
         if i <10:
             months.append('{year}-0{i}-01'.format(year=year,i=i))
         else: months.append('{year}-{i}-01'.format(year=year,i=i))
     return months

def get_hot_100(month):
  hot_100=[]
  chart=billboard.ChartData('hot-100',date=month)
  for i in chart:
    hot_100.append({'rank':i.rank,'title':i.title,'artist':i.artist})
  return hot_100
   
def get_current_100():
  hot_100=[]
  chart=billboard.ChartData('hot-100')
  for i in chart:
    hot_100.append({'rank':i.rank,'title':i.title,'artist':i.artist})
  return hot_100
  
    
if __name__=="__main__":
    print(get_all_years())
    print(get_months('2022'))
    print(get_hot_100(get_months('2022')[6]))

#print(get_current_100())
    