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

# Thursday: 5th november; 2026
## The chain rule

Quick refresher: a derivative is a rate of change: how much the output moves when you nudge the input a little. You’ve used it as velocity = dx/dt. A few you’ll need:

f(x)  |	f′(x)
xⁿ	 | n·xⁿ⁻¹
sin x| cos x
eˣ	| eˣ
a·x (a constant) | a


The problem: a neural network isn’t one simple function. It’s functions inside functions inside functions. How do you find the derivative of something like y = sin(x²)?

The problem: a neural network isn’t one simple function. It’s functions inside functions inside functions. How do you find the derivative of something like y = sin(x²)?
The chain rule: if y = f(g(x)), then
`dy/dx = f′(g(x)) × g′(x)`

In words: differentiate the outside function (leaving the inside alone), then multiply by the derivative of the inside. Each link in the chain contributes its own local rate, and you multiply them together.
Worked example: y = sin(x²)
`Inside: g = x², so g′ = 2x`
`Outside: f = sin(g), so f′ = cos(g) = cos(x²)`
`Multiply: dy/dx = cos(x²) × 2x`

An intuition from physics: if a car’s position depends on time, and fuel used depends on position, then the fuel rate per second = (fuel per metre) × (metres per second). Rates multiply along a chain.
Longer chains work the same way, one factor per link:
`y = f(g(h(x)))   →   dy/dx = f′(g(h(x))) × g′(h(x)) × h′(x)`
Why AI cares: every layer of a neural network is one link in this chain. To train it, you need to know how the final error changes when you nudge each weight, and the chain rule is exactly how that’s calculated. This algorithm is called backpropagation.


# Tuesday: 10th November; 2026
## Computational graphs
To let a computer apply the chain rule automatically, we first break any calculation into small steps, one basic operation each (add, multiply, square, and so on). Drawing those steps as a diagram gives a computational graph.
- Each node is a value, either an input or the result of one operation.
- Each edge shows which values feed into which operation.
Example: `f = (x + y) · z`, with `x = 2, y = 3, z = 4.`
```python
x ──┐
    (+) ── q ──┐
y ──┘          (×) ── f
z ─────────────┘
```
Running it left to right is the forward pass:
- `q = x + y = 5`
- `f = q · z = 20`
Each operation is simple enough that its own derivative is easy. These are the local derivatives, which only look at that one node:
- `For q = x + y: ∂q/∂x = 1 and ∂q/∂y = 1`
- `For f = q · z: ∂f/∂q = z = 4 and ∂f/∂z = q = 5`

Local derivatives are cheap because each node only has to know its own operation. Nobody has to differentiate the whole expression at once. The chain rule from Topic 1 then says: to get the derivative of f with respect to any input, multiply the local derivatives along the path from that input to f. Doing this systematically is the next topic.
An autograd engine like the Value class you’ll build records exactly this graph as the forward pass runs, so each value remembers which operation made it and which values it came from.


# Friday: 13th November; 2026.
## Lesson 1.06: probability and distribution
### Why ai cares about probability
All predictions a model makes is are a probability distribution. A classifier says “91% cat, 6% dog, 3% bird”, and a language model picks the next word from thousands of options, each with a probability. Training is about making those predicted probabilities match reality.
### Basic probability rules
Sample space and events:
- The sample space S is the set of all possible outcomes. For one die roll, S = {1, 2, 3, 4, 5, 6}.
- An event is a group of outcomes you care about. “Rolling an even number” is the event {2, 4, 6}.
- When all outcomes are equally likely:
```python
P(event) = (number of outcomes in the event) ÷ (total number of outcomes)
P(even) = 3/6 = 0.5
```
#### The three rules everything is built on
- A probability is never negative.
- Something always happens: P(S) = 1.
- If A and B can’t both happen, then P(A or B) = P(A) + P(B).
#### Two useful consequences:
- “Not”: P(not A) = 1 − P(A). The chance of not rolling a 6 is 1 − 1/6 = 5/6.
- “Or” when they can overlap: P(A or B) = P(A) + P(B) − P(A and B). You subtract the overlap so it isn’t counted twice.
#### Conditional probability: “given that…”
P(A | B) means “the probability of A, given that B has happened.” You narrow your world down to just B:
`P(A | B) = P(A and B) ÷ P(B)`
Example (a deck of 52 cards): what’s the chance a card is a King, given that it’s a face card (J, Q or K)?
- There are 12 face cards, 4 of them Kings.
- P(King | Face) = (4/52) ÷ (12/52) = 4/12 = 1/3
Knowing “it’s a face card” changed the chance of a King from 4/52 (about 8%) to 1/3 (about 33%).
#### Independence
Two events are independent if knowing one tells you nothing about the other. Then:
`P(A and B) = P(A) × P(B)`
- Two coin flips are independent: the first doesn’t affect the second.
- Drawing two cards without putting the first back is not independent: the first draw changes what’s left in the deck.

# Sunday: 15th November; 2026
## Random variables, PMF vs PDF, and common distributions
### What is a random variable?
A random variable (written with a capital letter, like X) is a number whose value depends on a random outcome.
- Roll a die: X = the number that comes up (1 to 6)
- Flip a coin: X = 1 for heads, 0 for tails
- Measure someone’s height: X = the height in cm
The point is to turn outcomes into numbers, so we can do maths with them: averages, spreads, and so on. There are two kinds:
- Discrete: which can take separate and countable values. eg include: die roll, number of emails per hour, which class an image belongs to.
- Continuous: Which can take any value in a range. eg include: height, temperature, time and a model's weights.
### PMF: probabilities for discrete variables
A probability mass function (PMF) gives the probability of each exact value: P(X = k).
For a fair die, two rules always hold and they include: 1. Every probability is between 0 and 1, and 2. They all add up to 1.
### PDF: density for continuous variables
For a continuous variable, the chance of hitting one exact value is zero. The probability that someone is exactly 170.000000… cm tall is 0. So instead we use a probability density function (PDF), f(x), and get probabilities from areas under its curve: `P(a ≤ X ≤ b) = area under f(x) between a and b`
A physics analogy: think of a rod with a mass density in kg/m. The density at a single point isn’t a mass; you only get mass by integrating over a length. Probability density works the same way. That’s also why a density value can be greater than 1, while the total area under the curve must equal 1.
### The five common distributions
A distribution is just a particular pattern of probabilities. These five come up constantly:
- Bernoulli: This models one yes/no trial with success chance p. It is given by `P(1) = p, P(0) = 1 − p`. It is used in AI for binary classification.
- Categorical: This models one trial with k possible outcomes. it is given by `P(X = i) = pᵢ, all pᵢ add to 1`. It is used in AI for multi-class classification.
- Uniform: This models all outcomes equally likely. it is given by `Continuous on [a, b]: f(x) = 1/(b − a)`. It is used in AI for random initial weights.
- Normal (Gaussian): This models the bell curve, centred at mean `μ` with spread `σ`. It is given by `f(x) = (1/(σ√(2π))) · e^(−(x−μ)²/(2σ²))`. it is used in AI for weight initialization, noise and errors.
- Poisson: This models How many rare events happen in a fixed interval, at average rate `λ`. it is given by `P(X = k) = λᵏ e^(−λ) / k!`. it is used in ai for counting events.
You may know Poisson from radiation physics: the number of decays a detector counts per second follows a Poisson distribution.
A rule of thumb for the normal distribution:
- about 68% of values fall within 1σ of the mean
- about 95% within 2σ
- about 99.7% within 3σ
### Quick worked examples:
- Bernoulli: a model says an email is spam with p = 0.8. Then P(spam) = 0.8 and P(not spam) = 0.2.
- Poisson: a server gets on average λ = 2 requests per second. What’s the chance of exactly 0 requests in a second?
`P(X = 0) = 2⁰ × e⁻² / 0! = 1 × 0.135 / 1 ≈ 0.135`
(Remember 0! = 1 and anything⁰ = 1.)
- Uniform: for a weight drawn uniformly between −1 and 1, the density is f(x) = 1/(1 − (−1)) = 0.5 everywhere in that range.

# Monday. 16th November; 2026.
## Expected value and variance
These are the two numbers that summarise any distribution: where its centre is and how spread out it is.
### Expected value: the weighted average
The expected value E[X] (also called the mean, μ) is the average result you’d get if you repeated the experiment many, many times. For a discrete variable, multiply each value by its probability, then add them up:
`E[X] = Σ xᵢ × P(xᵢ)`
Example: a fair die
`E[X] = 1×(1/6) + 2×(1/6) + 3×(1/6) + 4×(1/6) + 5×(1/6) + 6×(1/6)
     = 21/6 = 3.5`
     
You can never actually roll a 3.5. The expected value is the long-run average, not a value you’ll necessarily see.
Physics link: this is exactly the centre of mass formula, x̄ = Σ mᵢxᵢ / Σ mᵢ, with probabilities as the masses. Since probabilities add up to 1, there’s nothing to divide by. The expected value is the balance point of the distribution. Example: unequal probabilities. A game pays ₦100 with probability 0.2, and ₦0 with probability 0.8:
`E[X] = 100 × 0.2 + 0 × 0.8 = ₦20`
On average you’d win ₦20 per game, so paying more than ₦20 to play would lose money in the long run.
### Variance
This is the average squared distance from the mean. Two distributions can have the same mean but very different spreads:
- Always getting 50 has mean 50.
- Getting 0 or 100 with a coin flip also has mean 50.
Variance measures that spread: the average of the squared distances from the mean.
`Var(X) = E[(X − μ)²] = Σ (xᵢ − μ)² × P(xᵢ)`
There’s also a shortcut that’s often quicker:
`Var(X) = E[X²] − (E[X])²`
Standard deviation σ = √Var(X). It’s in the same units as X, so it’s easier to interpret than variance.
Why square the distances? Without squaring, distances above and below the mean would cancel out and always add up to zero. Squaring makes every distance positive, and it penalises big deviations more than small ones.
Example: the 0-or-100 coin game (mean 50)
`Var = (0 − 50)² × 0.5 + (100 − 50)² × 0.5
    = 2500 × 0.5 + 2500 × 0.5 = 2500
σ = √2500 = 50`
For “always 50,” the variance is 0: there’s no spread at all.
Physics link: variance is the moment of inertia about the centre of mass, Σ mᵢ(xᵢ − x̄)². Mass far from the centre counts more, just like outcomes far from the mean.
### Formulas for the common distributions
- Bernoulli (p)-0. With mean `p` and variance `p(1 − p)`
- Poisson (λ). With mean `λ` and variance `λ`
- Uniform on [a, b]. With mean `(a + b)/2` and variance `(b − a)²/12`
- Normal (μ, σ). With mean `μ` and variance `σ²`
Notice that Bernoulli’s variance p(1 − p) is largest at p = 0.5, when the result is most uncertain, and zero at p = 0 or 1. You’ll recognise Poisson’s “mean = variance” from counting statistics in radiation physics: the √N uncertainty on N counts.
### Why this matters in the field of AI engineering.
- The loss function is an expected value. Training minimises the average error over all the data.
- Variance shows stability. If the gradients vary a lot from batch to batch, training is noisy and jumpy. Many techniques (bigger batches, momentum, Adam) exist to reduce that variance.
- Weight initialisation sets the variance of the starting weights carefully. Too large and the signals explode through the layers; too small and they fade away.
- Normalisation layers (like batch norm) rescale data to mean 0 and variance 1.


# Tuesday. 17th November; 2026
## Joint and marginal distributions
So far we’ve looked at one random variable at a time. In real data, things come in pairs or groups: weather and whether people carry umbrellas, a patient’s age and their dose, an email’s words and whether it’s spam. A joint distribution describes two variables together.
### The joint distribution
P(X, Y) gives the probability of each combination of values. With two variables, it’s easiest to show as a table.
Example: X = weather, Y = whether someone carries an umbrella.
	        | No umbrella (Y=0)	    | Umbrella (Y=1)
Sun (X=0)	| 0.40	                | 0.10
Rain (X=1)	| 0.05	                | 0.45
Each cell is the probability of that pair. For example, P(Rain and Umbrella) = 0.45. All four cells together add up to 1.
### Marginal distributions
“sum out” the other variable
Often you want the probability of just one variable, ignoring the other. You get it by adding across a row or down a column:
`P(X = x) = Σ over all y of P(X = x, Y = y)`
	        | No umbrella	| Umbrella	| P(weather)
Sun	        | 0.40	        | 0.10	    | 0.50
Rain	    | 0.05	        | 0.45	    | 0.50
P(umbrella)	| 0.45	0.55	| 1.00
- P(Rain) = 0.05 + 0.45 = 0.50
- P(Umbrella) = 0.10 + 0.45 = 0.55
They’re called marginal because they’re literally written in the margins of the table.
### Conditional probability from the table
This connects back to Step 1. To find P(Umbrella | Rain), narrow your world down to the Rain row and divide by that row’s total:
`P(Umbrella | Rain) = P(Rain and Umbrella) ÷ P(Rain) = 0.45 ÷ 0.50 = 0.90`
So 90% of people carry an umbrella when it rains, but only 0.10 ÷ 0.50 = 20% do when it’s sunny.
### Checking independence
From Step 1: X and Y are independent if `P(X and Y) = P(X) × P(Y)` for every cell.
Check one cell: `P(Rain and Umbrella) = 0.45, but P(Rain) × P(Umbrella) = 0.50 × 0.55 = 0.275`.
They’re not equal, so weather and umbrellas are not independent. That makes sense: knowing it’s raining tells you a lot about umbrellas.
If they were independent, every cell would just be “row total × column total,” and knowing the weather would tell you nothing about umbrellas.
### Why it matters to AI
- A dataset is a joint distribution. Training data pairs inputs with labels, P(image, label). A model learns how they relate.
- Prediction is conditional probability. A classifier estimates P(label | input): “given this image, how likely is each class?”
- Marginals appear when you “average out” what you don’t know, which is central to Bayes’ theorem in Lesson 1.07 and to generative models later.
- Naive Bayes (Lesson 1.07) works by assuming features are independent so it can just multiply probabilities, even though that’s rarely exactly true.


# Thursday: 19th November; 2026
## The normal distribution and the Central Limit Theorem
### The normal distribution (bell curve)
What matters in this context most is its shape and its two settings:
- μ (mean): where the centre of the bell is
- σ (standard deviation): how wide the bell is
It’s symmetric around μ, most values sit near the middle, and values far from the middle become rare very quickly.
*** The 68–95–99.7 rule:***
Range	| Share of values inside it
μ ± 1σ	| about 68%
μ ± 2σ	| about 95%
μ ± 3σ	| about 99.7%
Example: adult heights with μ = 170 cm and σ = 10 cm. About 95% of people are between 150 and 190 cm, and someone over 200 cm (3σ above the mean) is in the top 0.15%.
*** The standard normal *** has μ = 0 and σ = 1. Any normal value can be converted to it with a z-score:
`z = (x − μ) / σ`
The z-score tells you how many standard deviations a value is from the mean. A height of 185 cm gives z = (185 − 170)/10 = 1.5.
### The Central Limit Theorem (CLT)
This is the reason the normal distribution shows up everywhere: 
If you add up or average many independent random values, the result is approximately normal, whatever the shape of the original distribution (as long as its variance is finite).
Example with dice:
- 1 die: flat. Each number from 1 to 6 is equally likely.
- Average of 2 dice: a triangle. Middle values like 3.5 are more likely, because there are more ways to make them.
- Average of 30 dice: almost a perfect bell curve centred at 3.5.
Each die is flat, but their average is a bell. The more values you average, the closer to normal it gets, and the narrower it becomes: the spread of the average shrinks like σ/√n.
*** Physics link: *** this is why measurement errors are usually normal. Each reading is affected by many small independent disturbances (temperature, electronics noise, vibration), and their combined effect is a bell curve. It’s also why repeating a measurement n times shrinks the uncertainty of the average by √n.
### Why this matters to AI:
- Weight initialisation: network weights usually start as small random values from a normal distribution.
- Noisy gradients: in training, each batch’s gradient is an average over many examples, so by the CLT the noise in it is roughly normal.
- Normalisation: data is often converted to z-scores (mean 0, standard deviation 1) so all features are on the same scale.
- Generative models: diffusion models start from pure normal noise and turn it step by step into an image.


# Friday 20th November; 2026
## log probabilities.

### The problem: multiplying tiny numbers
Many AI calculations multiply lots of probabilities together. For example, a language model scores a sentence by multiplying the probability of each word:
`P(sentence) = P(word 1) × P(word 2) × P(word 3) × …
            = 0.01 × 0.003 × 0.02 × …`
Each probability is small, so the product shrinks very fast. After a few hundred words, the true answer is so tiny that the computer can’t store it and rounds it to exactly 0. This is called underflow. Once it’s 0, you can’t compare sentences anymore: every long sentence looks equally “impossible.”
You can see it in Python:
`
p = 1.0
for i in range(400):
    p *= 0.01
print(p)    # prints 0.0, the real answer is 10^-800
`
### The fix: use logarithms
Logs turn multiplication into addition:
`log(a × b) = log(a) + log(b)`
So instead of multiplying probabilities, we add their logs:
`
So instead of multiplying probabilities, we add their logs:
`
Adding numbers like −4.6 never underflows. A 400-word sentence just gives a large negative number like −1842, which the computer handles easily.
```python
import math
log_p = 0.0
for i in range(400):
    log_p += math.log(0.01)
print(log_p)    # about -1842.07, no underflow
```
(In AI, “log” usually means the natural log, ln.)
### What log probabilities look like
Probability	    | Log probability (ln)
1.0 (certain)	| 0
0.5	            | −0.69
0.1         	| −2.30
0.01	        | −4.61
close to 0	    | very negative
Three things to remember:
- Since probabilities are between 0 and 1, log probabilities are always ≤ 0.
- Closer to 0 means more likely; more negative means less likely.
- Logs keep the order: if P(A) > P(B), then log P(A) > log P(B). So you can compare or maximise log probabilities instead of probabilities and get the same answer.
### The link to the loss function
When training, we want the model to give high probability to the correct answers. Taking logs, that means making the log probability as high as possible. Training tools prefer to minimise a number, so we flip the sign:
`loss = −log P(correct answer)`
This is called the negative log-likelihood, and it’s the same thing as the cross-entropy loss you saw in Lesson 1.09’s report:
Model’s probability for the correct class	| Loss = −ln(p)
0.9 (confident and right)	                | 0.11 (small)
0.5 (unsure)	                            | 0.69
0.1 (confident and wrong)	                | 2.30 (large)
0.01	                                    | 4.61 (very large)
The loss grows sharply as the probability of the right answer approaches 0, so confident wrong answers are punished heavily. That’s exactly what we want a model to learn from.
### why this matters to ai:
- Language models add up log probabilities of tokens instead of multiplying probabilities.
- Every classifier and LLM is trained by minimising −log P(correct answer), i.e. cross-entropy.
- Naive Bayes (Lesson 1.07) adds log probabilities of words so long emails don’t underflow.
- PyTorch has log_softmax built in for this reason, which is where Step 7 picks up.

# Saturday, 21st November; 2026
## Softmax: turning scores into probabilities
### The problem
At the end of a classifier, the network produces one raw number per class, called a logit (or score):
`cat: 2.0    dog: 1.0    bird: 0.1`
These aren’t probabilities. They can be negative, bigger than 1, and they don’t add up to 1. We need to turn them into a proper probability distribution (Step 2’s categorical distribution).
### The softmax formula
`softmax(zᵢ) = e^(zᵢ) / (e^(z₁) + e^(z₂) + … + e^(zₙ))`
Two steps:
- Exponentiate each score: e^z is always positive, so no negatives.
- Divide by the total: so everything adds up to 1.
Worked example: scores [2.0, 1.0, 0.1]
Class	| Score z	| e^z	    | e^z ÷ total
cat	    | 2.0	    | 7.389	    | 7.389 ÷ 11.212 = 0.659
dog	    | 1.0	    | 2.718	    | 2.718 ÷ 11.212 = 0.242
bird	| 0.1	    | 1.105	    | 1.105 ÷ 11.212 = 0.099
total		        | 11.212	| 1.000
So the model says “66% cat, 24% dog, 10% bird.”
Properties:
- Every output is between 0 and 1, and they always add up to 1.
- The order is kept: the highest score always gets the highest probability.
- e^z exaggerates differences: a score 1 higher means about 2.7× more probability. That’s why it’s called “soft” max: it leans strongly toward the biggest score without completely ignoring the others.
### The overflow problem and the “subtract the max” trick
e^z grows extremely fast. With scores like [1000, 1001, 1002], e^1000 is far too big for the computer to store. It becomes inf (infinity), and inf ÷ inf gives nan (“not a number”). This is a classic reason training suddenly shows loss = nan.
The fix: subtract the largest score from every score first:
`[1000, 1001, 1002] − 1002 = [−2, −1, 0]`
Now the biggest exponent is e⁰ = 1, so nothing can overflow. And the answer is exactly the same, because subtracting a constant c from every score multiplies the top and bottom of the fraction by the same e^(−c), which cancels out:
`e^(zᵢ − c) / Σ e^(zⱼ − c) = (e^(zᵢ) · e^(−c)) / (Σ e^(zⱼ) · e^(−c)) = e^(zᵢ) / Σ e^(zⱼ)`
### Log-softmax
Remember Step 6: training uses −log(probability of the correct class). Instead of computing softmax and then taking the log (which can give log(0) = −infinity for tiny probabilities), libraries compute log-softmax directly in one stable step:
`log_softmax(zᵢ) = (zᵢ − max) − log(Σ e^(zⱼ − max))`
PyTorch’s cross-entropy loss uses this internally.
### The code (plain functions)
```python
import math

def softmax(scores):
    biggest = max(scores)
    exps = []
    for s in scores:
        exps.append(math.exp(s - biggest))
    total = sum(exps)
    result = []
    for e in exps:
        result.append(e / total)
    return result

print(softmax([2.0, 1.0, 0.1]))
print(softmax([1000, 1001, 1002]))
```
### Why this matters to AI
- Every classifier ends with softmax to produce class probabilities.
- Language models apply softmax over their whole vocabulary to choose the next word.
- Attention in transformers uses softmax to decide how much each word should focus on every other word.
- Temperature (Lesson 1.16) divides the scores before softmax to make outputs more or less random.

# Tuesday. 24th November; 2026
## sampling and the Central Limit Theorem.
### Sampling
Sampling means generating random values that follow a distribution. It's how a language model picks its next word, and how we can check our formulas by simulation. 
#### The building block: random.random()
`import random`
random.random() gives a random decimal between 0 and 1, with every value equally likely (a uniform distribution). Every other kind of sampling is built from it.
#### Sampling a Bernoulli (a biased coin)
To get "1" with probability p: draw a random number, and if it's below p, return 1. Since the number is uniform on 0 to 1, it lands below 0.8 exactly 80% of the time.
```python
def sample_bernoulli(p, n):
    samples = []
    for i in range(n):
        if random.random() < p:
            samples.append(1)
        else:
            samples.append(0)
    return samples
```
#### Sampling a categorical (choosing one of several options)
For probabilities [0.7, 0.2, 0.1] (cat, dog, bird), imagine the line from 0 to 1 cut into pieces of those sizes:
`0 ────── cat ────── 0.7 ── dog ── 0.9 ─ bird ─ 1.0`
Draw a random number and see which piece it lands in. The pieces end at the running totals: 0.7, 0.9, 1.0.
```python 
def sample_categorical(probs, n):
    cumulative = []
    total = 0
    for p in probs:
        total += p
        cumulative.append(total)     # [0.7, 0.9, 1.0]

    samples = []
    for i in range(n):
        r = random.random()
        for j in range(len(cumulative)):
            if r <= cumulative[j]:
                samples.append(j)    # j = which option was chosen
                break                # stop at the first piece it fits in
    return samples
```
break exits the inner loop as soon as the right piece is found. This is the same idea a language model uses to pick the next word from its softmax probabilities.
#### The Central Limit Theorem, by simulation
This averages n_dice dice rolls, and repeats that many times:
```python
def average(values):
    return sum(values) / len(values)

def clt_demo(n_dice, n_averages):
    averages = []
    for t in range(n_averages):
        rolls = []
        for i in range(n_dice):
            rolls.append(random.randint(1, 6))
        averages.append(average(rolls))
    return averages
```
#### Testing it
```python
flips = sample_bernoulli(0.8, 10000)
print(average(flips))

animals = sample_categorical([0.7, 0.2, 0.1], 10000)
print(animals.count(0) / 10000, animals.count(1) / 10000, animals.count(2) / 10000)

avg1 = clt_demo(1, 5000)
avg30 = clt_demo(30, 5000)
print(average(avg1), average(avg30))
```
.count(x) counts how many times x appears in a list.

# Thursday. 26th November; 2026
## Bayes' theorem
### The puzzle
A disease affects 1 in 10,000 people. A test for it is 99% accurate: it catches 99% of sick people, and wrongly flags only 1% of healthy people. You test positive. What's the chance you actually have the disease?
Most people guess 99%. The real answer is under 1%. Bayes' theorem explains why.
### Where the formula comes from
From 1.06, conditional probability works in both directions:
```python
P(A | B) = P(A and B) / P(B)
P(B | A) = P(A and B) / P(A)
```
Both share P(A and B). From the second line, P(A and B) = P(B | A) × P(A). Substitute that into the first line:
`P(A | B) = P(B | A) × P(A) / P(B)`
That's Bayes' theorem. It lets you flip a conditional probability: if you know P(positive | sick), you can work out P(sick | positive), which is the one you actually care about.
### The four parts
Part	| Name	| Meaning in the medical example
P(A)	| Prior	| Your belief before the evidence: how common the disease is (1 in 10,000)
P(B | A)	| Likelihood	| How likely the evidence is if A is true: P(positive | sick) = 0.99
P(B)	| Evidence	| How likely the evidence is overall, from everyone: P(positive)
P(A | B)	| Posterior	| Your updated belief after the evidence: P(sick | positive)
In words: posterior = likelihood × prior ÷ evidence.
### Finding the evidence term
P(positive) counts every way of testing positive: sick people who test positive, plus healthy people who are wrongly flagged:
```p
P(positive) = P(pos | sick) × P(sick) + P(pos | healthy) × P(healthy)
            = 0.99 × 0.0001 + 0.01 × 0.9999
            = 0.000099 + 0.009999
            = 0.010098
```
This is called the law of total probability: add up the probability of the evidence across every possibility. It's the same "sum across the row" idea as the marginals.
### Solving the puzzle
`P(sick | positive) = 0.99 × 0.0001 / 0.010098 ≈ 0.0098 ≈ 0.98%`
### Why it's so low: count real people
Formulas can hide the intuition, so picture 1,000,000 people taking the test:
	| Test positive	| Test negative	| Total
Sick	| 99	| 1	| 100
Healthy	| 9,999	| 989,901	| 999,900
Total	| 10,098	| 989,902	| 1,000,000
Of the 10,098 positive results, only 99 are actually sick: 99 ÷ 10,098 ≈ 0.98%.
The test is good, but the disease is so rare that healthy people vastly outnumber sick ones. Even a 1% false-alarm rate, applied to almost a million healthy people, produces far more false positives than true ones. The prior matters enormously. This is why screening programmes use a second, confirmation test after a positive result.
### Why this matters to AI.
- Classifiers: a model's raw score has to be interpreted against how common each class is. A fraud detector that's "99% accurate" can still flag mostly innocent transactions if fraud is rare.
- Spam filters use Bayes to update "is this spam?" based on the words in an email.
- Naive Bayes is a real, fast text classifier built directly on this formula.
- Priors appear in training as regularisation.
