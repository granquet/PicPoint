from operator import attrgetter
from packages.algo import bisect_tuple
import datetime
import gpxpy
import gpxpy.gpx

def cmpDate(a ,b):
    return a > b.time

class Tracks:
    def __init__(self, fname):
        gpx_file = open(fname, 'r')
        self.gpx = gpxpy.parse(gpx_file)
        gpx_file.close()
        self.points = []
        pts = []
        for track in self.gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    pts.append(point)
        self.points = sorted(pts, key=attrgetter('time'))

    def findPointAtDatetime(self, dt):
        for point in self.points:
            if point.time == dt:
                return point

    def findPointClosestToDatetime(self, dt):
        tup = bisect_tuple(self.points, dt, cmpDate)
        if abs(self.points[tup[0]].time - dt) > abs(self.points[tup[1]].time - dt):
            return self.points[tup[1]]
        else:
            return self.points[tup[0]]

