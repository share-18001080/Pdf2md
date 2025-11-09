## Tensors For Inquiring Minds

_**Tensors for Inquiring Minds**_ takes readers on a journey to discover tensors –
powerful mathematical concepts used in many areas of modern science.


Starting from the familiar ground of numbers and operations with numbers,
readers are invited to re-examine these ideas in a new light, slowly building towards a deep understanding of the advanced mathematical concepts which they
underpin. The overriding goal of this book is to explain tensors, specifically, by
showing them in action and in relation to less complicated concepts, such as
numbers and vectors.


**Features**

- Requires minimal mathematical pre-requisites beyond high-school algebra

- Written in an accessible, engaging style

- Full-color illustrations

- Numerous exercises for every chapter, including full solutions


**Yury Deshko** holds a Master’s in theoretical physics (with a focus on general relativity) from Belarus State University and a doctorate in physics from the Graduate Center of the City University of New York (CUNY). His research at CUNY
focused on experimental spectroscopy and diamond photonics. He served as a
research associate at City College of New York until joining the semiconductor
industry as a photonics engineer. Yury Deshko’s pedagogical passion led him to
teach, for a number of years, the introduction to the special theory of relativity in
summer schools of Johns Hopkins University and Columbia University.


## Tensors For Inquiring Minds

##### Yury Deshko


First edition published 2026
by CRC Press
2385 NW Executive Center Drive, Suite 320, Boca Raton FL 33431


and by CRC Press
4 Park Square, Milton Park, Abingdon, Oxon, OX14 4RN


_CRC Press is an imprint of Taylor & Francis Group, LLC_


© 2026 Yury Deshko


Reasonable efforts have been made to publish reliable data and information, but the author and publisher cannot assume responsibility for the validity of all materials or the consequences of their use.
The authors and publishers have attempted to trace the copyright holders of all material reproduced
in this publication and apologize to copyright holders if permission to publish in this form has not
been obtained. If any copyright material has not been acknowledged please write and let us know so
we may rectify in any future reprint.


Except as permitted under U.S. Copyright Law, no part of this book may be reprinted, reproduced,
transmitted, or utilized in any form by any electronic, mechanical, or other means, now known or
hereafter invented, including photocopying, microfilming, and recording, or in any information storage or retrieval system, without written permission from the publishers.


[For permission to photocopy or use material electronically from this work, access www.copyright.com](https://www.copyright.com)
or contact the Copyright Clearance Center, Inc. (CCC), 222 Rosewood Drive, Danvers, MA 01923,
[978-750-8400. For works that are not available on CCC please contact mpkbookspermissions@tandf.co.uk](mailto:mpkbookspermissions@tandf.co.uk)


_Trademark notice_ : Product or corporate names may be trademarks or registered trademarks and are
used only for identification and explanation without intent to infringe.


ISBN: 978-1-041-02644-0 (hbk)
ISBN: 978-1-041-00713-5 (pbk)
ISBN: 978-1-003-62036-5 (ebk)


[DOI: 10.1201/9781003620365](https://doi.org/10.1201/9781003620365)


Typeset in Latin Modern font
by KnowledgeWorks Global Ltd.


Publisher’s note: This book has been prepared from camera-ready copy provided by the authors.


###### _To Mom_ _With a Love_ _That_ _Only a Son_ _Can Have_ ♡ _Iryna Dziashko_ _1962-2025_


### Contents

Acknowledgments xi


Preface xiii


About the Author xv


Chapter 1 [■] Introduction 1


1.1 WHO NEEDS TENSORS? 2


1.2 NAIVE NOTION OF TENSORS 3


1.3 EXAMPLE DEFINITIONS 4


1.4 DIAGRAMS 6


1.5 SCHEMATICS 7


1.6 SETS AND TUPLES 8


Chapter 2 [■] Numbers and Functions 11


2.1 POWER OF ABSTRACTION 11


2.2 TERMINOLOGY BARRIER 14


2.3 ALGEBRA OF NUMBERS 15


2.3.1 Functions 15


2.3.2 Indexed Objects 20


2.3.3 Linear Functions 22


2.3.4 Function Composition 25


2.3.5 Partial Application 28


2.3.6 Function Representations 29


2.3.7 Numbers 31


2.3.8 Algebraic Structure 32


**vii**


**viii** - Contents


2.4 POWER OF NOTATION 35


2.4.1 Polynomial Example 35


2.5 EINSTEIN’S SUMMATION RULE 39


Chapter 3 [■] Arrows and Vectors 44


3.1 ARROWS 44


3.2 ALGEBRA OF ARROWS 46


3.2.1 Combining Arrows 46


3.2.2 Arrow Product 48


3.3 BASIS 50


3.3.1 Basis Notation 51


3.4 MANY BASES 52


3.4.1 Transposition 55


3.4.2 Going The Opposite Way 57


3.5 ORTHONORMAL BASES 60


3.6 VECTORS DEFINED 60


Chapter 4 [■] Operators 63


4.1 OPERATORS ON ARROWS 63


4.1.1 Rotation Operator 68


4.2 LINEAR OPERATORS 70


4.3 PLOTTING LINEAR OPERATORS 73


4.4 EIGEN-PROBLEM 76


4.5 DEGENERATE LINEAR OPERATORS 77


4.5.1 Determinant of a Linear Operator 78


4.6 USING OPERATOR COMPONENTS 80


4.7 COMPONENTS TRANSFORMATION 80


4.8 FIRST NOTION OF TENSOR 84


Chapter 5 [■] Tensors 87


5.1 SCALAR PRODUCT AND DOL-OPERATOR 87


5.2 SCALAR PRODUCT PROPERTIES 90


5.3 INNER OPERATIONS 94


Contents                             - **ix**


5.4 CONJUGATE OBJECTS 95


5.4.1 Partial Application 95


5.5 CONJUGATE VECTORS 97


5.6 OPERATORS ARE VECTORS 99


5.7 PROJECTORS 106


5.7.1 Projector Components 108


5.7.2 Composition of Projectors 109


5.8 TENSOR PRODUCT 111


5.8.1 Tensor Product 1 112


5.8.2 Tensor Product 2 112


5.8.3 Tensor Product 3 112


5.8.4 Tensor Product 4 113


5.9 TENSORS DEFINED 113


5.9.1 Other Definitions 114


Chapter 6 [■] Applications of Tensors 118


6.1 FAMOUS TENSORS 118


6.1.1 Metric Tensor 119


6.1.2 Anisotropy Tensor 123


6.1.3 Electromagnetic Tensor 130


6.2 COMPOUND NUMBERS 133


6.3 HAMILTONIAN MECHANICS 138


6.3.1 System and State 139


6.3.2 State Dynamics 143


6.4 VECTORS AND TENSORS IN COMPUTATION 147


Chapter 7 [■] Solutions 151


Index 173


### Acknowledgments

My sincere gratitude goes to all reviewers of the early drafts of the
book for their valuable feedback. In particular, I want to thank Dr. Alex
Rylyakov, Dr. Mikhail Makouski, Prof. Anton Kananovich, and Dr. Mohammad Teimourpour. To Dr. Teimourpour I must give separate thanks
for numerous discussions, helpful suggestions on material presentation,
and hospitality.

_My friends, discussing the book with you was both illuminating and_
_fun._

Finally, special acknowledgment must be given to my son, Daniel,
for his help with fixing colors in many figures.


Yury Deshko
Weehawken, New Jersey


**xi**


### Preface

One of the greatest powers of the human mind is its capacity for _abstrac-_
_tion_ . This capacity allows us to create and appreciate art, understand
concepts such as happiness, duty, and so on, and to create and use mathematical concepts as practical tools of immense power and beauty.

This book explores _tensors_ – a type of mathematical objects that extends the notion of numbers and vectors. The method of exploration is
deliberately chosen to resemble a journey. Starting from familiar grounds
of numbers and operations with numbers, a reader will re-examine familiar concepts in a new light and then will arrive at new concepts gradually,
connecting the dots along the way.

Although the topic of the book is mathematical, the exploration will
lack proper mathematical rigor, aiming instead at simplicity, clarity, and
the use of helpful analogies.

This book is **not intended** to substitute more serious textbooks on

linear algebra or tensor algebra. Hopefully, the main benefit of reading
this book – either before, or after, or in addition to other books on
the subject – is that it should help lower the _“mental barrier”_ we all
encounter when learning new concepts, especially abstract mathematical

concepts.

To comprehend and enjoy the material of this book, the reader should
have a solid knowledge of basic high-school algebra and an open and
inquiring mind. The book is a bit longer than it could have been because
all derivations are detailed and all exercises are fully solved.

Some sections are marked with an asterisk, for example, **Transpo-**
**sition*** . Those sections contain material that is either optional or a bit
more advanced than usual. These sections can be skipped without significant impact on the main message of the book.


**xiii**


### About the Author

Dr. Yury Deshko is an American physicist, educator, and writer. He
is the author of _“Special Relativity For Inquiring Minds”_ – a textbook
designed for undergraduate students and motivated high-schoolers.

When not working on applied physics problems in silicon photonics,
Yury develops and teaches modern physics courses (Special Relativity
and Quantum Physics) in summer schools for young aspiring physicists.


~~**xv**~~


C H A P T E R 1

### Introduction


ATHEMATICAL METHODS PLAY INCREASINGLY
# M important roles in many domains of science. Modern mathemati
cal tools are numerous and require serious effort to master. The algebra
and calculus of _tensors_ are good examples of this.
The goal of this book is to explain tensors by showing them in action
and in relation to less complicated mathematical objects, such as vectors and numbers. Understanding numbers and vectors is essential for
understanding tensors; therefore, the former two concepts are discussed
in details first.
The development of concepts will happen in the following direction:


Numbers → Vectors → Tensors.


We will start with reviewing numbers as the simplest mathematical objects, and will consider operations on numbers – functions – in a more
general and abstract way than one usually does in school. Many abstract
concepts related to numbers and functions will be useful for studying
vectors and tensors.

From numbers and numeric functions, we will move on to vectors.
Vectors are closely related to numbers and can’t even be properly defined without the latter. Vectors are more powerful than numbers and
represent the next step in the hierarchy of mathematical objects. Vectors and functions on vectors (operations or _operators_ ) provide many
new concepts that are crucial for understanding tensors.
Careful study of vectors and functions on vector (operators) will inevitably lead us to tensors. Tensors and vectors are as intimately related,
as vectors and numbers. In fact, having studied the basics of tensor algebra, we will see that numbers, vectors, and tensors are conceptually


[DOI: 10.1201/9781003620365-1](https://doi.org/10.1201/9781003620365-1) **1**


**2** - Tensors For Inquiring Minds


interconnected. We will be able to recognize that numbers are very _re-_
_duced_ tensors [1] ; it is said that numbers are tensors of _rank_ zero. In a
similar sense, vectors are incompletely reduced tensors; it is said that
vectors are tensors of rank one. Therefore, the progression of the topics
from numbers to tensors can be viewed as follows:


Numbers → Vectors → Tensors.


Tensors [(][0][)] → Tensors [(][1][)] → Tensors [(][2][+)] _._


Here the superscript in parentheses indicates the rank of the tensor [2] .
As we move from numbers to tensors, the level of abstraction increases. To a significant degree, the difficulty of understanding tensors
is due to a high level of abstraction used in the definition of tensors as
mathematical objects. Abstraction is the price we pay for more powerful and versatile tools. But more powerful tools are needed as scientists
address more and more advanced problems.
The inventions of numbers, algebra, and then calculus were monumental breakthroughs. The transition from numbers to vectors and then
to tensors is a more natural process that occurred rather quickly on the
scale of the history of science.


1.1 WHO NEEDS TENSORS?


Today thousands of scientists – among them many physicists and mathematicians – use the methods of tensors. Tensor mathematics – the al
gebra and calculus of tensors – is a _tool_ . It is a fitting tool for some
problems, and not too fitting for others. This situation is quite analogous to _vector algebra and calculus_ .
Tensor literacy will enrich you and will open doors to new problems
and new methods of analysis. The following historical episode illustrates
the point well.
In an October 1912 letter to a physicist Arnold Sommerfeld, Albert
Einstein said the following:


1In a certain sense which will become clear after reading the book.
2Don’t worry if the concept of _rank_ seems unclear right now – it will be explained
in due time.


Introduction                                - **3**


_Einstein on General Relativity_


“I am now exclusively occupied with the problem of gravitation theory and
hope, with the help of a local mathematician friend, to overcome all the difficulties. One thing is certain, however, that never in my life have I been quite
so tormented. A great respect for mathematics has been instilled within me,
the subtler aspects of which, in my stupidity, I regarded until now as a pure
luxury. Against this problem [of gravitation] the original problem of the theory
of relativity is child’s play.”


In the period from 1905 to 1916 Einstein was feverishly working on the
General Theory of Relativity – the next best theory of gravity since
Newton. The mathematics of General Relativity is based on the calculus
of tensors, created by Italian mathematicians Ricci-Curbastro and LeviCivita roughly a decade before Einstein started working on the problem
of gravity [3] .
To overcome the mathematical difficulties, Einstein used the help of
his friend and former classmate Marcel Grossmann, who was an expert
in tensor calculus and non-Euclidean geometry. The General Theory
of Relativity was the first physical theory to use the power of tensors
(in combination with profound physical insights) to achieve remarkable
breakthroughs in understanding nature. Since then, the methods of tensor calculus and non-Euclidean geometries have been used in many physical theories and problems.
At the end of the book (Section 6.4 on page 147), a less dramatic
example is given. The example describes a real-world situation when the
understanding of vectors and tensors may lead to significant practical
benefits.


1.2 NAIVE NOTION OF TENSORS


We may think of tensors as some kind of “super-numbers.” In what sense
tensors are numbers and what makes them “super?”
Similar to numbers, tensors can be added and subtracted. Also, tensors can be “scaled” by multiplying them by “normal” numbers like 2

or _π_ .


3See _Einstein’s Italian Mathematicians_ by Judith R. Goodstein.


**4** - Tensors For Inquiring Minds


In contrast with numbers, tensors support a richer set of operations.
Given two tensors, we can “kind-of-multiply” them to get either a simple number as the result ( _scalar product_, Section 5.1), or we can get
another tensor, somewhat “bigger” and more complex than the original
two ( _tensor product_, Section 5.8.)
Looking at the evolution of the concept of numbers, we can see the
series of steps to higher levels of _generality_, _efficiency_, and _abstraction_ :
From natural numbers to whole numbers, to fractions, to real, and then
to complex numbers. At each step new _mathematical objects_ are introduced, and these new objects can be added and multiplied in a “usual
way.”
Tensors appeared as the result of quite the natural evolution of
“number-like mathematical objects.” Tensors extend the notion of numbers, all the way through vectors into a new and very powerful realm. If
numbers are “bare quantities” and vectors are “quantities with direction”
(e.g., velocity in physics), then tensors are “quantities with shape.”
Tensors are naturally and closely connected with numbers and vectors. In fact, numbers and vectors _are tensors!_


_Tensors Naively Defined_


  - Tensors are _mathematical objects_ that cover and extend the concepts of numbers
and vectors. As more powerful mathematical objects, tensors support many algebraic operations, including addition, subtraction, and scaling by a number.


  - Tensors might be viewed as “quantities with shape,” in analogy with vectors –
“quantities with direction.”


  - Numbers and vectors represent the lowest “tiers” (called _ranks_ ) in the hierarchy of

tensors.


  - Finally, tensors generalize the idea of _linear functions_ (see Subsection 2.3.3 on
page 22 and also Section 4.2). Tensors of higher ranks can “act” on tensors of
lower ranks in a very simple way, resembling familiar multiplication.


1.3 EXAMPLE DEFINITIONS


Now, what are tensors more rigorously? Can we give a short definition
to this concept? Let us take a look at several examples and see whether
they shed sufficient light. Although the definitions given below differ
from each other, they convey _the same idea in different ways_ .


Introduction                                - **5**


The _Encyclopedia of Mathematics_ [4] provides the following definition:


**Tensors Definition 1**


Tensor on a vector space _V_ over a field _k_ is an element _t_ of the vector

space
_T_ _[p,q]_ ( _V_ ) = (⊗ _[p]_ _V_ ) ⊗(⊗ _[q]_ _V_ [∗] ) _,_


where _V_ [∗] = Hom( _V,k_ ) is the dual space of _V_ .


To understand this definition, we first need to understand what _vec-_
_tor space_ is, what _field_ is, what _dual_ means, and what is going on with
superscripts and circles (e.g., in ⊗ _[q]_ ).
Wolfram Math World [5] provides another view of tensors:


**Tensors Definition 2**


An _n_ th-rank tensor in _m_ -dimensional space is a mathematical object
that has _n_ indices and _m_ _[n]_ components and obeys certain transformation
rules.


Here we encounter new concepts, such as: _rank of a tensor_, _m_  _dimensional space_, _indices_, _components_, and some kind of _transformation_
_rules_ . They all will be discussed later in the book.
Yet another definition can be found in the book _Encyclopedia of_
_Mathematics_ [6]


**Tensors Definition 3**


Just as a _vector_ is a mathematical quantity that describes translations
in two- or three-dimensional space, a tensor is a mathematical quantity
used to describe general transformations in _n_ -dimensional space. Precisely,
if the locations of points in _n_ -dimensional space are given in one coordinate system by ( _x_ [1] _,x_ [2] _,. . .,x_ _[n]_ ) and in a transformed coordinate system
by ( _y_ [1] _,y_ [2] _,. . .,y_ _[n]_ ) (it is convenient to use superscripts rather than subscripts), then a “rank 1 contravariant tensor” is a quantity _T_, with single
components, that transforms according to the rule:



_n_
_Tnew_ _[i]_ [=] ∑
_r_ =1



_∂y_ _[i]_

_∂x_ _[r]_ _[T][ r][.]_



4
[https://encyclopediaofmath.org/wiki/Tensor](https://encyclopediaofmath.org/wiki/Tensor_on_a_vector_space) on ~~a v~~ ector ~~s~~ pace
[5https://mathworld.wolfram.com/Tensor.html](https://mathworld.wolfram.com/Tensor.html)
6 _Encyclopedia Of Mathematics_, James Tanton, Facts On File, Inc, 2005.


**6** - Tensors For Inquiring Minds


Again we face a wall of new concepts: _vectors_, _transformations_, _n_  _dimensional space_, _contravariant tensors_, and their _components_ . Without
clear understanding of these concepts, it is impossible to learn what

tensors are.

The definitions given above are typical. They provide a good way to
_end_ the study of tensors, to summarize everything learned about them.
However, they are not good starting points. It is better to arrive at the
concept of tensor gradually, going from numbers, through vectors, to
tensors. This path starts in the next chapters. But before we begin, a
couple of preliminary remarks are needed.


1.4 DIAGRAMS


Sometimes to illustrate mathematical concepts and _relations between_
_them_, we will use diagrams. Diagrams are helpful in highlighting some
general features of _mathematical structures_ .
Let us study an example, shown in Figure 1.1. A collection of cars
in a parking lot – Figure 1.1(a) – can be schematically represented as a
set of _points_ Λ – Figure 1.1(b). Each point of the set Λ corresponds to a
certain car in the parking lot. Apart from the set of cars Λ, Figure 1.1(b)


Figure 1.1 Diagrams are used to graphically represent sets of objects
and relationships between them. (a) Cars in a parking lot as an example
of a set. (b) Connections/relations between the set of cars and other sets,
such as numbers, colors, and True/False sets. Arrows can connect (map)
elements of one set with another. Such mappings may have names: **mlg**
returns mileage for a given car, **clr** – color, and **smk** determines whether
two cars are of the same make.


Introduction                                - **7**


contains other sets, denoted as _K_, _N_, and _B_ . These sets correspond to
various values of cars’ properties, such as color (set _K_ ), mileage (set _N_ ),
and so on. The set _B_ is a very important set – called a _Boolean set_ .
Boolean set has just two points, one labeled _t_ for True, the other labeled
_f_ for False.
Reduced to a point of the set Λ, a car loses its individuality and
those parameters that make it unique (make, color, mileage, etc.) This
is remedied by using other sets, such as the set of various colors _K_ or
the set _N_ of numbers that can represent mileage, and so on.
A particular property of a car-point can then be represented using
an arrow that connects the car-point to another point in the relevant
set. We say that such an arrow _maps_ points of one set into another set.
Figure 1.1(b) shows three possible maps: **mlg** gives the mileage for each
car from the set Λ, **clr** gives the color for each car, and **smk** compares
whether two cars have the same make. The names given to these mappings are in agreement with implicit mathematical convention to give
functions a two or three letter name, like sin, log, or exp.


**Exercise 1.1** _Extend the diagram from Figure 1.1(b), adding a set of_
_different car makes (e.g., Ford, Toyota, Fiat, etc.). Come up with a_
_mapping from this set into the Boolean set B._


1.5 SCHEMATICS


To illustrate the concepts of functions, operators, their structures, and
properties, we will be using schematics like the one shown in Figure 1.2.
A simple schematic element is represented as a box with inputs
and outputs. A box can have a name (label) which describes what the


Figure 1.2 Schematics can be used to represent functions, operators,
their compositions and structure.


**8** - Tensors For Inquiring Minds


function does to its input. The number of inputs and outputs can vary
depending on the complexity of a function.
Various “boxes” can be combined (or _composed_ ) to create a more
complex structure. Figure 1.2 shows how the outputs of a function **dup**
(duplicate its input) are connected to the inputs of a function ( **mul** )
that multiplies its inputs. The result is a function that squares its input.
The placement of inputs on the left and outputs on the right sides
of boxes is purely conventional. If preferred, equivalent schematics can
be drawn when the inputs come from the right, like they do in more
traditional notation of function application: sin _ϕ_ or exp _x_ .


1.6 SETS AND TUPLES


We will use many notational conventions in this book. Most of them will
be typical for mathematics. For example, “+” denotes summation of two
quantities, “=” means equality of two quantities, “∗” – a multiplication,
and the parentheses in “3 ∗( _x_ + _y_ )” are used to indicate the order in
which operations should be performed (first add and then multiply).
At a certain point, we will be discussing “assemblies” [7] of quantities.
The simplest example – all natural numbers:


1 _,_ 2 _,_ 3 _,_ 4 _,_ 5 _, ...,n, ...._


Or we can consider all letters of some alphabet:


a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z _._


Both these examples can be formally considered as _sets_ – an assembly
of objects of similar kind. A set can be given a special name when it is
often referred to. For example, the set of natural numbers is denoted as


N = {1 _,_ 2 _,_ 3 _, ..._ } _._


Note the use of curly braces – they indicate that we are talking about a
set. Thus, for a set S with elements _a, b, x_, and _y_ we write


S = { _a, b, x, y_ } _._


The concept of a set is one of the most basic concepts in mathematics
and the set notation is very standardized.


7Collections, ensembles, groups, and families – these terms already have reserved
specific mathematical meanings, although they express similar ideas.


Introduction                                - **9**


Another useful concept is called a _tuple_ . A tuple is a series of quantities that are related in a certain way but can be of different kinds. It
is better to study examples:


(3 _,_ ’a’) – couple (pair) _,_


→



→

( _a,_



_b,θ_ ) – triple _,_



( _x,_ 4 _,_



→ _a,_ sin) – quadruple.



A series of _n_ quantities is called _n_ -tuple.

The most familiar use of tuples is the representation of coordinates
of points in space. In two dimensional plane with Cartesian coordinate
axes _x_ and _y_ we may have:


( _x,y_ ) = (2 _,_ 5) – couple (pair) _._


In three dimensional space:


( _x,y,z_ ) = (0 _,_ 1 _,_ −2) – triple _._


Notice the difference between the coordinate tuples and the examples
given above: The tuples with coordinates contain only numbers, whereas,
in the examples above, tuples contain quantities of various types (number and a letter for the pair, two vectors and a number for the triple,
etc.). The point is that tuples _can_ contain quantities of the same type,
but in general, they do not. Another important difference between sets
and tuples is the importance of the order of elements inside the tuple.
Consider a set with two elements:


S = {0 _,_ 1} = {1 _,_ 0} _._


The order in which we write the elements does not matter. In contrast,
the order is important for tuples:


(0 _,_ 1) ≠(1 _,_ 0) _._


This inequality becomes obvious if we interpret these pairs as coordinates
of points in a plane. The first pair corresponds to the point on the _x_ axis,
while the second pair corresponds to the point on the _y_ axis.

Finally, the tuples can be used to concisely describe _mathematical_
_structures_ . As a simple example, consider the set of whole numbers
Z = {0 _,_ ±1 _,_ ±2 _, ..._ }. We can do many arithmetic operations with these


**10** - Tensors For Inquiring Minds


numbers, but let’s focus only on the operation of addition. We can summarize our intention using a triple as follows:


(Z _,_ + _,_ 0) _._


This expression says that we are studying a set of whole numbers Z
equipped with a single operation “+”. Moreover, we recognize that for
this operation there is a special element 0 with “neutral” behavior:


_n_ + 0 = 0 + _n_ = _n_


for any number _n_ from the set Z. We will encounter more examples of
this sort later in the book.


CHAPTER HIGHLIGHTS


  - _The natural evolution of mathematical objects from numbers,_

_through vectors, leads to tensors._


  - _Each successive tier of mathematical objects in the progression_

_“numbers, vectors, tensors” is more abstract and more powerful._


  - _Numbers, vectors, and tensors are all conceptually interconnected._


  - _Just like the use of vectors opens up new methods for solving ab-_

_stract and applied problems, the use of tensors opens up new, even_
_more powerful, methods for solving problems in various domains_
_of science._


  - _Diagrams and schematics are helpful for illustrating various math-_

_ematical relations and structures._


  _A set is an assembly of objects of a similar kind. It is one of the_

_most basic concepts in mathematics._


  _A tuple is an ordered sequence of elements related to each other_

_by a common context. The elements of a tuple can be of different_
_kinds._


C H A P T E R 2

### Numbers and Functions


UMBERS ARE POWERFUL MATHEMATICAL
# N objects. They are used in an endless list of problems that involve

_quantities_ . As mathematics and sciences progressed, natural numbers
evolved into whole numbers, then into rational numbers and beyond. [1]

At a certain stage, physics required a mathematical tool to describe
quantities with arbitrary directions. For example, the motion of a body
involves velocity – a physical quantity describing how fast the body
is moving and in what direction. Quite rapidly vectors led to tensors.
Tensors had to be invented because there are many important problems
where tensors are very natural. Examples will be given in the last chapter
of the book.

At first glance, numbers, vectors, and tensors appear rather different.
However, they have a lot in common. Tensors are “numbers on steroids”
because all operations you can do with numbers, you can do with tensors
– and even more.

Before we turn to tensors, we should familiarize ourselves with vectors. And before that, we must review the main concepts associated with
numbers.


2.1 POWER OF ABSTRACTION


Mathematics is a remarkably effective and universal discipline, its methods and results can be applied in a wide range of fields. In part, the
universality of mathematics stems from the _general_ and _abstract_ nature
of mathematical concepts. Let us illustrate this using an example.


1A superb account of this process is given in the book _Number: The Language of_
_Science_ by Tobias Dantzig.


[DOI: 10.1201/9781003620365-2](https://doi.org/10.1201/9781003620365-2) **11**


**12** - Tensors For Inquiring Minds


Figure 2.1 49 objects can be arranged in a square 7 × 7. 48 objects can
be arranged as a rectangle of 6 × 8.


An astute farmer notices that 49 sacks of grains can be arranged in
a square with each side having 7 sacks (see Figure 2.1). After one sack
is used up, the remaining 48 sacks can be arranged as a rectangle of 6
by 8 sacks.
The farmer realizes that this curious fact has nothing to do with either grains or sacks. The same observation could be made about buckets,
chairs, people, and so on. As the first step of generalization, the farmer
states that 49 _objects_ can be arranged as a 7 by 7 square, while 48 objects can be arranged as a 6 by 8 rectangle. The farmer also notices that
48 = 49 − 1, whereas 6 = 7 − 1 and 8 = 7 + 1. She writes down the newly
discovered relation as follows:


7 ∗ 7 obj − 1 obj = (7 − 1) ∗(7 + 1) obj _,_


where _obj_ is the denotation of _any_ object.
As the grain is used up, the farmer discovers two more relations:


6 ∗ 6 obj − 1 obj = (6 − 1) ∗(6 + 1) obj


and


5 ∗ 5 obj − 1 obj = (5 − 1) ∗(5 + 1) obj _._


At this point the farmer makes an educated guess, stating that a
more general relation must exist:


_n_ ∗ _n_ − 1 = ( _n_ − 1) ∗( _n_ + 1) _._ (2.1)


In the last expression, the reference to objects is dropped and the expression is written purely in terms of _numbers_ .
A deeper analysis reveals that the relation given by (2.1) exists for
_any quantities_ that obey the usual rules of addition and multiplication.


Numbers and Functions                      - **13**


This includes rational numbers, real numbers, complex numbers (see
Section 6.2), and even operators [2] ! The relation


_x_ [2] − 1 = ( _x_ − 1)( _x_ + 1) (2.2)


holds true because of the way we define _rules for manipulation_ – addition
and multiplication in this case – of number-like objects, regardless of
what those number-like objects represent in a particular problem.


Figure 2.2 Mathematical thinking has many levels of abstractions. Going to higher levels of abstractions results in higher efficiency and more
powerful ideas and tools. It also becomes more challenging to understand
and master more advanced concepts and methods.


The path from “sacks of grain” to a variable _x_ is the path from concrete, specific objects to _abstract_ entities that are the product of _creative_
_imagination_ . This path to higher levels of abstraction is illustrated in
Figure 2.2. As we move to higher levels of abstraction, our mathematical tools become more powerful and more universally applicable: From
everyday arithmetic to economics, to general relativity, and quantum
gravity.


2For now think of operators as functions that act on non-numeric arguments.


**14** - Tensors For Inquiring Minds


Using more abstract mathematical objects requires serious mental effort. To reach the highest levels one needs to do mathematics professionally. However, any profession can benefit from _some_ level of abstraction,
and to understand vectors and tensors, we must go beyond the usual
high-school level. One of the goals of this book is to help readers build
tolerance and appreciation of more abstract aspects of mathematics.


2.2 TERMINOLOGY BARRIER


Every high school student has a working knowledge of bilinear operators
over associative and commutative fields, but hardly any of those students are aware of this fact. We refer here to the ability to simply add
and multiply numbers. This demonstrates that even familiar and basic
notions may look complicated when “dressed in unfamiliar clothing.”

When we learn new mathematical concepts, especially at a higher
level of abstraction, we often encounter what might be called a _termi-_
_nology barrier_ : a concept seems more difficult if it is formulated in a new
language, without sufficient connections to already familiar concepts,
and without clear examples of how the concept can be applied.

The new terminology is unavoidable when learning new concepts.
There will be a number of new mathematical concepts and definitions
introduced in this book. To lower the terminology barrier, every new
mathematical concept will be illustrated with examples and connections
to already familiar concepts. Additionally, it is recommended to do the
following exercise every time a new concept with unusual terminology is
introduced:


_Dealing With New Concepts_


  - Take a critical look at a new name and notation.


  - Think whether the new name or notation looks like something you know. Is the

resemblance helpful or misleading?


  - Be creative and try to come up with your own notation or word to describe the new

concept.


_Remember_ : Symbols and names are not essential. What is important is the
set of _relations_ of a new concept to other concepts. The relations show how
the concept fits and functions within the larger framework.


Numbers and Functions                      - **15**


Demonstrations of this approach can be found in the rest of the book.


2.3 ALGEBRA OF NUMBERS


We will start with the “familiar” numbers:


0 _,_ ±1 _,_ ±2 _,...,_ ± _n, ..._


This endless collection, considered as one entity, is called the _set of whole_
_numbers_ ; it is denoted as Z.
The set Z is not a formless heap of elements. On the contrary, it
has a rich _structure_ . The structure of any set, including the set of whole
numbers, is revealed through various _relations_ between all or some of its
elements. Here are several examples:


  - 1 and −1 are related, and so are 2 and −2, and generally, _n_ and

− _n_ .


  - Relation exists between 1 and 2, 2 and 4, 3 and 6, and generally,
between _n_ and 2 _n_ .


  - The pairs (1 _,_ 2), (2 _,_ 3), (3 _,_ 4), and so on, illustrate an important
relation of order that exists in Z.


  - The pairs (2 _,_ 1), (3 _,_ 1), (4 _,_ 2), (5 _,_ 1), (6 _,_ 3), and similar ones unite
a number and its greatest divisor is not equal to the number itself.


The list of relations can be continued indefinitely, but the general idea
of relations should be clear. Such number-to-number relations can be

schematically represented as boxes with inputs and outputs, as shown in
Figure 2.3. A few important relations are given descriptive names: **neg**,
**dbl**, **suc**, and **gsd** are examples from Figure 2.3; they correspond to the
negation of a number, doubling of a number, finding the successor of a
given number, and finding the greatest divisor smaller than the number
itself.


2.3.1 Functions


What we have just described is the idea of a _function_, or numeric function
of a single _argument_, to be precise. A function of a single argument
connects every _argument_ (input) to a certain _value_ (output), establishing
a _relation_ between a pair of elements.


**16** - Tensors For Inquiring Minds


Figure 2.3 Relations between elements of a set can be schematically
represented using boxes with inputs and outputs. Here the relations between numbers are given descriptive names: **neg** is negation, **dbl** is doubling, **suc** is getting the successive number, **gsd** is the greatest divisor
of a number smaller than the number itself.


Another view on relations is illustrated in Figure 2.4. Relations between elements can be “elevated” to the level of sets and depicted as
arrows connecting one set ( _domain_ ) to another set ( _range_ ). Symbolically

we can write:
**dbl**
Z �→ E _,_


where E denotes the set of all even numbers, **dbl** is the name of the
function that doubles its argument.
The relations of the type “one number to one number” – considered
above – can be generalized to “several numbers to one number,” or “one
number to several numbers,” or even “several numbers to several numbers.” The schematic representation of such relations is given in Figure

2.5.


Figure 2.4 Relations can be viewed on the level of sets. A function maps
(connects) one set with another in a meaningful way. For example, **dbl**
maps every integer from Z into the set of even numbers E.


Numbers and Functions                      - **17**


Figure 2.5 Relations of several elements to several elements: **dup** duplicates its input, **add** calculates the sum, **swp** swaps the order of the
arguments, **max** returns the maximum of three input numbers.


**Exercise 2.1** _Think how you would represent the generalized relations_
_of the types given in Figure 2.5 at the level of sets. What kind of diagrams_
_would you draw?_


_2.3.1.1_ _Binary Functions_


An important function of two variables is the familiar **add** relation:


**add** _nm_ = _n_ + _m._


The right-hand side of this equality is just another way of writing the
expression involving function with two input arguments. It is a special
case of a more general rule, which can be written as follows:


_f nm_ = _n_ ⊚ _m._


On the left, we have a _prefix_ notation, where a function _f_ is _applied_
to two arguments [3] . On the right, we have an _infix_ notation and a special symbol placed between the first and the second argument. Several
familiar examples are


  - **mul** _nm_ = _n_ ∗ _m_ – multiplication.


  - **pow** _nm_ = _n_ [∧] _m_ – power.


  - **sub** _nm_ = _n_ − _m_ – subtraction.


  - **div** _nm_ = _n_ / _m_ – division.


3The use of parentheses around the arguments will be discussed shortly.


**18** - Tensors For Inquiring Minds


The functions **mul**, **pow**, **sub**, and **div** are all examples of _binary_ functions – functions of two arguments.


**Exercise 2.2** _Think of your own example of a binary function. Create_
_its infix variant._


_2.3.1.2_ _Unary Functions_


Functions of single argument are called _unary_ functions. Various notations exist to describe the action of unary functions on their arguments.
The most often used notation looks like this:


_f_ ( _x_ ) = _y._


In this book, we will use another notation to express that the function
_f_ is _applied_ to its argument:


_f x_ = _y._


The parentheses will only be used to write an argument with structure:


_f_ ( _x_ + _y_ ∗ _z_ ) = _v._


Without the parentheses, the left-hand side of the last expression would
be understood as the sum of two terms:


_f x_ + _y_ ∗ _z_ = ( _f x_ ) + ( _y_ ∗ _z_ ) _._


It is said that function application has the highest _precedence_ in an
expression.


_Parentheses Or Not?_


Writing simple arguments without parentheses is a standard practice in
trigonometry. For example:




_[β]_ cos _[α]_ [ −] _[β]_

2 2




_[β]_
sin _α_ + sin _β_ = 2 sin _[α]_ [ +]



2 _._



One can find many similar examples in books and papers. Consider, for
instance, an iconic book _Mathematical Methods For Physicists_ by George B.


Numbers and Functions                      - **19**


Arfken and Hans J. Weber [4] . There we find:


(6 _._ 12) cos _nθ_ + _i_ sin _nθ_ = (cos _θ_ + _i_ sin _θ_ ) _[n]_ _,_ or


(6 _._ 13 _a_ ) ln _z_ = _ln r_ + _iθ,_ or


(10 _._ 80 _b_ ) erf _z_ = _π_ [−][1][/][2] _γ_ ( [1]

2 _[, z]_ [2][)] _[.]_


For many the habit of using parentheses is very strong and a serious effort
is required to accept the alternative. Surprisingly, however, when one starts
working with _operators_ – which are essentially different kinds of functions –
the resistance disappears and it becomes a universal practice **not to put**
**parentheses** around simple arguments. Here are some examples from the
same book:


→ → →
(1 _._ 117) _F_ = −∇ _ϕ,_ ∇ – is an operator,


(3 _._ 27) _x_ [′] = A _x,_ A – is an operator


The moral is this: We should not let our habits thwart learning new and helpful things.


Sometimes we will write the relation between numbers in the follow
ing way:

_f_ _f_
_x_ �→ _y_ or Z �→ E _._


The first variant emphasizes the relation between elements of a set, while
the second expresses the same relation on the level of sets (whole numbers
and even numbers, in this example). In both cases, _f_ denotes the name
of the function/relation.


_Arity of a Function_


_Arity_ is the characteristic of a function describing the number of its arguments: unary (1 argument), binary (2 arguments), and ternary (3 arguments). The function of _n_ arguments is called _n_ -ary. Unary and binary are
the most often used terms.


4Academic Press, Fourth edition, 1995.


**20** - Tensors For Inquiring Minds


2.3.2 Indexed Objects


Unary functions from the set of whole numbers Z provide a good introduction to _index notation_ – an important tool in tensor mathematics.
Let us start with the simplest case of _counting_ elements of some
set S. When counting, we label each element of the set with a unique
number, thus establishing a _relation_ between a number and an element
of a given set S. Put differently, we define a function from the set of
whole numbers (if we allow negative numbers to be used as labels) into
the set S, as shown in Figure 2.6.


Figure 2.6 Counting elements of a set S creates a function from the set
of whole numbers Z into the set S.


We can express counting symbolically as follows:


_f_
_i_ �→ _si,_


where _si_ is the element of the set S labeled with the number _i_ ( _i_ is for
_i_ ndex).
In many mathematical and physical problems, the set being counted
is also made of numbers; in other words, the function _f_ maps whole
numbers into other numbers. Consider the function


_f i_ = 2 _i_ + 1 _._


If we denote the output value of the function _f_ as _v_, then all values can
be indexed as

_vi_ = _f i_ = 2 _i_ + 1 _._


Using subscripts for indices is very common, it avoids confusion with the
power notation:
_v_ 1 ≠ _v_ [1] _,v_ 2 ≠ _v_ [2] _,...,vn_ ≠ _v_ _[n]_ _._


When the confusion is not possible or easy to avoid, placing indices as
superscripts might be helpful (see Section 5.8 for details).


Numbers and Functions                   - **21**


_Continious Index_


What if extend the idea of counting and allow ”the label” to be a continuous
variable? For example:
_vx_ = _f x_ = 2 _x_ + 1 _._


This is just another way of writing an unary function _f_ ! We thus arrive at the
idea of using a subscript to represent the argument of a function. Here is
an illustration from the Arfken and Weber book _Mathematical Methods For_

_Physicists_ :


_x_



(10 _._ 67) _Bx_ ( _p, q_ ) =



∫ _t_ _[p]_ [−][1] (1 − _t_ ) _[q]_ [−][1] _dt._

0



Don’t be intimidated by the right-hand side of this equation, notice that the
expression of the left describes a _ternary_ function, with the arguments _x_, _p_,
and _q_ .


_2.3.2.1_ _Multi-Index Objects_


It is possible, and often convenient, to label objects with several indices.
This results in _multi-index_ objects. Let us start with two indices and
look at several examples, schematically represented in Figure 2.7.


Figure 2.7 Mapping two whole numbers to another number can be described using indexed objects with two indices. Schematically they are
represented as boxes with two inputs and one output. See the text for
the definition of these particular objects.


First, if we denote as _tij_ the approximate number of hours elapsed
since the beginning of the year upto the _i_ -th day of the _j_ -th month, then
we will have
_tij_ = 24 ∗[30( _j_ − 1) + _i_ − 1] _._


**22** - Tensors For Inquiring Minds


Second, denote _hij_ the values of the following function:



_hij_ =



0 if _j_ ≤ _i_ .

⎧⎪⎪⎨⎪⎪⎩1 if _j_ - _i_ .



Third, denote _δij_ the values of the function



_δ ij_ =



1 if _i_ = _j_ .

⎧⎪⎪⎨⎪⎪⎩0 if _i_ ≠ _j_ .



Finally, denote _ϵij_ the values of the function



_ϵij_ =



0 if _i_ = _j_ .

1 if _i_ < _j_ .

⎧⎪⎪⎪⎪⎨⎪⎪⎪⎪⎩−1 if _i_ - _j_ .



The object _δ_ is very useful in mathematics. It is called Kronecker
delta, after German mathematician Leopold Kronecker. With the help of
Kronecker’s _δ_ many mathematical expressions can be written compactly
and many manipulations can be carried out efficiently, as we will soon

see.


Objects with three or more indices appear in certain problems. We
will define and discuss them when they become relevant for the study of

tensors.


2.3.3 Linear Functions


We will now encounter for the first time the deceptively simple concept
of _linear functions_ . Tensors represent a powerful extension of this idea.

Consider the following two functions:


**dbl** _n_ = 2 _n_ and **sqr** _n_ = _n_ [2] _._


The first function has an important property which the second one is
lacking. Namely, we have


**dbl** ( _n_ + _m_ ) = ( **dbl** _n_ ) + ( **dbl** _m_ )


and

**dbl** ( _a_ ∗ _n_ ) = _a_ ∗( **dbl** _n_ ) _._


Numbers and Functions                      - **23**


Compare this to the function **sqr** :


**sqr** ( _n_ + _m_ ) = ( **sqr** _n_ ) + ( **sqr** _m_ ) + 2 _nm_ ≠( **sqr** _n_ ) + ( **sqr** _m_ ) _,_


**sqr** ( _a_ ∗ _n_ ) = ( **sqr** _a_ ) ∗( **sqr** _n_ ) ≠ _a_ ( **sqr** _n_ ) _._


The function **dbl** is an example of a _linear function_, while **sqr** is not.


_Linear Functions_


A _linear function f_ is any function that satisfies the two simple conditions,
called _linearity_ conditions:


_f_ ( _n_ + _m_ ) = ( _f n_ ) + ( _f m_ )


and

_f_ ( _a_ ∗ _n_ ) = _a_ ∗( _f n_ ) _._


These conditions severely limit what a linear function can do.


In the vast family of functions, some are simpler than others. The simplicity
of a function is reflected in the conditions it satisfies. The more conditions we
place on a function – the simpler it becomes. An arbitrary function _f_ is not
limited by any constraints. Linear functions are among the simplest. Other
categories of functions, together with their constraints, are given in the table
below:

|Category|Condition|Example|
|---|---|---|
|Symmetric|_f_ (−_x_) = _f x_|_x_~~2~~|
|Anti-symmetric|_f_ (−_x_) = −(_f x_)|1/_x_~~3~~|
|Periodic|_f_ (_x_ +_ a_) = _f x_|cos (2_πx_/_a_)|
|Affne|_f_ (_x_ + _y_) =(_f x_) +(_f y_)|4_x_ + 7_f_|
|Homogeneous|_f_ (_a_ ∗_x_) =_ a_~~_n_~~(_f x_)|3_x_~~_n_~~|
|Linear|_f_ (_ax_ +_ by_) =_ a_(_f x_) +_ b_(_f y_)|_x_/2|



As a side-note, linear functions are both _affine_ and _homogeneous_ for _n_ = 1.


**Exercise 2.3** _Show that for any linear function we must have_


_f_ 0 = 0 _._


_Then show that_

_f n_ = _n_ ( _f_ 1) _._


_The last property demonstrates that the action of a linear function on_
_any number is completely determined by a single value f_ 1 = ( _f_ 1) _– its_
_action on the number one._


**24** - Tensors For Inquiring Minds


Unary linear functions acting on numbers seem too simple to be of importance. They are equivalent to multiplication by a pre-defined value.
Indeed, the action of a linear function _f_ on any number reduces to the
multiplication of that number by a fixed value _f_ 1 = _f_ 1.


Any example of a linear function over numbers will appear trivial:


_f x_ = 3 _x._


However, linear functions over vectors (and tensors) turn out to be very useful. The rest of the book aims to demonstrate this.


Example
Linear Functions


What is more important is the _concept of linearity_, as it can be more
fruitfully applied to other mathematical objects. We will encounter linear
functions in different contexts when we talk about _operators_ – functions
defined on vectors. Linearity in that case will not be trivial, but still
important and easy to understand.


**Exercise 2.4** _Draw a schematic representation of the linearity proper-_

_ties._


_2.3.3.1_ _Multilinear Functions_


The idea of linearity can be generalized. A function with two or more
arguments can satisfy linearity properties for each argument and this
way become a _multilinear function_ .

Let us consider a familiar function


**mul** _nm_ = _n_ ∗ _m._


The distributivity of multiplication implies that


**mul** ( _n_ + _p_ ) _m_ = ( **mul** _nm_ ) + ( **mul** _pm_ ) _,_


and

**mul** _n_ ( _m_ + _q_ ) = ( **mul** _nm_ ) + ( **mul** _nq_ ) _._


Numbers and Functions                      - **25**


The second linearity property is also satisfied for each argument:


**mul** ( _an_ ) _m_ = _a_ ( **mul** _nm_ ) _,_


and
**mul** _n_ ( _am_ ) = _a_ ( **mul** _nm_ ) _._


Multiplication is a _bilinear function_ . The ideas of linearity, bilinearity,
and multilinearity are important for a better understanding of tensors.
Now that we are familiar with the concept of multilinear functions,
we can more fully appreciate other definitions of tensors:


_Wikipedia on Tensors_


The first paragraph on tensors in Wikipedia states [5] :


” _In mathematics, a tensor is an algebraic object that describes a multilinear_
_relationship between sets of algebraic objects related to a vector space._ ”


Here the term _multilinear_ means exactly what we have just learned. The
meaning of the rest of the phrase will become more clear as we progress
through the book.


2.3.4 Function Composition


New functions can be built from already available functions. Several
“natural” and simple methods exist for this. Let’s study these methods
using, for the purpose of illustration, two trigonometric functions:


_f x_ = cos _x,_ _g x_ = sin _x._


First, we must understand that it is permissible to talk about functions
without mentioning their arguments. For example, we are allowed to

write

_f_ = cos _,_ _g_ = sin _._


This way we emphasize our attention to functions as mathematical objects in their own right. This is similar to how we use numbers: We
write just 5, not 5 _of something_, even though that _something_ is always
implicitly present.


5As of October 9, 2023.


**26** - Tensors For Inquiring Minds


_Argument-Free Notation_


The practice of manipulating functions without arguments (i.e., writing their
names only) is called _argument-free_ or _point-free_ notation. Later, when discussing linear operators, it will become very helpful.


Now we can define meaningful operations on functions, analogous to
arithmetic operations on numbers. First, we can add functions:


_u_ = _f_ + _g._


The application of this new function _u_ on any argument results in


_ux_ = ( _f x_ ) + ( _g x_ ) _._


_Adding Functions_


Having defined an addition of two functions, we can write expressions like


_f_ = cos + sin or _h_ = log + exp _._


It is important to remember that in these expressions we _do not add num-_
_bers_, we add functions – completely different mathematical objects.


In a similar way we can define the multiplication of functions:


_v_ = _f_ ∗ _g_ → _v x_ = ( _f x_ ) ∗( _g x_ ) _._


Thus, we gave a meaning to the following expressions:


cos + sin _,_ cos ∗ sin _._


Lastly, unlike numbers, functions can be _composed_ or sequenced. For
example, we can write


_hx_ = cos (sin _x_ ) or _w x_ = sin (cos _x_ ) _._


Note that _hx_ ≠ _w x_ .


More generally, and dropping the argument _x_, we can compose functions _f_ and _g_ in two different ways:


_h_ = _g_          - _f_ or _w_ = _f_          - _g._


Numbers and Functions                      - **27**


Here we used infix notation and a conventional denotation for a composition operation “○.”
The schematic representation of the idea of function composition is
given in Figure 2.8. Note how the order of the boxes differs from the
order of the functions in the expression for composition. This is the
consequence of placing the input to the boxes on the left and reading
the schematic from left to right.


Figure 2.8 Functions can be _composed_ to create a new function. In
composition the output of the first function is “connected” to the input
of the second.


In contrast to addition and multiplication, function composition does
not possess _commutativity_ . That is, in general we have


_g_              - _f_ ≠ _f_              - _g._


For example,


(cos        - sin) 0 = 1 (sin ○ cos) 0 = sin 1 ≠ 1 _._


Sometimes, however, commutativity is satisfied, as we will later see in
discussions of linear operators (see the end of Section 4.1.)
With the definitions given above, we can see the meaning of complex
expressions like this one:


_h_ = ( **sqr**         - cos) + ( **dbl** ∗ sin) _._


**28** - Tensors For Inquiring Minds


When applied to an argument, this function returns


_hx_ = cos [2] _x_ + 2 _x_ sin _x._


At this point, the benefit of such abstract exercises is not evident. However, they open a door to understanding how functions and operators [6]

can be manipulated and how their properties can be discussed in a manner analogous to more primitive mathematical objects, such as numbers.
For example, we will be able to understand how a function may _become_
_an argument to another function_, as in


**sqr** cos = cos ∗ cos _._


With this insight, the famous Euler’s identity


_e_ _[iπ]_ + 1 = 0


will have a simple and clear interpretation (see formula (6.5) in Section
6.2 on page 136).


2.3.5 Partial Application


Any binary function can be turned into an unary function if we fix
one of its arguments. Schematic representation of functions provides an
especially clear view of this procedure, shown in Figure 2.9. When a


Figure 2.9 Functions with several arguments can be reduced to functions with even fewer arguments by _partially applying_ – providing arguments to some, but not all of its inputs. In this example, partially
applying the binary function **mul** we get a unary function **dbl** which
doubles its argument.


function is applied to some of its argument – but not to all – it is said
to be _partially applied_ . The applied arguments are considered fixed, and
the remaining arguments are considered as varying. Partial application
reduces the arity of a function.


6
Operators are defined later in Chapter 4.


Numbers and Functions                      - **29**


We will encounter partial application later in the book when discussing two kinds of vectors: covariant and contravariant vectors (see
subsection 5.4.1).


_Partial Application_


Partial application is an under-appreciated concept. It is uncommon in mathematics and physics, but more likely to be encountered it in the area of computation. The situation is slowly changing and today one can encounter examples of partial application, for instance, in modern papers on quantum
physics:


”Assuming time-translation invariance, let us denote the transport function
as _T_ ( _t_ 1 − _t_ 0 _,_    - ) where the free slot is for the hidden variables.”


This is a quote from the paper _The wave function as a true ensemble_ by
Jonte Hance and Sabine Hossenfelder [7] . What the authors did here is to

apply the binary function _T_ to the first argument with the value _t_ 1 − _t_ 0, leaving
the second argument as the ”free slot.”


2.3.6 Function Representations


We explored the idea of functions as relations between elements of sets.
So far we mentioned three different ways to represent this idea:


1. _Schematically_ : using boxes with inputs and outputs.


2. _Diagrammatically_ : using arrows connecting elements of a set of
different sets.


3. _Symbolically_ : using mathematical formulas made from variables
and operations.


For completeness, let’s take a look at two more ways to represent func
tions.


_2.3.6.1_ _Functions as Graphs_


Numeric functions with single input and single output can be plotted as
curves in a plane. Figure 2.10 shows two curves: parabola for the **sqr**
function, and sinusoidal curve for _sin_ . Such graphs visually demonstrate


7Hance Jonte R. and Hossenfelder Sabine, 2022, _The wave function as a true_
_ensemble_ [, Proc. R. Soc. A.47820210705, http://doi.org/10.1098/rspa.2021.0705](http://doi.org/10.1098/rspa.2021.0705)


**30** - Tensors For Inquiring Minds


Figure 2.10 Simple functions (with one input argument _a_ and one output value _v_ ) can be represented as a curve in a plane with two axes: _a_ for
argument, and _v_ for value. Two functions are plotted here: _v_ = **sqr** _a_ = _a_ [2]

and _v_ = sin _a_ .


the relation between argument _a_ and value _v_ = _f a_ for a given function
_f_ . This is a powerful method for studying functions and their properties.
For instance, we can see the presence and locations of maxima, minima,
points of zero-values, regions of positive and negative values, and so on.


Representing functions as curves has its limits. Functions with several
inputs or several outputs often present significant challenge for clear and
informative plotting. In such cases, we can resort to other representations
of functions, for example using symbolic mathematical expressions.


_2.3.6.2_ _Functions as Tables_


Functions may also be represented as tables. This method works best for
functions whose arguments take on a discrete and limited set of values.
For example, if we record the temperature at noon every day during the
year, we will experimentally establish a relation between the day number
and the reading of the thermometer, as summarized in the Table 2.1.


TABLE 2.1 Functions can be represented as tables that relate arguments to values in a series of entries. Here, for every value of the argument _d_ from the first row, the value of _t_ is given in the second row.


|Col1|d|1|2|3|. . .|n|
|---|---|---|---|---|---|---|
||**t**|_t_1|_t_2|_t_3|. . .|_tn_|


Numbers and Functions                      - **31**


Tabular form is also convenient in practical applications when the
precision of the function’s values is not critical and the function can be
approximated by a series of values at a limited number of points.

We explored five different ways to talk about functions. The main
point of this exploration can be formulated in the following way:


_Concept and Its Representation_


The mathematical concept of a function as the relation between elements of
sets allows several representations. Each representation has its merits and
each representation highlights certain aspects of the concept.
None of the representation is definitive, none fully conveys what functions
are. Different representations show _different aspects_ of _the same idea_ : They
are different doors into the same room.


It is important to understand the _relation_ between mathematical
concepts and their various _representations_ . This theme will keep coming
up as we learn more about numbers, vectors, and tensors.


2.3.7 Numbers


Modern understanding of numbers differs greatly from how numbers
were viewed in the past. From puzzling zero and negative numbers to
tricky fractions and abstract real numbers, the family of mathematical
objects called numbers grew to include natural numbers, whole numbers,
rationals, real, and complex numbers.

Now, what defines a number? What properties does a mathematical
object have to satisfy to be accepted into the “number family”?

To be a number an object must “behave like a number”: We must
know how to add and multiply it with other numbers to get a numeric
answer as the result. In other words, numbers form a _set_ equipped with
two binary functions – addition and multiplication. These functions are
simple and satisfy several requirements:


_x_ + _y_ = _y_ + _x_ (commutativity) _._


_x_ ∗ _y_ = _y_ ∗ _x_ (commutativity) _._


_z_ ∗( _x_ + _y_ ) = _z_ ∗ _x_ + _z_ ∗ _y_ (distributivity) _._


**32** - Tensors For Inquiring Minds


_2.3.7.1_ _Neutral Elements_


There are two special numbers: 0 for addition and 1 for multiplication.
Their special character is expressed by the following equations:


0 + _x_ = _x_ for all _x,_


and


1 ∗ _x_ = _x_ for all _x._


The number 0 is the neutral element with respect to addition, and the
number 1 is the neutral element with respect to multiplication.


_2.3.7.2_ _Inverse Elements_


Every number (except zero) has two “anti-numbers” defined in a natural
way. In addition, every number _x_ has its “anti-number” ¯ _x_ such that


_x_ + ¯ _x_ = 0 _._


Similarly for multiplication, for every number _x_ there exists its “antinumber”:


_x_ ∗ _x_ ˜ = 1 _._


Here we deliberately deviated from the conventional notation: For the
inverse of _x_ with respect to addition we would have to write (− _x_ ), and
for the inverse with respect to multiplication: (1/ _x_ ) or ( _x_ [−][1] ).

In the following chapters, we will encounter new mathematical objects, such as vectors and tensors. Like numbers, they will be elements
of some sets and, like numbers, their pairs can be added and multiplied.
Like numbers, they may have neutral and inverse elements. And yet they
will differ from numbers in several important ways.

To better understand the distinct nature of vectors and tensors, it is
important to be able to look at the _structure_ of their corresponding sets.


2.3.8 Algebraic Structure


Numbers, as well as vectors and tensors, form _structured sets_ in the sense
that there are _relations_ between their elements. For numbers, two important relations are the familiar operations of addition and multiplication.
In mathematics, any set structured this way is called a _field_ . This is the
meaning of the word “field” in the _Tensor Definition 1_ on page 5.


Numbers and Functions                      - **33**


A set of elements, together with operations on the elements form
what mathematicians call an _algebraic structure_ or simply _algebra_ . Numbers form an algebraic structure, and so do vectors and tensors.


_Algebra of Functions_


Think of how functions, such as sin, cos, _f_, and so on, form an algebra
when the operation of _composition_ is given. Such an algebra is the subject
of _category theory_ .


The essential differences between numbers and, for example, vectors,
are _not_ how they are represented symbolically or graphically, but what is
the _structure_ of their sets, what are the _operations_ and their _properties_ .
The set of real numbers R equipped with usual operations of addition
and multiplication forms an algebraic structure called _field_ and it is
denoted using the tuple notation (see Section 1.6) as follows


(R _,_ + _,_ 0 _,_ ∗ _,_ 1) _._


Here we list the set, the operations with its elements, and the special
elements of those operations.
Vectors [8] (introduced in Chapter 3) also form a set. The elements
of this set can be added to yield another vector. If we denote a pair of

→ → →
vectors as _a_ and _b_, and the operation of their addition as “+,” then their
addition can be described by a vectorial equation:


→ → → →
_a_ + _b_ = _c._


→
Note that a different symbol “+” is used to represent the addition of
two vectors! We have to remember that despite being similar, number
addition and vector addition are _different operations_ after all! Indeed, we
are operating on elements of different natures and our notation should
reflect that. However, nearly always we can be less pedantic and use the
traditional symbol for addition:


→ → →
_a_ + _b_ = _c._


8Although we did not study vectors yet, some of the points made here might be
helpful. It is recommended to come back to this section after reading Chapter 3.


**34** - Tensors For Inquiring Minds


Numbers can be defined and used without vectors, while vectors _can_
_not_ be defined or used without numbers! A simple equation


→ → →
_a_ + _a_ = 2 _a_


requires not only a number but also a well defined operation of multiplication of a vector and a number:


→ → →
2 ∗ _a_ = _d._


→
Again, the arrow on top of the asterisk “∗” can usually be dropped, as
long as we remember that the multiplication of two numbers is _not the_
_same_ operation as the multiplication of a number and a vector.
Thus, from the more abstract standpoint, vectors form an algebraic
structure that can be denoted as follows:


→ → →
(V _,_ + _,_ 0 _,_ ∗ _,_ 1) _._


Here the capital V represents _all possible_ vectors – _vector space_ in mathe

→
matical jargon; 0 is a special neutral element with respect to the addition
of vectors (→+), analogous to the number zero; (→∗) denotes the operation
of multiplying a vector by a number; and 1 is the familiar number, the
same neutral element with respect to numeric multiplication.
Numbers and vectors form different algebraic structures, at least for
the following two reasons: 1) Numeric neutral element 1 has no coun

→
terpart among vectors (no multiplicative vector 1); 2) Multiplication of
two numbers yields a number, whereas in the definition of vectors, there
is no operation of multiplication of two vectors that would result in a
new vector – we only multiply a number and a vector [9] .
Returning to the Tensor Definition 1 on page 5, we now should be
able to understand the meaning of the phrase: _Tensor on a vector space_
_V over a field k.. ._ Here tensors are defined based on the idea of vectors, which, in turn, require the notion of numbers (or other number-like
mathematical objects that form _field_ ). We should expect tensors to form
an algebraic structure different from both numbers and vectors. That
structure will be more clear once we have learned the concepts of vectors and linear operations on them.


9Vector multiplication is a tricky operation, especially for vectors with dimensions
higher than three.


Numbers and Functions                      - **35**


2.4 POWER OF NOTATION


The power of mathematics that comes from abstraction is amplified by
a good notation. Notation is a tool which helps express ideas clearly and
manipulate them efficiently. Notation plays an especially important role
in mathematics.

Learning mathematics requires learning new and sometimes nonintuitive notation. Effort is needed to learn new notation, and, more
importantly, it is necessary to learn to see beyond symbols in order to
recognize _concepts_ and _relations_ between them. One of the goals of this
book is to help learn new notation, and make sense of unfamiliar, and
at times strange-looking, symbols used in mathematics.
Having finished this book, the reader should be able to appreciate
the expressiveness of formulas like this one:


_T_ _[p,q]_ ( _V_ ) = (⊗ _[p]_ _V_ ) ⊗(⊗ _[q]_ _V_ [∗] ) _._


This expression is used in one of the definitions of tensors given in the
introduction (see Section 1.3 in Chapter 1).


2.4.1 Polynomial Example


As an example, let us consider a simple mathematical function given by
the following cubic polynomial:


_P_ 3 _x_ = 2 _x_ [3] − 2 _x_ [2] − 4 _x._ (2.3)


Imagine we would like to understand the structure and properties
of this polynomial. We can use various approaches and examine the
function from different viewpoints. For example, we can examine the
schematic representation of the polynomial shown in Figure 2.11. The
schematic, built from more basic “building blocks,” reveals a moderately
complicated structure of the polynomial. It is definitely not as compact
as the symbolic expression (2.3).
Algebraic manipulations lead to an alternative way of writing the
same polynomial:
_P_ 3 _x_ = 2 _x_ ( _x_ + 1)( _x_ − 2) _._ (2.4)


The schematic representation of (2.4) is shown in Figure 2.12. Although
the schematic of the factorized expression looks simpler than for the
non-factorized, it still looks unwieldy compared to the symbolic form of
(2.4).


Figure 2.11 Schematic representation of the structure of a cubic polynomial, written symbolically as 2 _x_ [3] − 2 _x_ [2] − 4 _x_ .


Figure 2.12 Schematic representation of the structure of a cubic polynomial, written in factorized form 2 _x_ ( _x_ +
1)( _x_ − 2).


**38** - Tensors For Inquiring Minds


Figure 2.13 demonstrates a graphical representation of the cubic
polynomial _P_ 3 _x_ . Obviously, the curve is the same regardless of the
way we write the polynomial symbolically. The graphical representation shows that the polynomial has three _roots_ – values of the argument
_x_ for which the value of the polynomial _P_ 3 _x_ equals zero. It also shows
that the polynomial “explodes” at large positive and negative values of
the argument.


Figure 2.13 Graphical representation of the cubic polynomial _P_ 3 _x_ =
2 _x_ [3] − 2 _x_ [2] − 4 _x_ .


Neither graphical nor schematic representation provides an easy way
to find the positions of the _local extrema_ – points where the polynomial
changes its behavior from increasing to decreasing or vice versa. These
are marked as upward- or downward-oriented triangles in the Figure
2.13. The symbolic representation, together with the methods of calculus, quickly yields the desired result (the details of how calculus achieves
this are of no importance for the point being made.)
We can now appreciate the power of the abstract algebraic ways of
representing polynomials. A general polynomial of the degree _n_ can be
written as follows:


_Pn x_ = _a_ 0 _x_ [0] + _a_ 1 _x_ [1] + _a_ 2 _x_ [2] + _..._ + _anx_ _[n]_ _._ (2.5)


The reason for writing the first lowest terms


_a_ 0 + _a_ 1 _x_ = _a_ 0 _x_ [0] + _a_ 1 _x_ [1]


Numbers and Functions                      - **39**


will become more clear shortly, when we encounter Einstein’s summation
rule.

The expression (2.5) can be written more compactly:



_Pn x_ =



_i_ = _n_
∑
_i_ =0



_aix_ _[i]_ _._



Here we used a new notational tool – the summation sign ∑ (capital
Greek letter sigma Σ). The expression above should be read as follows:
The function _Pn x_ consists of the sum of terms _aix_ _[i]_ where the index
_i_ takes the values from zero to _n_, and appears as the subscript of the
coefficients _a_ and as the power of the variable _x_ .

The notation using ∑ is an improvement compared to the formula
(2.5), but there exists an even better way to write various sums of terms
with repeated indices. This new and better notation is called _Einstein’s_
_summation rule_ . It is extremely helpful in vector and tensor mathematics
and we consider this notation next.


2.5 EINSTEIN’S SUMMATION RULE


If there existed a Nobel Prize for notation one would definitely go to
Albert Einstein for what is known as _Einstein’s summation rule_ . In short,
the rule states: _Whenever you see repeated indices in an expression, un-_
_derstand the expression as the sum of many terms with similar structure_ .
For example:


_aixi_ = _a_ 1 _x_ 1 + _a_ 2 _x_ 2 + _a_ 3 _x_ 3 + _..._


It is a more efficient alternative to the traditional notation:



_i_ = _n_
∑
_i_ =1



_aixi_ = _a_ 1 _x_ 1 + _a_ 2 _x_ 2 + _a_ 3 _x_ 3 + _..._ + _anxn._



Already in this simple case, we saved at least 7 symbols: the summation
sign ∑ and the lower and upper limits ( _i_ = 1) and ( _i_ = _n_ ).


**Exercise 2.5** _Using Einstein’s summation rule, write the expression for_
_the general form of a polynomial of degree n._


The last problem reveals that we have to specify the range of values for
the summation index. For example:


_aixi_ _i_ = 1 _,_ 2 _,...,n._


**40** - Tensors For Inquiring Minds


The range for the summation index (or indices if there are several) is
usually clear from the context and it is the same across many expressions
written using Einstein’s summation rule.


**Exercise 2.6** _Assuming the summation indices i, j, and k range from_
1 _to_ 4 _, write out fully the following expressions:_


( _a_ ) _biyi_ ( _b_ ) _bjyj_ ( _c_ ) _bkyk._


The last problem demonstrates an important property of Einstein’s summation notation: _We are free to rename the summation indices_ . Renaming the indices does not affect the resulting value and can often be useful
for manipulating expressions. For example, given the expression


_aixi_ + _bjxj,_


we can immediately rewrite it as follows:


_aixi_ + _bjxj_ = _aixi_ + _bixi_ = ( _ai_ + _bi_ ) _xi._


Sometimes we need to be careful with new notation:



( _aixi_ ) [2] ≠ _a_ [2] _i_




[2] _i_ _[x]_ [2] _i_



_i_ _[.]_



Indeed, the left-hand side must be understood as


( _aixi_ )( _aixi_ ) = ( _aixi_ )( _ajxj_ ) = _aiajxixj._



Clearly, there will be terms like _a_ 1 _a_ 2 _x_ 1 _x_ 2 which are absent from the sum
_a_ [2] _[x]_ [2]




[2] _i_ _[x]_ [2] _i_



_i_ [. The next exercise helps to see this better.]



**Exercise 2.7** _Write out fully the expressions_



( _a_ )( _aixi_ )( _ajxj_ ) ( _b_ ) _a_ [2] _i_




[2] _i_ _[x]_ [2] _i_



_i_



_for i_ = 1 _,_ 2 _._


**Exercise 2.8** _Rewrite the expression_


( _aixi_ ) [2] = _[b][j][y][j]_

_ckck_


_in the traditional form, using the summation symbol_ Σ _. Assume that all_
_indices run from_ 1 _to N_ _._


Numbers and Functions                      - **41**


Einstein’s summation rule is used in a great number of problems and
we will use it extensively.


_Limitation of Einstein’s Summation Rule_


Einstein’s summation rule has its limitations. For example, it is _almost never_
_allowed_ [10] to write expressions with more than two repeated indices:


_aibici_ ←� NOT allowed!


Traditional notation allows writing such expressions with ease:


_i_ = _n_
∑ _aibici_ = _a_ 1 _b_ 1 _c_ 1 + _a_ 2 _b_ 2 _c_ 2 + _. . ._ + _anbncn._
_i_ =1


_2.5.0.1_ _Practice With ESR_


It is important to become proficient with Einstein’s summation rule because it will be used extensively when dealing with vectors and tensors.
Einstein’s summation rule (ESR for short) can be combined with
indexed objects introduced earlier (see page 20.) In addition to the indexed objects _δij_ and _ϵij_, it will be useful to introduce one more indexed
object:
Σ _i_ = 1 or Σ _i_ = 1 _._


Although this indexed object appears trivial, it proves useful. For example, it allows writing simple sums concisely:


Σ _iai_ = _a_ 1 + _a_ 2 + _..._ + _an._


**Exercise 2.9** _Write out in full form and then simplify the following_
_expressions:_ ( _a_ ) _δ_ 1 _iai_ ( _b_ ) _δ_ 3 _kak_ _i,k_ = 1 _,_ 2 _,_ 3 _,_ 4 _,_
( _c_ ) _ϵ_ 1 _jaj_ ( _d_ ) _ϵ_ 3 _jaj_ _i,j_ = 1 _,_ 2 _,_ 3 _,_ 4 _._


The action of Kronecker’s delta on another indexed object results in
“renaming” the index of the latter. Indeed, from the sum


_δkiai_ = _δk_ 1 _a_ 1 + _δk_ 2 _a_ 2 + _..._ + _δknan_


only the terms with _i_ = _k_ remains:


_δkiai_ = _ak._


10Exceptions are possible, but rare and are irrelevant to our goals.


**42** - Tensors For Inquiring Minds


**Exercise 2.10** _Using the last result, show that_


_ai_ + _aj_ = (1 + _δji_ ) _ai._


Double sums can be handled using Einstein’s summation rule as well:



_i_ ∑= _n_ _ai_ _j_ ∑= _n_ _bj_ ⎞ _i_ ∑= _n_
( _i_ =1 ) [⎛] ⎝ _j_ =1 ⎠ [=] _i_ =1



_j_ = _n_
∑ _aibj_ = Σ _i_ Σ _jaibj_ _i,j_ = 1 _,...,n._
_j_ =1



**Exercise 2.11** ( _a_ ) _Show that_


_δijaibj_ = _aibi_ _i,j_ = 1 _,...,n._


( _b_ ) _Write out fully_
_ϵijaibj,_


_assuming i,j_ = 1 _,_ 2 _._


Let us wrap up this chapter with a couple of more advanced problems:


**Exercise 2.12** ( _a_ ) _Show that_


_δijδjk_ = _δik_ _i,j,k_ = 1 _,...,n._


( _b_ ) _Show that_
_ϵijϵjk_ = − _δik_ _i,j,k_ = 1 _,_ 2 _._


_These relations have simple interpretations in terms of operators and_
_their components, discussed in Chapter 4._


Consider a number

_x_ = _δijϵij._


Using the fact that we can rename summation indices, we can write


_x_ = _δikϵik_ = _δjkϵjk_ = _δjiϵji._


From the definition of the indexed objects _δ_ and _ϵ_ follows that


_δji_ = _δij_ and _ϵij_ = − _ϵji._


Thus, we obtain
_x_ = _δjiϵji_ = − _δijϵij_ = − _x._


Therefore, the value of _x_ must be zero due to the different symmetries
of the indexed objects with respect to swapping their indices.


**Exercise 2.13** _Show that_


_ϵijaiaj_ = 0 _._


Numbers and Functions                      - **43**


CHAPTER HIGHLIGHTS


  - _The power of mathematical concepts and methods increases with the_

_level of abstraction._


  - _Learning new concepts often involves learning new terminology. The_

_latter can create an artificial mental barrier._


  - _“Usual” numbers form a mathematical structure. The structure is re-_

_vealed through various relations that exist between numbers._


  - _Relations between numbers are expressed using the concept of functions_

_and operations (e.g., addition). Each operation is characterized by its_
_arity – the number of arguments it accepts as an input._


  - _Functions can be represented schematically as boxes with inputs and_

_outputs._


  - _Functions that act on natural numbers can be written using index nota-_

_tion (e.g., f i_ = _fi)._


  - _Linear functions represent the simplest but still powerful and useful_

_kinds of functions._


  - _Functions can be composed to create new functions._


  - _A function with several inputs is said to be partially applied when not_

_all its inputs are populated._


  - _The same function can be represented in various ways: Graphical, as a_

_symbolic formula, as a table. The function is not reduced to any of its_
_representations._


  - _The power of abstract mathematical thinking comes, in part, from effi-_

_cient notation. Einstein’s Summation Rule (ESR) is a good example of_
_this._


#### C H A P T E R 3

### Arrows and Vectors

N THE PREVIOUS CHAPTER WE LEARNED ABOUT
# I numbers and various relations between them. As a particular class

of relations, we discussed functions. We introduced _binary_ and _unary_
functions and different ways functions can be combined ( _composed_ ) to
produce new functions. We also learned that functions can be represented
in various ways and that none of those different representations defines
the concept of function completely. Each representation of a function
highlighted some important aspect of it.
Vectors, which will be introduced in this chapter, also allow different
representations. We will start with a particular model of vector quantities
– _arrows_ . It is important to remember that while this model illustrates
the concept of vectors, it does not define vectors completely. In other
words, arrows are particular examples of vectors, but vectors are more
than directed line segments.
To arrive at the definition of vectors we must explore their properties
more fully. This will be the goal of the current chapter.


3.1 ARROWS


To arrive at the idea of vectors we will start with simple geometrical
objects – arrows in a plane, as illustrated in Figure 3.1.
Symbolically, we will denote vectors by placing an arrow over letters:


→ → → → →
_a,_ _b,_ _c,...,_ _α,_ _β._


→
The length of an arrow _a_ is denoted by the same letter without an arrow:


→
**length** _a_ = _a._


**44** [DOI: 10.1201/9781003620365-3](https://doi.org/10.1201/9781003620365-3)


Arrows and Vectors                         - **45**


Figure 3.1 Set of arrows starting at the same origin point _O_ . All imag

⇒
inable arrows taken as one set form the arrow space _A_ .


The set of all possible arrows – called _arrow space_ (or _vector space_ ) –
we will denote as
⇒ _A_ = {→ _a,_ → _b,_ → _c,...,_ → _α,_ → _β ..._ } _._


Diagrammatic representation of the set of arrows is given in the Figure

3.2.


Figure 3.2 All arrows, considered as unified collection of objects of similar nature, can be viewed as a mathematical set. Each arrow is an element of this set, denoted as a point.


_Functions on Arrows_


The function **length** is a unary function that accepts arrows as input (argument) and returns a numeric value – the lengths of the arrow.
On the level of sets, the **length** function _maps_ the set of all vectors into the
set of real numbers:
⇒ **length**
_A_ �→ R _._


**46** - Tensors For Inquiring Minds


In the next chapter, we will encounter other types of functions on arrows.
Some of them will return numbers like **length** does, and others will return
arrows, mapping _arrow space_ into its own copy:


⇒ ⇒
_A_ �→ _A._


_Arrows and Numbers_


Arrows in a plane include, in some sense, the notion of numbers. Indeed, as
shown in Figure 3.3, real numbers may be represented as points on a line –
number line. Positive numbers correspond to the arrows pointing to the right
of the origin (number zero), and negative numbers correspond to the arrows
directed to the left.


Figure 3.3 Real numbers can be represented by arrows oriented along
a fixed line – _number line_ .


3.2 ALGEBRA OF ARROWS


Next, we will establish similarities between arrows and numbers by exploring possible _algebraic operations_ on vectors.


3.2.1 Combining Arrows


Two arrows can be _combined_ in a natural way to yield the third arrow.
Using either the head-to-tail approach or a parallelogram method, the

→ →
vectors _a_ and _b_ can be combined graphically, as illustrated in Figure

3.4.

Symbolically, we express the combination of two arrows as


→ → →
_κ_ _a_ _b_ → _c,_


where the Greek letter _κ_ (kappa) denotes a binary function that combines arrows. Alternatively, _infix notation_ can be used


→ → →
_aκ_ _b_ = _c._


Arrows and Vectors                         - **47**


Figure 3.4 Two arrows can be combined to produce a new arrow. One
way to do this is to arrange two arrows “tail-to-tip.” This operation is

→ → →
called _addition of arrows_ : _a_ + _b_ = _c_ .


Usually, the same symbol is used for vector “addition” as for addition of
numbers:
→ → →
_a_ + _b_ = _c._


This leads to “double-booking” of the same symbol. In technical jargon,
the function “+” is _overloaded_ – defined on objects of different kinds
(numbers and arrows in this case). We must keep in mind that in the
following two expressions:


→ →
3 + _x_ and _a_ + _b_


the function [′′] + [′′] has different meanings (it is _implemented_ differently as
an operation). Ignoring this distinction may lead to syntactically correct
but meaningless expressions like this one:


→
3 + _a,_


which can not be evaluated or computed.
In the spirit of arrow notation, we could write


→ → → →
_a_ + _b_ = _c._


While this notation might be more rigorous and consistent, it is too
noisy and laborious to use. We will stick to the traditional overloaded
notation, remembering that the meaning is different.


**48** - Tensors For Inquiring Minds


_Anti-arrows and special arrow_


For every arrow there exists an “anti-arrow” (or _reverse_ arrow):


→ →
_a_ �→ (− _a_ )



→ →

with an obvious meaning of (− _a_ ) – arrow of the same length as _a_ but

pointing in the opposite direction. When added, an arrow and its reverse
result in a special element – _zero arrow_ :



→
_a_ ) – arrow of the same length as



with an obvious meaning of (−



→ →
_a_ + (− _a_ ) =



→

0 _._



Zero arrow has zero length and may have _any direction_ because the
latter does not matter in any operations with arrows. Zero arrow plays
the same role as the number zero in the algebra of numbers:



→

_b_ +



→ →

0 = 0 +



→

_b_



→

_b_ =



→

for any arrow _b_ .

So far we established several similarities between numbers and ar
rows. These similarities concerned addition. How about multiplication?


3.2.2 Arrow Product


Is there an operation on arrows in a plane analogous to the product of
two numbers? Let us remind ourselves how a product of two numbers
behaves:


_x_ ∗ _y_ = _y_ ∗ _x_


and

_x_ ∗( _y_ + _z_ ) = _x_ ∗ _y_ + _x_ ∗ _z._


The product of two numbers is commutative, it is proportional to each
of the factors, and the product distributes in a familiar way over the

sum.


→

Now, can we define some operation “∗” or simply “∗” on any pair of


→



_b_



arrows



→
_a_ and



→

_c_



→

_b_ =



→

_a_



→

∗



such that it produces an arrow _in the same plane as the original vectors_

→ →

and is proportional to both _a_ and _b_ ? Additionally, the product should

have a simple distributive property over the sum of two arrows:



→
_a_ and



and is proportional to both



→

_a_ ∗



→
_a_ ∗(



→

_b_ +



→
_c_ ) = (



→

_b_ ) + (



→

_a_ ∗



→
_c_ ) _._


Arrows and Vectors                         - **49**


It is an excellent exercise to come up with various candidates for the
product of two arrows and to analyze whether they satisfy this requirement. Here are some example considerations. The variant


→ → →
_a_ ∗ _b_ = _a_


→
does not work, since the result is not proportional to _b_ . For similar

→ → →
reasons, the variant _a_ ∗ _b_ = _b_ won’t work. The variant


→ → → →
_a_ ∗ _b_ = _a_ + 2 _b_


or any similar sum with arbitrary coefficients won’t work, since the re
→ → →
sults is not proportional to either _a_ or _b_ (doubling _a_ does not double


→
the result; similarly for _b_ ).
A reasonable candidate could be


→ → →
_a_ ∗ _b_ = _ab._


The result is proportional to _a_ and _b_, however, this definition won’t be
compatible with the multiplication properties:


→ → → → → → → → → →
_a_ ∗ 0 = _a_ ∗( _b_ + [− _b_ ]) = _a_ ∗ _b_ + _a_ ∗[− _b_ ] = 2 _ab._


This is unacceptable, because we must have


→ →
_a_ ∗ 0 = _a_ ∗ 0 = 0 _._


In later chapters, after we learn about _compound numbers_ (Section
6.2) and _linear operators_ (Section 4.2), we will encounter a useful definition of a product of two arrows _in a plane_ that yields an arrow in _the_
_same plane_ .


_Arrows and Numbers_


Operations with arrows require the concept of numbers. Indeed, without
numbers we could not write the following very natural relation:


→ → →
_a_ + _a_ = 2 _a._


The sum of identical arrows yields an arrow twice as long and pointing in
the same direction. Numbers are used in many other operations involving
arrows and are essential in the algebra of arrows.


**50** - Tensors For Inquiring Minds


3.3 BASIS


We can combine two non-parallel arrows [1] :


→ → →
_a_ + _b_ = _c._


→
When read from right to left, this equation states that an arrow _c_ can
be written as the sum of two other non-parallel arrows. This statement
can be generalized: _Any arrow can be “built from” a pair of non-parallel_
_arrows, by “stretching” each arrow if necessary_ (see Figure 3.5):


→ → →
_c_ = _αa_ + _β_ _b._


→ →
Figure 3.5 A pair of non-parallel arrows, _a_ and _b_, can be used as basis

→ → →
– building blocks for all other arrows. In this example: _c_ = _αa_ + _β_ _b_ .


→ →
The non-parallel arrows _a_ and _b_ are called _independent_ arrows (one
is not the scaled version of the other), and the pair of such arrows is
called the _basis_ . Once the basis is found and fixed, every arrow gets a
numeric _representation_ as a pair of real numbers:


→
_c_ �→( _α, β_ ) _._


The numbers _α_ and _β_ are called _components_ of the arrow → _c relative to_

→ →
_the basis_ { _a,_ _b_ } _._
_Note_ : All we require from the basis arrows is to be independent (nonparallel). They do not have to be perpendicular, and they can have any
length. It is often helpful, however, to choose arrows of some unit length
and pointing in orthogonal directions. We will return to this point in
Sections 3.5 and 5.2.


1Parallel arrows are combined trivially.


Arrows and Vectors                         - **51**


3.3.1 Basis Notation


After some experimentation, it has been established that a special notation for the basis arrows is convenient. All basis arrows are denoted by
a letter _e_ . Next, within the given basis the arrows are enumerated using
an integer subscript:
→ →
_e_ 1 _,_ _e_ 2 _._


An arrow → _a_ is also written in this basis using components with subscripts:


→ → →
_a_ = _a_ 1 _e_ 1 + _a_ 2 _e_ 2 _._


Similarly for any other arrow:


→ → →
_b_ = _b_ 1 _e_ 1 + _b_ 2 _e_ 2 _._


Of course these expressions are for arrows in a plane. For arrows in
three dimensions the basis will have three arrows {→ _e_ 1 _,_ → _e_ 2 _,_ → _e_ 3} and the
expansions will look like


→ → → →
_a_ = _a_ 1 _e_ 1 + _a_ 2 _e_ 2 + _a_ 3 _e_ 3 _._


This idea can be easily generalized to any number of dimensions!


**Exercise 3.1** _Use Einstein’s summation rule to write the expansion of_
→ →
_an arbitrary vector_ _a in terms of the basis vectors_ _e_ _i,i_ = 1 _,...,n._


Using components of arrows in a given basis, every graphical operation with arrows can be translated into an algebraic manipulation of
components. For example, an addition of three vectors


→ → → →
_a_ + _b_ + _c_ = _d_


has a component-wise representation (see Fig. 3.6):


_ai_ + _bi_ + _ci_ = _di._


This single equation must be understood as “encoding” several equations
– one for each value of the index _i_ . Such an approach is very convenient
when problems involve “arrows” in three or more dimensions.


**52** - Tensors For Inquiring Minds


Figure 3.6 Introduction of basis arrows {→ _e_ _i_ } translates operations on
arrows from a graphical problem involving manipulation of arrows into
an algebraic problem involving manipulation of numbers.


3.4 MANY BASES


Arrows of any basis are neither special nor unique. The choice of basis
arrows is arbitrary, with some choices more suitable to a given problem,
and some choices less so. Not infrequently several bases are used to
analyze the same problem from different “points of view.”
To differentiate between various sets of basis arrows they may be
labeled with different numbers of “prime” marks:


{→ _e_ _i_ } _,_ {→ _e_ ′ _i_ [}] _[,]_ {→ _e_ ′′ _i_ [}] and so on.


_“New” and “Old” Bases_


→
Usually, the basis { _e_ _i_ } is introduced first and is called the _old basis_ (or
_original basis_ ), whereas the basis {→ _e_ ′ _i_ [}][ is introduced second and is called]
the _new basis_ .


We can express any arrow in the new basis:


→ ′ → → →
_a_ = _a_ 1 _e_ ′1 [+] _[ a]_ [′] 2 _e_ ′2 [=] _[ a]_ [′] _i_ _e_ ′ _i_ _[.]_


Note that we added the “prime” marks to the components of the arrow
_a_ [′] _i_ [to help identify which basis is used to determine them.]


Arrows and Vectors                       - **53**


The same arrow is also expressed in terms of the “old”/original basis:



→
_a_ = _ai_



→
_e_ _i._



The components _ai_ and _a_ [′] _i_ [are related. To find how we can expand the]

new basis arrows in terms of the old ones:



→ _e_ ′1 [=] _[ E]_ [1]



→ _e_ ′



→ _e_ 1 + _E_ 2



→
_e_ 2



and



→ _e_ ′2 [=] _[ E]_ [3]



→ _e_ ′



→ _e_ 1 + _E_ 4



→
_e_ 2 _._



Here the numbers _E_ 1 _, E_ 2 _,_ represent the components of



→ _e_ ′



Here the numbers _E_ 1 _, E_ 2 _,_ represent the components of _e_ ′1 [relative to]

the basis {→ _e_ _i_ }; similarly for the numbers _E_ 3 _, E_ 4.



→ _e_ _i_ }; similarly for the numbers _E_ 3 _, E_ 4.



_Rotated Basis_



Consider new basis


→ _e_ ′1 [=]



→
_e_ 1 +



→
_e_ 2 and



→ _e_ ′2 [=]



→
_e_ 1 −



→
_e_ 2 _._



→ _e_ ′



In this case _E_ 1 = _E_ 2 = 1 and _E_ 3 = − _E_ 4 = 1. The basis vector



In this case _E_ 1 = _E_ 2 = 1 and _E_ 3 = − _E_ 4 = 1. The basis vector _e_ ′1 [is pointing]

diagonally between → _e_ 1 and → _e_ 2. Can you find the direction of → _e_ ′2 [?]



→
_e_ 1 and



→
_e_ 2. Can you find the direction of



→ _e_ ′



′2 [?]



More flexible notation for the components of basis arrows is preferred.
Instead of using _E_ with a single index, we can use double index notation:



→ _e_ ′1 [=] _[ E]_ [11]



→ _e_ 1 + _E_ 12



→
_e_ 2



and



→ _e_ ′2 [=] _[ E]_ [21] → _e_ 1 + _E_ 22



→
_e_ 2 _._



Note how the first index of _Eij_ matches the basis arrow being expanded,
while the second index matches the arrow it multiplies.

→

After plugging these expressions into the expansion of _a_ in terms of

→ _e_ ′ [and] → _e_ ′



After plugging these expressions into the expansion of



1 [and]



→ _e_ ′



2 [, we obtain]



→ ′
_a_ = _a_ 1 _[E]_ [11]



→ ′
_e_ 1 + _a_ 1 _[E]_ [12]



→ ′
_e_ 2 + _a_ 2 _[E]_ [21]



→ ′
_e_ 2 + _a_



→ ′
_e_ 1 + _a_ 2 _[E]_ [22]



→ ′
_e_ 1 + _a_



→
_e_ 2 _._



Grouping the terms with respect to the basis arrows, we find



→ ′
_a_ = ( _a_ 1




[′] 2 _[E]_ [21][)]




[′] 2 _[E]_ [22][)]



′

1 _[E]_ [11] [+] _[ a]_ [′] 2



→
_e_ 2 _._



→ ′
_e_ 1 + ( _a_ 1



′

1 _[E]_ [12] [+] _[ a]_ [′]


**54** - Tensors For Inquiring Minds


→

Comparing this with the expansion of _a_ in terms of the original basis,

we obtain:



_a_ 1 = _a_ [′]




[′] 1 _[E]_ [11] [+] _[ a]_ [′]




[′] 2 _[E]_ [21] [=] _[ a]_ [′] _i_



_i_ _[E][i]_ [1]



and



_a_ 2 = _a_ [′]




[′] 1 _[E]_ [12] [+] _[ a]_ [′] 2




[′] 2 _[E]_ [22] [=] _[ a]_ [′] _i_



_i_ _[E][i]_ [2] _[.]_



In a compact form, these two equations become


_aj_ = _a_ [′] _i_ _[E][ij][.]_


**Exercise 3.2** _Using Einstein’s summation rule, show that the relations_
_between the “new” and “old” basis arrows can be written as follows:_



→ _e_ ′ _i_ [=] _[ E][ij]_



→
_e_ _j._



_Power of ESR_


→

The relations between the components of a vector _a_ in different bases can

be quickly obtained using Einstein’s summation rule. Indeed, we have



→
_a_ = _aj_


from which follows


_Contravariant Vectors_



→ ′
_e_ _j_ = _ai_



→ _e_ ′



_i_ [(] _[E]_ _ik_



→
_e_ _j,_



′ _i_ [=] _[ a]_ [′]



→ ′
_e_ _k_ ) = _ai_ _[E]_ _ij_



→ ′
_e_ _k_ ) = _a_



_aj_ = _a_ [′] _i_ _[E]_ _ij_ _[.]_



An important observation can be made when we compare the relations

→

of components of an arbitrary arrow _a_ and the relation between the basis


arrows:



→ _e_ ′ _i_ [=] _[ E][ij]_



→
_e_ _j_ vs. _aj_ = _a_ [′] _i_ _[E][ij][.]_



The same set of components _Eij_ allows us to go from the original basis
→ _e_ _j_ to the “new” basis → _e_ ′ _i_ [, and in the] _[ opposite]_ [ direction – from] _[ a]_ [′] _i_ [to] _[ a][j]_

– for the components of arrows. Due to this “contrary” behavior of the
arrow components, arrows are called _contravariant vectors_ .

The following exercise helps better understand the contravariant nature of arrows.



→ _e_ ′



_i_ [, and in the] _[ opposite]_ [ direction – from] _[ a]_ [′] _i_


Arrows and Vectors                         - **55**


**Exercise 3.3** _Consider a “new” basis_


→ _e_ ′1 [=] _[ µ]_ → _e_ 1 _,_ → _e_ ′2 [=] _[ ν]_ → _e_ 2 _._


( _a_ ) _Write out the components Eij explicitly._
( _b_ ) _Given the coefficients a_ 1 _and a_ 2 _of a vector_ → _a, find the coefficients_
_a_ [′] 1 _[and][ a]_ [′] 2 _[relative to the “new” basis.]_


The last problem demonstrates that when basis arrows are scaled
(“stretched” or “compressed”), the corresponding coefficients are also
scaled, but in the _opposite direction_ . It has to be this way if we want the
→ → →
combination _a_ = _a_ 1 _e_ 1 + _a_ 2 _e_ 2 to remain the same and represent _the same_
_arrow_ in _different bases_ . Thus, the change (variation) of components of
arrows is in a certain sense opposite (contrary) to the behavior of the
basis arrows, justifying the name _contravariant_ .


_Covariant and Contravariant Vectors_


There are only two kinds of vectors [2] : _contravariant_ and _covariant_ . As we
found out, the components of contravariant vectors are related via the transformation rule
_aj_ = _a_ [′] _i_ _[E]_ _ij_ _[.]_


Later, in Section 5.6, we will discover new type of vectors ( _covariant vectors_ )
whose components transform similarly to basis vectors ( _covariantly_ ):


_b_ [′] _i_ [=] _[ E]_ _ij_ _[b]_ _j_ _[.]_


Here _Eij_ are the components of the “new” basis arrows in terms of the “old”
basis arrows:
→ _e_ ′ _i_ [=] _[ E]_ _ij_ → _e_ _j._


Arrows represent contravariant vectors. We will soon learn what kind of objects correspond to covariant vectors.


3.4.1 Transposition*


At this point a reminder must be given: All material in sections with an
asterisk (like this one) is either optional or slightly more advanced than
usual. These sections can be skipped without a significant impact on the
main message of the book.


2Although we have not formally defined vectors yet, we can still acknowledge
that they are not all the same.


**56** - Tensors For Inquiring Minds


The way of writing the relation between the components of the same

→

vector _a_ in different bases

_aj_ = _a_ [′] _i_ _[E][ij]_


seems different from the relation between the basis vectors:



→ _e_ ′ _i_ [=] _[ E][ij]_



→
_e_ _j._



→

The difference in notation – the use of _j_ for the components of _a_ instead

of _i_ – is superficial since the labeling of indices in these expressions is
not fixed. Indeed, we can rewrite the former expression as



_aj_ = _a_ [′] _i_




[′] _i_ _[E][ij]_ → _aj_ = _a_ [′]




[′] _k_ _[E][kj]_ → _ai_ = _a_ [′]



_k_ _[E][ki]_



and finally



_ai_ = _a_ [′] _j_ _[E][ji][,]_



keeping the summation of the “primed” component with the first index
of _E_ .
_ji_

We can modify the last expression further, writing


_ai_ = _Fija_ [′] _j_ _[.]_


Here the summation of the components _a_ [′] _j_ [happens with the] _[ second]_

index of some coefficients _Fij_, in full analogy with the relation between
the basis vectors. From the equality



_a_ [′]




[′] _j_ _[E][ji]_ [=] _[ F][ij][a]_ [′] _j_



_j_



follows the relations between the coefficients _Eij_ and _Fij_ :


_Fij_ = _Eji._


For a two dimensional plane, these can be written fully:


_F_ 11 = _E_ 11 _, F_ 12 = _E_ 21 _, F_ 21 = _E_ 12 _, F_ 22 = _E_ 22 _._


The coefficients _F_ are obtained from _E_ by _transposing_ the latter; symbolically we can write

_F_ = _T_ ( _E_ ) _,_


or, using a more traditional notation:


_F_ = _E_ _[T]_ and _Eij_ _[T]_ [=] _[ E][ji][.]_


Arrows and Vectors                         - **57**


_Matrices_


Often the coefficients and components that require two indices, like _Eij_, are
conveniently written using special tables called _matrices_ . For example, we
can write

_E_ _E_ 12
= ( _E_ _[E]_ 21 [11] _E_ 22 [)] _[ .]_


Using the matrix form, the operation of transposition looks like “swapping” of
the non-diagonal elements:


_E_ _[T]_ _E_ 21
= ( _E_ _[E]_ 12 [11] _E_ 22 [)] _[ .]_


Although matrices are often used in practical calculations, they will not be
used much in this book.


Using transposition, we can write the relation between the components of any vector in different bases as



_ai_ = _E_ _[T]_




[′]

_j_ (



_i_ [=] _[ E][ij]_



_ij_ _[a]_ [′]



→ _e_ ′



→
_e_ _j_ _._
)



Comparing the relations between the components of the vector and between the basis vectors, we see that the indices are labeled identically,
and the summation happens in a similar manner – using the second
index of the coefficients.

This form of writing the relations between the components of vectors might appear more consistent or aesthetically pleasing, but it has no
significant mathematical advantage. We did this exercise with the sole
purpose of introducing an important _operation of transposition_ . Transposition is used often in the world of vectors and tensors.


3.4.2 Going The Opposite Way



Above, we expanded the ”new” basis in terms of the ”old” one:



→ _e_ ′



_e_ _i_ [=]

_Eij_ → _e_ _j_ . We can expand the “old” basis → _e_ _i_ in terms of the “new”:



→
_e_ _j_ . We can expand the “old” basis



→
_e_ _i_ in terms of the “new”:



→ _e_ _i_ = _Eij_ ′



→ _e_ _i_ = _E_ ′



→ _e_ ′ _j_ _[.]_



→ _e_ ′



The components _Eij_ [′] [are related to the components] _[ E][ij]_ [. We will see that]

they “cancel” each other in a certain sense. Indeed, if we plug into the
last equation the expansion



→ _e_ ′ _j_ [=] _[ E][jk]_



→ _e_ ′



→
_e_ _k,_


**58** - Tensors For Inquiring Minds


we will arrive at the expression



→ _e_ _i_ = _Eij_ ′ _[E][jk]_ → _e_ _k._



**Exercise 3.4** _Write out explicitly the sum implied in Eij_ [′] _[E][jk][, assuming]_

_i_ = 1 _and k_ = 2 _._



Given the obvious fact that


→ _e_ 1 = 1


→
_e_ 2 = 0



→
_e_ 1 + 0


→ _e_ 1 + 1



→
_e_ 2 _,_


→
_e_ 2 _,_



we conclude that the components _Ejk_ and _Eij_ [′] [satisfy the relation]



_Eij_ [′] _[E][jk]_ [=] _[ δ][ik][,]_ (3.1)



where _δik_ is the already familiar Kronecker’s delta.

The relations (3.1) represent 4 equations with 4 unknowns. This
means that if we know the components _Eij_, we can calculate the components _Emn_ [′] [(unknowns) and vice versa. Indeed, the relations (3.1) will]

be explicitly written out as follows:


_E_ 1 [′] _j_ _[E][j]_ [1] = 1 _,_

_E_ 1 [′] _j_ _[E][j]_ [2] = 0 _,_

_E_ 2 [′] _j_ _[E][j]_ [1] = 0 _,_

_E_ 2 [′] _j_ _[E][j]_ [2] = 1 _._


If we denote (taking _Eij_ as known in this case)


_a_ = _E_ 11 _,b_ = _E_ 12 _,c_ = _E_ 21 _,d_ = _E_ 22 _,_


and (taking _Eij_ [′] [as unknown in this case)]



_w_ = _E_ [′]



11 [′] _[,x]_ [ =] _[ E]_ [′]



12 [′] _[,y]_ [ =] _[ E]_ [′]



21 [′] _[,z]_ [ =] _[ E]_ [′]



22 _[,]_



then the set of four equations becomes


_aw_ + _cx_ = 1 _,_ (3.2)


_bw_ + _dx_ = 0 _,_ (3.3)


_ay_ + _cz_ = 0 _,_ (3.4)


_by_ + _dz_ = 1 _._ (3.5)


Arrows and Vectors                         - **59**


**Exercise 3.5** _Solve the equations (3.2-3.5) and show that_


_w_ = _d_ /∆ _, x_ = − _b_ /∆ _, y_ = − _c_ /∆ _, z_ = _a_ /∆ _,_


_where_ ∆ = _ad_ − _bc._

Hint _: Notice how the four equations can be grouped into two indepen-_
_dent sets of two equations with two unknowns._


We showed that the components _Eij_ and _Emn_ [′] [satisfy the relations]


_Eij_ [′] _[E][jk]_ [=] _[ δ][ik][.]_


There are four more useful relations that the components _Eij_ and _Emn_ [′]
satisfy. To find them, we must expand the “new” basis arrows in terms
of the “old” ones:
→ _e_ ′ _i_ [=] _[ E][ij]_ → _e_ _j,_


and then expand the “old” arrows in terms of the “new” basis, to obtain


→ _e_ ′ _i_ [=] _[ E][ij][E]_ _jk_ [′] → _e_ ′ _k_ _[.]_


Using the same arguments as before, we conclude that


_EijEjk_ [′] [=] _[ δ][ik][.]_ (3.6)


These relations are not the same as (3.1), since the order of _E_ and _E_ [′] is
switched. If we try to switch the order of _E_ and _E_ [′] in (3.6)


_Ejk_ [′] _[E][ij]_ [=] _[ δ][ik]_


we will discover that the summation indices differ from the summation
indices in (3.1). Thus, there are two ways to express the fact that the
components _E_ and _E_ [′] “cancel” each other: _EE_ [′] = 1 and _E_ [′] _E_ = 1.
The relationship between the coefficients _Eij_ and _Eij_ [′] [, as well as the]
difference between covariant and contravariant vectors is summarized in
Figure 3.7.


**Exercise 3.6** _Starting with the relations (3.6) and using the same nota-_
_tion for the known and unknown components, write down the four equa-_
_tion with four unknowns w,x,y,z, and then solve them in terms of the_
_known components a,b,c,d. Prove that the values of the coefficients Eij_ [′] _[,]_
_determined by the relations (3.6) are the same as those determined by_
_the relations (3.1)._


**60** - Tensors For Inquiring Minds


Figure 3.7 Summary of relations between components for covariant
and contravariant vectors. Components of covariant vectors change in
the same way as the basis vectors. Components of contravariant vectors
change in the way opposite to the change of the basis vectors.


3.5 ORTHONORMAL BASES


When basis arrows have unit length and point in mutually perpendicular
directions, the basis is called _normal_ (normalized length) and _orthogonal_,
or just _orthonormal_ basis. There are infinitely many such bases and one
example is shown in Figure 3.8. Orthonormal bases are very convenient
because many calculations involving components are performed more efficiently and many expressions look simpler in such bases (as an example
see _scalar product_ in the Section 5.2).


3.6 VECTORS DEFINED


Now we are ready to define the concept of a vector, or rather vectors
since a single vector is both useless and hard to define.


Arrows and Vectors                         - **61**


Figure 3.8 Orthogonal arrows of unit length form _orthonormal basis_ .
Here we denoted the basis arrows using the letter _u_ instead of _e_ to
emphasize their unit length.


_Vectors_


Vectors are _mathematical objects_ with the following essential properties:


  - Vectors can be combined (added) pairwise to yield another vector.


  - Vectors can be multiplied by real numbers to yield vectors of parallel direction but
of different length (magnitude or scale).


  - There must be at least one basis, and all vectors can be represented via components in the specified basis.


  - When the basis changes, components transform _in a very specific way_, to ensure
that the _vector remains the same_ .


There are two kinds of vectors: _covariant_ and _contravariant_ . Arrows and

arrow-like quantities correspond to contravariant vectors.


We will see that arrows and arrow-like quantities are not the only
entities that behave like vectors. In the next chapter, we will learn about
various functions on vectors (called _operators_ ) and understand how some
of them represent _covariant vectors_ .


CHAPTER HIGHLIGHTS


  _Arrows in a plane provide a simple model for vectors._


  _Arrows can be manipulated in ways analogous to numbers: Two_
_arrows can be added, and an arrow can be “scaled” (stretched or_
_compressed). Arrows form an algebra._


**62** - Tensors For Inquiring Minds


  - _Basis is an extremely important concept. Basis is a set of objects_

_(arrows) that can be used to “build” all other similar objects (ar-_
_rows). At the same time, basis can not be used to build itself – basis_
_arrows are independent._


  - _Basis can be chosen in an infinite number of ways. There is no_

_special basis. Different bases might be useful for different problems._


  - _Given a basis, arrows can be specified by writing their components_

_(using index notation) relative to the basis._


  - _Einstein’s summation rule is very useful for manipulating expres-_

_sions involving components of arrows._


  - _The exact values of the arrow’s components depend on the basis._

_Changing the basis changes the values of components, while the_
_arrow remains the same. This is one of the defining properties of_

_vectors._


  - _When the basis is changed, components of the same arrow trans-_

_form in a very specific way. Depending on the exact form of trans-_
_formation, we can speak of two kinds of vectors: contravariant and_
_covariant. Arrow-like vectors are examples of contravariant vec-_

_tors._


C H A P T E R 4

### Operators


OPERATOR CONCEPT EXTENDS THE IDEA OF A
# O function. An unary numeric function f takes some numeric value

_x_ as an input and produces another numeric value _y_ :


_f_
_f x_ = _y_ or _x_ �→ _y._


In mathematical jargon, _f maps x_ into _y_ .
Similarly, we can study functions that _operate_ on arrows/vectors,
yielding other arrows/vectors. The parallel between unary functions over
numbers and unary operators over vectors is highlighted in Figure 4.1.


4.1 OPERATORS ON ARROWS


An action of an operator _F_ on arrows can be represented symbolically
as an equation:

_F_ → _a_ = → _b ._


Often a “hat” is placed on top of an operator [1], to emphasize that it is
different from a numeric function:


_F_ ̂ → _a_ = → _b ._


Notice that the argument of an operators _is not_ placed inside parentheses. This is a standard convention.


1In Quantum Physics, for example.


[DOI: 10.1201/9781003620365-4](https://doi.org/10.1201/9781003620365-4) **63**


**64** - Tensors For Inquiring Minds


Figure 4.1 Operators extend the idea of functions. (a) An unary function _f_ can be applied to a number _x_ to produce another number _y_ . (b)
An unary operator _F_ [̂] can be applied to a vector → _a_ to yield another vector

→
_b_ .


_Simple Operators_


It is easy to come up with examples of operators:


  - Unit operator (or _identity_ operator) _I_ [̂], such that


_I_ ̂→ _a_ = → _a._


  - “Zeroing” operator [̂] 0 that maps every vector into a zero vector:


̂ → →
0 _a_ = 0 _._


  - Scaling operator _S_ [̂] 5, such that

̂ → →
_S_ 5 _a_ = 5 _a._


  - Rotation operator _L_ [̂], such that
_L_ ̂ → _a_ = → _b,_


→ →
where _b_ is rotated by 45 [○] counter-clockwise relative to the vector _a_ .


To fully describe an operator _F_ [̂] we must describe how it acts _on_
_every_ arrow. In general, this requires an _infinite_ amount of information,
since the number of arrows is infinite and the action of _F_ [̂] on different


Operators                             - **65**


arrows might be different [2] . Describing the action of a general operator
in graphical terms using arrows is a hopeless task. In this situation the
component representation of arrows saves the day. Let’s see how it works.
→
If we fix a basis { _e_ _i_ }, then every vector gets an algebraic representation as a set of components:


→
→ { _e k_ }
_a_ �→ _ai,_


→ {→ _e k_ }
_b_ �→ _b_ _._
_j_


Now to describe the action of an operator _F_ [̂] on the vector → _a_ we can
specify the components of the result _bj_ for arbitrary components of the
input _ai_ . For vectors in a plane, we have


_b_ 1 = _F_ 1 _a_ 1 _a_ 2


and

_b_ 2 = _F_ 2 _a_ 1 _a_ 2 _._


Thus, a pair of binary numeric functions _F_ 1 and _F_ 2 is sufficient to describe an operator. A situation is significantly simplified in the case of a
very important class of _linear operators_ which we will discuss soon.


**Examples**


Let us take a closer look at a couple of operators. While studying these
examples we must keep in mind that the relations between components
are _specific to basis_ and will change if we change the basis. The question of how exactly the relation between components changes will be
addressed later in Section 4.7 for the simplest types of operators.
The first example operator _F_ [̂] acts on the components as follows:


_b_ 1 = _a_ 1 + _a_ 2 _,_


_b_ 2 = _a_ 1 ∗ _a_ 2 _._


To illustrate these relations visually, we can start with arrows of equal
lengths but pointing in all directions. The tips of such arrows will lie
on a circle, as shown in Figure 4.2 using blue dotted lines. The tips of


2Simple operators given before are special cases when it is easy to describe the
action of operators on _all_ vectors.


**66** - Tensors For Inquiring Minds


Figure 4.2 The action of the operator _F_ [̂] on planar arrow-vectors → _a_ . To
demonstrate how _F_ [̂] acts on arrows of different directions and lengths,
we consider what happens to the circles of two different radii.


→ →
all output arrows _b_ = _F_ [̂] _a_ lie on a curve shown in Figure 4.2 using a
solid red line. In the first example, the arrows tracing the circle of the
radius _R_ = 1 are transformed into arrows tracing a curve that looks like
a parabola.


Operators                             - **67**


→
**Exercise 4.1** _Show that when the components of the output arrow_ _b are_
_given by_
_b_ 1 = _a_ 1 + _a_ 2 _,_


_b_ 2 = _a_ 1 ∗ _a_ 2 _,_


_then the circle with the radius R becomes a parabola described by the_
_equation_
_b_ 2 = _b_ [2] 1 [/][2][ −] _[R]_ [2][/][2] _[.]_


In the second example, the operator _G_ [̂] acts on the components as
follows:

_b_ 1 = _a_ 1 − _a_ 2 _,_


_b_ 2 = − _a_ [2] 1 [∗] _[a]_ [2] _[.]_


The effect of this operator on the arrows forming a circle is illustrated
in Figure 4.3. It seems that increasing the radius of the circles does not
substantially change its “image” (solid red line) and only “stretches” the
output curve both horizontally and vertically.


_Linear and Nonlinear Operators_


The operators _F_ [̂] and _G_ [̂] are examples of rather complicated operators. They
are _nonlinear_ because they lack the simple property of _linearity_, defined previously in subsection 2.3.3.
Linear operators connect components of input and output vectors in a simple

way:
_b_ 1 = _A a_ 1 + _B a_ 2 _,_ _b_ 2 = _C a_ 1 + _D a_ 2 _._


Here _A, B, C_, and _D_ are numbers. Different linear operators differ only in
the values of these numbers. Despite their simplicity, linear operators are
powerful and widely used.


Since two arrows can differ only in their magnitude (length) and
directions, the action of an operator can be represented by a combination
of two steps: rotation and scaling; see Figure 4.4. The order of scaling
and rotation does not matter:


_F_ ̂ = ̂ _S_          - ̂ _R_ = ̂ _R_          - ̂ _S._


As our next step, we will study rotation operators in more details.


**68** - Tensors For Inquiring Minds


Figure 4.3 An action of an operator _G_ [̂] on a planar vector → _a_ . To demonstrate how _G_ [̂] acts on arrows of different directions and lengths, we consider what happens to the circles of two different radii.


4.1.1 Rotation Operator


A simple non-trivial operator [3] rotates a vector by some angle, as demonstrated in the Figure 4.5. Strictly speaking, there are infinite number of
such operators, one for each rotational angle _θ_ .


3An example of a trivial operator is the identity operator ̂ _I_ which does not change
the input vector: _I_ [̂] → _a_ = → _a_ . Another example is the operator that always returns “zero”
arrow: [̂] 0 → _a_ = →0.


Operators                             - **69**


Figure 4.4 An action of an operator _F_ [̂] on a planar vector → _a_ can be
described by the sequence of rotation _R_ [̂] and scaling _S_ [̂] : _F_ [̂] = _S_ [̂] - _R_ [̂] .


Figure 4.5 The action of the rotation operator _R_ [̂] on a planar vector → _a_
results in the rotation by a specified angle _θ_ . Such rotation possesses an

important property: _R_ [̂] (→ _a_ + → _b_ ) = _R_ [̂] → _a_ + ̂ _R_ → _b_ .


**70** - Tensors For Inquiring Minds


An important property of any rotation operator is that it preserves
some relations between arrows. For example, given a vector


→ → →
_c_ = _a_ + _b,_


→ →
its “image” ( _R_ [̂] _c_ ) can be constructed from rotated vectors ( ̂ _R_ _a_ ) and


→
( _R_ [̂] _b_ ):
_R_ ̂ → _c_ = ̂ _R_ (→ _a_ + → _b_ ) = ( _R_ [̂] → _a_ ) + ( ̂ _R_ → _b_ ) _._


This property is the consequence of two features of the rotation operator:
1) it does not change the length of a vector; 2) it rotates every vector
by the same amount, thus keeping the relative angle between any two
vectors intact, as illustrated in Figure 4.5.
Another important property of rotation operators is an obvious one:


̂ → →
_R_ ( _αa_ ) = _α_ ( ̂ _R_ _a_ ) _._


Rotation operators represent a subset of a larger set of important operators – _linear operators_ .


4.2 LINEAR OPERATORS


_Linear operators_ are operators with a simple yet important property of
_linearity_ . Two things are required for a linear operator _L_ [̂] :


_L_ ̂ (→ _a_ + → _b_ ) = ( _L_ [̂] → _a_ ) + (̂ _L_ → _b_ )


and
_L_ ̂ ( _α_ → _a_ ) = _α_ (̂ _L_ → _a_ ) _._


Rotation operators satisfy these requirements, as we established in the
previous section.
To represent linear operators numerically using basis arrows requires
→ → →
relatively little information. Indeed, for a general arrow _a_ = _a_ 1 _e_ 1 + _a_ 2 _e_ 2
the action of the operator _L_ [̂] can be written as


_L_ ̂ ( _a_ 1→ _e_ 1 + _a_ 2→ _e_ 2) = [̂ _L_ ( _a_ 1→ _e_ 1)] + [̂ _L_ ( _a_ 2→ _e_ 2)] = _a_ 1(̂ _L_ → _e_ 1) + _a_ 2(̂ _L_ → _e_ 2) _._


Thus, to define the action of the linear operator _L_ [̂] on an arbitrary arrow
→ → →
_a_, it is sufficient to define its action on the basis arrows _e_ 1 and _e_ 2.


Operators                             - **71**


Operator _L_ [̂] acts on arrows to yield other arrows. Thus, we can write


_L_ ̂ → _e_ 1 = → _f_ 1 and _L_ [̂] → _e_ 2 = → _f_ 2 _._


→ →
Like any other vectors, the vectors _f_ 1 and _f_ 2 can be written in terms of
the basis vectors:
→ → →
_f_ 1 = _l_ 1 _e_ 1 + _l_ 2 _e_ 2 _,_


→ → →
_f_ 2 = _l_ 3 _e_ 1 + _l_ 4 _e_ 2 _._


These equations can be written more compactly if we improve the notation. Firstly, instead of numbers _l_ 1 _,l_ 2 _,l_ 3 _,l_ 4 we will write


_L_ ̂ → _e_ 1 = _L_ 11→ _e_ 1 + _L_ 12→ _e_ 2


and
_L_ ̂ → _e_ 2 = _L_ 21→ _e_ 1 + _L_ 22→ _e_ 2 _._


Notice how the subscript indices match nicely with the indices of the
basis arrows: The first subscript index of _Lij_ corresponds to the basis
vector being acted on, while the second index corresponds to the basis
vectors being multiplied by _Lij_ . The second step is to use the summation
agreement: _L_ ̂ → _e_ 1 = _L_ 1 _j_ → _e_ _j,_


_L_ ̂ → _e_ 2 = _L_ 2 _j_ → _e_ _j._


Finally, we can write the most compact form:


_L_ ̂ → _e_ _i_ = _Lij_ → _e_ _j._ (4.1)


In summary, the action of a linear operator _L_ [̂] on the basis arrows (and,
consequently, on _any_ arrow) is completely determined by its components
_Lij_ – just four numbers for arrows in a plane [4] .
The components of a linear operator _L_ [̂] are specific to the basis. This
is completely analogous to the components of arrow-vectors. Indeed, the
use of a basis translates arrows and linear operators from the graphical
world of drawings into the algebraic world of numbers:


→ →
→ { _e_ 1 _,_ _e_ 2}
_a_ →�→→ _ai,_
̂ { _e_ 1 _,_ _e_ 2}
_L_ �→ _Lij._


4In general, for a space of _N_ dimensions the number of components equals _N_ 2.


**72** - Tensors For Inquiring Minds


_Simple Linear Operators_


Four simple linear operators can be defined without specifying their compo
nents:



→ →

- Unit operator, such that _I_ [̂] _a_ = _a_ .


- “Zeroing” operator that maps every vector into a zero vector:



→

0 _._



̂0



→

_a_ =




- Scaling operators, such that _S_ [̂]



→
_a_ for some specified value _α_ .



→

_a_ = _α_



→



→




- Rotation operators, such that _R_ [̂] _θ_



→

_a_ =



_b_, where



Rotation operators, such that _Rθ_ _a_ = _b_, where _b_ is simply rotated by specified

angle _θ_ .



To find the components of any operator we must see how it acts on basis
vectors. Let’s see how this works for the scaling operator _S_ [̂] described above:



_S_ ̂


_S_ ̂



→
_e_ 2 _._



→
_e_ 1 = _α_



→ →
_e_ 1 + 0 _e_ 2 _,_



→
_e_ 1 + 0



→ →
_e_ 2 = 0 _e_ 1 + _α_



From these equations, we can read the components _Sij_ and write them in
matrix form:

_S_ ̂ _S_ 12 0
= ( _S_ _[S]_ 21 [11] _S_ 22 [) = (] _[α]_ 0 _α_ [)] _[ .]_


A similar approach can be used to find the components of any linear opera
tor.


**Exercise 4.2** _Consider an operator_ _N_ [̂] _which “normalizes” an arrow –_
_returns an arrow of unit length pointing in the same direction as the_
_original one. For example:_



→
_ua_ =



→

_a_


_a_ _[.]_



_N_ ̂



→

_a_ =



_Is it a linear operator?_


Operators                             - **73**


_J_ ̂ _-operator_


Operator that rotates any vector in a plane by 90 degrees counter-clockwise
has a special notation (it will be heavily used in Sections 6.2 and 6.3):


_R_ ̂ _π_ /2 = ̂ _J._


→
It is instructive to see how this operator acts on an orthonormal basis { _e_ _i_ }:


_J_ ̂→ _e_ 1 = → _e_ 2 = 0 → _e_ 1 + 1 → _e_ 2


and
_J_ ̂→ _e_ 2 = −→ _e_ 1 = −1 → _e_ 1 + 0 → _e_ 2 _._


From the last two expressions we can find the components of the _J_ [̂] -operator:


_Jij_ = ( _J_ _[J]_ 21 [11] _JJ_ 1222 [) = (] − [ 0] 1 10 [)] _[ .]_


Here we used _matrix_ form of presenting the components of linear operators.
In this form, the first index of the components corresponds to the row in the
matrix-table, and the second index corresponds to the column.
Another important property of this operator can be seen when we act on any
vector twice:

̂ → →
_J_ ( _J_ [̂] _a_ ) = − _a._


Indeed, rotating any vector twice by 90 degrees results in total rotation by
180 degrees – the direction of the original vector is flipped. What we showed
is that the sequence _J_ [̂]    - _J_ [̂] is the same as the operator (− _I_ [̂] ):


̂
_J_               - _J_ [̂] = − _I._ [̂]


If you are familiar with complex numbers and know that _i_ [2] = _i_ ∗ _i_ = −1, you
might see the analogy between the _J_ [̂] -operator and the ”imaginary unit” _i_ .
The analogy is not accidental and will be explored in detail in Section 6.2.


4.3 PLOTTING LINEAR OPERATORS


A numeric unary function _f x_ = _y_ can be represented graphically as a
plot “ _y vsx._ ” In this plot, we indicate a value _y for each value of x_ .
Linear operators of the type


_L_ ̂ → _a_ = → _b_


**74** - Tensors For Inquiring Minds


also allow graphical representation. We can, for example, draw an arrow
→ _b for each value of_ → _a_ . The input vector → _a_ can vary both its lengths
and direction. For a linear operator _L_ [̂] the change in length of the input
→
vector _a_ is handled trivially:


_L_ ̂ ( _α_ → _a_ ) = _α_ (̂ _L_ → _a_ ) _._


In words: To find the action of a linear operator on a scaled vector we
first apply the operator to the original vector and then scale the result.
It also follows that all vectors _L_ [̂] ( _α_ → _a_ ) corresponding to different values
of the scale factor _α_ are _parallel_ – they are all parallel to the vector
→ →
_b_ = _L_ [̂] _a_ .

The preceding considerations show that to describe the action of a
linear operator on various input vectors we can focus only on vectors
with unit lengths, but pointing in all possible directions. The tips of all
such vectors form a unit circle, as illustrated in Figure 4.6.


Figure 4.6 Input vectors for a linear operator can vary in direction.
In this example, the components of the operator are: _L_ 11 = 2/10 _,L_ 12 =
3/10 _,L_ 21 = 5/10 _,L_ 22 = −7/10 _._


For linear operators, it is sufficient to plot only the half of the circle,

since
_L_ ̂ (−→ _a_ ) = −(̂ _L_ → _a_ ) _._


In other words, the missing half is the inverted copy of the original half.
An illustration of this is given in Figure 4.7 for an operator _L_ [̂] with
components _L_ 11 = 2/10 _,L_ 12 = 3/10 _,L_ 21 = 5/10 _,L_ 22 = −7/10.
Another linear operator, with components _L_ 11 = 5/10 _,L_ 12 = 2 _,L_ 21 =
0 _,L_ 22 = 3/2, is graphically represented in Figure 4.8. In the Figure 4.8(a)


Operators                             - **75**


Figure 4.7 To graphically describe a linear operator we can specify how
it acts on vectors from the top half of the circle (the bottom is found by
inverting the top). In this example, the components of the operator are:
_L_ 11 = 2/10 _,L_ 12 = 3/10 _,L_ 21 = 5/10 _,L_ 22 = −7/10 _._


the action of the operator only on unit vectors from the top half-plane is
shown, with the missing part (bottom half-plane) is easily constructed by
inverting the transformed part through the origin. Although not easily
seen, there are two pairs of vectors [5] that are transformed rather simply
by this linear operator – they are scaled without rotation. Two such
vectors are shown in Figure 4.8(b). Such vectors are called _eigen-vectors_
of a given operator. Eigen-vectors are discussed in more detail in the

next section.

Another way to graphically represent a linear operator is to plot two
functions: 1) How much an input unit vectors gets rotated; 2) How much
an input unit vector gets stretched. This is done in Figure 4.8(c) and
(d). From the Figure 4.8(c) it can be seen that there are two unit vectors
that are not rotated by the operator (rotation angle is zero for the input
vectors at 90 degrees and at about 130 degrees or 310=130+180 degrees).
Eigen-vectors are important and finding them for a given linear operator is an problem often encountered in physics and mathematics. This
problem is called _eigen-vector problem_ or _eigen-problem_ for short.


5Two vectors and their reversed images.


**76** - Tensors For Inquiring Minds


Figure 4.8 Graphical representation of a linear operator _L_ [̂] with components: _L_ 11 = 5/10 _,L_ 12 = 2 _,L_ 21 = 0 _,L_ 22 = 3/2 _._ (a) The effect of the
operator on unit-length arrows with direction from 0 [○] to 180 [○] ; (b) Two
special arrow-vectors that do not change their direction under the action
of the operator _L_ [̂] . The operator simply scales the arrows. Such vectors
are called _eigen-vectors_ of the operator; (c) Horizontal axis: initial orientation of the unit-length arrow; vertical axis: rotation angle of each
unit-length arrow. Two special angles are highlighted. For each special
angle, the arrow is not rotated. Such arrows are called eigen-vectors of
the operator _L_ [̂] ; (d) Horizontal axis: initial orientation of the unit-length
arrow; vertical axis: the scaling factor of each unit-length arrow.


4.4 EIGEN-PROBLEM*


_Eigen-vectors of a linear operator_ are special vectors that are not rotated
by the operator, eigen-vectors can only be scaled [6] . This requirement can


6Strictly speaking, it is possible to ”flip” the direction of a vector, effectively
rotating it by 180 degrees. However, the resulting vector is still parallel to the original

one.


Operators                             - **77**


be expressed using a simple equation:


_L_ ̂ → _a_ = _α_ → _a,_


→ →
or, if there exists another eigen-vector _b_ different from _a_ :


_L_ ̂ → _b_ = _β_ → _b._


Here the numbers _α_ and _β_ specify the scaling coefficients. The equations

given above are called _eigen-problem equations_ . The vectors → _a_ and → _b_ are
called _eigen-vector_, the scaling factors _α_ and _β_ are called _eigen-values_ .
In general, _α_ ≠ _β_, as illustrated in Figure 4.8(b).
Not all linear operators have eigen-vectors. A simple example is the
operator of rotation by a finite angle _θ_ ≠ 180 [○] :


̂ → →
_Rθ_ _a_ ≠ _αa._


Simply speaking, it is impossible to rotate a vector without changing its
direction.
All “well-behaved” linear operators [7] (excluding rotation operators
like _R_ [̂] _θ_ ) have the same number of eigen-vectors as the number of basis
vectors. Any “well-behaved” linear operator that operates on vectors in
a plane has two eigen-vectors, as illustrated in Figure 4.8(b). Operators
acting on vectors in three dimensions may have up to three eigen-vectors.
It is possible to find linear operators that have fewer eigen-vectors
than the number of basis vectors. Such operators are called _degenerate_
_operators_ . They are important and we will consider them next for the
special case of two dimensions.


4.5 DEGENERATE LINEAR OPERATORS


In some special cases a linear operator _L_ [̂], when applied to the basis
→ →
arrows _e_ 1 and _e_ 2, can produce parallel arrows:


( _L_ [̂] → _e_ 1) ∥(̂ _L_ → _e_ 2)


or
_L_ ̂ → _e_ 1 = _λ_ (̂ _L_ → _e_ 2)


for some number _λ_ .


7We will encounter ill-behaved linear operators in the next section.


**78** - Tensors For Inquiring Minds


Using components notation, this condition can be written as follows:


_L_ 11→ _e_ 1 + _L_ 12→ _e_ 2 = _λL_ 21→ _e_ 1 + _λL_ 22→ _e_ 2 _._


The vector on the left-hand side is the same vector as on the right-hand
side if they have the same components in the given basis. Therefore, we
must equate the corresponding components:


_L_ 11 = _λL_ 21 and _L_ 12 = _λL_ 22 _._


Cross-multiplying these equations, we obtain


_λL_ 11 _L_ 22 = _λL_ 12 _L_ 21 _,_


from which follows

_L_ 12 _L_ 21 − _L_ 11 _L_ 22 = 0 _._


Linear operator satisfying this condition is called _degenerate_ for the reasons explained below.


**Exercise 4.3** _Show that a degenerate linear operator_ _L_ [̂] _“collapses” all_
_vectors onto the same line, i.e. all_ ( _L_ [̂] → _a_ ) _have the same direction._


Later, in Section 5.7, we will encounter a whole class of useful degenerate linear operators, called _projectors_, whose job is to project any
vector onto a specified direction.


4.5.1 Determinant of a Linear Operator


A non-zero vector has length – its simple numeric characteristic independent of the choice of basis. Operators do not have lengths, but they
do have certain numeric characteristics that also do not depend on the
choice of basis. The two important characteristics of any linear operator
are _determinant_ and _trace_ .

The quantity
_D_ = _L_ 12 _L_ 21 − _L_ 11 _L_ 22


computed from the components of a linear operator is called its _deter-_
_minant_ . Determinant has a clear geometric meaning which can be seen
from the action of the operator _L_ [̂] on the orthonormal basis, as illustrated
in Figure 4.9. Denoting _L_ 11 = _L_ 1, _L_ 12 = _L_ 2, _L_ 21 = _L_ 3, and _L_ 22 = _L_ 4, we
can calculate the area of the parallelogram built from the vectors ( _L_ [̂] → _u_ 1)
and ( _L_ [̂] → _u_ 2) as follows:


_A_ = ( _L_ 1 + _L_ 3)( _L_ 2 + _L_ 4) − 2( _L_ 1 _L_ 2/2 + _L_ 3 _L_ 4/2 + _L_ 2 _L_ 3) _._


Operators                             - **79**


Figure 4.9 A linear operator _L_ [̂] transforms basis vectors → _ui_ into → _v_ _i_ =
_L_ ̂ → _ui_ . For non-degenerate operators the vectors → _v_ _i_ form sides of a parallelogram with non-zero area _A_ = _L_ 12 _L_ 21 − _L_ 11 _L_ 22.


It is simply the area of the rectangle _O_ 126 minus the areas of two rectangles with sides _L_ 2 and _L_ 3, together with two pairs of triangles.
After simplification, the last equation reduces to


_A_ = _L_ 1 _L_ 4 − _L_ 2 _L_ 3 = _L_ 11 _L_ 22 − _L_ 12 _L_ 21 _._


Thus, the determinant of a linear operator _L_ [̂] equals to the ratio of
the area of the parallelogram built from the vectors ( _L_ [̂] → _u_ 1) and (̂ _L_ → _u_ 2) to

→ →
the area of the parallelogram built from the unit vectors _u_ 1 and _u_ 2. Put
differently, a determinant measures how much an area of the parallelogram built from basis vectors is distorted by an operator. Obviously, for
a degenerate linear operator, this ratio is zero, since all arrows “collapse”
onto a single direction.


_Determinant_


For arrow-vectors in three and higher dimensions, we also have linear operators. The meaning of determinant in these higher-dimensional
cases remains similar: Determinant expresses the ratio of _volumes_ built

→ → →
from basis vectors _e_ 1 _,_ _e_ 2 _. . .,_ _e_ _n_, and from their “transformed” versions
_L_ ̂→ _e_ 1 _,_ ̂ _L_ → _e_ 2 _. . .,_ ̂ _L_ → _e_ _n_ .


**80** - Tensors For Inquiring Minds


The second numeric characteristic of a linear operator – called _trace_ – will
be explored below in the Exercise 4.5, after we learn how the components
_Lij_ of a linear operator _L_ [̂] transform when we change basis.


4.6 USING OPERATOR COMPONENTS


It is possible, and is often convenient, to work with a linear operator
using only its components, without referring to arrows or some other
graphical representation.
The action of a linear operator _L_ [̂] on a vector → _a_ can be written in
terms of components:


_L_ ̂ → _a_ = ̂ _L_ ( _ai_ → _e_ _i_ ) = _ai_ (̂ _L_ → _e_ _i_ ) = _ai_ ( _Lij_ → _e_ _j_ ) _._


On the other hand
_L_ ̂ → _a_ = → _b_ = _bj_ → _e_ _j._


Comparing the last two expressions, we observe that the action of a
linear operator can be written entirely in components:


_aiLij_ = _bj._


**Exercise 4.4** _Show that the same relation holds in any other basis._
_Namely, prove that_
_a_ [′] _i_ _[L]_ [′] _ij_ [=] _[ b]_ [′] _j_ _[.]_


The relation between components of the operator _L_ [̂] and vectors → _a_


→
and _b_ can be written differently:


_bj_ = _Lijai_ → _bj_ = _L_ _[T]_ _ji_ _[a][i]_ [→] _[b][i]_ [=] _[ L][T]_ _ij_ _[a][j][.]_


Here we used the operation of transposition (introduced in the subsection 3.4.1 on page 55) and index renaming to make summation over the
second index of _L_ _[T]_
_ij_ [.]


4.7 COMPONENTS TRANSFORMATION


_Warning:_ This section has the highest density of algebraic manipulations in the whole book. However, the manipulations are rather trivial,
they consist only in multiplications and additions. The challenge for the
reader is to stay focused and follow the derivations closely because the
final result is very important. The symbolic operations in this section are


Operators                             - **81**


typical for linear algebra. Without good notation, such calculations may
become too tedious. This is why we will first demonstrate how to use
Einstein’s summation rule to quickly get the desired result. Only after
that we will derive the same result again, showing all steps in detail.
Now let’s get the job done!

At the first look at components, the difference between vectors and
linear operators is in the number of component indices: one for vectors
( _ai_ ), and two for linear operators ( _Lij_ ). To further compare vectors and
linear operators, we can study how the components of the latter transform between different bases.


_Power of ESR and Index Notation_


We first demonstrate the power of Einstein’s summation rule and index notation and find how the transformation relations can be quickly deduced.
We start with the expansion of an operator in the “new” (primed) basis:



_L_ ̂



→ _e_ ′



_i_ [=] _[ L]_ [′] _il_



_il_



→ _e_ ′ _l_ _[.]_ (4.2)



Next, we use the relation between “new” and “old” basis vectors and the
linearity of _L_ [̂] to fully expand the left-hand side:



→ _e_ ′ _i_ [=] _[ E]_ _ij_



→
_e_ _j,_



→ _e_ _k_ = _Ekl_ ′



→ _e_ ′ _l_ _[,]_



→ _e_ ′



_L_ ̂



→ _e_ ′ _i_ [= ̂] _[L]_ [ (] _[E]_ _ij_



→ _e_ _j_ ) = _Eij_ (̂ _L_



→ _e_ _j_ ) = _EijLjk_



→ _e_ _k_ = _EijLjkEkl_ ′



→ _e_ _k_ = _EijLjkE_ ′



→ _e_ ′ _l_ _[.]_



→ _e_ ′



Comparing this to the right-hand side of the equation (4.2), we arrive at



_L_ [′]




[′] _il_ [=] _[ E]_ _ij_ _[L]_ _jk_ _[E]_ [′]



_kl_ _[.]_



Now we will repeat the steps in detail.
The components ( _L_ [′] _ij_ [) of a linear operator][ ̂] _[L]_ [ in the “new” (primed)]

basis are determined in the same way as for the “old” basis:



11



12



_L_ ̂


_L_ ̂



→ _e_ ′



→ _e_ ′



2 [=] _[ L]_ [′]



1 [=] _[ L]_ [′]



→ _e_ ′2 _[,]_



→ _e_ ′



→ _e_ ′



1 [+] _[ L]_ [′]



21



22



→ _e_ ′2 _[.]_



→ _e_ ′



→ _e_ ′



1 [+] _[ L]_ [′]



Next, in the left-hand sides of these equations, we replace



→ _e_ ′



Next, in the left-hand sides of these equations, we replace _e_ ′ _i_ [with their]

expansion in the “old” basis and use the linearity of the operator _L_ [̂] :



→ _e_ 1 + _E_ 12→ _e_ 2) = _E_ 11(̂ _L_



→ _e_ 1) + _E_ 12(̂ _L_ → _e_ 2)



_L_ ̂



→ _e_ ′1 [= ̂] _[L]_ [(] _[E]_ [11]


**82** - Tensors For Inquiring Minds


and



→ _e_ 2) = _E_ 21(̂ _L_



→ _e_ 1) + _E_ 22(̂ _L_ → _e_ 2) _._



_L_ ̂



→ _e_ ′2 [= ̂] _[L]_ [(] _[E]_ [21]



→ _e_ 1 + _E_ 22



The action of _L_ [̂] on the “old” basis is determined by the components _Lij_ :



→
_e_ _j._



_L_ ̂



→ _e_ _i_ = _Lij_



Using these relations, we further transform



→ _e_ ′1 [=] _[ E]_ [11][(] _[L]_ [11]



→ _e_ 2) + _E_ 12( _L_ 21



→ _e_ 1 + _L_ 22



→
_e_ 2)



→ _e_ 1 + _L_ 12



→ _e_ 1 + _L_ 12



and



_L_ ̂


_L_ ̂



→ _e_ ′2 [=] _[ E]_ [21][(] _[L]_ [11]



→ _e_ 2) + _E_ 22( _L_ 21



→ _e_ 1 + _L_ 22



→
_e_ 2) _._



Opening the parentheses and grouping the terms with identical basis

vectors, we get



→ _e_ ′1 [=] _[ µ]_ [1]



→
_e_ 2



→
_e_ 1 + _ν_ 2



→
_e_ 1 + _µ_ 2



and



_L_ ̂


_L_ ̂



→ _e_ ′2 [=] _[ ν]_ [1]



→
_e_ 2 _,_



where, in order to avoid clutter, we introduced notation


_µ_ 1 = _E_ 11 _L_ 11 + _E_ 12 _L_ 21 _,_ _µ_ 2 = _E_ 11 _L_ 12 + _E_ 12 _L_ 22


and


_ν_ 1 = _E_ 21 _L_ 11 + _E_ 22 _L_ 21 _,_ _ν_ 2 = _E_ 21 _L_ 12 + _E_ 22 _L_ 22 _._


Finally, we expand the “old” basis vectors in terms of the “new” ones,

to arrive at



→ _e_ ′



11



12



21



22



2 [=] _[ ν]_ [1][(] _[E]_ [′]



1 [=] _[ µ]_ [1][(] _[E]_ [′]



→ _e_ ′



→ _e_ ′



→ _e_ ′



→ _e_ ′2 [)]



→ _e_ ′



1 [+] _[ E]_ [′]



2 [) +] _[ µ]_ [2][(] _[E]_ [′]



′1 [+] _[ E]_ [′]



and



_L_ ̂


_L_ ̂



→ _e_ ′



11



12



21



22



→ _e_ ′



→ _e_ ′



→ _e_ ′



→ _e_ ′2 [)] _[.]_



→ _e_ ′



1 [+] _[ E]_ [′]



′2 [) +] _[ ν]_ [2][(] _[E]_ [′]



′1 [+] _[ E]_ [′]



Opening the parentheses and grouping the terms with identical basis
vectors results in



11 [′] [+] _[ µ]_ [2] _[E]_ [′]



12 [′] [+] _[ µ]_ [2] _[E]_ [′]



→ _e_ ′



→ _e_ ′



2 [= (] _[ν]_ [1] _[E]_ [′]



′1 [= (] _[µ]_ [1] _[E]_ [′]



21 [′] [)]



→ _e_ ′



22 [′] [)]



→ _e_ ′2



→ _e_ ′



1 [+ (] _[µ]_ [1] _[E]_ [′]



and



_L_ ̂


_L_ ̂



11 [′] [+] _[ ν]_ [2] _[E]_ [′]



12 [′] [+] _[ ν]_ [2] _[E]_ [′]



21 [′] [)]



→ _e_ ′



22 [′] [)]



→ _e_ ′2 _[.]_



→ _e_ ′



1 [+ (] _[ν]_ [1] _[E]_ [′]


Operators                             - **83**


From the last two equations, we can read the components _L_ [′] _ij_ [of the]

operator _L_ [̂] in terms of its components _Lmn_ :



_L_ [′]




[′] 11 [=] _[ µ]_ [1] _[E]_ [′]



11 [′] [+] _[ µ]_ [2] _[E]_ [′]



21 [′] _[,]_ _L_ [′]




[′] 12 [=] _[ µ]_ [1] _[E]_ [′]



12 [′] [+] _[ µ]_ [2] _[E]_ [′]



22 _[,]_



_L_ [′]




[′] 21 [=] _[ ν]_ [1] _[E]_ [′]



11 [′] [+] _[ ν]_ [2] _[E]_ [′]



21 [′] _[,]_ _L_ [′]




[′] 22 [=] _[ ν]_ [1] _[E]_ [′]



12 [′] [+] _[ ν]_ [2] _[E]_ [′]



22 _[.]_



To keep the formulas manageable, we will use the summation convention
and write first



_L_ [′]




[′] 11 [=] _[ µ][i][E]_ _i_ [′]



_i_ 2 _[,]_



_i_ 2 _[.]_



_L_ [′]




[′] 21 [=] _[ ν][i][E]_ _i_ [′]



_i_ [′] 1 _[,]_ _L_ [′]


_i_ [′] 1 _[,]_ _L_ [′]




[′] 12 [=] _[ µ][i][E]_ _i_ [′]


[′] 22 [=] _[ ν][i][E]_ _i_ [′]



Then, observing the matching indices, we can shorten these relations
even further:



_L_ [′]




[′] 1 _j_ [=] _[ µ][i][E]_ _ij_ [′]


[′] 2 _j_ [=] _[ ν][i][E]_ _ij_ [′]



_ij_ _[,]_



_L_ [′]



_ij_ _[.]_



After that, having looked at the expressions for _µi_ and _νi_, we can
shorten them to the following:


_µi_ = _E_ 1 _kLki_ and _νi_ = _E_ 2 _kLki._


Plugging these expressions into the formulas for _L_ [′] _ij_ [, we obtain]



_L_ [′]




[′] 1 _j_ [=] _[ E]_ [1] _[k][L][ki][E]_ [′]



_ij_ [′] [and] _[ L]_ [′] 2




[′] 2 _j_ [=] _[ E]_ [2] _[k][L][ki][E]_ [′]



_ij_ _[.]_



Finally, comparing the indices, we arrive at the most compact form of
relations:



_L_ [′]




[′] _mj_ [=] _[ E][mk][L][ki][E]_ [′]



_ij_ [′] _[.]_ (4.3)



Comparing this to the transformation of components of a contravariant

vector:



_a_ [′]




[′] _j_ [=] _[ a][i][E]_ _ij_ [′]



_ij_ _[,]_



we see both similarities and differences.

The similarity is seen in the transformation rule for the second index
of the operator _L_ [̂] : It transforms according to the _contravariant_ rule. The
difference is seen in the transformation rule for the first index which
transforms according to the _covariant_ rule.

We conclude that linear operators _L_ [̂] which map vector into vectors

as



→

_b_



→

_a_



_L_ ̂

�→


**84** - Tensors For Inquiring Minds


have a “mixed nature”: They combine the behavior of covariant and contravariant vectors, as seen from the transformation of their components.
Soon we will encounter linear operators whose components transform
like two covariant vectors, or like two contravariant vectors (see _tensor_
_product_ in Section 5.8).


_Objects and Components_


Notions of vectors and operators are _independent of any basis and compo-_
_nents_ . Components simply _represent_ vectors or operators in a given basis.
Neither vectors nor operators are reduced to their components, like a building is not reduced to its projections on a piece of paper.
Components are simply computational tools, but their transformation properties tell something about the corresponding mathematical object.


**Exercise 4.5** _The area of the parallelogram built on unit vectors is 1._
_The area of the parallelogram built on the vectors_ ( _L_ [̂] → _u_ 1) _and_ (̂ _L_ → _u_ 2) _does_
_not depend on the basis used to express the components of the operatorL_ ̂ _. Therefore, the determinant should be a quantity independent of the_
_basis._

_Another characteristic of an operator which is independent of the_
_basis is called_ trace _. It is defined as the sum of the diagonal components_
_of an operator:_

_tr_ _L_ [̂] = _L_ 11 + _L_ 22 _._


_Prove that trace is independent of the choice of a specific basis. That is,_
_show that, given two sets of basis vectors_ {→ _e_ _i_ } _and_ {→ _e_ ′ _i_ [}] _[, the following]_
_equality holds_
_L_ 11 + _L_ 22 = _L_ [′] 11 [+] _[ L]_ [′] 22 _[.]_


4.8 FIRST NOTION OF TENSOR


Although a more satisfactory definition of tensors will be deduced later,
we can now recognize at least one type of tensor. This type of tensor is
represented by linear operators considered above.
Tensors are mathematical objects which, like numbers and vectors,
can be added pairwise, multiplied by numbers, and, very importantly,
_whose components transform in a certain way_ . The components of linear


Operators                             - **85**


operators of the type _L_ [̂] → _a_ = → _b_ transform according to the formula


_L_ [′] _ij_ [=] _[ E][im][L][mn][E]_ _nj_ [′] _[.]_


In Section 5.8 we will encounter tensors with other transformation

rules. However, those rules will be analogous to the expression given
above. We will also learn what it means to add two tensors, and even
what it means to “multiply” a pair of tensors.
Finally, another important aspect of operators and tensors can be
seen when we write


→ →
_b_ = _L_ [̂] _a_ or _bj_ = _aiLij._


These formulas express a _linear relation_ between two vectors, and the
operator _L_ [̂] (or tensor) encodes that relation. Linear relations between
vector quantities are very important in physics. Examples of this are
given in the last chapter.


CHAPTER HIGHLIGHTS


  - _Operators extend the idea of functions._


  - _Numeric functions (e.g.,_ sin _x) act on numbers and yield other_
_numbers. Operators may act on vectors to yield other vectors or_
_numbers._


  - _Linear operators represent a simple and yet powerful class of op-_

_erators on vectors._


  - _Linear operators can be represented graphically or symbolically._


  - _In a given basis, every linear operator can be specified using com-_
_ponents. This is similar to how a vector is represented via its com-_

_ponents._


  - _When the basis changes, the components of a linear operator trans-_
_form in a very specific way, called transformation rule or law._


  - _Mathematical expressions involving linear operators can be written_
_using components (e.g., Lij) or they can be written in more abstract_
_operator form using operator notation_ _L_ [̂] _._


  - _Degenerate linear operators collapse two or more basis vectors onto_
_the same line. They form a special subset of linear operators._


**86** - Tensors For Inquiring Minds


  - _There are two characteristics of linear operators that do not change_

_when a new basis is chosen: Determinant and trace._


  - _Linear operators represent the simplest type of tensors, called ten-_

_sors of the second rank – one tier above vectors._


  - _Linear operators and tensors are used to express linear relations_

_between different vector quantities._


#### C H A P T E R 5

### Tensors

HE FIRST EXAMPLE OF AN OPERATOR – AND
# T corresponding tensor – that we encountered had a simple type:


_L_ ̂ → _a_ = → _b._


It is a linear unary function mapping vectors into vectors.
As the next step, we will expand our toolset and study operators that
take two vectors as their input arguments. Their action on the arguments
can be symbolically written as follows:


_L_ ̂ → _a_ → _b_ = _x_


if the result is a number, or


_L_ ̂ → _a_ → _b_ = → _c_


if the result is another vector. We will start with the former case.


5.1 SCALAR PRODUCT AND DOL-OPERATOR


Given a pair of vectors, for example, arrows in a plane, we can _quantify_

_their mutual orientation_ . In other words, given two vectors → _a_ and → _b_,
we can calculate a number that measures, for instance, their _degree of_
_overlap_ (or _alignment_ ) which tells how much in common the vectors have
with regard to their directions and lengths.
We are looking for a binary operator ̂ _σ_ that yields a number based

on two vectors:
̂ → →
_σ_ _a_ _b_ = _x._


[DOI: 10.1201/9781003620365-5](https://doi.org/10.1201/9781003620365-5) **87**


**88** - Tensors For Inquiring Minds


We will call this operator ̂ _σ dol_ -operator [1], based on the key letters of
the phrase “degree of overlap.”
There are many approaches to quantify mutual orientation of a pair
of vectors. One simple way is to measure the angle between them:


→ →
∠ _a_ _b_ = _θ._


However, we will limit our search for candidates to linear operators or –
in the case of binary operator ̂ _σ_ – to _bilinear operators_ .


**Exercise 5.1** _Prove that the operator_ ∠ _is not linear._


If the dol-operator ̂ _σ_ is linear in each of its arguments, we must have


̂ _σ_ (2→ _a_ ) → _b_ = ̂ _σ_ (→ _a_ + → _a_ ) → _b_ = ̂ _σ_ → _a_ → _b_ + ̂ _σ_ → _a_ → _b_ = 2(̂ _σ_ → _a_ → _b_ ) _._


In general, we require


̂ → → → →
_σ_ ( _αa_ ) _b_ = _α_ (̂ _σ_ _a_ _b_ ) _._


In addition, we will not be concerned with the order in which the vec
→ → → →
tors _a_ and _b_ are considered. Put differently, we consider _a_ aligned to _b_

to the same degree as → _b_ is aligned to → _a_ . Mathematically this requirement
is written as follows:
̂ _σ_ → _a_ → _b_ = ̂ _σ_ → _b_ → _a._


Functions and operators with this property are called _symmetric_ in their

arguments.


_Anti-symmetric Operators_


Since angles are measured as clockwise (negative) or counter-clockwise
(positive), the operator ∠ is not symmetric. It is called _anti-symmetric_ :


→ → → →
∠ _a_ _b_ = −(∠ _b_ _a_ ) _._


1This is not a standard terminology, but it conveys the concept well.


Tensors                             - **89**


Finally, we recognize that some pairs of vectors are not overlapping at
all. It can be said that their degree of overlap is zero. Mutually orthogonal
vectors provide an example of vectors with zero overlap, they kind of
“have nothing in common.” Thus, we expect


→



_b_ = 0



̂ _σ_



→

_a_



if



→ →
_a_ ⊥ _b_ .


Now every vector can be written in the form



→ →
_a_ = _aua,_



where _a_ is the length of the vector,



→
_ua_ is the unit-length vector pointing


→



in the same direction as



→
_a_ . Similarly for


→



_b_ :



→

_b_ = _bub._



Since dol-operator ̂ _σ_ is linear in each argument, we can write


→



→
_ua_



→
_ub_ ) _._



̂ _σ_



→
_a_ _b_ = _ab_ (̂ _σ_



The problem is thus reduced to quantifying the mutual overlap of
unit vectors → _u_ and → _u_



unit vectors → _ua_ and → _ub_ . The only difference between these vectors is

their directions. Furthermore, only relative angle should matter, since
rotating both vectors by the same amount should not affect their mutual/relative orientation. Although we can’t use the angle between these
vectors directly, we can use some function of the angle:



→
_ua_ and



→
_ub_ = _f θ._



̂ _σ_



→
_ua_



Firstly, this function has to be periodic since changing the mutual angle
by 2 _π_ results in the same mutual orientation. Secondly, for orthogonal
vectors the function must return zero degree of overlap:


_f_ ( _π_ /2) = 0 _._


After some search and reflection, a reasonable candidate function can
be written in the following way:


_f θ_ = cos _θ._


**90** - Tensors For Inquiring Minds


We arrived at the traditional operation of _scalar product_ (numeric product) of two vectors. For scalar product, a special _infix notation_ is conventionally used:


̂ → → → →
_σ_ _a_ _b_ = _a_ ⋅ _b_ = _ab_ cos _θ._


What is the geometric meaning of scalar product? As shown in the

→ →
Figure 5.1, one way to interpret the scalar product _a_ ⋅ _b_ = _ab_ cos _θ_ is to
consider it as the area of a rectangle with sides _a_ and _b_ cos _θ_ . A special
care must be taken for cases when the mutual angle is greater than _π_ .


Figure 5.1 Scalar product of two vectors can be given a simple geometric interpretation as the unsigned area of a rectangle with the sides _a_
and _b_ cos _θ_ or with the sides _a_ cos _θ_ and _b_ .


5.2 SCALAR PRODUCT PROPERTIES


The expression for the scalar product of two vectors


→ →
_a_ ⋅ _b_ = _ab_ cos _θ_


implies the _commutativity_ of scalar product operation:


→ → → →
_b_ ⋅ _a_ = _ba_ cos _θ_ = _ab_ cos _θ_ = _a_ ⋅ _b._


_Non-commutativity_


Commutativity is a familiar property, present in both addition and multiplication of numbers. It is sometimes accepted as a natural property of any
multiplication-like operation. This view is limiting, however, and we will later
learn how to multiply objects without commutativity:


_A_ � _B_ ≠ _B_ � _A._


Tensors                             - **91**


Here we used an arbitrary infix symbol � to denote the non-commutative
product of some objects _A_ and _B_ . What exactly those objects are and what
their product might mean will be clear when we introduce them properly.
Right now we want to highlight the non-commutativity as a valid property of
some binary operations.


Besides commutativity, scalar product has other useful properties.
First, it is trivial to demonstrate that we can “pull out” constant scale
factors of vectors:
→ → → →
( _αa_ ) ⋅ _b_ = _α_ ( _a_ ⋅ _b_ )


and similarly
→ → → →
_a_ ⋅( _β_ _b_ ) = _β_ ( _a_ ⋅ _b_ ) _._


To arrive at the second important property of the scalar product,
recall that in the geometric interpretation of the scalar product we had
expressions
_b_ cos _θ_ = _b_ ∥ or _a_ cos _θ_ = _a_ ∥ _,_

where _b_ ∥ is the part of the vector → _b_ parallel to → _a_ ( _a_ ∥ is the part of the

→ →
vector _a_ parallel to _b_ .)

→ → →
Now, if the vector _a_ is “made from” two other vectors _c_ and _d_ :


→ → →
_a_ = _c_ + _d,_


then, as illustrated in the Figure (5.2),


_a_ ∥ = _c_ ∥ + _d_ ∥ _,_


where all terms represent parts of the respective vectors parallel to the

→ → → →
vector _b_ . Of course, the angles between the vectors _a_, _c_, _d_ and the


→
vector _b_ may all be different:


_a_ ∥ = _a_ cos _θ_ = _c_ cos _ϕ_ + _d_ cos _ψ._


Given that


→ → → → → →
_a_ ⋅ _b_ = _ab_ cos _θ,_ _c_ ⋅ _b_ = _cb_ cos _ϕ,_ _d_ ⋅ _b_ = _db_ cos _ψ,_


we arrive at the _distributive property_ of scalar product:


→ → → → → → → → →
( _c_ + _d_ ) ⋅ _b_ = _a_ ⋅ _b_ = ( _c_ ⋅ _b_ ) + ( _d_ ⋅ _b_ ) _._


**92** - Tensors For Inquiring Minds


Figure 5.2 Simple geometric construction illustrates the distributive

→ → → → → → →
property of scalar product: ( _c_ + _d_ ) ⋅ _b_ = ( _c_ ⋅ _b_ ) + ( _d_ ⋅ _b_ ).


Putting it all together, we can express the properties of scalar product in a single expression:


→ → → → → → → → → →
( _αa_ + _β_ _b_ ) ⋅ _c_ = _c_ ⋅( _αa_ + _β_ _b_ ) = _α_ ( _a_ ⋅ _c_ ) + _β_ ( _b_ ⋅ _c_ ) _._


_Orthogonality_


We might wonder whether we can define, instead of the degree of overlap,
some measure of orthogonality for a pair of vectors. Indeed, a reasonable
candidate might be (using infix notation):


→ →
_a_ ⊢ _b_ = _ab_ sin _θ._


While this is an acceptable definition, the expression on the right-hand side
appears in a different, more powerful, and useful, operation of the _outer prod-_
_uct_ of two vectors. The concept of outer product is related to the concept of
_tensor product_ (see Section 5.8) but is beyond the scope of this book.


Using the properties of the scalar product and expanding vectors in
terms of the basis vectors, we can write the scalar product in terms of
vector components. First write


→ → → → → → →
( _a_ 1 _e_ 1 + _a_ 2 _e_ 2) ⋅ _b_ = _a_ 1( _b_ ⋅ _e_ 1) + _a_ 2( _b_ ⋅ _e_ 2) _._


Tensors - **93**



Next, expand



→

_b_ to find



→ →
_e_ _i_ = _b_ 1( _e_ 1 ⋅



→ →
_e_ _i_ ) + _b_ 2( _e_ 2 ⋅



→
_e_ _i_ ) _._



( _b_ 1



→ →
_e_ 1 + _b_ 2 _e_ 2) ⋅



Finally, combining the results of two previous steps, we arrive at the
expression


→



→

_a_ ⋅



_b_ = _a_ 1 _b_ 1(



→
_e_ 1) + _a_ 1 _b_ 2(



→
_e_ 2 ⋅



→
_e_ 1) + _a_ 2 _b_ 1(



→
_e_ 1 ⋅



→
_e_ 2) + _a_ 2 _b_ 2(



→
_e_ 2 ⋅



→
_e_ 2) _._



→
_e_ 1 ⋅



For arbitrary basis vectors the scalar product is then given by


→



→

_a_ ⋅



_b_ = _a_ 1 _b_ 1 _e_ [2]




[2] 1 [+ (] _[a]_ [1] _[b]_ [2] [+] _[ a]_ [2] _[b]_ [1][)] _[e]_ [1] _[e]_ [2] [cos] _[θ]_ [ +] _[ a]_ [2] _[b]_ [2] _[e]_ [2] 2



2 _[,]_



where _θ_ is the angle between the basis vectors → _e_ 1 and → _e_ 2. For a special

case of orthonormal basis the scalar product takes the simplest form:



where _θ_ is the angle between the basis vectors



→
_e_ 1 and



→

_a_ ⋅



→

_b_ = _a_ 1 _b_ 1 + _a_ 2 _b_ 2 = _aibi._



→ →

But in general we must know the values for all products _e_ _i_ ⋅ _e_ _j_ . A special

notation is used for these products:



But in general we must know the values for all products



→
_e_ _i_ ⋅



→
_e_ _i_ ⋅



→ →
_e_ _i_ _e_ _j._



_ηij_ =



→
_e_ _j_ = ̂ _σ_



This notation allows a more compact way of writing scalar products for
general basis:


→



→

_a_ ⋅



_b_ = _ηijaibj._



_Scalar Product Components_


Let’s take a look, how the derivation of the last result can be done using
index notation.



→
_e_ _i_ ) ⋅



→



→

_b_ ) _._



→

_a_ ⋅



→

_b_ = ( _ai_



→

_b_ = _ai_ ( _e_ _i_ ⋅



→
_e_ _i_ ⋅



→
_e_ _i_ ⋅[ _bj_



→ →
_e_ _j_ ]) = _ai_ ( _bj_ [ _e_ _i_ ⋅



→
_e_ _j_ ]) = _ai_ ( _bj_ [



Expanding



→

_b_, we get


→

_a_ ⋅



→



→

_b_ = _ai_ ( _e_ _i_ ⋅[ _bj_



→
_e_ _j_ ]) _._



We thus showed that



→ →
_a_ ⋅ _b_ = _aibj_



→
_e_ _i_ ⋅



→
_e_ _j._



In the process, we had to use twice the distributive property of the scalar
product, as well as the distributive property of number multiplication.


**94** - Tensors For Inquiring Minds


**Exercise 5.2** _In the index form of the scalar product of two vectors_


→ → → →
_a_ ⋅ _b_ = ( _aibj_ )( _e_ _i_ ⋅ _e_ _j_ )


_we observe the expression with two indices:_


_βij_ = _aibj._


_Can βij represent the components of some linear operator_ _β_ [̂] _? If so, how_
_does this operator act on vectors?_


5.3 INNER OPERATIONS


The following fact is easy to take for granted and overlook: _Vectors_
_are not used by themselves. They need numbers._ Without multiplying
a vector by a number, we could not write the simplest expansion of a
→
vector _a_ in a basis:

→ → →
_a_ = _a_ 1 _e_ 1 + _a_ 2 _e_ 2 _._


Note that all operations we considered so far never took us outside


⇒
of the combined realm of numbers R and vectors _A_ . Indeed, a product of
a number and a vector _α_ → _a_ uses one element of each space and produces

→ →
a vector. Similarly, a sum of two vectors _a_ + _b_ takes two elements from

⇒ ⇒
_A_ and returns another element of _A_ . Finally, the dol-operator ̂ _σ_ takes


⇒
two elements from _A_ and returns an element of R. These points are
illustrated in Figure 5.3(a).
Another way of looking at this reveals that in the hierarchy of mathematical objects, the operations we considered so far never took us up
the ladder of _ranks_, as illustrated in Figure 5.3(b). At the lowest level,
we have _rank-0_ elements – numbers. The first ladder corresponds to the
_rank-1_ elements – vectors. One step higher we have _rank-2_ elements –
tensors of the second rank, and so on.
All operations that _do not_ result in the element of higher rank are
called _inner operation_ . For instance, the scalar product of vectors is often
called _inner product_ [2] . The phrase _inner sum_ is not used for the binary
operator (+).


2There also exists an _outer product_, which is related to the _tensor product_ discussed in Section 5.8.


Tensors                             - **95**


Figure 5.3 (a) In vector algebra we use number space R alongside vector


⇒
space _A_ . All operations considered so far yield results from either of these
spaces; such operations (sum, product, etc.) are called _inner operations_ .
(b) In contrast to inner operations, _outer operations_ create mathematical
objects of higher rank than the input arguments. For example, the outer
product of two vectors yields a second-rank tensor.


5.4 CONJUGATE OBJECTS


Starting from the idea of scalar product or, equivalently, from the dol
operator

̂ → →
_σ_ _a_ _b_ = _x_


we can arrive at an important notion of _conjugate_ objects. Two objects
are conjugate of each other if, roughly speaking, they are somehow related via a simple rule. We will study this notion using vectors.
→
For every vector _a_ there exists a mathematical object, related to
→
_a_ via the dol-operator. To see this, we first need to revisit the idea of
_partial application_, discussed in subsection 5.4.1. This time, however, we
will extend the idea of partial application to binary operators.


5.4.1 Partial Application


Given a pair of vectors, the dol-operator yields a number:


̂ → →
_σ_ _a_ _b_ = _x._


What happens when we provide only one vector, leaving the secondinput slot of ̂ _σ_ empty (the box here indicates a missing second argument):


̂ _σ_ → _a_ ◻ ?


**96** - Tensors For Inquiring Minds


This is called a _partial application_ of the operator ̂ _σ_ . This construction
has the behavior of a unary operator that maps any vector into a number:


→ ̂ _σ_ → _a_
_c_ �→ _y._


We will use a special notation for the partially applied operator:


← _a_ = ̂ _σ_ → _a._


_Linear Operator_


←
The unary operator _a_ is a _linear operator_ :


← → → ← → ← →
_a_ ( _b_ + _c_ ) = ( _a_ _b_ ) + ( _a_ _c_ ) _._


←
The action of a unary operator _a_ on any vector is then naturally defined

as
← _a_ → _b_ = ̂ _σ_ → _a_ → _b_ = _ab_ cos _θ._


←
Notice that in the left-most expression the operator _a_ and the argument


→
vector _b_ are separated by space, in agreement with the notation for the
application of functions and operator to their arguments.


Figure 5.4 (a) The dol-operator is a binary operator linear in each of
its arguments ( _bilinear_ ). (b) When only one argument is supplied, the
operator becomes _partially applied_ and is denoted using the _conjugate_
←
_vector_ notation _a_ . (c) Applied to two vector arguments ( _fully applied_ ),
dol-operator yields a number – scalar product of the vectors.


All three possible “states” of the dol-operator ̂ _σ_ are illustrated in
Figure 5.4. The middle state of partial application corresponds to a linear
→ ←
operator built from the first input vector _a_ and as denoted as _a_ . The


Tensors                             - **97**


← →
operator _a_ is called the _conjugate_ to a vector _a_ . The conjugation is
understood _relative to the scalar product or, equivalently, binary operator_

̂
_σ_ .


_Quantum Notation_


In quantum physics vectors and their duals are used to describe information
about quantum systems (so called quantum states.) Paul Dirac introduced a
very powerful notation for these vectors, called _bra_ and _ket_ vectors. Ket vectors correspond to contravariant arrow-vectors and are denoted as follows:


→
_a_ �→ ∣ _a_ ⟩ _._


Bra vectors correspond to covariant vectors and are denoted as


←
_a_ �→ ⟨ _a_ ∣ _._


Scalar product of bra and ket vectors is then written using _brackets_ :


← →
_a_ _a_ = ⟨ _a_ ∣ _a_ ⟩ _._


5.5 CONJUGATE VECTORS


The notation for the conjugate vectors is suggestive for a reason. The
←
left-pointing arrow on top of _a_ indicates that this _is a vector_ . This might
←
be surprising since we just convinced ourselves that _a_ is a linear operator.
To convince ourselves that ← _a_ is also a vector, we must check whether the
conjugate of vectors possesses the defining properties of vectors. Let’s
do it.

To demonstrate that we can add two conjugate vectors – which are
also linear operators – we must describe how to add operators. Operators are essentially functions, and we already understand how to add
functions of a numerical arguments (go back to subsection 2.3.4 if you

← ←
need a refresher.) We can add two operators, _a_ and _b_, in a similar way:


← ← ←
_a_ + _b_ = _c,_


→
where for any contravariant vector _d_ the following holds:


←→ ← ← → ←→ ←→
_c_ _d_ = ( _a_ + _b_ ) _d_ = ( _a_ _d_ ) + ( _b_ _d_ ) _._


**98** - Tensors For Inquiring Minds


As a side-note, we point out once more that the addition operation “+”


←



_b_ is applied to a new type of mathematical object – conjugate



in



←
_a_ +



→



←→



vectors. The addition operator in



vectors. The addition operator in _a_ _d_ + _b_ _d_ is applied to usual numbers.

It is easy to see how conjugate vectors can be multiplied by numbers:



←

_a_



_d_ +



_b_



←

_a_ =



_α_



←

_b,_



where for any contravariant vector


←



→
_c_ we have



→
_c_ = _α_ (



→
_c_ ) _._



_b_



←

_a_



_Conjugate Basis_


If conjugate objects are vectors, they must have some basis. The basis
for conjugate vectors can be taken by conjugating any basis from the

arrow-vectors:



← →
_e_ 1 = ̂ _σ_ _e_ 1 _,_



← →
_e_ 2 = ̂ _σ_ _e_ 2 _._



The linearity of the operator ̂ _σ_ for both arguments results in the following
relation



← _a_ = ̂ _σ_



→ _a_ = ̂ _σ_ ( _a_ 1



→
_e_ 1 + _a_ 2



→
_e_ 2) = _a_ 1



←
_e_ 1 + _a_ 2



←
_e_ 2 _._



In other words, _any conjugate vector can be expanded in terms of some_

←

_basis conjugate vectors_ { _e_ _i_ }.


**Exercise 5.3** _Derive the relationship_



←
_a_ = _a_ 1



←
_e_ 1 + _a_ 2



←
_e_ 2



_in more details, without leaving out steps._


_Component Transformation_


Finally, we must show that the components of any conjugate vector
change properly when the (conjugate) basis is switched.



We start by writing the same operator



←
_a_ in different bases:



←
_a_ = _a_ 1



←
_e_ 1 + _a_ 2



← ′
_e_ 2 = _a_ 1



← ′
_e_ 2 = _a_



← _e_ ′



1 [+] _[ a]_ [′] 2



2



← _e_ ′2 _[.]_



Here



← _e_ ′1 [= ̂] _[σ]_



← _e_ ′



→ _e_ ′1 _[,]_



→ _e_ ′



← _e_ ′2 [= ̂] _[σ]_



← _e_ ′



→ _e_ ′2 _[.]_



→ _e_ ′


Tensors                             - **99**


Expanding the primed basis in terms of the non-primed, and using the
linearity of the operator ̂ _σ_ for all arguments, we get


← _e_ ′1 [= ̂] _[σ]_ → _e_ ′1 [=] _[ E]_ [11] ← _e_ 1 + _E_ 12← _e_ 2 _,_


← _e_ ′2 [= ̂] _[σ]_ → _e_ ′2 [=] _[ E]_ [21] ← _e_ 1 + _E_ 22← _e_ 2 _._


←
Plugging these equations into the expansion of _a_, after grouping the
terms, we arrive at


← ← ← ′ ← ′ ←
_a_ = _a_ 1 _e_ 1 + _a_ 2 _e_ 2 = ( _a_ 1 _[E]_ [11] [+] _[ a]_ [′] 2 _[E]_ [21][)] _e_ 1 + ( _a_ 1 _[E]_ [12] [+] _[ a]_ [′] 2 _[E]_ [22][)] _e_ 2 _._


Comparing the coefficients in front of the basis vectors, we conclude that


_a_ 1 = _a_ [′] _i_ _[E][i]_ [1] _[,]_


_a_ 2 = _a_ [′] _i_ _[E][i]_ [2] _[.]_


In a more compact form:
_aj_ = _a_ [′] _i_ _[E][ij][.]_


This is the same form we obtained before for arrow-vectors, with the only
(unessential) difference of notation – using _E_ instead of _L_ to denote the
relation between the “old” and “new” bases.

The conclusion is as follows: _The conjugate vectors have completely_
_analogous properties as the arrow-vectors, when referred to their own_
_conjugate bases_ .
We thus showed that vectors in plane have “conjugate image” – a
set of linear operators which also behave like vectors. These conjugate
vectors belong to the special vector space called _conjugate vector space_


⇒
or _dual vector space_ . The “usual” vector space is denoted as _A_ and its


⇐
dual companion is denoted as _A_ . The relationship between the “original”
and the _conjugate/dual_ space is illustrated in the Figure 5.5.


5.6 OPERATORS ARE VECTORS


Starting with the scalar product or, equivalently, bilinear dol-operator
̂ _σ_, we obtained unary linear operators using partial application


→ ← →
_a_ �⇒ _a_ = ̂ _σ_ _a._


**100** - Tensors For Inquiring Minds


←
Figure 5.5 Conjugate vectors like _a_ form a conjugate space which we


⇐ ⇒
denote _A_ . It is _conjugate_ or _dual_ to the “usual” vectors space _A_ .


←
We then showed that all such linear operators _a_ behave like vectors.
They can be multiplied by a number, added, written in terms of some
basis, and have components that transform according to a special rule:


← ← ′ ←′
_a_ = _ai_ _e_ _i_ = _aj_ _e_ _j_ where _ai_ = _a_ [′] _j_ _[E][ji][.]_


We discovered a natural connection ( _duality_ ) between every arrow-vector
and its conjugate vector:
→ ̂ _σ_ ←
_a_ ←→ _a._


We can start with unary linear operators, without specifying their
origin, and show that they behave like vectors. We will do it now.


Figure 5.6 Some linear operators map vectors into numbers: Γ [̂] → _a_ = _x_ .
Such operators form a vector space of their own.


Imagine _all possible_ unary linear operators that map vectors into
numbers (see Figure 5.6). Let us denote some such operator as Γ: [̂]


Γ̂ → _a_ = _xa,_


Γ̂ ( _α_ → _a_ ) = _α_ (̂Γ → _a_ ) = _αxa._


Tensors - **101**



→
_a_ +



→

_b_ :



For



→

_c_ =



Γ̂



→ _c_ = (̂Γ



→ _a_ ) + (̂Γ



→

_b_ ) = _xa_ + _xb_ = _xc._



Here _xa_, _xb_, and _xc_ are real numbers.

We can demonstrate that operators like Γ can be added: [̂]


Γ̂ = ̂Γ1 + ̂Γ2


and they can be multiplied by numbers:


Γ̂3 = _α_ Γ̂1 _._


We can also find basis and expand an arbitrary operator in that basis:


Γ̂ = _γ_ 1Γ̂1 + _γ_ 2Γ̂1 + _..._ + _γn_ Γ̂ _n_ = _γi_ Γ̂ _i_


and establish the transformation rule for the components _γi_ between
different bases. In effect, we will demonstrate that unary linear operators
of the same type as Γ (mapping arrow-vectors into numbers) behave like [̂]
vectors and therefore must be considered as such.


_Describing an Operator_


Remember that when we say that an operator Γ [̂] is given or known, we mean


→

that we know how it acts on _any vector_ _a_ :



Γ̂



→
_a_ = _xa._



_Addition_


If we know two operators Γ [̂] 1 and Γ [̂] 2, then making sense of their _operator_
_sum_ Γ [̂] = Γ [̂] 1 + Γ [̂] 2 is easy:



Γ̂



→ _a_ = (̂Γ1



→ _a_ ) + (̂Γ2



→
_a_ ) = _xa_ + _ya,_



where _xa_ = Γ [̂] 1


_Multiplication_



→ _a_ and _ya_ = ̂Γ2



→

_a_ .



If we know the operator Γ [̂] 1 then making sense of the product of that
operator with any number Γ [̂] = _α_ Γ [̂] 1 is easy:



Γ̂



→
_a_ = _α_ (̂Γ1



→
_a_ ) = _αxa,_



where _xa_ = Γ [̂] 1



→

_a_ .


**102** - Tensors For Inquiring Minds


_Finding Basis_


Using the linearity of the operator Γ, we can apply it to an arbitrary [̂]

→

vector _a_ as follows:



Γ̂



→ _a_ = ̂Γ ( _ai_



→ _e_ _i_ ) = _ai_ (̂Γ→ _e_ _i_ ) _._



The last expression states that to know the action of the operator Γ [̂]

→

on an arbitrary vector _a_ it is sufficient to specify its action on all basis



→

on an arbitrary vector _a_ it is sufficient to specify its action on all basis

vectors → _e_ ̂



vectors → _e_ _i_ . In other words, the operator ̂Γ is fully specified if we know a

set of numbers



_γi_ = Γ [̂] → _e_ _i._



Notice how similar this last expression is to the definition of components
_Lij_ of a linear operator _L_ [̂] .


_Operators and Vectors_


→

A vector _a_ is completely determined if we specify its components in a given

basis:



→ →
_a_ = _ai_ _e_ _i._



A linear operator Γ [̂] that maps vectors into numbers



→

_a_



Γ̂
�→ _xa_



is completely determined if we specify its action on basis vectors:



_γi_ = Γ [̂] → _e_ _i._



This makes the similarity between vectors and operators Γ [̂] stronger.



Let’s expand the input vector



→
_a_ in a different basis:



→ ′
_a_ = _aj_



→ ′
_a_ = _a_



→ _e_ ′ _j_ _[.]_



→ _e_ ′



In this case, the action of the linear operator Γ will be [̂]



Γ̂ ( _a_ [′] _j_



_j_ [) =] _[ a]_ [′]



_j_ [) =] _[ a]_ [′] _j_



→ _e_ ′




[′] _j_ [(̂][Γ]




[′]

_j_ _[γ]_ _j_ [′]



→ _e_ ′



_j_ _[.]_



Here _γj_ [′] [= ̂][Γ]



→ _e_ ′ _j_ [.]


Tensors                             - **103**


The relation between the components _ai_ and _a_ [′] _i_ [of the contravariant]
vector → _a_ is known; the relation between the values _γi_ and _γj_ ′ [is then]
easily found:
_γi_ [′] [= ̂][Γ] → _e_ ′ _i_ [= ̂][Γ][(] _[E][ij]_ → _e_ _j_ ) = _Eijγj,_


and, in a similar way:


_γi_ = Γ [̂] → _e_ _i_ = ̂Γ( _Eij_ ′ → _e_ ′ _j_ [) =] _[ E]_ _ij_ [′] _[γ]_ _j_ [′] _[.]_


These relations correspond to the _covariant vector_ .


_Covariant Vectors_


The components of contravariant vectors allow us to “assemble” them from
the “building blocks” – basis vectors:


→ →
_a_ = _ai_ _e_ _i._


The basis vectors and all other vectors constructed from them all _live in_


⇒
_the same vector space_, which we denoted _A_ – the space of _contravariant_

_vectors_ .


Unary linear operators, including all conjugate vectors, belong to a different


⇒ ⇐
vector space – _conjugate_ or _dual_ to _A_ . We denoted this vectors space as _A_ .
Figure 5.5 illustrates this point.
This implies that it is _incorrect_ to write


Γ̂ = _γi_ → _e_ _i._ ( _incorrect!_ )


⇐
Conjugate space _A_ has its own basis (or bases).


It is important to understand that the coefficients _γi_ and _γj_ [′] [refer to]

bases used for contravariant vectors (bases {→ _e_ _i_ } and {→ _e_ ′ _i_ [}][). They can]
also refer to bases used for covariant vectors. Let’s find some such basis
related to the coefficients _γi_ .
Every covariant vector Γ is completely determined if we know its [̂]
action on _all_ basis contravariant vectors → _e_ _i_ . Therefore, to specify some
basis vectors for Γ we should find certain covariant vectors that can be [̂]
used as “building blocks” for Γ. As a matter of fact, we already encoun- [̂]
tered basis covariant vectors when we discussed dol-operator and conju→
gate vectors of _e_ _i_ . We now will define similar vectors without referring to


**104** - Tensors For Inquiring Minds


dol-operator ̂ _σ_ . Specifically, the first basis vector Γ [̂] 1 for covariant vectors
→
acts on _e_ _i_ as follows:


̂ →
Γ1 _e_ 1 = 1 (5.1)

̂ →
Γ1 _e_ 2 = 0 (5.2)

̂ →
Γ1 _e_ 3 = 0 (5.3)


_..._ (5.4)


Thus, Γ [̂] 1 returns zero for all basis vectors except for → _e_ 1. Similarly, we
define the second covariant basis vector Γ [̂] 2 to return zero for all basis
→
vectors except for _e_ 2, and so on for other basis covariant vectors. A
compact way to express this idea uses index notation:


Γ̂ _i_ → _e_ _j_ = _δij._


Here _δij_ is the Kronecker delta, introduced in Chapter 2 on page 21.
Having defined this covariant basis, we can write now


Γ̂ = _γ_ 1Γ̂1 + _γ_ 2Γ̂1 + _...γn_ Γ̂ _n_ = _γj_ Γ̂ _j._

Clearly, Γ̂ → _e_ _i_ = _γi._

(To demonstrate this quickly, recall that Γ [̂] → _e_ _i_ = _γj_ Γ̂ _j_ → _e_ _i_ = _γjδji_ = _γi_ .)
In other words, the coefficients _γi_ are also _components_ of the covariant
vector Γ in [̂] _covariant basis_ {Γ [̂] _i_ }.


_Geometric Representation_


Arrows provide a simple geometric representation of _contravariant_ vectors. Now that we encountered _covariant_ vectors, it is natural to ask
what geometric representation covariant vectors have?
Unary linear operators map vectors into numbers. In a certain sense,
they “complete” vectors to a mathematical construction that can be
unambiguously assigned a number. One such construction is the oriented
area (for a plane) or a volume (for three and higher dimensions).
Let’s use arrows in three-dimensional space as an example. What
→
completes a given arrow-vector _a_ to a volume? We can build a solid
figure with a well-defined volume using the arrow as the side of a cylinder,
and some two-dimensional area-element as its “complement.” This area→
element will correspond to a linear operator that maps the vector _a_ into
a number – the volume of the solid object built using the vector and the
area-element, as shown in Figure 5.7(a).


Tensors                             - **105**


Figure 5.7 (a) A covariant vector Γ [̂] 1 can be represented by an oriented

→
piece of plane with certain area. Its action on a contravariant vector _a_
result in a number – volume of a skewed cylinder built by moving the area
along the vector. (b) A covariant vector Γ [̂] 2 has different orientation and
magnitude from Γ [̂] 1. (c) The shape of the conjugate vector (an oriented
piece of plane) does not matter, as long as its orientation and area stay
the same.


_Covariant Vectors_


→
Contravariant arrow-vectors _a_ are oriented line segments, regardless of
whether they are in a plane, in three-dimensional space, or in spaces of
higher dimensions.


Covariant vectors have different “structure” for spaces of different dimensions. In three dimensions, as we saw, they are oriented areas. In a plane,
they will be oriented line segments similar to arrow-vectors. In four dimensional space covariant vectors will be oriented three-dimensional volumes.
Thus, unlike contravariant arrow-vectors, covariant vectors are more difficult
to visualize.


The question of the geometric meaning of the addition of two covariant vectors – and other operations on them – although interesting and useful, is
outside of the scope of this book.


**106** - Tensors For Inquiring Minds


5.7 PROJECTORS


→
In many problems, it is useful to take a vector _b_ and find that part
→
of it which will be parallel to another vector _a_, as illustrated in the
Figure 5.8. This procedure can be described using the concept of a binary

→ →
operator. This operator, when given a pair of vectors _a_ and _b_, returns

→ → → →
the “component” of _b_ oriented along _a_ – a _projection_ of _b_ onto _a_ :


_P_ ̂ → _a_ → _b_ = → _b_ ∥ _,_


→ →
where _a_ is parallel to _b_ ∥.


→ →
Figure 5.8 A vector _b_ has the “component” _b_ ∥ along a given vector

→
_a_ . The length of this component is _b_ cos _θ_ where _θ_ is the angle between

→ →
vectors _a_ and _b_ .


From the Figure 5.8, it is clear that



→ →
_b_ ∥ = _uab_ cos _θ_ =



→

_a_

_a_ _[b]_ [cos] _[θ,]_



→ →
where _ua_ is a unit-length vector parallel to _a_ .
The right-hand side of the last expression can be written using doloperator ̂ _σ_, or even better, using the conjugate vector notation:



→
_a_ ←→

[(] _a_ _b_ ) _._
_a_ [2]



→
_b_ =
∥



→

_a_

_[ab]_ [cos] _[θ]_ [ =]
_a_ [2]



For each vector → _a_ there exists a corresponding operator – _projection_
_operator_ or _projector_ – that projects all other vectors onto the direction
→
specified by _a_ .


Tensors - **107**



_Projector Notation_


→



A projector operator that projects any vector _b_ onto the direction specified

by a vector → _a_ will be denoted as ~~_A_~~ ̂:



A projector operator that projects any vector



→ _a_ will be denoted as ~~_A_~~ ̂:



~~_A_~~ ̂ → _b_ =



→

_a_
_a_ [2] [(]



←

_a_



→



_b_ ) _._



Such projector exists for any non-zero vector


→ _a_ �→̂ ~~_A_~~ _._



→
_a_ :



In this notation, the same (but capitalized) letter is used for the projector as
for the vector. In addition, the capitalized letter is doubly underlined to remind
that we project onto the direction parallel to the specified vector.
Similarly, we will have other projectors


→



_b_ �→ ~~_B,_~~ [̂]



→ _c_ �→̂ ~~_C,_~~ _. . ._



Projector _A_ [̂] corresponding to the vector


→

_b_ as follows:



→
_a_ acts on an arbitrary vector



_A_ ̂ → _b_ =



→

_a_ ←

_a_

[(]
_a_ [2]



→

_b_ ) _._



In the argument-free notation (see note on page 26), this operator takes
the following form:



→←

_a_ _a_


_[.]_
_a_ [2]



̂
_A_ =



→

_a_ ←

[(] _a_ ) =
_a_ [2]



_Note_ : The order of the vectors → _a_ and ← _a_ in the last expression is very

important because it has a completely different meaning from the ex
←→

pression _a_ _a_ . Indeed, as we agreed, the expression



_Note_ : The order of the vectors



→
_a_ and



←

_a_



→
_a_ . Indeed, as we agreed, the expression



←→

_a_ _a_ =



→

_a_ ⋅



→ 2
_a_ = _a_



yields the length squared of the vector



→
_a_ . In contrast, the expression



→←

_a_ _a_



works as an operator!


**108** - Tensors For Inquiring Minds


We obtained interesting and useful expression for an operator that


→

accepts a vector _b_ and produces another vector as the result. This ex
→

pression involves some kind of “multiplication” of a vector _a_ and its



accepts a vector



→

pression involves some kind of “multiplication” of a vector _a_ and its

←

conjugate _a_ :



←

_a_ :



→←

_a_ _a._



It is our first encounter with _tensor product_ . We will learn more about
this new type of multiplication below.


5.7.1 Projector Components


To find the components of a projector operator



̂
_A_ =



→←

_a_ _a_


_a_ [2]



in a given basis, we apply it to the basis vectors:



→ _ai_
_e_ _i_ =

_a_ [2]



→

_a_

_a_ [2]



←

_a_



→ _ai_
_e_ _i_ =



→

_a._



_A_ ̂



→
_e_ _i_ =



Expanding the vector



→
_a_ in the same basis, we arrive at



~~_i_~~ _j_



_A_ ̂



→ _e_ _i_ = _aiaj_

_a_ [2]



→ _e_ _j_ = _A_



→
_e_ _j,_



from which follows the expression for the components



_A_ ~~_[a]_~~ _[i]_ ~~_[a]_~~ _[j]_

_[.]_

~~_i_~~ _j_ [=] _a_ [2]



**Exercise 5.4** _Using the components of a projector_



_A_

_[,]_

~~_i_~~ _j_ [=] _[ a]_ _a_ _[i][a]_ [2] _[j]_



_calculate its determinant._


_Symmetry of Projectors_


From the expression for the components of a projector follows that



~~_A_~~




~~_[A]_~~
_ij_ [=]



_ji_ _[,]_



which means that to fully specify its components, we need only 3 numbers
(for vectors in a plane we need ~~_A_~~, ~~_A_~~, and ~~_A_~~ ), as opposed to 4 numbers



, ~~_A_~~



, and ~~_A_~~



), as opposed to 4 numbers



11



12



22



required to specify a general linear operator.


Tensors                             - **109**


5.7.2 Composition of Projectors*


The idea of composing two functions - discussed in subsection 2.3.4 on
page 25 - can be extended to linear operators. That is, some types of
linear operators can be composed. Indeed, suppose we have a linear

operator
_L_ ̂ → _a_ = → _b_


and
_M_ ̂ → _b_ = → _c._


We can apply the operators _L_ [̂] and _M_ [̂] sequentially:


_M_ ̂ ( _L_ [̂] → _a_ ) = → _c._


This way we obtained a new operator _K_ [̂] which we call _composition of lin-_
_ear operators_ _L_ [̂] and _M_ [̂] . The same notation for composition of operators
as for the composition of functions can be used:


_K_ ̂ = _M_ [̂]        - _L._ [̂]


Now we can find the components of the operator _K_ [̂] . On the one hand,


_K_ ̂ → _e_ _i_ = _Kij_ → _e_ _j._


On the other,
_K_ ̂ → _e_ _i_ = ̂ _M_ ( _L_ [̂] → _e_ _i_ ) = ̂ _M_ ( _Liq_ → _e_ _q_ ) _._


Using the linearity of the operator _M_ [̂], we can write


_K_ ̂ → _e_ _i_ = _Liq_ ( ̂ _M_ → _e_ _q_ ) = _Liq_ ( _Mqj_ → _e_ _j_ ) _._


We arrive at the following expression of the components of _K_ [̂] :


_Kij_ = _LiqMqj,_


where the summation over _q_ is implied, according to Einstein’s summation rule. Now let us apply this result to projectors.
→ →
Suppose we want to project a vector _c_ first on the vector _a_, and


→
then project the result onto the vector _b_ . We can do it by sequential
application of two projectors:



→←
_b_ _b_

_b_ [2]



̂
_A_ =



→←

_a_ _a_ ̂
and _B_ =
_a_ [2]


**110** - Tensors For Inquiring Minds



to the vector



→

_c_ :



_B_ ̂ ( _A_ ̂ → _c_ ) = (̂ _B_ - ̂ _A_ )



→

_c._



Composing two linear operators we obtain another linear operator:


_L_ ̂ = _B_ ̂           - ̂ _A._


The components of the product operator _L_ [̂] can be expressed in terms of
the components of the factors – projectors _A_ [̂] and _B_ [̂] :



_Lij_ = _A_

~~_i_~~ _k_ _[B]_




_[a][i][b][j][.]_

_kj_ [=] _[ a]_ _a_ _[k]_ [2] _b_ _[b]_ [2] _[k]_



The expression _akbk_ is recognized as the scalar product of the vectors


→



→

_a_



and



_b_ in orthonormal basis, so the components _Lij_ are simply given by


→



_Lij_ = _λaibj,_ _λ_ =


where _λ_ is a scalar value – a number.



→
_a_ ⋅ _b_


_[,]_
_a_ [2] _b_ [2]



_Note_ : The operator _L_ [̂] = _B_ [̂] - _A_ [̂] is no longer a projector in the sense in


→



which it was defined earlier. There is no vector

_Lij_ = _[d]_ _d_ _[i][d]_ [2] _[j]_ _[.]_


The following exercise explores this point.


**Exercise 5.5** _(a) Show that a projector_



_d_ such that



̂
_A_ =



→←

_a_ _a_


_a_ [2]



_has the following property:_


̂ ̂
_A_          - ̂ _A_ = _A._


_(b) Does the result of composition_ _L_ [̂] = _B_ [̂] - _A_ [̂] _have this property?_


**Exercise 5.6** _Consider the composition_


̂
_M_ = _A_ [̂]        - _B_ [̂] _._


_Find its components and compare them to the components of_


_L_ ̂ = _B_ ̂           - ̂ _A._


Tensors                             - **111**


5.8 TENSOR PRODUCT


We arrived at an extremely important idea that allows “building” tensors
of various kinds from simple “ingredients,” such as vectors. To begin, let
us take a closer look at a projector operator:



̂
_A_ = [1]

_a_ [2]



→ _a_ ← _a,_ _A_




[1]

_[a][i][a][j][.]_

~~_i_~~ _j_ [=] _a_ [2]



From the first expression, written without the components, it is clear
that the operator _A_ [̂] involves a contravariant vector → _a_ and its covari

←

ant conjugate _a_ . This distinction is absent in the second expression for

the components of the operator _A_ [, making the expression for the com-]



ant conjugate



~~_i_~~ _j_ [, making the expression for the com-]



ponents misleading. To fix this, a special notation for components is
introduced. In this notation, the components of contravariant vectors
are written using superscripts:


→
_a_ �→ _a_ _[i]_ _,_


while the components of covariant vectors are written in the “usual” way,
as subscripts:

←
_a_ �→ _ai._


With this in mind, the components of the projector _A_ [̂] are written in the

following way:




[ ●]

[1]

- _j_ [=] _a_ [2]



_A_ _[i]_ [ ●]




_[a][i][a][j][.]_
_a_ [2]



Now it should be clear that in the last expression vectors of different
kinds are used: one contravariant, and the other covariant. The little
grey circles serve visual purpose only, they help separate the first contravariant index from the second covariant one.


_Clash of Notation_


The use of superscripts to denote components of contravariant vectors leads
to the clash of notations. For example, given an expression _a_ [2], how should
we understand it: Is it the length squared of a vector, or is it the second component of a contravariant vector? Surprisingly, this is not a serious problem


at all, since the meaning of superscripts is usually clear from the context in
which such expressions appear.


**112** - Tensors For Inquiring Minds


5.8.1 Tensor Product 1


In the expressions



̂
_A_ = [1]

_a_ [2]



→

_a_



← _a,_ _A_ _[i]_ [ ●]




[ ●]

[1]

- _j_ [=] _a_




_[a][i][a][j]_
_a_ [2]



the combination of vectors → _a_ ← _a_ and their component expression _aiaj_ rep
resent a mathematical object – operator in this case – that is neither a
vector, nor a number. Such “amalgamation” of two vectors into a tensor
is called a _tensor product_ . Tensor product is a simple and versatile way

to construct tensors.



the combination of vectors



→

_a_



Special notation for the tensor product of two vectors exists:



→←

_a_ _a_ =



→
_a_ ⊗



←

_a._



This separate notation may appear redundant, since we understand from
the order of the vectors → _a_ and ← _a_ _not a_



the order of the vectors → _a_ and ← _a_ that the expression on the left is _not a_

_scalar product_ . However, using the infix operator ⊗ is convenient because
it allows writing other types of tensor products with ease and consistency.



→
_a_ and



5.8.2 Tensor Product 2


Using the tensor product notation, we can write


←



←
_a_ ⊗



→
_a_ or, more generally,



_b_ ⊗



→

_a._



→

_a_ =



→

_a_ .



→

_b_ ⋅



These expressions _represent tensors_ and not scalar products


←



←

_b_



The components of a tensor _T_ = _b_ ⊗



→
_a_ are as follows:



_T_ [●] _[j]_

_i_  - [=] _[ b][i][a][j][.]_



The important fact is reflected in the position of indices of the tensor _T_ :
It behaves like a covariant vector in the first index, and as a contravariant
vector in the second index.


5.8.3 Tensor Product 3


With the help of the infix operator ⊗ we can write, without creating
ambiguity, a tensor product of two contravariant vectors:


→



_b,_ _T_ _[ij]_ = _a_ _[i]_ _b_ _[j]_ _._



_T_ =



→
_a_ ⊗



The positions of the indices reflect the fact that this kind of tensor is
contravariant in both of them.


Tensors                             - **113**


A simplified notation is sometimes used:


→ → →→
_a_ ⊗ _b_ = _a_ _b,_


→→
but it may lead to confusion, since the expression _a_ _b_ is too similar to the

→ →
scalar product _a_ ⋅ _b_, especially when using handwriting. We will avoid
this simplified notation.


5.8.4 Tensor Product 4


The last kind of tensor that we can construct from vectors is given by
the tensor product of two covariant vectors:


_T_ = ← _a_ ⊗ ← _b,_ _Tij_ = _aibj._


←←
Again, one may encounter expressions like _a_ _b_, but we will prefer to use
the infix operator ⊗.


**Exercise 5.7** _Write the transformation rules for tensors of all four_
_kinds considered above._


5.9 TENSORS DEFINED


We are now in a good position to summarize our understanding of tensors. Before we do this, let’s quickly review the path we took to reach
this position.
Having defined contravariant and covariant vectors, we examined
the natural idea of _operators_ – functions on vectors. We focused on an
important class of operators called _linear operators_ .
We studied linear operators that map vectors to other vectors, like
rotation, and, having examined the transformation of operator components, derived the first type of transformation (see Section 4.7). This
type of transformation corresponds to the tensor of a mixed kind: contravariant in the first index and covariant in the second index. Later
we encountered many operators of this kind – projector operators (see
Section 5.7.)
Projector operators are unary linear operators. They are built upon
the bilinear dol-operator ̂ _σ_ . This binary operator introduced to us the
idea of conjugate space and unary linear operators mapping vectors into
numbers.


**114** - Tensors For Inquiring Minds


From further analysis of projector operators, we arrived at the idea
of tensor product and unlocked a key method of building tensors of
various kinds. Using a pair of vectors, we listed four different kinds
of tensors: covariant-covariant, covariant-contravariant, contravariantcovariant, and contravariant-contravariant. All these tensors can be
viewed as operators acting on vectors, either covariant or contravariant,
depending on the tensor type.

Having reviewed our steps, we can define tensors as follows:


_Tensors_


Tensors are _mathematical objects_ with the following essential properties:


  - Tensors can be combined (added) pairwise to yield another tensor.


  - Tensors can be multiplied by real numbers to yield another tensor.


  - Tensors can be represented via components, written relative to some basis.


  - When the basis changes, components of tensors transform in a very specific way,

to ensure that _tensors remains the same_ .


This definition is deliberately analogous to the definition of vectors.
In some sense tensors are _next tier vectors_ . Tensors are mathematical

objects following vectors in the ladder of abstraction and power, like
vectors are mathematical objects following numbers in the ladder of
abstraction and power.


5.9.1 Other Definitions


Let us revisit the definitions of tensors given in the introduction. The
first one read:


_Tensors Definition 1_


Tensor on a vector space _V_ over a field _k_ is an element _t_ of the vector space


_T_ _[p,q]_ ( _V_ ) = (⊗ _[p]_ _V_ ) ⊗(⊗ _[q]_ _V_ [∗] ) _,_


where _V_ [∗] = Hom( _V, k_ ) is the dual space of _V_ .


Tensors                             - **115**


⇒
In this definition the set of vectors _V_, which we denoted as _A_, is
called _vector space_ . Recall that vectors and operation with vectors require
numbers. Numbers, which can be added, multiplied in a usual way, form
what mathematicians call _field_ . Therefore, all vectors taken together are
technically called “vector space _V_ over a field _k_ .”
Next, the use of the operation of tensor product ⊗ in the definition
makes more sense, since it is the basic way to build tensors from vectors.
Notice that two types of vectors are mentioned: one from the vector
space _V_, and the other from its conjugate (dual) – vector space _V_ [∗] ;


⇐
in our notation _V_ [∗] = _A_ . The conjugate vectors behave very much like
vectors from the original vector space: they can be added, multiplied by
numbers, expanded in their own basis, and so on. This close correspondence between vector space and its conjugate is called _homomorphism_ [3]

and denoted Hom( _V,k_ ).
Tensor of the kind _T_ _[p,q]_ ( _V_ ) = (⊗ _[p]_ _V_ ) ⊗(⊗ _[q]_ _V_ [∗] ) has _p_ contravariant
indices and _q_ covariant indices. We mostly dealt with tensors of the
following types: _T_ [1] _[,]_ [1] _, T_ [0] _[,]_ [2] _,T_ [2] _[,]_ [0] .
Finally, tensors are vectors because they can be added, multiplied by
numbers, have components, and have vector-like transformation rules.
Tensors of a given type, e.g. _T_ [2] _[,]_ [1], taken together, form a vector space;
there is a separate vector space for each type of tensor.


The second definition stated:


_Tensors Definition 2_


An _n_ th-rank tensor in _m_ -dimensional space is a mathematical object that
has _n_ indices and _m_ _[n]_ components and obeys certain transformation rules.


Here tensor is mentioned in connection with some _m_ -dimensional

⇒
space, which we recognize as the underlying vector space _A_ . In our case,
the number of dimensions, given by the number of independent directions
in a plane, equals 2.


3From Greek _homos_ (same) and _morphe_ (shape).


**116** - Tensors For Inquiring Minds


The rank of a tensor is given by the number of indices or the number
of vectors that go into the tensor product. For example:


←



_L_ =



←
_a_ ⊗


←



_b_ �→ _Lij_ is the tensor of the second rank,



_b_ ⊗



→ _k_
_c_ �→ _M_ - ● _i j_ - is the tensor of the third rank.



_M_ =



←
_a_ ⊗



Since the value of each index runs from 1 to _m_, where _m_ is the dimension
of the vector space, tensors of the rank _n_ should have _m_ _[n]_ components in
total. The essential property of tensor components is how they transform
when the basis changes – _the tensor transformation rule_ .


The last definition, given in the introduction, looks as follows:


_Tensors Definition 3_


Just as a _vector_ is a mathematical quantity that describes translations in twoor three-dimensional space, a tensor is a mathematical quantity used to describe general transformations in _n_ -dimensional space. Precisely, if the locations of points in _n_ -dimensional space are given in one coordinate system by
( _x_ [1] _, x_ [2] _, . . ., x_ _[n]_ ) and in a transformed coordinate system by ( _y_ [1] _, y_ [2] _, . . ., y_ _[n]_ )
(it is convenient to use superscripts rather than subscripts), then a “rank 1
contravariant tensor” is a quantity _T_, with single components, that transforms
according to the rule:



_∂y_ _[i]_

_∂x_ _[r]_ _[T][ r][.]_



_Tnew_ _[i]_ [=]



_n_
∑
_r_ =1



We now know that tensors can be used to describe the transformation
of one vector into another (e.g., projectors). Similar ideas can be applied
to vectors in spaces with higher dimensions. In this sense, tensors can
describe general transformations in _n_ -dimensional space.

The essential property of tensor components is their transformation
rule. In this definition a transformation rule for a tensor of the first rank
(a ”usual” vector) is given:



_T_



′ _i_ _i_
= _Z_ _r_ _[T][ r][,]_



where the set of numbers _Z_ _[i]_ _r_ [describes the relation between the “old”]

basis (coordinates _x_ ) and the “new” basis (coordinates _y_ ).


Tensors                             - **117**


CHAPTER HIGHLIGHTS


  - _Two vectors can be compared for similarity by calculating the “de-_

_gree of overlap.” The longer two vectors are and the closer their_
_mutual direction – the greater the overlap is._


  - _Degree of overlap can be described by a bilinear operator_ ̂ _σ. This_

_operator is closely related to the concept of the scalar product of_

_two vectors._


  _When scalar product (or, equivalently, degree of overlap) is defined_

_for vectors, each vector receives a “special relative” – conjugate_
_vector – that lives in different vector space, called conjugate or_
_dual space._


  - _When the degree-of-overlap operator_ ̂ _σ is partially applied, the re-_

_sult is a unary linear operator that yields a number for every input_
_vector. Importantly, such an operator is also a vector, albeit not_
_an arrow-like vector._


  - _Unary linear operators that act on arrow-like vectors behave like_

_vectors themselves and form a vector space of their own. The latter_
_is conjugate to the “usual” space of arrow-like vectors._


  - _If arrow-like vectors are contravariant vectors, then their conju-_

_gate counterparts are covariant vectors. Covariant vectors can be_
_represented geometrically as oriented area elements (for three di-_
_mensional space)._


  - _Projectors are unary linear operators that act on input arrows to_

_yield another arrow that is parallel to a certain direction. Projec-_
_tors are degenerate operators._


  - _Projectors can be written using the efficient tensor product nota-_


_tion._


  - _Tensor product is a simple and powerful way to build up tensors of_

_any rank and any kind from a number of covariant and contravari-_

_ant vectors._


  - _Tensors are mathematical objects with many properties similar to_

_vectors. However, their rank is higher and tensors can be used to_
_express linear relations between vectors._


#### C H A P T E R 6

### Applications of Tensors

E ARE NOW READY TO APPRECIATE HOW
# W tensors are used in “real life.” In this chapter we will encounter

examples of tensors that are used in mathematics, physics, and engineering. Before we get to the examples of tensors, one more helpful notation
must be explained.


_δ-Notation_


When a quantity _x_ changes by a tiny amount, we will denote the change
using the small Greek letter _δ_ (delta) as follows:


_δx_           - tiny change of _x._


For example, for the earth going around the sun in 365 days, one second
elapsed on a clock can be considered a tiny change _δt_ . When a drop of
water falls into a nearly full bucket the mass of the latter changes by a
tiny amount _δm_, and so on.
That’s all there is to _δ_ -notation. We are not going into the realm of
calculus, where mathematicians talk about infinitesimal quantities and
limits; we will be simply using “tiny changes.” Now on to tensors.


6.1 FAMOUS TENSORS


We will study several examples of tensors that readers most likely encounter in geometry, physics, and engineering. The material in the previous chapters should be enough to prepare readers to deal with tensors
of any kind. However, we will limit considerations to simple tensors of
lower ranks.


**118** [DOI: 10.1201/9781003620365-6](https://doi.org/10.1201/9781003620365-6)


Applications of Tensors                        - **119**


6.1.1 Metric Tensor


_Metric tensor_ is used to determine distances between pairs of points in
space. A distance between two points is equal to the length of a vector
connecting them, as shown in Figure 6.1. For a vector


→ → →
_d_ = _b_ − _a,_ _d_ _[i]_ = _b_ _[i]_ − _a_ _[i]_


its length squared is given by the scalar product


→ → → →
_d_ [2] = _d_ ⋅ _d_ = ̂ _σ_ _d_ _d._


Figure 6.1 Distance between two points (1 and 2) equals to the lengths


→
of the vector _d_ connecting these points.


Using components in an arbitrary basis (not orthonormal), the length
squared is written as


_d_ [2] = ̂ _σ_ ( _d_ _[i]_ [→] _e_ _i_ )( _d_ _[j]_ [→] _e_ _j_ ) = _d_ _[i]_ _d_ _[j]_ (̂ _σ_ → _e_ _i_ → _e_ _j_ ) _._


The set of values

→ → → →
_ηij_ = ̂ _σ_ _e_ _i_ _e_ _j_ = _e_ _i_ ⋅ _e_ _j_


corresponds to the components of a special tensor – _metric tensor_ . The
transformation rule of these components is easily found by expanding
the “old” basis vectors in terms of the “new” (primed) basis, and using
the linearity of ̂ _σ_ :


_ηij_ [′] [= ̂] _[σ]_ → _e_ ′ _i_ → _e_ ′ _j_ [= ̂] _[σ]_ [ (] _[E][im]_ → _e_ _m_ )( _Ejn_ → _e_ _n_ ) = _EimEjnηmn._


**120** - Tensors For Inquiring Minds


This is the transformation rule of a covariant-covariant tensor of the

second rank. The metric tensor has to be of this kind since it maps a

contravariant-contravariant tensor


→ →
_d_ ⊗ _d,_ _d_ _[i]_ _d_ _[j]_


into a scalar. Each index of the metric tensor must transform in a way


→
that “compensates” the contravariant transformation of _d_ in the tensor


→ → ←
product _d_ ⊗ _d_ . This is analogous to how a covariant vector _b_ maps a
contravariant vector → _a_ into a number:


←→
_b_ _a_ �→ _x_


→ →
_η_ ( _a_ ⊗ _a_ ) �→ _y._


**Exercise 6.1** _Although the primary use of the metric tensor is to cal-_


→
_culate distances between a pair of points connected by a vector_ _d, it can_
_be applied to any pair of contravariant vectors:_


→ →
_η_ ( _a_ ⊗ _b_ ) _._


_a) What is the meaning of this operation? b) What are the components_
_of the metric tensor in an orthonormal basis?_


In most elementary problems of geometry and physics, a coordinate
system in a plane is Cartesian and basis vectors are orthonormal. As the
result, the components of the metric tensor are trivial – zeros and ones
– and are the same everywhere in the plane.
When non-Cartesian coordinates are used in a plane, e.g. polar coordinates shown in Figure 6.2, the basis vectors are aligned with the
coordinate grid [1] and have different orientations in different points. In
this case the components of the metric tensor _ηij_ change from point to


→
point to ensure that the lengths of the vector _d_


_d_ [2] = _ηijd_ _[i]_ _d_ _[j]_


remains the same.


1In principle, it is possible to have basis vectors “decoupled” from the coordinate
system, but this is not very convenient.


Applications of Tensors                        - **121**


→
Figure 6.2 Components of the same vector _d_ differ in various points

→ →
of the plane because the unit basis vectors { _u_ 1 _,_ _u_ 2} in those points are

→
aligned with the grid of the polar coordinate system. The vector _u_ 1
→
points in the direction of increasing distance _r_ ; the vector _u_ 2 points in
the direction of increasing angle _θ_ .


Moreover, for surfaces more sophisticated than a plane (e.g., sphere,
paraboloid, saddle-like surface, and myriad of others), it is impossible to
use coordinate system and basis such that the metric tensor is constant.
The components of the metric tensor will vary across the surface to
reflect the real, and not a merely “coordinate induced,” difference of a
surface from a plane. In other words, variations of the components of
the metric tensor indicate that the surface is _curved_ .

As an example, consider the two-dimensional surface of a sphere,
shown in Figure 6.3. Each point on the surface can be located using a
pair of coordinates – the angle _θ_ = _x_ [1] complimentary to the latitude, and
the longitude angle _ϕ_ = _x_ [2] . If a pair of close points on the sphere have


**122** - Tensors For Inquiring Minds


Figure 6.3 (a) Positions of points on the surface of a sphere can be
specified using two coordinates: angle _θ_ = _x_ [1] and _ϕ_ = _x_ [2] . (b) A part of
a sphere covered by a coordinate grid ( _x_ [1] _,x_ [2] ) can be represented using perpendicular axes, similar to Cartesian coordinates ( _x,y_ ). Distance
between two points on a uniformly spaced coordinate grid differs from
point to point: _d_ [2] = _R_ [2] ( _δx_ [1] ) [2] + _R_ [2] sin [2] _x_ [1] ( _δx_ [2] ) [2] .


coordinates


1 �→ ( _θ,ϕ_ ) _,_


2 �→ ( _θ_ + _δθ,ϕ_ + _δϕ_ ) _,_


then the distance squared between these points is given by


_d_ [2] = _R_ [2] ( _δθ_ ) [2] + _R_ [2] sin [2] _θ_ ( _δϕ_ ) [2] _._


This formula is obtained by applying Pythagoras theorem to the tiny
right triangle with the sides indicated using arrows in Figure 6.3. The
length of the side resulting from the change of the coordinate _ϕ_ is
_rδϕ_ = _R_ sin _θδϕ_ ; the length of the side resulting from the change of the
coordinate _θ_ equals _Rδθ_ .


Applications of Tensors                        - **123**


Using the uniform notation for coordinates, the distance squared is

written as
_d_ [2] = _R_ [2] ( _δx_ [1] ) [2] + _R_ [2] sin [2] _x_ [1] ( _δx_ [2] ) [2] _._


Comparing this to the Cartesian expression _d_ [2] = ( _δx_ [1] ) [2] + ( _δx_ [2] ) [2], we
can see that not all components of the metric tensor in the spherical
coordinate basis are constant. Namely, the component _η_ 22 = _R_ [2] sin [2] _x_ [1]

depends on the coordinate _x_ [1] = _θ_ .


_Einstein’s Equations for Gravity_


The notion of the metric tensor is central to the Einstein’s General Theory of
Relativity. The theory describes the effects of gravity in terms of geometrical
notions – curvature of the universe at various points of space and time due
to the effects of energy and motion in those points.


The main equation of the theory can be written using index notation as follows:
_Rij_ − _gij_ (Λ − _R_ /2) = _κTij._


Here _gij_ is the metric tensor, _Rij_ is the curvature tensor, and _Tij_ is the tensor
of energy and motion. The scalar quantity _R_ is the numerical characteristic of
the curvature tensor _Rij_, while Λ is the so-called _cosmological term_ required
to describe the measured expansion of the observable universe.


The goal of the theory is to find metric tensors satisfying the equation above
and then understand what geometric shapes those metric tensors describe.
The difficulty comes with the fact that both the curvature tensor _Rij_ and
the tensor of energy and motion _Tij_ depend on the metric tensor, making
Einstein’s equations highly _nonlinear_ .


6.1.2 Anisotropy Tensor


_Anisotropy tensor_ is a general term for various tensors used in physics
to describe properties of materials like crystalline solids. Many physical properties – mechanical, optical, electronic, thermal – describe the
response of the material to external “forces” or perturbations. Mathematical description of such responses requires tensors.
To understand the general idea, let us consider a simple situation,
depicted in Figure 6.4. Suppose that a tree bends in the wind, so that
when the wind blows in the direction of the _x_ axis, the displacement of
the tree-top is also along the _x_ axis, with the magnitude proportional to


**124** - Tensors For Inquiring Minds


Figure 6.4 (a) A tree bends in the wind by the amount and the direction

→
determined by the velocity vector _v_ ; On the right, the top view of the
tree is given. (b) For an arbitrary direction of the wind, the displacement


→
of the tree-top _d_ will not be parallel to the direction of the wind, but it
→
will still be proportional to the wind velocity _v_ .


→
the magnitude of the wind’s velocity _v_ :


→ → → →
_d_ = _dxu_ 1 = _Avxu_ 1 = _Av._


Next, suppose that when the wind blows along the _y_ axis, the tree-top
is also displaced in the direction of the _y_ -axis:


→ → → →
_d_ = _dy_ _u_ 2 = _Bvy_ _u_ 2 = _B_ _v._


→
In both cases the displacement vector _d_ is parallel to the vector of wind’s
velocity.
For a general direction of the wind, the magnitude of the tree-top
displacement will be proportional to the magnitude of the wind’s velocity, but _the direction of the displacement will differ from the direction of_
_the wind_ :
→ →
_d_ ∝ _v,_ _d_ ∦ _v._


Applications of Tensors                        - **125**


Indeed, for a wind vector


→ → → → →
_v_ = _vxu_ 1 + _vy_ _u_ 2 = _v_ 1 + _v_ 2 _,_


the “response” of the tree-top will be different for different components
of the wind vector:


→ → → → → → → → →
_d_ = _d_ 1 + _d_ 2 = _Av_ 1 + _B_ _v_ 2 = _Av_ cos _θu_ 1 + _Bv_ sin _θu_ 2 = _dxu_ 1 + _dxu_ 2 _._


Clearly,
_d_
_y_ = _[B]_ [ sin] _[ θ]_
_dx_ _A_ cos _θ_ [≠] [tan] _[ θ.]_


Thus, although the displacement magnitude _d_ is still proportional to the
magnitude of the wind’s velocity _v_, the direction of the displacement
no longer coincides with the direction of the wind. This fact can be
expressed using tensor notation:


_d_ _[i]_ = _T_ _[i]_ _j_ _[v][j][.]_ (6.1)


In the special coordinates, considered at the beginning of this problem,
the components of the tensor _T_ are simple:


_T_ [1] 1 [=] _[ A,T]_ [ 1] 2 [=][ 0] _[,T]_ [ 2] 1 [=][ 0] _[,T]_ [ 2] 2 [=] _[ B .]_


In all other coordinate systems and bases, the components of the “response tensor” _T_ can be found using the transformation rule for the
contravariant-covariant tensor of the second rank.
Expressions similar to the equation (6.1) can be written for a variety
of physical phenomena. We will consider a couple of examples next.


**Mechanics: Stress Tensor**


Mechanics of elastic media use many tensor tools. One of the basic tensors is the _stress tensor._ [2] This tensor describes the distribution of me
chanical stress inside a deformed elastic body, as illustrated in the Figure

6.5.
An elastic ball, shown in the Figure 6.5(a), can be squeezed by external forces, resulting in the change of shape ( _deformation_ ) and the
appearance of mechanical stress inside the ball; see Figure 6.5(b). In
general, the induced stress will change from point to point inside the


2Also known as _Cauchy stress tensor_ or _true stress tensor._


**126** - Tensors For Inquiring Minds


Figure 6.5 Stress tensor describes the distribution of stress inside an
elastic medium. (a) An elastic ball without stress and deformation. (b)
Applying external forces deforms elastic body and creates mechanical
stress inside. (c) Forces perpendicular to the sides of the square lead to
stretching or compression, whereas forces parallel to the surfaces result
in shear. (d) Total force applied to each side of the square removed from

→ →
the stressed body is given by the stress tensor: _f i_ = ̂ _σ_ _e_ _i_ . See text for
more details.


deformed ball. To describe the stress around a given point _P_, we can
imagine that a small part of the body is removed, leaving a tiny squareshaped hole. If nothing is done, the empty part of the ball around the
point _P_ will not remain square, due to the “forces” acting within the
body and at the boundary of the hole. To keep the hole square, we must
compensate the forces due to mechanical stress and apply the balancing


→ → → →
forces _f_ 1 _,_ _f_ 2 _,_ _f_ 3 _,_ _f_ 4 to each side of the square [3] . Only two such forces
are shown in the Figure 6.5(b) for simplicity.
The direction and magnitude of a force needed for a given side can
→
be found as follows: First, find the unit-length vector _e_ _i_ perpendicular


3For a three dimensional ball, the shape of the hole will be a cube, and the
number of forces will be 8 – one for each face of the cube.


Applications of Tensors                        - **127**


to the side. Second, calculate the force using the Cauchy stress tensor:


→ →
_f i_ = ̂ _σ_ _e_ _i._


The traditional notation for mechanical stress tensors is the Greek letter

sigma – _σ_ . It should not be confused with our notation for the doloperator defined earlier (see Section 5.1).
It is easy to understand why the “balancing forces” are not, in general, pushing perpendicular to the sides of the square. The idea is illustrated in Figure 6.5(c). An elastic square (cube) can be deformed in two
basic ways: 1) A square can be squeezed by forces perpendicular to the
sides ( _normal stress_ ); 2) A square can be deformed into a parallelogram
by forces parallel to the sides ( _shear stress_ ). Both types of stress can
exist at the same time, resulting from forces directed at an arbitrary
→
angle relative to the vector _e_ _i_ perpendicular to the sides.


**Electronics: Mobility Tensor**
Many materials conduct electric current. An important characteristic
of any such material is its _electrical resistance_ . When a voltage _V_ is
applied to a piece of conducting material, the current _I_ will flow
between the terminals, as shown in Figure 6.6.


Figure 6.6 Electron mobility tensor describes the response of charge
carriers inside an anisotropic material to external electric field. (a) When


→
electric field _E_ – and corresponding voltage _V_ is applied to a body, the
motion of electric charges (electric current _I_ ) is induced. (b) Applying
the same electric field (and voltage) in different directions may result in
different magnitudes of the current. This is due to the _mobility_ of electric
charges being different for different directions of motion.


**128** - Tensors For Inquiring Minds


The basic law that relates the voltage _V_ and the current _I_ between
the terminals is _Ohm’s law_ :


_V_ = _IR._


Here _R_ is the electrical resistance of a given piece of material.
For the same material, currents flowing in different directions may
experience different resistances even for the same geometrical shape. In
the example shown in Figure 6.6(a,b), for currents flowing horizontally
and vertically through a square we can write


_V_ = _I_ 1 _R_ 1 and _V_ = _I_ 2 _R_ 2 _._


We can take another view on the movement of electric charge through
the material if we rewrite Ohm’s law as follows:


_I_ = _GV._


Here instead of resistance, we use an equally useful physical parameter
called _conductance G_ . In a certain sense, conductance is more fundamental since it is closely related to basic physical laws that govern the
motion of electric charges.
Electric current is the flow of a large number of charge carriers, such
as electrons or ions, shown as red dots in Figure 6.6(a,b). The current _I_ is
proportional to the average speed _u_ of the carriers through the material:


_I_ ∝ _u._


The carriers, in their turn, move because there is an electric field _E_
between the terminals due to applied voltage _V_ . The average speed _u_ of
charge carriers is often simply proportional to the electric field:


_u_ = _µE,_


where the coefficient _µ_ is called _mobility_ of charge carriers.
Now for anisotropic materials, the relation between the average ve
locity → _u_ of charge carriers and the applied electric field _E_ → can be written
using the concept of _mobility tensor_ :


→ _u_ = ̂ _µ_ _E._ →


The mobility tensor expresses how easy it is to make electrons move in


→
a given direction by applying an external electric field _E_ .


Applications of Tensors                        - **129**


Let us summarize: Applying voltage between terminals creates an


→

electric field _E_ in a given direction. The electric field is proportional to

the voltage between the terminals: _E_ = _V_ / _d_ . The electric field leads to
the “mass migration” of charge carriers with the average speed


_u_ = _µE_ = _µV_ / _d._


This type of motion is called electric current:


_I_ ∝ _u_ �→ _I_ ∝ _[µ]_

_d_ _[V.]_


From the last expression, we can see how the relationship _I_ = _GV_ or
Ohm’s law _V_ = _IR_ appears. Furthermore, because the mobility ̂ _µ_ is in
general a tensor, the measured resistance of a given piece of material
may be different for different directions of applied voltage drop _V_ .


_Anisotropy Tensors in Physics_



Besides two examples of tensors (stress and mobility) given above, there
are many other tensors used in physics. Some tensors are similar to stress
and mobility tensors in the sense that they express the linear relationship


→ →

between “action” ( _a_ ) and “response” ( _r_ ) vectors



→
_a_ ) and “response” (



→
_r_ ) vectors



→ _r_ = ̂ _t_ → _a._



But more advanced tensors are also used to express linear relationships
between more simple tensors and vectors. For example, in certain materials
mechanical stress can lead to the separation of electric charges and thus
create voltage drop between different points of the body. This phenomenon
is known as the _piezoelectric effect_ . Now if we characterize induced charge

→ _i_

separation using a vector _p_ = _p_, then we can write using index notation


_p_ _[i]_ = _d_ _[ijk]_ _σjk,_



where _σjk_ are the components of the stress tensor described above, and
_d_ _[ijk]_ – piezoelectric tensor of the third rank (three indices!)


For readers interested in more examples and details, the book _Physical_
_Properties of Crystals: Their Representation by Tensors and Matrices_
by J. F. Ney is highly recommended.


As the last example of tensors in physics, we will consider a more
fundamental case from field theory.


**130** - Tensors For Inquiring Minds


6.1.3 Electromagnetic Tensor


In applied physics and engineering one works with electric and magnetic
fields that are described using two _different_ physical vector quantities:

→ →
_E_ – for electric field strength and _B_ – for magnetic field strength.
When a charged particle, say an electron, is placed in an electric
field, the latter acts on that particle with a force proportional to the
field strength:
_Fe_ = _qE,_


where _q_ is the charge of the particle, _Fe_ denotes the force due to the


→
electric field _E_ .
When the same charged particle is _moving_ in a magnetic field, the
latter acts on the particle with a force proportional to the magnetic field
strength:
_Fm_ = _qvB,_


where _v_ is the speed of the charged particle, _Fm_ denotes the force due to


→
the magnetic field _B_ . The difference between the effects of electric and
magnetic fields on a charged particle is illustrated in Figure 6.7.


Figure 6.7 Electromagnetic field acts on stationary and moving charged
particles. (a) Electric field between the plates of a charged capacitor acts
on any charged particle with the force _Fe_ = _qE_ directed along the electric


→
field vector _E_ . (b) A charged particle moving with the speed _v_ across
magnetic field between the poles of a magnet will be affected by a force
_Fm_ = _qvB_ . The force depends on the relative orientation of the velocity

vector → _v_ and the magnetic field _B_ →. When → _v_ is parallel to _B_ → – the force

is zero. The force is maximal when → _v_ is perpendicular to _B_ →.


Applications of Tensors                        - **131**


The distinction between electric and magnetic fields is technical and
_not fundamental_ . Figuratively speaking, the electric field differs from
magnetic field to the same degree as the rest differs from uniform motion.
Electric and magnetic fields are different aspects of the same physical
entity – _electromagnetic field_ .

From the expressions for the electric and magnetic forces _Fe_ and
_Fm_ we can see that physical quantities _E_ and _B_ have different units of
measurement – a fact which upsets some physicists. They note: If electric
and magnetic fields are different aspects of the _same physical object_, they
must be measured using the same units, similar to how we measure the
height and width of a building using the same units of length.

The way to fix the issue with different units for electric and magnetic
fields is to change the way we measure... _velocity_ ! Nature provides us with
a special standard of speed – the speed of light in a vacuum, denoted as
_c_ . The speed of light in a vacuum is a “nature-made” absolute quantity,
in contrast to such human-made standards as units of length (meter) or
time (second). This is why in fundamental physical theories, including
the theory of electromagnetic field, it is wise to specify all speeds as
fractions of the speed of light.

Thus, in physical formulas, instead of writing _v_ as meters per second,
we should use a “normalized” quantity:


_v_ ¯ = _v_ / _c_ → _v_ = ¯ _vc._


Once we apply this approach to the expression of the magnetic force, we
obtain

_Fm_ = _qvB_ = _qv_ ¯( _cB_ ) _._


Now we can see that the quantities _E_ and _cB_ have the same physical
meaning – _the force per unit charge_ . It is these physical quantities that
should be used to describe different aspects of the same electromagnetic
field. We will denote them as follows:



→
_E_ =



→
E = E _[i]_ _,_ _c_



→
B = B _[j]_ _._



→
_B_ =



_Electromagnetic Tensor_


A deep and beautiful discovery of the theory of electromagnetic field can now
be stated: Electric and magnetic fields E _[i]_ and B _[j]_ are not separate _vector_
quantities, they are, in fact, represent certain _components of a tensor_ that
describes electromagnetic field.


**132** - Tensors For Inquiring Minds


This tensor is conventionally written as _F_ _[µν]_ ( _F_ here stands for _field_, not
force!) _F_ _[µν]_ is a second-rank tensor. The indices _µ_ and _ν_ run from 0 to 3.
The relationships between the “usual” electric field and the electromagnetic
tensor are given by

E _[i]_ = _F_ _[i]_ [0] _,_ _i_ = 1 _,_ 2 _,_ 3 _._


The relationships between the “usual” magnetic field and the electromagnetic tensor can be written in the following way:


B [1] = _F_ [32] _,_ B [2] = _F_ [13] _,_ B [3] = _F_ [21] _._


A convenient way to write all components of a second-rank tensor is
to use a table-like structure called _matrix_ :



⎞
⎟⎟⎟
⎠



_F_ _[µν]_ =



⎛ _F_ [00] _F_ [01] _F_ [02] _F_ [03]

_F_ [10] _F_ [11] _F_ [12] _F_ [13]

⎜⎜⎜ _F_ [20] _F_ [21] _F_ [22] _F_ [23]
⎝ _F_ [30] _F_ [31] _F_ [32] _F_ [33]



_._



In the matrix, the first index _µ_ of _F_ _[µν]_ corresponds to the row, while the
second index _ν_ corresponds to the column. Both rows and columns are
enumerated from 0 to 3.


Using matrix form, we can write the electromagnetic tensor in terms
of the electric and magnetic fields:



0 −E [1] −E [2] −E [3]



⎞
⎟⎟⎟
⎠



_F_ _[µν]_ =



⎛
⎜⎜⎜
⎝



E [1] 0 −B [3] B [2]



E [2] B [3] 0 −B [1]



_._



E [3] −B [2] B [1] 0



The last expression makes apparent two features of electromagnetic tensor components. First, all diagonal elements vanish:


_F_ [00] = _F_ [11] = _F_ [22] = _F_ [33] = 0 _._


Second,

_F_ _[µν]_ = − _F_ _[νµ]_ _,_


a property known as _antisymmetry_ . This property requires all diagonal
elements to be equal to zero.


Applications of Tensors                        - **133**


_Electromagnetic Tensor Components_


The first kind of tensor of the second rank that we encountered was a linear operator _L_ [̂] . The components of any linear operator are given relative to
some basis and the components specify how the operator transforms basis

vectors:
_L_ ̂ → _e_ _i_ = _Lij_ → _e_ _j._


What is the basis used to express components of electromagnetic tensor
_F_ _[µν]_ ?

An Electromagnetic tensor is a physical operator which is used to express
the action of an electromagnetic field on a moving charged particle. Components of electromagnetic tensor connect special versions of velocity ( _vν_ )
and force ( _f_ _[µ]_ ) acting on a charged particle:


_f_ _[µ]_ = _qF_ _[µν]_ _vν_ _._


Without going into details, we will note that on the left-hand side of this equation, we have a four-component force, and on the right-hand side, we have
both electric and magnetic effects combined in a single tensor.


6.2 COMPOUND NUMBERS


The machinery of arrow-vectors and operators, which we developed in
the previous chapters, helps us establish the connection between planar
arrow-vectors and _complex numbers_ . We won’t be discussing complex
numbers in a conventional way, so we will intentionally avoid using conventional name for them, using the term _compound numbers_ instead.
A point in a plane is uniquely specified by a pair of Cartesian coordinates ( _x,y_ ). Alternatively, the point can be specified by an arrow-vector
connecting the point and the origin of the coordinates, as shown in the
Figure 6.8. If we choose the basis vectors → _e_ 1 and → _e_ 2 along the coordinate
axes _x_ and _y_, respectively, then we can write


→ → →
_a_ = _xe_ 1 + _y_ _e_ 2 _._ (6.2)


Thus, there exists a natural connection between planar arrow-vectors
and pairs of numbers ( _x,y_ ):


→
_a_ ↔ ( _x,y_ ) _._


→ →
_Any_ vector _a_ can be obtained from the basis vector _e_ 1 by appropriate
scaling and rotation:
→ →
_a_ = _a_ ̂ _Rθ_ _e_ 1 _._


**134** - Tensors For Inquiring Minds


Figure 6.8 A point _P_ in a plane can be specified by an arrow-vector → _a_,
or using a pair of numbers ( _x,y_ ) – Cartesian coordinates of the point _P_ .


→
In particular, the second basis vector _e_ 2 is given by:


→ → →
_e_ 2 = ̂ _Rπ_ /2 _e_ 1 = ̂ _J_ _e_ 1 _,_


where we used a special symbol _J_ [̂] for the operator of 90-degree counterclockwise rotation. The operator _J_ [̂] has an interesting property: Applied
twice to any vector, it flips the direction of the latter:


_J_ ̂ ( ̂ _J_ → _a_ ) = ( ̂ _J_         - ̂ _J_ ) → _a_ = ̂ _J_ 2 → _a_ = −→ _a._


Symbolically this can also be written in the argument-free form:


_J_ ̂ [2] = −̂ _I._


Using the operator _J_ [̂], we can rewrite the expression (6.2) as follows:


→ _a_ = ( _xI_ ̂ + _y_ ̂ _J_ )→ _e_ 1 _._


Usually, the operator _I_ [̂] is omitted if it is clear from the context that
expressions involve operators. With this in mind, the expression for the
→
vector _a_ can be rewritten:


→ →
_a_ = ( _x_ + _y_ ̂ _J_ ) _e_ 1 _._


Given that _x_ = _a_ cos _θ_, and _y_ = _a_ sin _θ_, we obtain


→ →
_a_ = _a_ (cos _θ_ + sin _θ_ ̂ _J_ ) _e_ 1 _,_


Applications of Tensors                        - **135**


from which follows the expression for the rotation operator


_R_ ̂ _θ_ = cos _θI_ ̂ + sin _θ_ ̂ _J_ = cos _θ_ + sin _θ_ ̂ _J._ (6.3)


Rotation of a vector by the angle _θ_ can be performed as a single step,
or as a sequence of _N_ rotations, each by a smaller step _δθ_ = _θ_ / _N_ . Symbolically, this can be written as a sequence ( _composition_ ) of _N_ identical
operations:

̂
_Rθ_ = ̂ _Rδθ_        - ̂ _Rδθ_        - _..._        - ̂ _Rδθ_ = [ ̂ _Rδθ_ ] _[N]_ _._


→
When a vector _a_ is rotated by a tiny angle _ϕ_, its tip travels along
the arc with the length _aϕ_, in the direction perpendicular to the vector
itself, as illustrated in Figure 6.9. The unit length vector, pointing per→ → →
pendicular to _a_ can be obtained from a unit vector _ua_ pointing along _a_
by rotating the former with the operator _J_ [̂] :



̂→
_J_ _ua_ = ̂ _J_ [⎛] ⎝



→

_a_

⎞

_a_
⎠ _[.]_



→
As the result of the rotation by a tiny angle _ϕ_, the vector _a_ becomes


̂ → → → → → →
_Rϕ_ _a_ ≈ _a_ + _aϕ_ ( ̂ _J_ _ua_ ) = _a_ + _ϕJ_ ̂ _a_ = (1 + _ϕJ_ ̂ ) _a._


For a tiny angle _ϕ_ = _δθ_ this becomes


_R_ ̂ _δθ_ → _a_ = (1 + _δθ_ ̂ _J_ )→ _a._


→
Figure 6.9 Rotation of a vector _a_ by a tiny angle _ϕ_ . (a) The tip of the

→
vector _a_ will move along the arc of the circle with radius _a_ . The length
of the arc is _φa_ . (b) The tangent line to the arc will be perpendicular
to the vector → _a_ . The unit vector parallel to the tangent can be found by
rotating the unit vector → _ua_ with the operator ̂ _J_ .


**136** - Tensors For Inquiring Minds


Applying this to the relation


_R_ ̂ _θ_ ≈[ ̂ _Rδθ_ ] _[N]_


we arrive at

_R_ ̂ _θ_ ≈[1 + _δθ_ ̂ _J_ ] _[N]_ = [1 + _[θ]_ [ ̂] _[J]_

_N_ []] _[N]_ _[.]_


In the limit of ever-smaller steps ( _N_ →∞ and _δθ_ → 0), the result becomes
the famous limit



1 + _[x]_
( _N_




_[x]_

_N_ [)]



_N_



= _e_ _[x]_ as _N_ →∞ _._



We thus discovered the following expression for the rotation operator



̂
_Rθ_ :



̂ _J_
_Rθ_ = _e_ _[θ]_ [ ̂] _._



Comparing this to the expression (6.3), we find the important relation
between two different representations of the rotation operator _R_ [̂] _θ_ :


_J_
_e_ _[θ]_ [ ̂] = cos _θ_ + ̂ _J_ sin _θ._ (6.4)


We can recognize the famous _Euler’s formula_ in this expression. In
words, it expresses the fact that a vector in a plane can be rotated
in a single step by the angle _θ_ or using the sequence of tiny rotations by
an angle _δθ_ = _θ_ / _N_ when the number of steps _N_ increases indefinitely.

For the special case of _θ_ = _π_, Euler’s formula becomes


_J_ _J_
_e_ _[π]_ [ ̂] = −1 �→ _e_ _[π]_ [ ̂] + 1 = 0 _._ (6.5)


So far we have established connections between different ways to
represent points in a plane:


1. Coordinate pair ( _x,y_ ).



2. Arrow-vector



→

_a_ .



3. Operator sum _z_ ( _x,y_ ) = _x_ + _yJ_ [̂] .


_J_
4. Operator product _z_ ( _a,θ_ ) = _ae_ _[θ]_ [ ̂] .


Neither of these representations is exceptionally advantageous. Different
problems may benefit from different approaches.

_J_
We will call the representations _z_ = _x_ + _yJ_ [̂] and _z_ = _ae_ _[θ]_ [ ̂] _compound_
_numbers_ . Compound numbers provide another approach to problems


Applications of Tensors - **137**



that involve points in a plane. Anything that can be analyzed and solved

→

using either Cartesian coordinates ( _x,y_ ), or arrow-vectors _a_ can also be

treated using compound numbers. The apparatus of compound numbers
(or _complex numbers_, if you prefer) is extremely powerful and useful in
physics and engineering.

Which form of compound numbers works best: sum _z_ = _x_ + _Jy_ [̂] or
_J_
product _z_ = _ae_ _[θ]_ [ ̂] ? The answer depends on the type of operation we want
to perform. Given a pair of compound numbers


_J_
_za_ = _xa_ + _yaJ_ [̂] = _ae_ _[θ][a]_ [ ̂]


and


_J_
_zb_ = _xb_ + _ybJ_ [̂] = _be_ _[θ][b]_ [ ̂] _,_


finding their sum _zc_ = _za_ + _zb_ is easier using sum-form:


_zc_ = ( _xa_ + _xb_ ) + ( _ya_ + _yb_ ) _J._ [̂]


On the other hand, the product of two compound numbers _zc_ = _zazb_ is
calculated easily using their product form:


_J_ _θbJ_ [̂]
_zc_ = _abe_ _[θ][a]_ [ ̂] _e_ _._


The last expression can be simplified if we use the trigonometric identity


cos _θ_ cos _ϕ_ − sin _θ_ sin _ϕ_ = cos( _θ_ + _ϕ_ )


and the property _J_ [̂] [2] = −1:


_zc_ = _ab_ (cos _θa_ +sin _θaJ_ [̂] )(cos _θa_ +sin _θaJ_ [̂] ) = _ab_ [cos( _θa_ + _θb_ )+sin( _θa_ + _θb_ ) _J_ [̂] ] _._


We deduce that

_zc_ = _abe_ _[θ][a]_ [ ̂] _J_ _eθbJ_ [̂] = _abe_ ( _θa_ + _θb_ ) _J_ [̂] _._


Since a compound number can be represented by a composition of scaling
and rotation, the interpretation of the product of two compound numbers
is clear: To multiply a number _za_ by a number _zb_, we must scale the

→ →

arrow-vector _a_ by a factor _b_ – the length of the arrow-vector _b_ – and

rotate it by an angle _θb_ .



arrow-vector



→
_a_ by a factor _b_ – the length of the arrow-vector



Finally, it is evident that multiplication of compound numbers is

commutative:


_zc_ = _zazb_ = _zbza._


**138** - Tensors For Inquiring Minds


_Composition Rule_


The property

_J_
_zc_ = _zazb_ = _ab e_ [(] _[θ][a]_ [+] _[θ][b]_ [) ̂]


can be deduced from the operator form of compound numbers. Indeed, we
could write
_zc_ = _zazb_ = _ab_ _R_ [̂] _θa_ _R_ [̂] _θb_


and notice that a sequence of two rotations can be replaced with a single
rotation by the combined angle:


_zc_ = _ab_ _R_ [̂] _θa_ + _θb_ = _ab e_ [(] _[θ][a]_ [+] _[θ][b]_ [) ̂] _J_ _._


_Pauli Matrices_


We made heavy use of the operator _J_ [̂], which has the components


_J_ ̂ [0] 1
−1 0 [)] _[ .]_
= (


In quantum physics, when dealing with the spin of elementary particles [4],
one encounters similar-looking matrices:


̂ _σ_ 1 1 10 [)] or ̂ _σ_ 3 0 −01 [)] _[ .]_
= ( [0] = ( [1]


These are called _Pauli matrices_ [5] after the physicist Wolfgang Pauli.
Readers can easily convince themselves that ̂ _σ_ 1 turns the basis vector → _e_ 1
into → _e_ 2 and vice versa, while the operator ̂ _σ_ 3 flips the direction of the basis

→ →
vector _e_ 2, leaving _e_ 1 intact.


6.3 HAMILTONIAN MECHANICS*


Quantum physics makes heavy use of vectors and operators, as well as
compound numbers (or complex numbers). However, these mathematical


4Spin of a particle is its fundamental characteristic, like its mass or charge. However, unlike mass or charge spin is a tensor quantity.
5The second Pauli matrix ̂ _σ_ 2 is essentially proportional to the operator ̂ _J_ .


Applications of Tensors                        - **139**


tools are not exclusive to quantum physics. Classical physics uses similar mathematical tools. Classical physics also shares many fundamental
physical concepts with quantum physics, such as _system_, _state_, _state evo-_
_lution_, _dynamical equation_, and many more. We will now get acquainted
with the basics of _Hamiltonian Mechanics_ – a way to study mechanical
motion using the ideas of energy and momentum as the starting points
(as opposed to forces and velocities of Newtonian Mechanics.)

The reader is assumed to be familiar with the basics of Newtonian

Mechanics and with the expressions for simple concepts, such as momentum, kinetic energy, or the energy of a stretched spring. The asterisk after
the title of this chapter is a reminder that the material that follows is a
bit more advanced than the rest.


6.3.1 System and State


A part of nature that can be clearly isolated and studied is called a _phys-_
_ical system_ . An electron, an atom, a molecule, a crystal, a pendulum, a
comet, a star – these are examples of physical systems of various degrees
of complexity.

Since physics is an experimental science, the study of a physical
system – or system for short – is based on _measurements_ of different
_parameters of the system_ . Such measurable parameters are also called
_observables_ . For example, when a projectile is studied, we can measure
its _position_ and _momentum_ at different moments of time. Position and
momentum of a body are observables.

In mechanics, the knowledge of position and momentum of a given
system at one moment of time _t_ 0 is sufficient to completely know their
value at any later moment of time _t_ . In addition, other useful physical quantities, such as energy or angular momentum, can be expressed
through position _x_ and momentum _p_ . Symbolically, we can write this as
follows:

know ( _x_ 0 _,p_ 0) at _t_ 0 �→ know ( _x,p_ ) at _t._


_State_ of a system is the collection of observables which is, in a certain
sense, _complete and self-sufficient_ . In other words, state is “all there is to
know” about a system. If the state of a system is known at one moment
of time _t_ 0, then we should be able to determine the state at any later (or
earlier) moment of time _t_ . In classical mechanics the pair of observables
( _x,p_ ) defines the state of a mechanical system.


**140** - Tensors For Inquiring Minds


_Oscillator_


In order to better understand the roles of position and momentum we
will study a specific system: An _oscillator_ . As an oscillator model, we
will consider a body with mass _m_ attached to a spring with a spring
constant _k_, as shown in Figure 6.10.


Figure 6.10 Mechanical model of an oscillator: A body with mass _m_
attached to a spring with spring constant _k_ . When displaced from equilibrium by the amount _x_ and released, the oscillator will begin periodic

motion.


When the body is moving with speed _v_, it has kinetic energy

_Ek_ = _[mv]_ [2]

2 _[.]_


When the spring is stretched by the amount _x_, it has potential energy

_Ep_ = _[kx]_ 2 [2] _[.]_


The total mechanical energy of the oscillator is given by



_E_ = _Ek_ + _Ep_ = _[kx]_ [2]



2 _[.]_




[2]

+ _[mv]_ [2]
2 2



We can write the total mechanical energy using the momentum _p_ = _mv_
instead of velocity:




[2]

+ _[p]_ [2]
2 2



_E_ = _[kx]_ [2]



(6.6)
2 _m_ [=] _[ H.]_



Here we used the letter _H_ to denote the _Hamiltonian_ of the system –
_the expression of total energy of terms of position and momentum_ . In
the absence of friction, the total mechanical energy of a system remains
constant ( _H_ = const.)
While both _x_ and _p_ change during the motion of the oscillator, their
combination satisfies the relation:



_H_ = _[x]_ [2]




_[x]_ [2] _[p]_ [2]

2/ _k_ [+] 2



_x_ [2]

_[p]_ [2] → 1 =

2 _m_ 2 _H_



_x_ [2] _p_ [2]

2 _H_ / _k_ [+] 2



2 _mH_ _[.]_


Applications of Tensors                        - **141**


Figure 6.11 (a) During the motion of the oscillator, both the position
_x_ and momentum _p_ change, while the point _P_ = ( _x,p_ ) remains on the
ellipsis. (b) The motion of the oscillator in the _normalized_ coordinates
_x_ ¯ and ¯ _p_ is described by a circle with the radius _ξ_ = ~~√~~ _H_ ~~¯~~ . A particular


→
combination of ¯ _x_ and ¯ _p_ can be described by a _state vector_ _ξ_ = ¯ _x_ + ¯ _pJ_ [̂] .


The last expression reminds the equation for an ellipsis with the axes _a_
and _b_, written for Cartesian coordinates:




_[x]_ [2] _[y]_ [2]

[+]
_a_ [2] _b_ [2]



1 = _[x]_ [2]



_b_ [2] _[.]_



Thus, in the _xp_ plane this equation describes an ellipsis, as illustrated in
Figure 6.11(a). The maximal value for _x_ can be found from the following
condition: At the maximal stretch of the spring, the body stops ( _p_ = 0)
and all energy is stored in the stretched spring:



_kA_ [2]

= _H_ → _A_ =
2



√



2 _H_


_k_ _[.]_



When the spring is not stretched and all energy is stored in the moving
body, the momentum has the maximal value:



_B_ [2]



2 _mH._



→ _B_ = ~~√~~
2 _m_ [=] _[ H]_



The analysis of the oscillator motion can be simplified if we make
the equation (6.6) _dimensionless_ : Instead of the usual units for distance
( _m_ ), momentum ( _kg_ ∗ _m_ / _s_ ), and energy ( _J_ ), we will express them as
scaled versions of some “natural” values _x_ 0, _p_ 0, and _H_ 0:


_x_ = ¯ _xx_ 0 _,_ _p_ = ¯ _pp_ 0 _,_ _H_ = _HH_ [¯] 0 _,_


**142** - Tensors For Inquiring Minds


where ¯ _x_, ¯ _p_, _H_ [¯] are unitless quantities. There are many ways to do such
a transformation but we will use a simple approach based on the restenergy of an electron.


_Dimensionless Quantities_


To understand the idea of dimensionless quantities, consider the following
situation: An average human consumes and spends 1800 Calories per day.
A physicist might prefer to express this quantity in standard units, and write
_Eday_ = 7 _._ 531 × 10 [9] Joules. But we can also express the energy required for
a day in terms of the number of ...cookies:


_Eday_ = 13 _Eccc_ = _E_ [¯] _dayEccc_


where _Eccc_ is the energy content of a single chocolate chip cookie. In this
expression, _E_ [¯] _day_ is the dimensionless energy.


When an electron is at rest, its energy ( _rest-energy_ ) is given by the
most famous equation in physics:


_He_ = _mec_ [2] _._


Now we will use this quantity as the measure of all other energies. We
will write _H_ = _HH_ [¯] _e_ where _H_ [¯] is a pure mathematical number (as opposed
to “physical” number with units.)

Next we can find the reference value for position. Suppose the oscillator has the energy _He_ . Then its maximum displacement will be



_xe_ =


and the maximum momentum


_pe_ =



√



2 _He_


_k_ _[,]_



√



2 _mHe._



The Hamiltonian can be written in dimensionless units:



_HH_ ¯ _e_ = _[kx]_ _e_ [2]




[2] _e_ _e_

_[p]_ [2]
2 _[x]_ [¯][2][ +] 2



_e_
2 _m_ _[p]_ [¯][2][ =] _[ H][e][x]_ [¯][2][ +] _[ H][e][p]_ [¯][2] _[.]_



Therefore, the relationship between the dimensionless position and momentum is described by the equation of a circle in the ¯ _xp_ ¯ plane:


¯
_H_ = ¯ _x_ [2] + ¯ _p_ [2] _._


Applications of Tensors                        - **143**


We showed that the state of the oscillator ( _x,_ ¯ ¯ _p_ ) can be specified by
a point in the ¯ _xp_ ¯ plane. The latter can be described by a compound
number (a state vector):

→
_ξ_ = ¯ _x_ + ¯ _pJ._ [̂]


See Figure 6.11(b) for illustration. The radius of the circle is determined
by the total energy:


¯

_ξ_ = √ _H,_


→
where _ξ_ denotes the length of the planar vector _ξ_ .


6.3.2 State Dynamics


To know the properties of the oscillator at different moments of time we


→
must be able to find its state _ξ t_ at every moment of time, given the


→
initial state _ξ_ 0 at time _t_ = 0. Thus, we must understand what drives the


→
change of the state vector _ξ t_ . In other words, we must know the _state_


→
_dynamics_ . The evolution of the state vector _ξ_ in time is described by an
equation. We will “derive” it now.


→
As the time advances by a small amount _δt_, the state vector _ξ_ also


→
changes by a small amount _δ_ _ξ_ . During motion, both position and momentum change, therefore:


→
_δ_ _ξ_ = _δx_ ¯ + _δp_ ¯ _J._ [̂]


On the other hand, since the tip of the state vector follows along the
circle of radius _ξ_, its change can be written as the result of clockwise
rotation [6] by a small angle _δϕ_ :



⎞
⎟
⎠⎤⎥⎥⎥⎥⎥⎦



→
_δ_ _ξ_ = −( _δϕξ_ )



̂⎛
_J_ ⎜

⎡⎢⎢⎢⎢⎢⎣ ⎝



→
_ξ_

_ξ_



→
= − _δϕ_ ( _J_ [̂] _ξ_ ) _._



If we denote the rate of change of the angle _ϕ_ in time as


_ω_ = _[δ][ϕ]_

_δt_ _[,]_


6If the oscillator starts from state _ξ_ 0 = (0 _, ξ_ ) then ¯ _x_ will grow as ¯ _p_ decreases.


**144** - Tensors For Inquiring Minds


then we will arrive the equation for the state evolution:


→



_δ_



_ξ._ (6.7)



_ξ_
_δt_ [= −] _[ω]_ [ ̂] _[J]_



→



_Hamiltonian Equations_


The left-hand side of (6.7) can be written in terms of the position and mo
mentum:


→



_δ_



_δ_ _ξ_

_δt_ [=] _[ δ]_ _δt_ _[x]_ [¯]




_[x]_ [¯]

_δt_ [+] _[ δ]_ _δt_ _[p]_ [¯]



_δt_



_J._ ̂



Doing the same with the right-hand side of the equation (6.7), we obtain


→

− _ωJ_ [̂] _ξ_ = _pω_ − _ωxJ._ [̂]


We thus derived the time-evolution equations for position and momentum:



_δx_ ¯



_δx_ ¯ _δp_ ¯

_δt_ [=] _[ ω][p,]_ [¯] _δt_



_δt_ [= −] _[ω][x.]_ [¯]



These equations are called _Hamiltonian equations_ ; they are the central
equations of _Hamiltonian dynamics_ . Hamiltonian dynamics is the approach
to mechanics alternative to Newtonian dynamics. Instead of using the concept of forces and Newton’s second law, Hamiltonian dynamics uses the
concept of Hamiltonian – the expression of energy written in terms of position and momentum.


For the oscillator the angular speed _ω_ turns out to be constant. To
show this, recall that ¯ _x_ = _x_ / _xe_ and _p_ = ¯ _ppe_ and write



_δx_ ¯



_δx_ ¯ _[δx]_

_δt_ [=] _x_




_[v]_
_xeδt_ [=] _xe_



_xe_



_._



Here we used the definition of velocity: _v_ = _δx_ / _δt_ .

In Newtonian mechanics the velocity and momentum are related as
_p_ = _mv_, therefore



_δx_ ¯ _p_

_δt_ [=] _mxe_



_pe_ ¯
= _p._
_mxe_



Compare this expression to the first equation of motion to find



_pe_
_ω_ =
_mxe_



=



√



_k_

_m_ _[,]_


Applications of Tensors                        - **145**


where the last result was obtained after substituting the expressions for
_xe_ and _pe_ in terms of the reference energy _He_ .


_Frequency of Oscillations_


Note that the expression for the frequency _ω_ of revolution of the state vector

→

_ξ_ depends only on the parameters of the oscillator:



_ω_ =

~~√~~



_k_

_m_ _[.]_



The choice of units _He_, _xe_, and _pe_ does not affect the value of _ω_, only the
graphical representation of the evolution as circular motion.


Another illuminating relationship exists between the angular speed
_ω_ and the energy _He_ . To find it we can use the fact



_p_ [2] _e_



_pe_ _pe_

�→
2 _m_ [=] _[ H][e]_ _m_ [=][ 2] _[H][e]_



_pe_



and arrive at



_ω_ = [2] _[H][e]_

_xepe_



_._



One last transformation is needed for the equation of state evolution.
By acting with the rotation operator _J_ [̂] on both sides of


→



_δ_



→

_ξ_



_δ_ _ξ_

_δt_ [= −] _[ω]_ [ ̂] _[J]_



we obtain



→



̂

_ξ_

_J_ _[δ]_

_δt_ [=] _[ ω]_



_J_ ̂ _[δ]_



→

_ξ._



This expression allows us to write the time-evolution equation for the


→



state vector



_ξ_ in _Schr¨odinger form_ :


→

_ξ_

_heJ_ [̂] _[δ]_ _δt_ [=] _[ H][e]_



→

_ξ,_ (6.8)



where _he_ = _xepe_ /2 – the quantity with the units of angular momentum
or, equivalently, energy multiplied by time. Such quantity is known in


**146** - Tensors For Inquiring Minds


physics as _action_ and it plays an important role in classical and quantum
mechanics.


_Quantum of Action_


The fundamental constant of nature, known as _Planck constant h_, is the
smallest possible action. Physicists found that action is quantized: In all
physical processes action changes in steps of _h_ .


_Schr¨odinger Equation_


The dynamical equation for the oscillator (6.8) is completely analogous to
the famous equation of Quantum Physics, known as Schr¨odinger Equation:


_ih_ [̵] _[δ]_ [Ψ]

_δt_ [=] _[ H]_ [Ψ] _[.]_


Without going into details, we will note that in this equation Ψ corresponds


→
the the state of quantum system, analogous to _ξ_ . The ”imaginary unit” is
analogous to the operator _J_ [̂] ( _i_ [2] = −1). The fundamental constant _h_ [̵] is the
elementary quantum of action. Finally, _H_ represents quantum version of the
Hamiltonian.


Having shown that the angular speed _ω_ is constant, we can deduce
the time dependence of position and momentum for the oscillator [7] :


_x_ ¯ = _ξ_ cos _ωt,_ _p_ ¯ = _ξ_ sin _ωt_


and consequently


_x_ ( _t_ ) = _xeξ_ cos _ωt,_ _p_ ( _t_ ) = _peξ_ sin _ωt._


Given that



_,_
_pe_



_ξ_ =



√



_H_
= _[A]_
_He_ _xe_




_[A]_ = _[B]_

_xe_ _pe_



7
We assume here that initially, at _t_ = 0, the oscillator is stretched to the maximum
and has no initial momentum.


Applications of Tensors                        - **147**


where _A_ is the maximum displacement of the oscillator with the energy
_H_, and _B_ is the maximum momentum for the same oscillator, we can

write

_x_ = _A_ cos _ωt,_ _p_ = _B_ sin _ωt._


The amplitude of oscillation _A_ and the maximum momentum _B_ can be
written in terms of the oscillator parameters _k_, _m_, and its total energy

_H_ :



2 _Hm._



_A_ =



√



2 _H_



_B_ = ~~√~~
_k_ _[,]_



This is the mathematical description of the _oscillatory motion_ .


6.4 VECTORS AND TENSORS IN COMPUTATION*


As the last example we will consider a somewhat technical problem. This
example should demonstrate that the ability to recognize and manipulate
tensors might pay off in unexpected places.
Imagine you are exploring a system of tunnels connecting large chambers, as schematically illustrated in Figure 6.12. If we number each entrance/exit (called _ports_ ) then we can characterize the propagation of
sound between a pair ( _i,j_ ) of ports using two parameters: attenuation of
the signal and the time delay between its emission and detection as the
signal travels through the structure. In the theory of wave propagation,
these two parameters are encoded in so called _S_ -parameter and the set
of _S_ -parameters for all combinations _i_ → _j_ of ports is called _S_ -matrix.
The relevant theory is developed by Gunnar Filipsson in the paper
_A general computer algorithm for S-matrix calculation of interconnected_
_multiports_ [8], but here we will only need the central formula from that
work:


_Sij_ [′] [=] _[ S][ij]_ [+] _a_ 1 _kl_ [[] _[S][il][S][kj]_ [(][1][ −] _[S][lk]_ [) +] _[ S][ik][S][lj]_ [(][1][ −] _[S][kl]_ [) +] (6.9)

+ _SilSkkSlj_ + _SikSllSkj_ ] _,_


where

_akl_ = 1 − _Skl_ − _Slk_ + _SklSlk_ − _SkkSll._


_Note_ : No summation is implied in expressions like _Skk_ and _Sll_ . The values
_k_ and _l_ are fixed and represent the number of ports that connect adjacent


[8https://doi.org/10.1109/EUMA.1981.332972](https://doi.org/10.1109/EUMA.1981.332972)


**148** - Tensors For Inquiring Minds


Figure 6.12 A sound signal (acoustic wave) can propagate in a complicated system of chambers connected by tunnels. Shouting at the entrance
of one tunnel and listening at the exist of another, we can measure how
much delay and attenuation the sound experiences.


chambers. With this in mind, we can introduce special notation in order
to get rid of indexed expressions:


_Skk_ = _α,_ _Sll_ = _β,_ _Skl_ = _µ,_ _Slk_ = _ν_


and

_akl_ = _a_ = 1 − _µ_ − _ν_ + _µν_ − _αβ._


The problem is then to calculate the set of values _Sij_ [′] [given the set]
of values _Sij_ for all combinations of port numbers _i, j_ = 1 _,_ 2 _, ...,n_ . A
simple approach consists of changing the values of each variable _i, j, k_,
and _l_ step by step and performing the usual arithmetic operations at
each step. The approach works but it is too slow.
The key to an improved solution is to recognize that the expression
for “new” values of _S_ [′] -parameters can be written in vector-tensor form:


_S_ ̂ [′] = ̂ _S_ + ̂ _A_ + _B_ [̂] + _C_ [̂] + _D,_ [̂]


where the terms _A_ [̂] through _D_ [̂] correspond to each term in the parentheses
of equation (6.9). For example:


_Aij_ = [(][1][ −] _[ν]_ [)] _SilSkj._

_a_


Here we used the notation introduced above for _a_ and _ν_ .


Applications of Tensors                        - **149**


The next step is to recognize that _Skj_ can be viewed as the _j_ -th
component of some vector:


→
_Skj_ = _W_ ( _k_ ) _[j]_ �→ _W_ ( _k_ ) _,_


while _Sil_ is the _i_ -th component of a dual vector:


←
_Sil_ = _V_ ( _l_ ) _i_ �→ _V_ ( _l_ ) _._


Using these vectors, the tensor-operator _A_ [̂] can be written using tensor
product notation:

̂ ← →
_A_ = [(][1][ −] _[ν]_ [)] _V_ ( _l_ ) ⊗ _W_ ( _k_ ) _._

_a_


With this approach, we can rewrite the operators _B_ [̂], _C_ [̂], and _D_ [̂] in a
similar way:
_B_ ̂ = [(][1][ −] _[µ]_ [)] _V_ ← ( _k_ ) ⊗ _W_ → ( _l_ ) _,_

_a_



̂
_C_ = _[α]_


_a_


and
_D_ ̂ = _[β]_


_a_



← →
_V_ ( _l_ ) ⊗ _W_ ( _l_ ) _,_


← →
_V_ ( _k_ ) ⊗ _W_ ( _k_ ) _._



The main reason behind these manipulations is that some computations involving vectors and their tensor products can be optimized using
advanced algorithms. In the real-world application of this theory, once
we transition from the step-by-step approach to the vector-tensor approach, the calculations can be sped up by a factor of 10! The Table
6.1 shows specific calculation time improvement that was made possible
after using the vector-tensor nature of the expression. The main point
is not that we can save 3 seconds, but that each calculation step is performed 10 times faster. Imagine that a long and complicated calculation
that takes 10 days can be done in just one day! That gives the desired
result earlier, saves time and also power used by the computer. This all
translates into _actual economic benefits_ .


TABLE 6.1 Calculations can be done up to 10 times faster when using
vector-tensor approach.


|Col1|Step-by-step|Vector-Tensor|
|---|---|---|
||3_._0_s_|0_._276_s_|


**150** - Tensors For Inquiring Minds


Having learned about vectors and tensors, you may discover new
ways to analyze familiar problems in your field of study. Good luck!


CHAPTER HIGHLIGHTS


  - _Tensors_ _find_ _application_ _in_ _various_ _areas_ _of_ _science_ _and_
_mathematics._


  - _Geometrical properties of surfaces and spaces can be described us-_

_ing metric tensors._


  - _Physical properties of solids are often anisotropic – depending on_

_the direction of applied “force.” Such properties are best described_
_by various tensors: stress tensor, mobility tensor, piezoelectric ten-_
_sor, and others._


  _At the fundamental level, electric and magnetic fields are united_

_in a single physical object – electromagnetic field. Electromagnetic_
_field is described by an antisymmetric tensor of the second rank._


  - _The concept of linear operators, and in particular of the rotation_

_operator_ _J_ [̂] _, can be used to extend the numbers from a number line_
_to the number plane and arrive at complex numbers (or compound_
_numbers, as we called them)._


  - _Operators and compound numbers are used in many physical theo-_

_ries, and play an especially important role in Hamiltonian dynam-_
_ics and quantum mechanics._


C H A P T E R 7

### Solutions


_Exercise 1.1_


Figure 7.1 The set _M_ contains all possible makes of cars: Ford, Toyota,

etc.


The diagram in Figure 7.1 shows the set _M_ – the set of all possible
makes of cars. A mapping **trk** returns _true_ if a given car maker produces
trucks.


_Exercise 2.1_


Any binary function can be viewed as a unary function if two inputs are
replaced by a single input of a _pair of numbers_ . Similarly for a function
with two outputs. This idea is illustrated in Figure 7.2(a): The function
**swp** is viewed as a unary function which swaps the numbers in an _ordered_


[DOI: 10.1201/9781003620365-7](https://doi.org/10.1201/9781003620365-7) **151**


**152** - Tensors For Inquiring Minds


Figure 7.2 (a) Two inputs (outputs) of a function can be replaced with
a single input of a _**pair**_ of numbers, turning a binary function into a
unary one. (b) Mappings (functions) **swp** and **max** operate on the level
of sets: The set of all pairs Z [2] = Z×Z and the set of triples Z [3] = Z×Z×Z.
The function **swp** maps the set Z [2] into itself, while the function **max**
maps the set Z [3] into Z.


_pair_ :
**swp** ( _n,m_ ) = ( _m,n_ ) _._


Given the set Z of whole numbers, we can create the set of all possible
_ordered pairs_ ( _n,m_ ). This set can be denoted as follows:


(Z _,_ Z) or Z × Z _._


The latter notation is standard in mathematics, but the former way
of writing is also acceptable. We can similarly denote the set of all _ordered_
_triples_ :
(Z _,_ Z _,_ Z) or Z × Z × Z _._


With the notation introduced above, the action of functions with
multiple inputs or outputs can be depicted on the level of sets. Figure
7.2(b) shows how this works for the functions **swp** and **max** .


Solutions                               - **153**


_Exercise 2.2_


Consider a binary function that accepts a pair of natural numbers and
returns the third natural number in the following way:


**rep** 32 = 33 **rep** 14 = 1111 _._


Thus, the output is a natural number with identical digits given by the
first number, repeated a number of times specified by the second number.
Infix variant of this operation can be written, rather arbitrarily, like
this:

**rep** _nm_ = _n_ � _m_ = _nnn...n._


_Exercise 2.3_


A linear function _f_ must satisfy the linearity condition


_f_ ( _a_ ∗ _n_ ) = _a_ ∗( _f n_ ) _._


For _a_ = 0 we must have


_f_ (0 ∗ _n_ ) = 0 ∗( _f n_ ) _,_


or, equivalently
_f_ 0 = 0 _._


Also, for _a_ = _m_ and _n_ = 1 we must have


_f_ ( _m_ ∗ 1) = _m_ ∗( _f_ 1) _,_


from which follows
_f m_ = _m_ ( _f_ 1) _._


_Exercise 2.4_


The schematics in Figure 7.3(a) and (b) demonstrate the two linearity
requirements.


_Exercise 2.5_


Using Einstein’s summation rule, a polynomial of degree _n_ can be written
as follows:
_Pn x_ = _aix_ _[i]_ _,_ _i_ = 0 _,_ 1 _,_ 2 _...,n._


**154** - Tensors For Inquiring Minds


Figure 7.3 The linearity conditions can be represented schematically
with different relative configurations (order) of the “boxes.”


_Exercise 2.6_


The expression
_biyi,_ _i_ = 1 _,_ 2 _,_ 3 _,_ 4


represents the sum of four terms:


_S_ = _b_ 1 _y_ 1 + _b_ 2 _y_ 2 + _b_ 3 _y_ 3 + _b_ 4 _y_ 4 _._


Similarly,
_bjyj,_ _j_ = 1 _,_ 2 _,_ 3 _,_ 4


stands for the same sum _S_, just as the expression


_bkyk_ = _b_ 1 _y_ 1 + _b_ 2 _y_ 2 + _b_ 3 _y_ 3 + _b_ 4 _y_ 4 _._


Solutions - **155**



_Exercise 2.7_


In the expression

( _aixi_ )( _ajxj_ )


both parentheses contain the identical sum:


_aixi_ = _ajxj_ = _a_ 1 _x_ 1 + _a_ 2 _x_ 2 _._


Opening the parentheses, we obtain



( _aixi_ )( _ajxj_ ) = _a_ [2] 1




[2] 1 _[x]_ [2] 1




[2] 1 [+] _[ a]_ [2] 2




[2] 2 _[x]_ [2] 2



2 [+][ 2] _[a]_ [1] _[a]_ [2] _[x]_ [1] _[x]_ [2] _[.]_



In contrast, the expression _a_ [2] _i_




[2] _i_ _[x]_ [2] _i_



_i_ [stands for]



_a_ [2]




[2] _i_ _[x]_ [2] _i_




[2] _i_ [=] _[ a]_ [2] 1




[2] 1 _[x]_ [2] 1




[2] 1 [+] _[ a]_ [2] 2




[2] 2 _[x]_ [2] 2



2 _[.]_



Clearly,


_Exercise 2.8_



_a_ [2]




[2] _i_ _[x]_ [2] _i_




[2] _i_ [≠(] _[a][i][x][i]_ [)][2] _[.]_



The left-hand side of the expression


( _aixi_ ) [2] = _[b][j][y][j]_

_ckck_


can be written as



_i_ = _N_

( _aixi_ ) [2] ∑
= ( _i_ =1


The right-hand side takes the form:



2


_aixi_
)



_bjyj_

_ckck_



_j_ = _N_

∑
_j_ =1


=

_k_ = _N_

∑
_k_ =1



_bjyj_


_ckck_



_._



Therefore, the original equality can be re-written using the traditional
summation sign:

_j_ = _N_



_bjyj_


_ckck_



(



_aixi_
)



_i_ = _N_

∑
_i_ =1



2



=



∑
_j_ =1


_k_ = _N_

∑
_k_ =1



_._



Already one can see the advantage of Einstein’s summation rule.


**156** - Tensors For Inquiring Minds


_Exercise 2.9_


The expression

_δ_ 1 _iai,_ _i_ = 1 _,_ 2 _,_ 3 _,_ 4


represents the sum


_δ_ 11 _a_ 1 + _δ_ 12 _a_ 2 + _δ_ 13 _a_ 3 + _δ_ 14 _a_ 4 _._


The only non-zero term corresponds to _δ_ 11 = 1, therefore


_δ_ 1 _iai_ = _a_ 1 _._


Similarly, we have


_δ_ 3 _kak,_ _k_ = 1 _,_ 2 _,_ 3 _,_ 4


representing

_δ_ 31 _a_ 1 + _δ_ 32 _a_ 2 + _δ_ 33 _a_ 3 + _δ_ 34 _a_ 4 = _δ_ 33 _a_ 3 _._


Consequently,

_δ_ 3 _kak_ = _a_ 3 _._


Next,


_ϵ_ 1 _jaj_ = _ϵ_ 11 _a_ 1 + _ϵ_ 12 _a_ 2 + _ϵ_ 13 _a_ 3 + _ϵ_ 14 _a_ 4


can be simplified to


_ϵ_ 1 _jaj_ = _a_ 2 + _a_ 3 + _a_ 4


using the definition of _ϵij_ .

Finally, the expression


_ϵ_ 3 _jaj_ = _ϵ_ 31 _a_ 1 + _ϵ_ 32 _a_ 2 + _ϵ_ 33 _a_ 3 + _ϵ_ 34 _a_ 4


is reduced to


_ϵ_ 3 _jaj_ = _a_ 4 − _a_ 1 − _a_ 2 _._


_Exercise 2.10_


The sum


_ai_ + _aj_


can be rewritten using the facts _aj_ = _δjiai_ and _δij_ = _δji_ :


_ai_ + _aj_ = _ai_ + _δijai_ = (1 + _δij_ ) _ai_ = (1 + _δji_ ) _ai._


Solutions                               - **157**


_Exercise 2.11_


(a) The expression _δijaibj_ can be simplified using the fact _δijbj_ = _bi_ :


_δijaibj_ = _aibi_ = _a_ 1 _b_ 1 + _a_ 2 _b_ 2 _._


(b) Fully writing out _ϵijaibj_ results in


_ϵ_ 11 _a_ 1 _b_ 1 + _ϵ_ 12 _a_ 1 _b_ 2 + _ϵ_ 21 _a_ 2 _b_ 1 + _ϵ_ 22 _a_ 2 _b_ 2 _._


From the definition of _ϵij_ follows that only the terms with _i_ ≠ _j_ survive:


_ϵijaibj_ = _a_ 1 _b_ 2 − _a_ 2 _b_ 1 _._


_Exercise 2.12_


(a) Firstly, we can recall that when _δij_ is summed with a vector _aj_ it
simply “renames” the index that is being used for summation:


_δijaj_ = _ai._


Using this property, we immediately get


_δijδjk_ = _δik._


Another – and longer – way to get this result is to write out the summation fully:

_δijδjk_ = _δi_ 1 _δ_ 1 _k_ + _δi_ 2 _δ_ 2 _k_ + _..._ + _δinδnk._


If _i_ ≠ _k_, all terms on the right are zero. Indeed, _δi_ 1 _δ_ 1 _k_ is zero unless _i_ = 1
and _k_ = 1; similarly, _δi_ 2 _δ_ 2 _k_ is zero unless _i_ = 2 and _k_ = 2 and so on.
Therefore, the only non-zero value for _δijδjk_ is when _i_ = _k_ . Let _i_ = _k_ = _m_,
then in the sum


_δm_ 1 _δ_ 1 _m_ + _δm_ 2 _δ_ 2 _m_ + _..._ + _δmmδmm_ + _..._ + _δmnδnm._


there is only one non-zero term, namely


_δmmδmm_ = 1 ⋅ 1 = 1 _._


Summarizing the above arguments, we conclude that


_δijδjk_ = 1 if _i_ = _k_ and 0 otherwise _._


This is equivalent to the expression


_δijδjk_ = _δik._


**158** - Tensors For Inquiring Minds


(b) The expression _ϵijϵjk_, when fully expanded as a sum, takes the form


_ϵijϵjk_ = _ϵi_ 1 _ϵ_ 1 _k_ + _ϵi_ 2 _ϵ_ 2 _k._


If _i_ = _k_ = 1, the sum is reduced to


_ϵ_ 1 _jϵj_ 1 = _ϵ_ 11 _ϵ_ 11 + _ϵ_ 12 _ϵ_ 21 = 1 ⋅(−1) = −1 _._


Similarly, for _i_ = _k_ = 2 we get


_ϵ_ 2 _jϵj_ 2 = _ϵ_ 21 _ϵ_ 12 + _ϵ_ 22 _ϵ_ 22 = (−1) ⋅ 1 = −1 _._


On the other hand, if _i_ = 1 and _k_ = 2, we obtain


_ϵ_ 1 _jϵj_ 2 = _ϵ_ 11 _ϵ_ 12 + _ϵ_ 12 _ϵ_ 22 = 0 _._


Same for _i_ = 2 and _k_ = 1:


_ϵ_ 2 _jϵj_ 1 = _ϵ_ 21 _ϵ_ 11 + _ϵ_ 22 _ϵ_ 21 = 0 _._


We thus manually checked all cases and showed that


_ϵijϵjk_ = − _δik_ _i,j,k_ = 1 _,_ 2 _._


_Exercise 2.13_


Let us denote:


_x_ = _ϵijaiaj._


Since we can rename the summation indices, we can write


_ϵijaiaj_ = _ϵikaiak_ = _ϵjkajak_ = _ϵjiajai._


Now we have _ϵji_ = − _ϵij_ and this leads to


_ϵjiajai_ = − _ϵijaiaj._


We thus showed that _x_ = − _x_ and therefore _x_ = 0.


_Exercise 3.1_


→

An expansion of an arbitrary vector _a_ in terms of the basis vectors is

given by



→
_a_ = _a_ 1



→
_e_ 1 + _a_ 2



→
_e_ 2 + _a_ 3



→
_e_ 3 + _...an_



→
_e_ _n._



This can be compactly written using Einstein’s summation rule:



→
_a_ = _ai_



→
_e_ _i_ _i_ = 1 _,_ 2 _,...,n._



If the number of basis vectors is known and fixed, as is usually the case,
we can omit the range of the summation index and simply write



→
_a_ = _ai_



→
_e_ _i._


Solutions - **159**



_Exercise 3.2_


The expression



→ _e_ ′1 [=] _[ E]_ [11]



→ _e_ ′



→ _e_ 1 + _E_ 12



→
_e_ 2 _,_



can be written using Einstein’s summation rule as follows:



→ _e_ ′1 [=] _[ E]_ [1] _[j]_ → _e_ _j._



Similarly for the second basis vector:


→ _e_ ′2 [=] _[ E]_ [2] _[j]_ → _e_ _j._


Combining both results, we obtain



→ _e_ ′ _i_ [=] _[ E][ij]_ → _e_ _j._



_Exercise 3.3_


(a) Writing the expansion of the “new” basis as follows:



→ _e_ ′1 [=] _[ µ]_



→ →
_e_ 1 + 0 _e_ 2 _,_



→
_e_ 1 + 0



→ _e_ ′



→
_e_ 1 + _ν_



2 [=][ 0]



→
_e_ 2 _,_



we can immediately find the components _Eij_ :


_E_ 11 = _µ, E_ 12 = 0 _, E_ 21 = 0 _, E_ 22 = _ν._



We note that the “new” basis vectors are simply scaled versions of the
“old” ones: → _e_ ′ → _e_ ≠



“old” ones: → _e_ ′ _i_ [is parallel to] → _e_ _i_ but may have different lengths (if _µ,ν_ ≠ 1).

(b) The simple relations between the “new” and “old” basis vectors allow
us to find



→ _e_ ′



_i_ [is parallel to]



→ _e_ ′1 [/] _[µ]_



→ _e_ ′2 [/] _[ν.]_



and


If the vector



→
_a_ is expanded using the “old” basis:



→
_e_ 1 =


→
_e_ 2 =



→
_a_ = _a_ 1



→
_e_ 1 + _a_ 2



→
_e_ 2 _,_



then we can write



→ ′
_a_ = ( _a_ 1 [/] _[µ]_ [)]



→ _e_ ′



1 [+ (] _[a]_ [′] 2




[′] 2 [/] _[ν]_ [)]



→ _e_ ′2 _[,]_


**160** - Tensors For Inquiring Minds


and immediately find



_a_ [′]




[′] 1 [=] _[ a]_ [1][/] _[µ,]_ _a_ [′]




[′] 2 [=] _[ a]_ [2][/] _[ν.]_



Therefore, when the “new” basis vectors are scaled by factors _µ_ and _ν_,
the corresponding “new” components of the vectors are scaled by 1/ _µ_ and
1/ _ν_ – _in the opposite direction_, to counter the effect of basis variation.
The arrow-like vectors are thus called _contravariant vectors_ .


_Exercise 3.4_


The compact expression

_E_ [′]

_ij_ _[E][jk]_


for _i_ = 1 and _k_ = 2 can be expanded into a sum:



_E_ [′]



1 [′] _j_ _[E][j]_ [2] [=] _[ E]_ [′]



11 [′] _[E]_ [12] [+] _[ E]_ [′]



12 _[E]_ [22] _[.]_



_Exercise 3.5_


The system of four equations


_aw_ + _cx_ = 1 _,_ (7.1)


_bw_ + _dx_ = 0 _,_ (7.2)


_ay_ + _cz_ = 0 _,_ (7.3)


_by_ + _dz_ = 1 (7.4)


can be solved by noticing that the first two equations do not involve the
unknowns from the second pair of equations, and vice versa.

From the equation

_bw_ + _dx_ = 0


we first find _w_ = − _dx_ / _b_ and substitute it into the first equation:


− _adx_ / _b_ + _cx_ = 1 _,_


from which we easily find


_b_
_x_ =
_cb_ − _ad_ [= −] ∆ _[b]_ _[,]_


where we introduced the notation ∆ = _ad_ − _bc_ . Then



_w_ = − _[dx]_




_[d]_
_b_ [=] ∆



∆ _[.]_


Solutions                               - **161**


The second pair of equations can be solved similarly. First, we get


_z_ = − _[a][y]_

_c_ _[,]_


and substitute it into the last of four equations:


_by_ − _[ad][y]_ = 1 _._

_c_


From the last expression follows


_y_ = − _[c]_

∆ _[.]_



Consequently,


_Exercise 3.6_



_z_ = _[a]_

∆ _[.]_



Firstly, we start with the compact expression


_EijEjk_ [′] [=] _[ δ][ik]_


and write it out fully for all four combinations of the indices _i_ and _k_ :



_E_ 11 _E_ [′]


_E_ 11 _E_ [′]


_E_ 21 _E_ [′]


_E_ 21 _E_ [′]



11 [′] [+] _[ E]_ [12] _[E]_ [′]

12 [′] [+] _[ E]_ [12] _[E]_ [′]

11 [′] [+] _[ E]_ [22] _[E]_ [′]

12 [′] [+] _[ E]_ [22] _[E]_ [′]



21 = 1 _,_

22 [′] = 0 _,_

21 [′] = 0 _,_

22 [′] = 1 _._



Secondly, using the notation


_E_ 11 = _a,_ _E_ 12 = _b,_ _E_ 21 = _c,_ _E_ 22 = _d,_


and



_E_ [′]



11 [′] [=] _[ w,]_ _E_ [′]



12 [′] [=] _[ x,]_ _E_ [′]



21 [′] [=] _[ w,]_ _E_ [′]



22 [=] _[ z,]_



we arrive at the four equations which we can group into two pairs of
equations, each pair involving only two unknowns. The first pair is


_aw_ + _by_ = 1 _,_


_cw_ + _dy_ = 0;


**162** - Tensors For Inquiring Minds


the second pair:


_cx_ + _dz_ = 1 _,_


_ax_ + _bz_ = 0 _._


The first pair is easily solved when we find


_w_ = − _[d][y]_

_c_ _[,]_


and substitute it into the first equation of the first pair:


− _[ad][y]_ + _by_ = 1 _,_

_c_



from which follows:


Immediately we get


Similarly, we first find



_y_ = − _[c]_ ∆ = _ad_ − _bc._

∆


_w_ = _[d]_

∆ _[.]_



_z_ = − _[ax]_

_b_ _[,]_


and substitute into the first equation of the second pair:


_cx_ − _[adx]_ = 1 _._

_b_



Solving for _x_, we get


and therefore



_x_ = _[b]_

∆ _[,]_


_z_ = _[a]_

∆ _[.]_



We conclude that although two conditions _E_ [′]




[′]

_ij_ _[E][jk]_ [ =] _[ δ][ik]_ [ and] _[ E][ij][E]_ [′]



_ij_ _[jk]_ [ =] _[ik]_ _[ij]_ _jk_ [=]

_δik_ result in slightly different equations, they put the same constraints on
the relations between the coefficients _Eij_ ( _a,b,c,d_ ) and _Enm_ [′] [(] _[w,x,y,z]_ [)][.]



_nm_ [′] [(] _[w,x,y,z]_ [)][.]


Solutions                               - **163**


_Exercise 4.1_


The equation of a circle with the radius _R_ can be written using Cartesian
coordinates:

_x_ [2] + _y_ [2] = _R_ [2] _._


The transformation


_b_ 1 = _a_ 1 + _a_ 2 _,_ _b_ 2 = _a_ 1 ∗ _a_ 2


moves every point ( _x,y_ ) into a new point ( _x_ [′] _,y_ [′] ) related by the same
equations:

_x_ [′] = _x_ + _y,_ _y_ [′] = _xy._


Squaring _x_ [′], we get


( _x_ [′] ) [2] = _x_ [2] + _y_ [2] + 2 _xy_ = _R_ [2] + 2 _y_ [′] _._


Therefore, the components of the transformed vector are related as follows:

_y_ [′] = ( _x_ [′] ) [2] /2 − _R_ [2] /2 ⇔ _b_ 2 = _b_ [2] 1 [/][2][ −] _[R]_ [2][/][2] _[.]_


_Exercise 4.2_


The operator of the normalization _N_ [̂] fails to satisfy the first linearity
condition because



→
_a_ ) _._



_N_ ̂ ( _α_



→ _a_ ) ≠ _α_ ( ̂ _N_



→

Indeed, the left-hand side must be a unit vector in the direction of _αa_,

→

which is the same as the direction of _a_ :



Indeed, the left-hand side must be a unit vector in the direction of _α_



→

_a_ :



_N_ ̂ ( _α_ → _a_ ) =



→ _ua_ = ̂ _N_



→

_a._



In addition, the operator _N_ [̂] does not satisfy the second linearity condi
tion:



→



→

_b_ ) = ( _N_ [̂]


→



→ _a_ ) + ( ̂ _N_



→

_b_ ) _._



_N_ ̂ (



→
_a_ +



→
_e_ 1 and



_b_ = 1000



→
_e_ 2. The sum-vector



→
_a_ +



Take, for instance,



→

_a_ =



Take, for instance, _a_ = _e_ 1 and _b_ = 1000 _e_ 2. The sum-vector _a_ + _b_ will be

→

pointing almost along the second basis vector _e_ 2, therefore



→
_e_ 2, therefore



→ →
_e_ 1 + 1000 _e_ 2)



→
_e_ 1 + 1000



_N_ ̂ (



will be a unit vector _almost parallel_ to



→
_e_ 2. However, the vector



→
_e_ 1 +



→
_e_ 2



( _N_ [̂]



→ _e_ 1) + ( ̂ _N_ [1000→ _e_ 2]) =



→
_e_ 2.



will go diagonally between



→
_e_ 1 and


**164** - Tensors For Inquiring Minds


_Exercise 4.3_


The condition for the degeneracy of a linear operator can be written as
follows:



→ _e_ 1 = _λ_ _L_
(̂



_L_ ̂



→
_e_ 2 _._
)



For simplicity, let us denote



→ _v_ = ̂ _L_ → _e_ 2. Then we have



→
_e_ 1 = _λ_



_L_ ̂



→

_v._



→

For an arbitrary vector _a_ we can find the action of the degenerate

linear operator _L_ [̂]



→
_e_ 1 + _a_ 2



→ _e_ 2) = _a_ 1(̂ _L_



→ _e_ 1) + _a_ 2(̂ _L_



→
_e_ 2) _._



_L_ ̂



→ _a_ = ̂ _L_ ( _a_ 1



Now we can use the degeneracy condition to find



→ →
_v_ + _a_ 2 _v_ = ( _a_ 1 _λ_ + _a_ 2)



→ →

_v_ = _αv._



_L_ ̂



→
_a_ = _a_ 1 _λ_



→ →

Thus, any vector _a_ is mapped into a vector parallel to _v_ . In other words,

the degenerate linear operator “collapses” all vectors onto a single line.



Thus, any vector



→
_a_ is mapped into a vector parallel to



_Exercise 4.4_


The relation



_L_ ̂ → _a_ =



→

_b_



→ _e_ ′



can be written using components relative to the “new” basis {



can be written using components relative to the “new” basis { _e_ ′ _i_ [}][. Ex-]


→

panding the vector _a_, we get:



→
_a_, we get:



→ _e_ ′




[′] _i_ [(̂] _[L]_



_L_ ̂ ( _a_ [′] _i_



_L_ ̂ ( _a_ [′] _i_



′ _i_ [) =] _[ a]_ [′] _i_



→ _e_ ′ _i_ [)] _[.]_



Now the components of the operator _L_ [̂] relative to the “new” basis are
defined similarly to the components relative to the “old” basis:



→ _e_ ′



_ij_



_L_ ̂



_i_ [=] _[ L]_ [′]



→ _e_ ′ _j_ _[.]_



→ _e_ ′



Combining the last two expressions, we obtain



→ ′
_a_ = ( _ai_




[′]

_ij_ [)]



_L_ ̂



′

_i_ _[L]_ [′]



→ _e_ ′ _j_ _[,]_



→ _e_ ′



where we indicated that the summation with the components of the

→

vector _a_ happens first. Comparing this result with the expansion of the



vector



→

_b_ relative to the “new” basis


→



→ _e_ ′ _j_ _[,]_



→ _e_ ′



_b_ = _b_ [′]

_j_



we can see that the following relation holds



_a_ [′]




[′] _i_ _[L]_ [′]




[′] _ij_ [=] _[ b]_ [′]



_j_ _[.]_


Solutions - **165**



_Exercise 4.5_


To evaluate the right-hand side of the expression



_L_ 11 + _L_ 22 = _L_ [′]




[′] 11 [+] _[ L]_ [′]



22 _[,]_



we need to recall to rule of transformation of components of the linear

operator:



_L_ [′]




[′] _mj_ [=] _[ E][mk][L][ki][E]_ _ij_ [′]



_ij_ _[.]_



Using the last expression we can write



_L_ [′]




[′] 11 [=] _[ E]_ [1] _[k][L][ki][E]_ _i_ [′]



_i_ [′] 1 [= (] _[E]_ _i_ [′]



_i_ [′] 1 _[E]_ [1] _[k]_ [)] _[L][ki]_



and



_L_ [′]




[′] 22 [=] _[ E]_ [2] _[k][L][ki][E]_ _i_ [′]



_i_ [′] 2 [= (] _[E]_ _i_ [′]



_i_ [′] 2 _[E]_ [2] _[k]_ [)] _[L][ki][.]_



Summing up, we obtain



_L_ [′]




[′] 11 [+] _[ L]_ [′]




[′] 22 [= (] _[E]_ _i_ [′] 1



_i_ [′] 1 _[E]_ [1] _[k]_ [+] _[ E]_ _i_ [′]



_i_ [′] 2 _[E]_ [2] _[k]_ [)] _[L][ki][.]_



The sum in the parentheses can be made more compact using Einstein’s
summation rule:



_E_ [′]



_i_ [′] 1 _[E]_ [1] _[k]_ [+] _[ E]_ _i_ [′]



_i_ [′] 2 _[E]_ [2] _[k]_ [=] _[ E]_ [′]



_ij_ _[E][jk][.]_



We showed that


therefore


_Exercise 5.1_



_Eij_ [′] _[E][jk]_ [=] _[ δ][ik][,]_



_L_ [′]




[′] 11 [+] _[ L]_ [′]



22 [=] _[ δ][ik][L][ki]_ [=] _[ L][ii]_ [=] _[ L]_ [11] [+] _[ L]_ [22] _[.]_



The operator ∠ is not linear in either of its arguments. Indeed, scaling
the first argument by an arbitrary factor _α_ does not affect the measured
angle:



→

_b_ ≠ _α_ (∠



→

_a_



→

∠( _αa_ )



→ →

_b_ = ∠ _a_



→

_b_ ) _._



Same applies to the second argument.


**166** - Tensors For Inquiring Minds


_Exercise 5.2_


Components of any linear operator are defined as the coefficients in the
expansion



_L_ ̂



→ _e_ _i_ = _Lij_ → _e_ _j._



For the potential operator _β_ [̂] this means



_β_ ̂



→
_e_ _j_ = _ai_ ( _bj_



→
_e_ _i_ = ( _aibj_ )



→
_e_ _j_ ) = _ai_



→

_b._



Thus, the operator _β_ [̂] maps all basis vectors into vectors parallel to

→



_b_ = _b_
_j_



→ _e_ _j_ . Consequently, the operator ̂ _β_ maps _all_ vectors into the same


→



direction parallel to the vector _b_ . It is an example of a _degenerate linear_

_operator_ . See also Exercise 4.3.


_Exercise 5.3_


By definition



← _a_ = ̂ _σ_



→ _a_ = ̂ _σ_ ( _a_ 1→ _e_ 1 + _a_ 2



→
_e_ 2) _._



Using the linearity of ̂ _σ_, we first write



→
_e_ 1 + _a_ 2



→
_e_ 1)] + [̂ _σ_ ( _a_ 2



→
_e_ 2)] _._



̂ _σ_ ( _a_ 1



→
_e_ 2) = [̂ _σ_ ( _a_ 1



Using the linearity again, we get



→
_e_ 1) = _a_ 1(̂ _σ_



←
_e_ 1



̂ _σ_ ( _a_ 1



→
_e_ 1) = _a_ 1



and


which lead to



→
_e_ 2) = _a_ 2(̂ _σ_



̂ _σ_ ( _a_ 2



→
_e_ 2) = _a_ 2



← _a_ = ̂ _σ_ ( _a_ 1



→
_e_ 1 + _a_ 2



→
_e_ 2) = _ai_



←
_e_ 2 _,_


←
_e_ _i._



→

We showed that the vector conjugate to _a_ can be expanded in terms of

→

basis conjugate to _e_ _i_ .



We showed that the vector conjugate to



→
_e_ _i_ .



_Exercise 5.4_


The determinant of a linear operator _L_ [̂] can be calculated from its components according to:


_det_ _L_ [̂] = _L_ 11 _L_ 22 − _L_ 12 _L_ 21 _._


Solutions - **167**



For a projector _A_ [̂] we have




[2] 1 _[a]_ [2] 2



_A_



~~1~~ 1 _[A]_



~~2~~ 2 [=] _[ a]_ [1] _[a]_ _a_ [1] _[a]_ [4] [2] _[a]_ [2]




[1] _[a]_ [2] _[a]_ [2] 1

= _[a]_ [2]
_a_ [4] _a_



1 2

_a_ [4]



and




[2] 1 _[a]_ [2] 2



_A_



~~1~~ 2 _[A]_




_[a]_ [1] _[a]_ [2] _[a]_ [2] _[a]_ [1]
~~2~~ 1 [=] _a_ [4]




[2] _[a]_ [2] _[a]_ [1] 1

= _[a]_ [2]
_a_ [4] _a_



1 2


_[.]_
_a_ [4]



It immediately follows that _det_ _L_ [̂] = 0.

A helpful related exercise is Exercise 5.2.


_Exercise 5.5_


(a) First, we can write symbolically:



→←
_a_ _a_ )

=
_a_ [2]



→
_a_ (



←

_a_



←→ ←
_a_ _a_ ) _a_


_,_
_a_ [4]



→
_a_ )



_A_ ̂ - ̂ _A_ = [(]



→←
_a_ _a_ ) (


_a_ [2]



→ 2
_a_ = _a_ is reduced to



which, using the fact



←

_a_



̂
_A_ - ̂ _A_ =



→←
_a_ _a_ _[A.]_ [̂]

[=]
_a_ [2]



Second, using components, we write the product of two operators as
follows:



( _A_



_._

~~_i_~~ _j_ [)][(] _[A]_ ~~_j_~~ _k_ [) =] _[ a][i][a]_ _a_ _[j][a]_ [4] _[j][a][k]_



Recalling that _ajaj_ = _a_ [2], we find



( _A_



~~_i_~~ _j_ [)][(] _[A]_



= _A_

~~_j_~~ _k_ [) =] _[ a]_ _a_ _[i][a]_ [2] _[k]_ ~~_i_~~



~~_i_~~ _k_ _[.]_



←



Every projector of the type _L_ = _d_ _d_ / _d_ [2] has this property.

(b) For a composition of two projectors



Every projector of the type _L_ =



→

_d_



_L_ ̂ = _B_ ̂           - ̂ _A_


the components are given by


_Lik_ = _λaibk,_ _λ_ =



→ →
_a_ ⋅ _b_


_[.]_
_a_ [2] _b_ [2]


**168** - Tensors For Inquiring Minds


Composition of two such operators can be evaluated using their compo
nents:


→



_b_ ) _aibj._



_LikLkj_ = ( _λaibk_ )( _λakbj_ ) = _λ_ [2] _ai_ ( _akbk_ ) _bj_ = _λ_ [2] (


We thus showed that


→



→

_a_ ⋅



_L_ ̂ ○̂ _L_ = _λ_ (



→

_a_ ⋅


→



_b_ ) _L._ [̂]



Now



_b_ ) [2]



→

_a_ ⋅



= cos _θ,_
_a_ [2] _b_ [2]



→

_b_ ) = [(]



_λ_ (



→

_a_ ⋅



→

_b_ . Therefore,



where _θ_ is the angle between the vectors



→
_a_ and



_L_ ̂ ○̂ _L_ = cos _θL_ ̂ ≠̂ _L._


→ _b_ we have the property _L_ [̂] - _L_ [̂] = _L_ [̂] .



Only for



→

_a_ =



_Exercise 5.6_


The components of the composition


_L_ ̂ = _B_ ̂           - ̂ _A._


are


_Lik_ = _λaibk,_ _λ_ =



→ →
_a_ ⋅ _b_


_[.]_
_a_ [2] _b_ [2]



Reversing the order of arguments of the composition results in


̂
_M_ = _A_ [̂]        - _B_ [̂] _,_


with the components


→



_Mik_ = _λbiak,_ _λ_ =


In general, _M_ 12 ≠ _L_ 12 because _a_ 1 _b_ 2 ≠ _b_ 1 _a_ 2.



→

_b_ ⋅ _a_


_[.]_
_a_ [2] _b_ [2]


Solutions                               - **169**


_Exercise 5.7_


To arrive at the transformation rules for the components of different
types of tensors, we will use a simple fact: A general tensor with components _t_ _[ij]_ will behave just like the tensor product of two contra-variant
vectors _a_ _[i]_ _b_ _[j]_ . Thus, we will study four types of tensor products:


_a_ _[i]_ _b_ _[j]_ _,_ _aibj,_ _a_ _[i]_ _bj,_ _aib_ _[j]_ _._


It will be helpful to recall the transformation rules of contravariant and covariant vectors. An arrow-like contravariant vector can be

expanded in a basis:

→ _i_ →
_a_ = _a_ _e_ _i._


Every vectors from a “new” basis can be similarly expanded:



→ _e_ ′



_j_ 


_j_ [=] _[ E]_ _j_ [ ●] - _[k]_



→
_e_ _k._



Here we deliberately included the “dummy” symbol “ ● ” to visually align

→

the indices according to their order. Expanding the same vector _a_ rela
tive to the “new” basis has the form:



→ ′ _i_ →
_a_ = _a_ _e_ ′ _i_ _[,]_



and similarly



→ _i_ →
_a_ = _a_ _e_ _i._


→ _e_ _k_ = ( _E_ ′) ● _k_ - _j_ → _e_ _j._



We also obtained the relation between the components of the same vector
→
_a_ in different bases:

_a_ [′] _[i]_ = ( _E_ [′] ) _k_ [●]             - _[i]_ _[a][k][.]_


Another contravariant vector will have similar relations:


_b_ [′] _[j]_ = ( _E_ [′] ) _l_ [●]                - _[j][b][l][,]_


and their tensor product _t_ _[ij]_ = _a_ _[i]_ _b_ _[j]_ will be transformed according to



_k_ [●] - _[i]_ [(] _[E]_ [′][)][ ●] _l_ _[j]_



( _t_ [′] ) _[ij]_ = ( _E_ [′] ) _k_ [●] - _[i]_




[ ●] _l_ - _[j][t][kl][.]_



Using the transformation rule of covariant components:




[′] _i_ [=] _[ E]_ _i_ [ ●] - _[k]_




[′] _j_ [=] _[ E]_ _j_ [ ●] - _[l]_



_a_ [′]



_i_ [ ●] - _[a][k]_ and _b_ [′]



_j_ [ ●] - _[b][l][,]_


**170** - Tensors For Inquiring Minds


we immediately arrive at transformation rule of the components of a
doubly-covariant tensor:




[′] _ij_ [=] _[ E]_ _i_ [ ●]  - _[k]_



_j_ [ ●] - _[t][kl][.]_



_t_ [′]



_i_ [ ●] - _[k][E]_ [ ●] - _[l]_



In a similar fashion, by combining the transformation rules of contravariant and covariant vectors, we can obtain the transformation of contra
covariant tensor:




- _l_ _[,]_



( _t_ [′] ) _[i]_ - [ ●]




_[i]_ - [ ●] _j_ [= (] _[E]_ [′][)][ ●] _k_ - _[i]_




[ ●] _k_ - _[i]_ _[E]_ [ ●] - _[l]_



_j_ [ ●] - _[l]_ _[t][k]_ - [ ●] _l_



and covariant-contravariant tensor:



( _t_ [′] ) _i_ [●] - _[j]_



_i_ [ ●] - _[k]_ [(] _[E]_ [′][)][ ●] _l_ _[j]_



_k_ - _[.]_



_i_ [●] - _[j]_ [=] _[ E]_ _i_ [ ●] - _[k]_




[ ●] _l_ - _[j][t]_ _k_ [ ●] - _[l]_



_Exercise 6.1_



→



(a) The action of the metric tensor on a tensor product



→
_a_ ⊗



(a) The action of the metric tensor on a tensor product _a_ ⊗ _b_ can be

understood once we write it out using components. First, let’s write the
expression for the distance squared:



_d_ [2] = _ηijd_ _[i]_ _d_ _[j]_ _._


In a similar way, we can write


→



_η_ ̂ (→ _a_ ⊗



_b_ ) = _ηija_ _[i]_ _b_ _[j]_ _._



Using the fact



→
_e_ _j_



_ηij_ = ̂ _σ_



→
_e_ _i_



and bilinear nature of the dol-operator ̂ _σ_, we deduce



→
_e_ _i_



→

_b._



_ηija_ _[i]_ _b_ _[j]_ = _a_ _[i]_ _b_ _[j]_ (̂ _σ_


Thus, we showed that



→ _i_ → _j_ → →
_e_ _j_ ) = ̂ _σ_ ( _a_ _e_ _i_ )( _b_ _e_ _j_ ) = ̂ _σ_ _a_



→ _i_ → _j_ →
_e_ _j_ ) = ̂ _σ_ ( _a_ _e_ _i_ )( _b_ _e_ _j_ ) = ̂ _σ_



→

_b._



_η_ ̂ (→ _a_ ⊗



→ →

_b_ ) = _a_ ⋅



The connection between the metric tensor and scalar products is not


→

surprising. Indeed, if we recall that if vector _d_ connects two points in a

plane and is given by



→ →

_d_ = _b_ −



→
_a,_ _d_ _[i]_ = _b_ _[i]_ − _a_ _[i]_ _,_



then



_ηijd_ _[i]_ _d_ _[j]_ = _ηij_ ( _a_ _[i]_ − _b_ _[i]_ )( _a_ _[j]_ − _b_ _[j]_ ) = _ηija_ _[i]_ _a_ _[j]_ + _ηijb_ _[i]_ _b_ _[j]_ + 2 _ηija_ _[i]_ _b_ _[j]_ _._


Solutions                               - **171**


We arrived at the familiar theorem of planar geometry – theorem of

cosine:

_d_ [2] = _a_ [2] + _b_ [2] − 2 _ab_ cos _θ._


(b) Vectors of orthonormal basis all have unit lengths ( _normalized_ vectors):



→ _e_ _i_ = _ηii_ = 1 _._



_e_ [2] _i_ [= ̂] _[σ]_



→
_e_ _i_



Different vectors of orthonormal basis are perpendicular to each other
( _orthogonal_ vectors):



→
_e_ _i_ ⋅



→ →
_e_ _j_ = ̂ _σ_ _e_ _i_



→
_e_ _j_ = _ηij_ = 0 _._



We showed that


when the basis is orthonormal.



_ηij_ = _δij_


### Index

Abstraction, xiii, 2, 4, 13
Action quantum, 146
Algebra, 33
Argument, 15
Arrow

addition, 46
product, 48
representation, 50
Arrows, 44

independent, 50


Barrier

mental, xiii
terminology, 14
Basis, 50

conjugate, 98
new, 52
old, 52
orthonormal, 60, 120


Category theory, 33
Commutativity, 27, 90
Composition, 8

of operators, 135
of operators, 109
Conjugate, 95, 97

vector, 97
Coordinate

system, 5

Cartesian, 133
polar, 120


Determinant, 78
Distributivity, 91



Eigen-value, 77
Einstein, 2

summation rule, 39
Euler’s formula, 136


Field, 14, 32, 115
Function, 15

addition, 26
arity, 19
binary, 18
composition, 26, 33
linear, 23
multilinear, 24
representation, 29
symmetric, 88
unary, 18


General relativity, 3, 123
Grossmann Marcel, 3


Hamiltonian, 140

mechanics, 139
Homomorphism, 115


Kronecker delta, 22, 41, 58


Linearity, 23, 70


Map, 7
Mathematical

object, 4, 61
structure, 6, 9
Matrix, 73, 132


Notation

delta, 118



**173**


**174** - Index


index, 20, 81
infix, 17, 46, 90
prefix, 17
Numbers, 15, 31

complex, 13, 133
compound, 49, 133
real, 46


Ohm’s law, 128
Operator, 1, 61, 63

addition, 97, 101
bilinear, 88
components, 65, 71, 80

transformation, 81, 85
degenerate, 78
determinant, 78
linear, 67, 70, 96
nonlinear, 67
overloading, 47
plotting, 74
projector, 78, 106

components, 108
rotation, 70
trace, 78, 84
unary, 100
Oscillator, 140


Partial application, 28, 95
Partial application, 99
Pauli matrices, 138
Planck constant, 146
Polynomial, 35
Ports, 147
Precedence, 18
Product

inner, 94
tensor, 94


Relations, 6, 15, 35


S-parameter, 147



Schematic, 7
Schr¨odinger equation, 146
Set, 8

Boolean, 7
numeric, 31
State, 139
Structure, 15, 32

algebraic, 33


Tensor, 5, 84

anisotropy, 129
definition, 113
electromagnetic, 130
metric, 119
mobility, 127
product, 92, 108, 111
rank, 2, 94, 116
stress, 125
Transposition, 56
Tuple, 9


Vector, 1

components, 50
contravariant, 54, 103, 104
covariant, 55, 61, 105
definition, 60
eigen, 75, 76
multiplication, 34
normalized, 60
projection, 106
space, 5, 34, 45, 115

dual, 99, 103

Vectors

overlap, 87
scalar product, 90, 93


