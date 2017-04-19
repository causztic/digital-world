import cv2
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from camera.camerabase import CameraBase

class CameraOpenCV(CameraBase):
    '''
    Implementation of CameraBase using OpenCV
    '''
    _update_ev = None

    def __init__(self, **kwargs):
        self._device = None
        self.frame = None
        super(CameraOpenCV, self).__init__(**kwargs)

    def init_camera(self):
        # consts have changed locations between versions 2 and 3
        PROPERTY_WIDTH = cv2.CAP_PROP_FRAME_WIDTH
        PROPERTY_HEIGHT = cv2.CAP_PROP_FRAME_HEIGHT
        PROPERTY_FPS = cv2.CAP_PROP_FPS
        # create the device
        self._device = cv2.VideoCapture(0)
        # Set preferred resolution
        self._device.set(PROPERTY_WIDTH,
                          self.resolution[0])
        self._device.set(PROPERTY_HEIGHT,
                          self.resolution[1])
        # and get frame to check if it's ok
        ret, frame = self._device.read()

        # source:
        # http://stackoverflow.com/questions/32468371/video-capture-propid-parameters-in-opencv # noqa
        self._resolution = (int(frame.shape[1]), int(frame.shape[0]))
        # get fps
        self.fps = self._device.get(PROPERTY_FPS)

        if self.fps <= 0:
            self.fps = 1 / 30.

        if not self.stopped:
            self.start()

    def _update(self, dt):
        if self.stopped:
            return
        if self._texture is None:
            # Create the texture
            self._texture = Texture.create(self._resolution)
            self._texture.flip_vertical()
            self.dispatch('on_load')
        try:
            ret, frame = self._device.read()
            self._format = 'bgr'
            self.frame = frame
            try:
                self._buffer = frame.imageData
            except AttributeError:
                # On OSX there is no imageData attribute but a tostring()
                # method.
                self._buffer = frame.tostring()
            self._copy_to_gpu()
        except:
            Logger.exception('OpenCV: Couldn\'t get image from Camera')

    def start(self):
        super(CameraOpenCV, self).start()
        if self._update_ev is not None:
            self._update_ev.cancel()
        self._update_ev = Clock.schedule_interval(self._update, self.fps)

    def stop(self):
        super(CameraOpenCV, self).stop()
        if self._update_ev is not None:
            self._update_ev.cancel()
            self._update_ev = None