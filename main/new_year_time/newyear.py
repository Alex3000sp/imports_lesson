import argparse
from datetime import datetime, date, time

parser = argparse.ArgumentParser('Days till New Year')
parser.add_argument('newyear', type= str, help='Shows how much time wait till New Year')
parser.add_argument('--hours', action='store_true', help='Shows hours with days')
args = parser.parse_args()
current_datetime = datetime.now()
new_year = datetime(2022, 1, 1, 00, 00)
current_date = date(2021, 12, 30)
dt = str(new_year - current_datetime)
if args.newyear and args.hours:
    print(new_year - current_datetime)
else:
    print(f'{dt.split()[0]} day')

    

    
