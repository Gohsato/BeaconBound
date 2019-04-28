# OpenCV
Some notes on opencv

## Core
top left is  (0,0)
bottom right is (len(x),len(y))

images are stored as (x,y,c)  
where c = (B,G,R) values

## Links

opencv concepts:
https://docs.opencv.org/3.4/d2/d96/tutorial_py_table_of_contents_imgproc.html

brightest pixel:
https://www.pyimagesearch.com/2014/09/29/finding-brightest-spot-image-using-python-opencv/

Thresholding:
https://docs.opencv.org/3.4/d7/d4d/tutorial_py_thresholding.html


## March 6th
Currently it works pretty well.

Three

Current Limitations:  
- the beacon needs to be the brightest thing.  
    - It can account for noise
    - another large, bright object will mess it up

Further work:
- Automate radius **selection**

## March 13th
Thought over the week of some new ideas:
- Use circle detection
- Find average brightness, find brightess pixel
  - Then calculate deviation, if deviation is big enough -> positive
- look at histograms for more ideas

Progress:
- made histogram

## March 18th
Work from this session:
- Circle detection is probably not worth the effort (its kinda really hard)
  - Might be able to do it after a threshold or something
  
- Finding the brightest pixel, then calculating the deviation works well
  
Consider square detection

Next step is to combine deviation-alg with threshold-alg
Then need to test.
can possibly improve deviation formula instead of max/avg.
IQR? std dev?

After detection engine is made
Also can do while waiting for more test data.
begin infrastucture for actual app.

next time:
- try square detection
- color sampling
- think about how to setup the app

## March 20th

Implemented FAST corner detection.
works well under some circumstaces, not under others

## April 3rd

Brightest pixel works well when elevation is low
- may have to tune the threshold with some kind of dynamic value that could use the time-order of the pictures to calculate the threshold

Future work on alg:
- use different color sampling
- try to go back to square detection? need to know if there'll be squares
  
For now need to switch to infrastructure
- algorithm can just be brightness devation based

Class: BeaconFinder
- Maintains state to have dynamic params
- can save images to file?

methods:
- consumes image filenames => bool if beacon found
- method to return params

## April 10th

