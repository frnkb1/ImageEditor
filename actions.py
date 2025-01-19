from PIL import Image
from typing import List

def mirror(raw: List[List[List[int]]])-> List[List[List[int]]]:

    #TODO
    for rows in raw:
        rows = rows.reverse()
    return raw


def grey(raw: List[List[List[int]]]) -> List[List[List[int]]]:
    """
    Assume raw is image data. Modifies raw "averaging out" each
    pixel of raw. Specifically, for each pixel it totals the RGB
    values, integer divides by three, and sets the all RGB values
    equal to this new value
    """
    for rownum in range(len(raw)):
        for pixelnum in range(len(raw[rownum])):
            avg = 0
            for rgb in range(len(raw[rownum][pixelnum])):
                avg = avg + raw[rownum][pixelnum][rgb]

            avg = int(avg / 3)
            for rgb in range(len(raw[rownum][pixelnum])):
                raw[rownum][pixelnum][rgb] = avg
    return raw


def invert(raw: List[List[List[int]]]) -> List[List[List[int]]]:
    """
    Assume raw is image data. Modifies raw inverting each pixel.
    To invert a pixel, you swap all the max values, with all the
    minimum values. See the doc tests for examples.
    """
    for rownum in range(len(raw)):
        for pixelnum in range(len(raw[rownum])):
            if not (raw[rownum][pixelnum].count(raw[rownum][pixelnum][0]) == (len(raw[rownum][pixelnum]))):
                max_index = [0]
                min_index = [0]
                max_ = max(raw[rownum][pixelnum])
                min_ = min(raw[rownum][pixelnum])

                # finding max value duplicates
                counter = 0
                for rgb in range(len(raw[rownum][pixelnum])):
                    if raw[rownum][pixelnum][rgb] == max_:
                        raw[rownum][pixelnum][rgb] = min_
                    elif raw[rownum][pixelnum][rgb] == min_:
                        raw[rownum][pixelnum][rgb] = max_

    return raw