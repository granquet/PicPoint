from packages.img import Photo
from packages.gpx import Tracks
import glob
import datetime
from operator import attrgetter


collection = []
for f in glob.iglob('*.jpg'):
    myImg = Photo(f)
    collection.append(myImg)
    myImg.updatePosition(999, 4200000, 4200000, "N", "E")

print("sorting")
sorted_collec = sorted(collection, key=attrgetter("date"))

for n in sorted_collec:
    print(n.date)

g = Tracks("concat.gpx")
pt = g.findPointAtDatetime(datetime.datetime.strptime('2017-09-12 07:44:08', "%Y-%m-%d %H:%M:%S"))
print(pt)
pt = g.findPointClosestToDatetime(datetime.datetime.strptime('2017-09-12 07:44:00', "%Y-%m-%d %H:%M:%S"))
print(pt)
