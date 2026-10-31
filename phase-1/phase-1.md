# Linear Algebra Intuition



# VECTORS
a vector can be defined in three different ways, depending on the context:
- computer science: it is seen as a 1D array of list of numbers
- physics: it is a quantity that has both magnitude and direction.
- machine learning: it is a single data point and feature representation

## key terminology:
- dimension: this refers to the number of elements in a vector. 

## vector operations in AI
- vector addition: Adding corresponding elements of two vectors of the same size (a+b). it is used in neural networks when adding bias terms to layer inputs.
- Scalar multiplication: multiplying every element of a vector by a single number (c . a)
- Dot product: multiplying corresponding elements and summing them up (a . b)
- vector magnitude: this is obtained by squaring each of the elements in the vector, adding them together and taking the square root. the answer to the operation is what is said to be the magnitude of the vector written ass ||vector||.

#### Cosine similarity: 
**the problem** if you want to know if two sentences mean the same thing for instance( "how do i fic my car" vs, "where do i repair my automobile"), the sentences are not the same, so comparing them based on their lengths or exact word matches won't work wee. **The solution** Cosine similarity measures the angle between two vectors, regardless of their magnitude (length). 
- A score of 1.0 means they point in the exact smae direction (they have identical semantic meaning).
- A score of 0.0 means they are completely unrelated
- A score of -1.0 means they are exact opposites
#### how cosine similarity is computed
it is obtained by first of all taking the dot product of two vectors, then dividing it by the multiplication of the individual magnitudes of each vector. 
**note** I took some exercises in math on each of the operations in vectors

# Matrices
If a vector is a single point or line of data then a matrix is a 2d grid of numbers.

## The rule of matrix multiplication
- before multiplying two matrices (A * B), their inner dimensions must match. that is if matrix A has shape (m * n) and matrix B has shape (n * p), you can multiply them because the inner numbers (n) match. and the resulting matix C will have the outer dimensions: (m * p)
**note** I did some exercises on matrices tool

# Thursday: 29th october; 2026
## RECAP OF PHASE 1
##  PHASE 01: MATH FOUNDATIONS 
### Lesson 01: linear algebra
### Vectors
A vector in code is just a python list. And a list is a collection of a group of items that are arranged together, each item can be altered, and each item is separated by a comma and the whole list is enclosed by square bracket.
- did some examples and answered some questions about vectors
- did code practice on the concepts as well since i did not focus more on code the last time i studied the concept.
#### vector magnitude (The length of a vector)
using pure math by hand, this is derived by first of all taking the exponent of the elements in the vector then adding them together then taking the square root of the resulting sum. 
- in code, getting the square root of a number is done using the math module which i can import and use when i want to.
### Dot product
i also went through this one more time, this time focusing more on the code aspect and how to use it in the AI field.
i did not really spend much time here since i have done most of this before, i then went straight to cosine similarity.
### cosine similarity
This is seen as the angle between two arrows (vectors). the fomular is given by:
`cos θ = (a · b) / (|a| × |b|)`
***note*** the cosine similarity is always between 1 and -1 and that is because cosine in general never goes beyond these range. here is a simple table depicting some of the cosine meanings of some angles:
```python 
Angle θ |  cos θ	|  Meaning
0°	    |  1	    |  Pointing exactly the same way
60°     |  0.5	    |  Fairly similar direction
90°	    |  0        |  Perpendicular, unrelated
180°	|  −1	    |  Exactly opposite
```
There is a rule that guides the lengths here: 
- They are always positive, because when you square a negative number, it becomes positive.
I still went futher to practice the code for it and also understand it's implementation in python as well.

#### summary
```python
Function	| What it does
add(a, b)	| Adds vectors position by position
sub(a, b)	| Subtracts vectors position by position
mag(a)	    | Length of a vector
dot(a, b)	| Dot product
cosine_similarity(a, b)	| Angle-based similarity, from −1 to 1
```
all of the above were all implemented in code as well, and pushed to my forked repo too. 


### matrices
A matrix is defined in plain mathematics as a grid of numbers arranged in rows and columns. The arrangements in the rows and columns are know as the dimension of the matrix. In vector format, a matrix is a group of vectors with another having another right on top of it. In python, a matrix is a list of lists.
```python
m = [[1, 2],
     [3, 4],
     [5, 6]]
```
In python, this matrix (m) can be written on one line, but so far as this convention of putting it in a list is used corrected, python would always see and treat it as a matrix.
### reading a matrix in python
just like a list is treated in python, you can index out a particular element in the vectors that make up a matrix. for a matrix like m, it can be written like this: `m = [[1, 2], [3, 4], [5, 6]]`
so the following would be the elements of the matrix:
`m[0] = [1, 2]`, `m[0][1] = 2`, `m[2][1] = 6` etc.
### multiplying matrix by a vector
There is a rule to adhere to when doing multiplications of matrix by vectors: 
- The vector’s length must match the number of columns. If each row has 2 numbers, so the vector needs 2 numbers for the dot product to work.

# Saturday: 31st october; 2026
### matrix vector multiplication

### linear independence, basis and rank.
#### linear combinations
A linear combination can be defined as some amount of one vector, plus some amount of another.
here is a depiction of how it is done:
`3 × [1, 0]  +  4 × [0, 1]  =  [3, 4]`

#### span: everywhere you can reach
The span of some vectors is seen to be every point you can reach using linear combinations of them.
here is a picture of it:
`With [1, 0] and [0, 1] you can reach any point on the 2D plane: [x, y] = x·[1,0] + y·[0,1]. Their span is the whole plane`

#### linear independence
Trying` [1, 2]` and `[2, 4]`. You will notice that `[2, 4] = 2 × [1, 2]`. It points in the same direction, so it adds no new reach. Together they still only span a line.
This is a little bit complicated, but it is an occurrence that happens when a vector can be built from others.
When one vector can be built from the others, they’re linearly dependent, at least one is redundant. However, if none can be built from the others, they’re linearly independent. Each adds a new direction
In 2D, two vectors are dependent exactly when one is a multiple of the other, which means they lie on the same line.

#### Basis: the minimum set of building blocks
A basis is defined as a set of vectors that:
- can reach everything (spans the space), and
- has no redundant vectors (is linearly independent)

`[1, 0]` and `[0, 1]` are the standard basis for 2D, but `[1, 1]` and `[1, −1]` are a basis too. Any two vectors that don’t lie on the same line work. 2D always needs exactly 2 basis vectors, and 3D needs exactly 3. That number is the dimension.

#### Rank: how many dimensions a matrix really uses
The rank of a matrix is seen as the number of independent columns it has, which tells us how many dimensions its outputs can actually fill.

Rank matters because a rank-deficient matrix loses information: once points are squashed onto a line, you can’t tell where they started. In AI, rank also explains a popular technique called LoRA that i will be diving into very soon, which fine-tunes huge models by adding small low-rank matrices instead of changing everything.