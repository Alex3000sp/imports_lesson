import enum
import argparse
import random

class Toy(enum.Enum):
    ball = 'Ball'
    star = 'Star'
    angel = 'Angel'
    car = 'Car'
    cone = 'Cone'

class Color(enum.Enum):
    red = 'Red'
    green = 'Green'
    white = 'White'
    blue = 'Blue'
    brown = 'Brown'

parser = argparse.ArgumentParser('Chose a random toy')
parser.add_argument('toy', type= str, help='Shows a random toy you have')
args = parser.parse_args()

if args.toy:
    print(f'{random.choice([val.value for val in Color])} {random.choice([val.value for val in Toy])}')
