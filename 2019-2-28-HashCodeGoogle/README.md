To solve this problem in synthesis we have implemented an heuristic with some intuitions:
Seeing that taking 2 images, more tags have more is probable that the min of the max of the 3 parameters to evaluate is higher,
we first ordered all the images in a decreasing order of number of tags and we try to associated an image starting from the first after that image
to a fixed number of next images and then we take the best one ( the one that maximize the min of 3 parameters).
We choose to select this window of next images for a complexity problem in the bigger dataset and because in principle more are distant 2 images (distance =| number of tag1 - number of tag2 |)
more is proable that the evaluation (max of min) is lower
To put together the vertical images we adopt a simple strategy, after having ordered in decreasing order the vertical images by the number of tags we put together
the first 1 with the one that maximize the total number of tags in the final image.
As before for a problem of complexity we set a window to search the right one. We do this stuff with Vertical images before start to computing the slideshow
To exclude some images while we are searching the best one in the window, we use a simple Upper Bound that is the 1/2*min(TagImage1,TagImage2) that is the best that can do 2 nearby images


|When|Score|
|----------------------------|------------------|
| DURING THE CHALLENGE | 708,657          |
| AFTER THE CHALLENGE  | 988,295          |
| BEST SCORE AFTER THE CHALLENGE           | 1,255,321        |

