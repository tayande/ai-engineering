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
**note**
I took some exercises in math on each of the operations in vectors
