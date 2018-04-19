"""THe pseudocode for the edge segmentation is as follow:"""

# (1) for (auto it = Filtered Lines. Begin (); it != Filtered Lines. end (); ++it)
# (2) {
# (3)    CvPoint poly Points ;
# (4)
# (5)    //First point is to the left of the right point
# (6)    if ((* it)   (* it) )
# (7)    {
# (8)       polyPoints  = cvPoint ((* it) , 0);
# (9)       polyPoints  = cvPoint ((* it) , 0);
# (10)          polyPoints  = cvPoint ((* it) , (* it) );
# (11)          polyPoints  = cvPoint ((* it) , (* it) );
# (12)     }
# (13)     else //First point is to the right of the right point
# (14)     {
# (15)        polyPoints  = cvPoint ((* it) , 0);
# (16)        polyPoints  = cvPoint ((* it) , 0);
# (17)        polyPoints  = cvPoint ((* it) , (* it) );
# (18)        polyPoints  = cvPoint ((* it) , (* it) );
# (19)     }
# (20)
# (21)     cv Fill ConvexPoly (inImage, &polyPoints , 4, cvScalar (0, 0, 0));
# (22) }