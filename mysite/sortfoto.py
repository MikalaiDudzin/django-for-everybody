import piexif
import os
import shutil


directory = 'D:\Project\pythonProject\Myphotos'
files = os.listdir(directory)
files_get = filter(lambda x: x.endswith('.jpg') or x.endswith('.JPG') or x.endswith('.mp4') or x.endswith('.MP4'), files)
os.chdir('D:\Project\pythonProject\Myphotos')


for x in files_get:
    print(x)

    if (os.path.isdir(x) == False):
        try:
            foto = piexif.load(x)
        except Exception:
            qq = None
        else:
            qq = None

            for i in ("0th", "Exif", "GPS", "1st"):
                for tag in foto[i]:
                    if ((piexif.TAGS[i][tag]["name"] == "DateTime") or (
                    (piexif.TAGS[i][tag]["name"] == "DateTimeOriginal"))):
                        qq = foto[i][tag]

        if (qq == None):

            g = "0000-00-00"
        else:
            qq = qq.decode("utf-8")
            qq = qq[0:7]
            qq = qq.replace(":", "-")
            g = qq

        z = g[5:7]


        if (z == "01"):
            zz = "январь"
        elif (z == "02"):
            zz = "февраль"
        elif (z == "03"):
            zz = "март"
        elif (z == "04"):
            zz = "апрель"
        elif (z == "05"):
            zz = "май"
        elif (z == "06"):
            zz = "июнь"
        elif (z == "07"):
            zz = "июль"
        elif (z == "08"):
            zz = "август"
        elif (z == "09"):
            zz = "сентябрь"
        elif (z == "10"):
            zz = "октябрь"
        elif (z == "11"):
            zz = "ноябрь"
        elif (z == "12"):
            zz = "декабрь"
        else:
            zz = "no"

        g = g[0:5] + zz

        if (os.path.exists(g) != True):

            os.mkdir(g)

        shutil.copyfile(x, g + "/" + x)
        os.remove(x)