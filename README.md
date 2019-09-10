<div align="center">

# CANNY EDGE DETECTION
</div>

Canny edge detection is a image processing method used to detect edges in an image while suppressing noise. The main steps are as follows:

1. Grayscale Conversion
Convert the image to grayscale

1. Gaussian Blur
Perform a Gaussian blur on the image. The blur removes some of the noise before further processing the image. A sigma of 1.4 is used in this example and was determined through trial and error.
1. Determine the Intensity Gradients
The gradients can be determined by using a Sobel filter where 
**A** is the image. An edge occurs when the color of an image changes, hence the intensity of the pixel changes as well.

1. Non Maximum Suppression
The image magnitude produced results in thick edges. Ideally, the final image should have thin edges. Thus, we must perform non maximum suppression to thin out the edges.

1. Double Thresholding
We notice that the result from non maximum suppression is not perfect, some edges may not actually be edges and there is some noise in the image. Double thresholding takes care of this. It sets two thresholds, a high and a low threshold. In my algorithm, I normalized all the values such that they will only range from 0 to 1. Pixels with a high value are most likely to be edges. For example, you might choose the high threshold to be 0.7, this means that all pixels with a value larger than 0.7 will be a strong edge. You might also choose a low threshold of 0.3, this means that all pixels less than it is not an edge and you would set it to 0. The values in between 0.3 and 0.7 would be weak edges, in other words, we do not know if these are actual edges or not edges at all. Step 6 will explain how we can determine which weak edge is an actual edge.
This threshold is different per image so I had to vary the values. In my implementation I found it helpful to choose a threshold ratio instead of a specific value and multiple that by the max pixel value in the image. As for the low threshold, I chose a low threshold ratio and multiplied it by the high threshold value:
```sh
highThreshold = max(max(im))*highThresholdRatio;
lowThreshold = highThreshold*lowThresholdRatio;
```
Doing this allowed me to successfully use approximately the same ratios for other images to successfully detect edges.


1. Edge Tracking by Hysteresis
Now that we have determined what the strong edges and weak edges are, we need to determine which weak edges are actual edges. To do this, we perform an edge tracking algorithm. Weak edges that are connected to strong edges will be actual/real edges. Weak edges that are not connected to strong edges will be removed. To speed up this process, my algorithm keeps track of the weak and strong edges that way I can recursively iterate through the strong edges and see if there are connected weak edges instead of having to iterate through every pixel in the image.

1. Cleaning Up
Finally, we will iterate through the remaining weak edges and set them to zero resulting in the final processed image:



# Orignal Image
![](https://github.com/shimaaelhosary/Canny-Edge-Detector/blob/master/screenshots/image.jpg)

# Result
![](https://github.com/shimaaelhosary/Canny-Edge-Detector/blob/master/screenshots/Capture.PNG) 







                    

