import glob
from PIL import Image
for infile in glob.glob("ThinkBig.png"):
   img = Image.open(infile)
   img.thumbnail((128, 128), Image.ANTIALIAS)
   if infile[0:2] != "Th_":
      img.save("Th_" + infile, "png")
