from __future__ import absolute_import
import time
import logging
import os
import requests
from PIL import Image
from io import BytesIO


class CameraCapture(object):
    def __init__(self, url="http://127.0.0.1:8080/?action=snapshot",
                 timeout=10, verify=False):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        self.url = url
        self.timeout = int(timeout)
        self.verify = verify
        self.logger.info("CameraCapture initialized")

    def get_img(self):
        self.logger.info("Getting image")
        res = requests.get(
            self.url, stream=True, timeout=self.timeout, verify=self.verify
        )
        img = Image.open(BytesIO(res.content))
        self.logger.info("img type: {}".format(type(img)))
        return img
