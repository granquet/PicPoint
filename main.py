from packages.img import Photo
from packages.gpx import Tracks
import glob
from datetime import datetime
from operator import attrgetter
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--offset', help='date offset to adjust timestamps between gps track and pictures in H:M:S format')
parser.add_argument('--pic', help='path to a single picture or a path containing a collection of pictures', required=True)
parser.add_argument('--gpx', help='path to a single gpx file', required=True)
args = parser.parse_args()

print(args)

collection = []

if(args.offset is None):
    sign = 1
    dtOff = datetime.strptime('0:0:0', "%H:%M:%S")
else:
    sign = -1 if args.offset.startswith('-') else 1
    args.offset = args.offset[1:] if sign == -1 else args.offset
    dtOff = datetime.strptime(args.offset, "%H:%M:%S")

for f in glob.iglob(args.pic):
    myImg = Photo(f)
    myImg.setDateOffset([sign,dtOff])
    collection.append(myImg)

sorted_collec = sorted(collection, key=attrgetter("date"))
g = Tracks(args.gpx)

for n in sorted_collec:
    print(n.getDate())
    pt = g.findPointClosestToDatetime(n.getDate())
    print(pt)
    #myImg.updatePosition(999, 4200000, 4200000, "N", "E")
