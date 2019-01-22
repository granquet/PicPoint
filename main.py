from packages.img import Photo
from packages.gpx import Tracks
import glob
from datetime import datetime
from operator import attrgetter
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--offset', help='date offset to adjust timestamps between gps track and pictures in $H:%M:%S format')
parser.add_argument('--pic', help='path to a single picture or a path containing a collection of pictures')
parser.add_argument('--gpx', help='path to a single gpx file')
args = parser.parse_args()

print(args)

collection = []
for f in glob.iglob(args.pic):
    myImg = Photo(f)
    dtOff = datetime.strptime(args.offset, "%H:%M:%S")
    myImg.setDateOffset(dtOff)
    collection.append(myImg)

sorted_collec = sorted(collection, key=attrgetter("date"))
g = Tracks(args.gpx)

for n in sorted_collec:
    print(n.getDate())
    pt = g.findPointClosestToDatetime(n.getDate())
    print(pt)
    #myImg.updatePosition(999, 4200000, 4200000, "N", "E")
