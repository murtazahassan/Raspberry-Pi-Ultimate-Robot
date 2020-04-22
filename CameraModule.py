from picamera import PiCamera


def piCam(w=640,h=480,x=0,y=0,fill=False):
    camera = PiCamera()
    camera.resolution = (w,h)
    camera.start_preview(fullscreen=fill,window = (x,y,w,h))

if __name__ == '__main__':
    piCam()