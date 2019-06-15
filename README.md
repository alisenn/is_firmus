# is_firmus
this is a python project which determines if two block forms a firmus

Although a firmus can be thought to exist in higher dimensions with more sophisticated blocks,
we will assume that the blocks have homogeneous mass distribution and are two dimensional.
Therefore, boxes can be assumed to be on a plane that is spanned by a Cartesian coordinate
system spanned by x and y axes. We will also assume that gravity acts in the −y direction.
Blocks’ edges are always parallel to the axes of the coordinate system.
For two blocks to form a firmus, the following conditions should be met:
I. The lower block should have its lower edge placed directly on the x axis.
II. The upper block should have its lower edge (at least partially) coincide with the upper edge
of the lower block.
III. The upper block should have its center of mass abscissa in the range of the lower block’s
upper edge.
Anything else is not a firmus.

A block will be provided as the following list: [x 1 , y 1 , x 2 , y 2 ], where (x 1 , y 1 ) and (x 2 , y 2 )
are the diagonal corners of the block. However, it is not known whether you are given the
(lower-left & upper-right) corners, or the (upper-left & lower-right) corners.
• The is firmus function should return one of the following lists:
– ["FIRMUS", area] if the two blocks form a firmus. area is a floating point number
for the area of the firmus.
– ["ADDENDUM", [x1, y1, x2, y2]] if the two blocks do not form a firmus but the
first two criteria to be a firmus hold. [x1, y1, x2, y2] are the diagonal coordinates
of the smallest third block which, when created and glued to the upper block, makes
the lower block and the extended upper block a firmus. With the extension, the upper
block should still be a rectangle.
– ["DAMNARE", area] in all other cases. area is a floating point number for the total
area covered by both blocks. Note that this area is not necessarily equal to the sum of
the two block’s areas since an overlapping area, if any, should be counted only once.
