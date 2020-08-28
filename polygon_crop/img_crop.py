from tkinter import *
import PIL
from PIL import Image, ImageTk, ImageDraw
import numpy as np
import sys
import cv2

class img_processing(object):

    def img_crop(self,img_array, winWidth = 500):
        """
        img_crop crop image based on the user defined polygon area

        Parameters
        ----------
        img_array : numpy array
            array of the image
        winWidth : int, optional
            window size of the open image, by default 500

        Returns
        -------
        numpy arr
            cropped image
        """
        pp = self._polygon_select(img_array, winWidth)
        newIm = self._polygon_crop(img_array, pp)
        return newIm


    def _polygon_select(self,img, basewidth = 500):
        cs = list()
        img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        length, wid, _ = img.shape

        wid_ratio = basewidth/wid
        baselength = int(round(length * wid_ratio))
        img = cv2.resize(img, dsize=(basewidth, baselength), interpolation=cv2.INTER_CUBIC)

        print("Press ESC to exit the edit mode")
        # mouse callback function
        def draw_circle(event,x,y,flags,param):

            if event == cv2.EVENT_LBUTTONDOWN:
                cv2.circle(img,(x,y),5,(0,0,255),-1)
                cs.append((int(round(x/wid_ratio)), int(round(y/wid_ratio))))
                print("click on x: " + str(x) + " y: " + str(y))


        cv2.namedWindow('image')
        cv2.setMouseCallback('image',draw_circle)

        while(1):
            cv2.imshow('image',img)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break

        cv2.destroyAllWindows()
        return cs

    def _polygon_crop(self,img_array, polygon):

        mask_img = Image.new('1', (img_array.shape[1], img_array.shape[0]), 0)
        ImageDraw.Draw(mask_img).polygon(polygon, outline=1, fill=1)
        mask = np.array(mask_img)

        new_img_array = np.empty(img_array.shape, dtype='uint8')
        new_img_array[:,:,:3] = img_array[:,:,:3]

        new_img_array[:,:,0] = new_img_array[:,:,0] * mask
        new_img_array[:,:,1] = new_img_array[:,:,1] * mask
        new_img_array[:,:,2] = new_img_array[:,:,2] * mask

        return new_img_array
