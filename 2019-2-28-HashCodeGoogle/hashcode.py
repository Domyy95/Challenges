from __future__ import division

import sys
import numpy as np
import operator
import hashlib

# To solve this problem in synthesis we have implemented an heuristic with some intuitions:
# Seeing that taking 2 images, more tags have more is probable that the min of the max of the 3 parameters to evaluate is higher,
# we first ordered all the images in a decreasing order of number of tags and we try to associated an image starting from the first after that image
# to a fixed number of next images and then we take the best one ( the one that maximize the min of 3 parameters).
# We choose to select this window of next images for a complexity problem in the bigger dataset and because in principle more are distant 2 images (distance =| number of tag1 - number of tag2 |)
# more is proable that the evaluation (max of min) is lower
# To put together the vertical images we adopt a simple strategy, after having ordered in decreasing order the vertical images by the number of tags we put together
# the first 1 with the one that maximize the total number of tags in the final image.
# As before for a problem of complexity we set a window to search the right one. We do this stuff with Vertical images before start to computing the slideshow
# To exclude some images while we are searching the best one in the window, we use a simple Upper Bound that is the 1/2*min(TagImage1,TagImage2) that is the best that can do 2 nearby images

# SCORE      : 708,657
# SCORE AFTER: 988,295
# BEST SCORE : 1,255,321

windowVertical = 1000
windowSlideShow = 1000


class Photo:
    def __init__(self, idPhoto, photo_type, num_tags, tags):
        self.num_tags = num_tags
        self.photo_type = photo_type
        self.tags = tags
        self.idPhoto = idPhoto


class Slide:
    def __init__(self, photos):
        self.photos = []
        self.tags = set()
        for photo in photos:
            self.photos.append(photo.idPhoto)
            self.tags |= set(photo.tags)

    def __str__(self):
        output = ""
        for idPhoto in self.photos:
            output += str(idPhoto) + " "
        output += "\n"
        return output


class Slideshow:
    def __init__(self, slides):
        self.slides = slides

    def __str__(self):
        output = str(len(self.slides))
        output += "\n"
        for slide in self.slides:
            output += slide.__str__()
        return output


def parse_input(file):
    photos = []
    with open(file, "r") as f:
        for i, line in enumerate(f):
            if i == 0:
                num_collections = line
            else:
                values = line.split(" ")
                num_tags = values[1]
                photos.append(
                    Photo(i - 1, values[0], values[1], values[2 : int(num_tags) + 2])
                )
    return int(num_collections), photos


def dump_slideshow(file, slideshow):
    with open(file, "w") as f:
        f.write("{} ".format(slideshow))
        f.write("\n")


def print_photos(photos):
    for photo in photos:
        print(photo.num_tags, photo.photo_type)


# Returns slides
def adjustVerticalList(verticalPhotos):
    slides = []

    while len(verticalPhotos) > 1:
        current_first_vertical = verticalPhotos.pop(0)
        current_second_vertical = verticalPhotos[0]

        slide = Slide([current_first_vertical, current_second_vertical])

        best_max = len(slide.tags)

        current_best_index = 0

        for indexVerticalPhoto in range(0, min(windowVertical, len(verticalPhotos))):
            current_second_vertical = verticalPhotos[indexVerticalPhoto]
            slide = Slide([current_first_vertical, current_second_vertical])
            current_best_max = len(slide.tags)
            if current_best_max > best_max:
                best_max = current_best_max
                current_best_index = indexVerticalPhoto

        slides.append(
            Slide([current_first_vertical, verticalPhotos.pop(current_best_index)])
        )

    return slides


def horizontalPhotosToSlide(horizontalPhotos):
    slides = []

    for photo in horizontalPhotos:
        slides.append(Slide([photo]))

    return slides


def main():
    num_collections, photos = parse_input(sys.argv[1])

    photos = sorted(photos, key=operator.attrgetter("num_tags"), reverse=True)

    slides = []
    slides.extend(
        horizontalPhotosToSlide(list(filter(lambda r: r.photo_type == "H", photos)))
    )
    slides.extend(
        adjustVerticalList(list(filter(lambda r: r.photo_type == "V", photos)))
    )
    slides_output = []

    slides_output.append(slides.pop(0))

    # Larry Page hire us

    while len(slides) > 0:
        current_slide = slides_output[len(slides_output) - 1]
        best_index_min = 0
        best_min = 0

        for current_index in range(0, min(len(slides), windowSlideShow)):
            slide = slides[current_index]
            upper_bound = min(len(current_slide.tags), len(slide.tags)) / 2
            if upper_bound > best_min:
                similarity = min(
                    len(current_slide.tags - slide.tags),
                    len(slide.tags - current_slide.tags),
                    len(slide.tags & current_slide.tags),
                )
                if similarity > best_min:
                    best_min = similarity
                    best_index_min = current_index

        slides_output.append(slides.pop(best_index_min))

    dump_slideshow(
        sys.argv[2] if len(sys.argv) > 2 else "out.txt", Slideshow(slides_output)
    )


if __name__ == "__main__":
    main()
