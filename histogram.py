from __future__ import print_function
from __future__ import division
import cv2 as cv
import numpy as np
HIST_SIZE = 256
HIST_RANGE = (0, 256) # the upper boundary is exclusive
ACCUMULATE = False

hist_w = 512
hist_h = 400
bin_w = int(round( hist_w/HIST_SIZE ))


def color_hist(src):
    bgr_planes = cv.split(src)
    histImage = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)
    b_hist = cv.calcHist(bgr_planes, [0], None, [HIST_SIZE], HIST_RANGE, accumulate=ACCUMULATE)
    g_hist = cv.calcHist(bgr_planes, [1], None, [HIST_SIZE], HIST_RANGE, accumulate=ACCUMULATE)
    r_hist = cv.calcHist(bgr_planes, [2], None, [HIST_SIZE], HIST_RANGE, accumulate=ACCUMULATE)
    cv.normalize(b_hist, b_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
    cv.normalize(g_hist, g_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
    cv.normalize(r_hist, r_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
    for i in range(1, HIST_SIZE):
        cv.line(histImage, ( bin_w*(i-1), hist_h - int(round(b_hist[i-1][0])) ),
                ( bin_w*(i), hist_h - int(round(b_hist[i][0])) ),
                ( 255, 0, 0), thickness=2)
        cv.line(histImage, ( bin_w*(i-1), hist_h - int(round(g_hist[i-1][0])) ),
                ( bin_w*(i), hist_h - int(round(g_hist[i][0])) ),
                ( 0, 255, 0), thickness=2)
        cv.line(histImage, ( bin_w*(i-1), hist_h - int(round(r_hist[i-1][0])) ),
                ( bin_w*(i), hist_h - int(round(r_hist[i][0])) ),
                ( 0, 0, 255), thickness=2)
    cv.imshow('Source image', src)
    cv.imshow('calcHist Demo', histImage)

def grey_hist(src):
    src = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    histImage = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)
    hist = cv.calcHist(src, [0], None, [HIST_SIZE], HIST_RANGE, accumulate=ACCUMULATE)
    cv.normalize(hist, hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
    for i in range(1, HIST_SIZE):
        cv.line(histImage, ( bin_w*(i-1), hist_h - int(round(hist[i-1][0])) ),
                ( bin_w*(i), hist_h - int(round(hist[i][0])) ),
                ( 255, 0, 0), thickness=2)
    cv.imshow('calcHist Demo', histImage)


if __name__ == "__main__":
    src = cv.imread('negatives/15442923.jpg')
    grey_hist(src)
    cv.waitKey(0)
    exit()
    