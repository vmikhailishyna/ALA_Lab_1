# ALA_Lab_1

Theoretical questions 2 points
1. 0.25pts What are linear transformations?
A linear transformation is a mapping between vector spaces that preserves vector addition and scalar multiplication.

2. 0.25pts What is a linear transformation matrix and how can it be interpreted?

Every linear transformation φ from an n-dimensional vector space into an m-dimensional vector space can be represented by an m*n matrix A, called the matrix representation of φ.
Geometrically, it describes how the basis vectors of space transform (stretch, rotate, reflect, share) => how all space is modified.

3. 0.25pts What features and properties does a rotation matrix have?
A rotation matrix will always be a square matrix. As a rotation matrix is always an orthogonal matrix the transpose will be equal to the inverse of the matrix. The determinant of a rotation matrix will always be equal to 1.

4. 0.25pts Suppose some arbitrary linear transformation has been performed; how do you find the linear transformation matrix that will return everything to its original form? Is it always possible to perform an inverse transformation?

If A⁻¹ exists, then it has the property that when multiplied by the original matrix A, the result is equal to the identity matrix I. That is, we must use the formula A⁻¹ * A = I.
The inverse transformation exists only if determinant A  != 0.

5. 1pts The absolute value of the determinant of a transformation matrix is less than 1, what conclusions can be drawn about this transformation (how does space change under this transformation)? What if it is greater than 1? Equal to 1? Equal to 0?

The absolute value of the determinant is less than 1. The transformation results in a contraction of space. That is, any object or area in the original space will be scaled by the coefficient of the determinant, and since it is less than 1, this will result in a reduction of the object in space. 

The absolute value of the determinant is greter than 1. Here, the opposite will be true compared to a determinant that is less than zero. That is, the transformation expands either the space or the object.

The absolute value of the determinant is equal to 1.
The figures remain unchanged in size. But displacement may occur.

The absolute value of the determinant is equal to 0.
The area can become linear.
