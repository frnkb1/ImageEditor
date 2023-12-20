from PIL import Image
from typing import List

def mirror(raw: List[List[List[int]]])-> None:

    #TODO
    for rows in raw:
        rows = rows.reverse()
    return


def grey(raw: List[List[List[int]]]) -> None:
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
    return


def invert(raw: List[List[List[int]]]) -> None:
    """
    Assume raw is image data. Modifies raw inverting each pixel.
    To invert a pixel, you swap all the max values, with all the
    minimum values. See the doc tests for examples.

    >>> raw = [[[233, 100, 115], [0, 0, 0], [255, 255, 0]],[[199, 201, 116], [1, 9, 0], [255, 100, 100]]]
    >>> invert(raw)
    >>> raw
    [[[100, 233, 115], [0, 0, 0], [0, 0, 255]],
     [[199, 116, 201], [1, 0, 9], [100, 255, 255]]]
    """
    #TODO
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

    return