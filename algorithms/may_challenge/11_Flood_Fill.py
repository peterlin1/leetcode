class Solution(object):

    def floodFill(self, image, sr, sc, newColor):
        """
        An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from
        0 to 65535).

        Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel
        value newColor, "flood fill" the image.

        To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the
        starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those
        pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the
        aforementioned pixels with the newColor.

        At the end, return the modified image.

        277 / 277 test cases passed.
        Status: Accepted
        Runtime: 76 ms
        Memory Usage: 14.1 MB


        Parameters
        ----------
        image : list

        sr : int

        sc : int

        newColor : int


        Returns
        -------
        ret : list


        Examples
        --------
        >>> Solution().floodFill([[1, 1, 1],
        ...                       [1, 1, 0],
        ...                       [1, 0, 1]], 1, 1, 2)
        [[2,2,2],[2,2,0],[2,0,1]]

        """

        if image[sr][sc] == newColor:
            return image

        self._origColor = image[sr][sc]

        def _fill_pixel(row, col):
            if (0 <= row < len(image)) and (0 <= col < len(image[0])) and image[row][col] == self._origColor:
                image[row][col] = newColor
                _fill_pixel(row + 1, col)
                _fill_pixel(row - 1, col)
                _fill_pixel(row, col + 1)
                _fill_pixel(row, col - 1)

        _fill_pixel(sr, sc)
        return image
