from datetime import datetime,timedelta
import piexif
from PIL import Image
import logging, sys


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
        ratio = int(1e7)
        logging.debug("Writing exif data: ( alt: {} lat: {} lon: {} )".format(alt,lat,lon))

        altRef = 0
        if alt < 0:
            altRef = 1

        self.exif["GPS"][piexif.GPSIFD.GPSAltitudeRef] = altRef
        self.exif["GPS"][piexif.GPSIFD.GPSAltitude] = (int(abs(alt) * 1e2), int(1e2))
        self.exif["GPS"][piexif.GPSIFD.GPSLatitudeRef] = reflat
        self.exif["GPS"][piexif.GPSIFD.GPSLatitude] = (int(lat * ratio), ratio)
        self.exif["GPS"][piexif.GPSIFD.GPSLongitudeRef] = reflon
        self.exif["GPS"][piexif.GPSIFD.GPSLongitude] = (int(lon * ratio), ratio)
        exif_bytes = piexif.dump(self.exif)
        piexif.insert(exif_bytes, self.fname)

    def setDateOffset(self, off):
        self.sign,self.off = off

    def getDate(self):
        td = timedelta(hours=self.sign * self.off.hour, minutes=self.sign * self.off.minute, seconds=self.sign * self.off.second)
        return self.date + td

