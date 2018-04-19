"""The pseudocode for finding the threshole of the photo is as follow:"""

# (1) for (int i = start Y; i  height; ++i)
# (2) {
# (3)     for (int j = start X; j  width; ++j)
# (4)    {
# (5)        unsigned char blue = pixel Data [i * step + j * channels];
# (6)        unsigned char green = pixel Data [i * step + j * channels + 1];
# (7)        unsigned char red = pixel Data [i * step + j * channels + 2];
# (8)
# (9)         if (red == 0 && green == 0 && blue == 0)
# (10)           {
# (11)                  continue;
# (12)          }
# (13)
# (14)      //Find thersholds
# (15)      if (red  mMinimumRed)
# (16)      {
# (17)        mMinimumRed = Red;
# (18)      }
# (19)
# (20)      if (red  mMaximumRed)
# (21)      {
# (22)                  mMaximumRed = Red;
# (23)      }
# (24)
# (25)      int redGreenRange = red – green;
# (26)      int redBlueRange = red – blue;
# (27)
# (28)      if (redGreenRange  mRedGreenRangeMin)
# (29)      {
# (30)           mRedGreenRangeMin = redGreenRange;
# (31)      }
# (32)
# (33)      if (redGreenRange  mRedGreenRangeMax)
# (34)     {
# (35)        mRedGreenRangeMax = redGreenRange;
# (36)      }
# (37)
# (38)      if (redBlueRange  mRedBlueRangeMin)
# (39)     {
# (40)        mRedBlueRangeMin = redBlueRange;
# (41)      }
# (42)
# (43)      if (redBlueRange  mRedBlueRangeMax)
# (44)      {
# (45)           mRedBlueRangeMax = redBlueRange;
# (46)      }
# (47)   }
# (48) }