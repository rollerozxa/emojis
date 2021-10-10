import os
from pathlib import Path

OPTIMIZE_PNG = True

def inkscape_convert(source, output_prefix, width, height):
	return os.system('inkscape %s.svg -o %s%s.png -w %s -h %s' % (source, source, output_prefix, width, height))
	
def optipng(image):
	return os.system('optipng -o7 -zm1-9 -nc -strip all -clobber %s.png' % image)

vectors = Path("./").glob("*.svg")

for vector in vectors:
	print("Rasterizing "+vector.stem+"...")
	# Large PNG (512x512)
	vector_png = Path(vector.stem+".png")
	if not vector_png.exists():
		print("   Rasterizing to 512x512")
		inkscape_convert(vector.stem, '', 512, 512)
		if OPTIMIZE_PNG: optipng(vector.stem)
	else:
		print("   512x512 already exists!")
	
	# Small PNG (50x50), intended for using on Discord without Nitro
	vector_png = Path(vector.stem+"_50x.png")
	if not vector_png.exists():
		print("   Rasterizing to 50x50")
		inkscape_convert(vector.stem, '_50x', 50, 50)
		if OPTIMIZE_PNG: optipng(vector.stem+'_50x')
	else:
		print("   50x50 already exists!")

