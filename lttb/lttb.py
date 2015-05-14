import math


def largest_triangle_three_buckets(data, threshold):
    """
    Return a downsampled version of data.

    Parameters
    ----------
    data: list of lists
        data must be formated this way: [[x,y], [x,y], [x,y], ...]
    threshold: int
        threshold must be >= 2 and <= to the len of data

    Returns
    -------
    data, but downsampled using threshold
    """

    # Check if data and threshold are valid
    if not isinstance(data, list):
        raise Exception("incorrect data provided")
    if not isinstance(threshold, int) or threshold <= 2 or threshold >= len(data):
        raise Exception("threshold not well defined")
    for i in data:
        if not isinstance(i, list) or len(i) != 2:
            raise Exception("incorrect data provided")

    # Bucket size. Leave room for start and end data points
    every = (len(data) - 2)/(threshold - 2)

    a = 0  # Initially a is the first point in the triangle
    next_a = 0
    max_area_point = (0, 0)

    sampled = [data[0]]  # Always add the first point

    for i in range(0, threshold-2):
        # Calculate point average for next bucket (containing c)
        avg_x = 0
        avg_y = 0
        avg_range_start = math.floor((i+1)*every) + 1
        avg_range_end = math.floor((i+2)*every) + 1
        avg_rang_end = avg_range_end if avg_range_end < len(data) else len(data)

        avg_range_length = avg_rang_end - avg_range_start

        while avg_range_start < avg_rang_end:
            avg_x += data[avg_range_start][0]
            avg_y += data[avg_range_start][1]
            avg_range_start += 1

        avg_x /= avg_range_length
        avg_y /= avg_range_length

        # Get the range for this bucket
        range_offs = math.floor((i+0)*every) + 1
        range_to = math.floor((i+1)*every) + 1

        # Point a
        point_ax = data[a][0]
        point_ay = data[a][1]

        max_area = -1

        while range_offs < range_to:
            # Calculate triangle area over three buckets
            area = math.fabs((point_ax - avg_x)*(data[range_offs][1] - point_ay) - (point_ax - data[range_offs][0])*(avg_y-point_ay))*0.5
            if area > max_area:
                max_area = area
                max_area_point = data[range_offs]
                next_a = range_offs  # Next a is this b
            range_offs += 1

        sampled.append(max_area_point)  # Pick this point from the bucket
        a = next_a  # This a is the next a (chosen b)

    sampled.append(data[len(data)-1])  # Always add last

    return sampled