"""The code for finding the image segmentation is as follow:"""

# (1) for (int i = 0; i  inImage − height; ++i)
# (2) {
# (3)     for (int j = 0; j  inImage − width; ++j)
# (4)          {
# (5)       int bluePos = i * step + j * channels;
# (6)       int greenPos = i * step + j * channels + 1;
# (7)       int redPos = i * step + j * channels + 2;
# (8)
# (9)       unsigned char red = inPixel Data [redPos];
# (10)          unsigned char green = inPixel Data [greenPos];
# (11)          unsigned char blue = inPixel Data [bluePos];
# (12)          int redGreen = red – green;
# (13)          int redBlue = red – blue;
# (14)
# (15)        if ((red  mMinimumRed && red  mMaximumRed)
# (16)           && (redGreen  mRedGreenRangeMin
# (17)              && redGreen  mRedGreenRangeMax)
# (18)          &&(redBlue  mRedBlueRangeMin
# (19)              && redBlue  mRedBlueRangeMax))
# (20)        {
# (21)          //pixel is within floor range set to white
# (22)          outPixelData [redPos] = 255;
# (23)          outPixelData [greenPos] = 255;
# (24)          outPixelData [bluePos] = 255;
# (25)          ++total Pixels;
# (26)        }
# (27)        else
# (28)        {
# (29)          outPixelData [redPos] = 0;
# (30)          outPixelData [greenPos] = 0;
# (31)          outPixelData [bluePos] = 0;
# (32)       }
# (33)   }
# (34)