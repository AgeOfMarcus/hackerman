import pyscreenshot as ImgGrab

def box(x1,y1,x2,y2):
	im = ImgGrab.grab(bbox=(x1,y1,x2,y2))
	return im.tobytes()
def all():
	im = ImgGrab.grab()
	return im.tobytes()