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

# Sunday: 1st November; 2026
# lesson 2
## Matrix Transformations & Eigenvalues.
### A matrix as a transformation
In lesson 2 we were more focused on the multiplication of matrices and vectors. Here we are looking at what that multiplication does. A 2×2 matrix takes every point in the plane and moves it somewhere else. The whole plane gets stretched, rotated, flipped, or squashed, and the matrix is the rule for those moves.
The key trick here is that the columns of a matrix show where the basis vectors land. In more clear terms, In 2D the basis vectors are `x̂ = [1, 0]` and `ŷ = [0, 1]`. If a matrix is `[[a, b], [c, d]]`, then x̂ lands at `[a, c]` and ŷ lands at `[b, d]`. Every other point follows, because every vector is some mix of x̂ and ŷ.
### The common transformations
- Scaling: [[2, 0], [0, 3]] stretches x by 2 and y by 3.
- Rotation by θ: [[cos θ, -sin θ], [sin θ, cos θ]] spins everything around the origin and preserves lengths.
- Reflection: [[1, 0], [0, -1]] flips across the x-axis.
- Shear: [[1, k], [0, 1]] slants the plane, like pushing the top of a deck of cards sideways.
- Projection: [[1, 0], [0, 0]] flattens everything onto a line, so information is lost.
### Composing transformations
Applying transformation A and then B equals multiplying by the single matrix BA, and the order matters. Rotate-then-scale is different from scale-then-rotate. This is why matrix multiplication isn’t commutative, and a neural network is a chain of such transformations. this means that transformation A and B is BA. keeping in mind that AB is not the same as BA.
### The determinant
The determinant of a matrix measures how much a transformation scales area. For `[[a, b], [c, d]]` it is ad - bc.
- det = 2 means areas double.
- det = 1 means area is preserved, as in a rotation.
- det < 0 means the plane is flipped.
- det = 0 means the plane is squashed onto a line or point. The matrix is singular, it loses information, and it can’t be inverted.
### The inverse
The inverse matrix A⁻¹ undoes A, so A⁻¹A = I. It exists only when det ≠ 0.
### Eigenvectors and eigenvalues
This is the main idea of the lesson. When a matrix transforms the plane, most vectors change direction. But some special vectors stay on their own line, and they only get stretched or shrunk. These are eigenvectors, and the stretch factor is the eigenvalue:
`A v = λ v`
Here A is the matrix, v is the eigenvector, and λ is the eigenvalue. Think of the eigenvectors as the “natural axes” of a transformation.
here are some of the meanings for different values of eigenvalue: 
- λ = 2 means the vector is stretched to twice its length.
- λ = 1 means it is unchanged.
- λ = 0 means it is crushed to nothing.
- λ < 0 means it is flipped.
How to find them: rearrange to `(A - λI)v = 0`. A non-zero v exists only when `det(A - λI) = 0`. This gives the characteristic equation, whose roots are the eigenvalues. Then plug each λ back in to find its eigenvector.
Here is a worked example: for A = `[[2, 0], [0, 3]]` the eigenvalues are 2 and 3, with eigenvectors along the x-axis and y-axis. For a pure rotation in 2D there are no real eigenvectors, because every direction changes.
### Why this matters for AI
- PCA (dimensionality reduction) uses the eigenvectors of the data’s covariance matrix, which point along the directions of most variation.
- Training stability: eigenvalues of the matrices in a network affect whether signals and gradients explode or vanish.
- Google’s original PageRank was an eigenvector problem.
- SVD, coming later in this phase, generalizes the same idea.
### Understanding check

# Monday: 2nd november; 2026
## Lesson 4: Calculus for ML: Derivatives & Gradients.
### The big idea: how does the output change when I nudge the input?
Machine learning is considered to be mostly one loop: make a prediction, measure how wrong it is (the loss), then adjust the model’s numbers to make the loss smaller. And that is where Calculus comes in, it tells us which direction to adjust and by how much.
### The derivative: the slope at a point
For a function f(x), the derivative f'(x) answers: if I nudge x a tiny bit, how much does f change? It is the slope of the curve at that point.
The definition uses a tiny step h:
`f'(x) ≈ (f(x + h) - f(x)) / h, as h → 0`
Example: f(x) = x². At x = 3, nudging x by 0.001 gives f = 9.006001, a change of about 0.006 for a step of 0.001. The slope is about 6, and that matches the rule f'(x) = 2x.
***What the sign and size tell you:***
- Positive slope: increasing x increases f.
- Negative slope: increasing x decreases f.
- Zero slope: a flat spot, which could be a minimum, a maximum, or a plateau.
### Rules you’ll use constantly
- Power rule: d/dx xⁿ = n·xⁿ⁻¹
- Constant multiple: d/dx [c·f] = c·f’
- Sum rule: the derivative of f + g is f’ + g’
- Product rule: (f·g)’ = f’g + fg’
- Chain rule (next lesson): for compositions like f(g(x)). It is what makes backpropagation work.
- Handy ones: d/dx eˣ = eˣ, d/dx ln x = 1/x, and the derivative of the sigmoid σ(x) is σ(x)(1 - σ(x)).
### Partial derivatives: many inputs
Real models have thousands or millions of parameters. For f(x, y) = x² + 3y, a partial derivative measures the change from nudging one input while holding the others fixed:
`∂f/∂x = 2x`
`∂f/∂y = 3`
### The gradient: all partials in one vector
The gradient stacks the partial derivatives into a vector:
`∇f = [∂f/∂x, ∂f/∂y, …]`
This ties back to Phase 1: the gradient is a vector, and it points in the direction of steepest increase of f. Its length says how steep that is. So the negative gradient points in the direction of steepest decrease.
### Gradient descent: the engine of ML
To minimize a loss, repeat:
`θ ← θ - α · ∇L(θ)`
Here θ is the parameters, ∇L is the gradient of the loss, and α is the learning rate, the step size. Imagine standing on a foggy hillside and always stepping downhill.
- α too small: you move painfully slowly.
- α too large: you overshoot the valley and bounce around or diverge.
- Non-convex losses: you can get stuck in local minima or flat saddle points, which is a real concern in deep learning.
### Checking your math: numerical gradients
Analytic derivatives are easy to get wrong, so we can check them with the nudge idea: compute (f(x + h) - f(x - h)) / 2h for each parameter and compare it to the formula. This is called gradient checking, and it’s a standard debugging tool when building neural networks.
### Why this matters for AI
Training any neural network is gradient descent on a loss function. Everything coming next, the chain rule, autodiff, and backpropagation, is about computing these gradients efficiently.
