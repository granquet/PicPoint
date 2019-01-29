from datetime import datetime,timedelta
import piexif
from PIL import Image


class Photo:

    def __init__(self, fname):
        self.fname = fname
        img = Image.open(fname)
        self.exif = piexif.load(img.info["exif"])
        exif_date = self.exif["Exif"][piexif.ExifIFD.DateTimeOriginal]
        self.date = datetime.strptime(exif_date.decode("utf-8"), "%Y:%m:%d %H:%M:%S")
        img.close()
        return

    def updatePosition(self, alt, lat, lon, reflat, reflon):
        self.exif["GPS"][piexif.GPSIFD.GPSAltitude] = (alt, 1)
        self.exif["GPS"][piexif.GPSIFD.GPSLatitudeRef] = reflat;
        self.exif["GPS"][piexif.GPSIFD.GPSLatitude] = [lat, 1000000];
        self.exif["GPS"][piexif.GPSIFD.GPSLongitudeRef] = reflon;
        self.exif["GPS"][piexif.GPSIFD.GPSLongitude] = [lon, 1000000];
        exif_bytes = piexif.dump(self.exif)
        piexif.insert(exif_bytes, self.fname)

    def setDateOffset(self, off):
        self.sign,self.off = off

    def getDate(self):
        td = timedelta(hours=self.sign * self.off.hour, minutes=self.sign * self.off.minute, seconds=self.sign * self.off.second)
        return self.date + td

