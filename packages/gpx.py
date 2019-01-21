from operator import attrgetter
import datetime
import gpxpy
import gpxpy.gpx

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
        prev_pt = None
        for point in self.points:
            if point.time > dt:
                if prev_pt == None:
                    return point
                if abs(prev_pt.time - dt) > abs(point.time - dt):
                    return point
                else:
                    return prev_pt
            prev_pt = point

