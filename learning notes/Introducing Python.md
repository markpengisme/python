## 精通python(oreilly)

### ch1
install python3

### ch2
everything is implemented as an object
- =(use it to assign a value to a variable)
```python
    >>> a=2
    >>> print(a)
    2
```
- type(thing)

- Names cannot begin with a digit. 
    not valid : 1apple
    
- Operator:
```
    +,-,*,
    /(float),//(integer),%(mod),
    **(exponentiation)
    divmod(9,5)=(1,4)
```
- Bases
    0b=binary
    0o=octal
    0x=hex
```python
    >>> a=0b10
    >>> a
    2
```
- String(use single , double or three single quotes enclose)
    '\n' : Begin new line
    '+' : Combine strings
    '*' : Duplicate strings
    '[]' : Extract a Character
    ```python
    >>> letter='qwertyuiop'
    >>> letter[1]
    'w'
    >>> letter[0]
    'q'
    >>> letter[-1]
    'p'
    ```
    '[start,end,step]' :
    ```python
    >>> a='apple'
    >>> a[:]
    'apple'
    >>> a[1:]
    'pple'
    >>> a[:-1]
    'appl'
    >>> a[::2]
    'ape'
    >>> a[::-1]
    'elppa'
    ```
    'len(string)' :  Get Length
    'string.split('sep')' : 
    ```python
    >>> a="aa,bb,cc"
    >>> a.split(',')
    ['aa', 'bb', 'cc']
    ```
    'S.join(iterable)->str' :
    ```python
    >>> b=a.split(',')
    >>> c=','.join(b)
    >>> c
    'aa,bb,cc'
    ```
    'S.title()':Capitalize all the words
    'S.upper()':Convert all characters to uppercase
    'S.lower()':Convert all characters to lowercase
    'S.swapcase()':Swap uppercasee and lowercase
    'S.replace(a,b):Replace a substring with b
    
### ch3
- list=list(),[]
    - Lists of Lists [[ ],[ ]]
    - L.append() : Add an Item to the End
    - L1.extend(L2) : Combine Lists
    - L.insert(index,object) : Insert object before index
    - L.remove(value) : Remove first occurrence of value in L
    - L.pop(index) -> item : remove and return item at index (default last)
    - L.index(value [,start[,stop]]) -> integer : return first index of value
    - L.count(value) -> integer : return number of occurrences of value
    - L.sort(key=None, reverse=False) -> None
    - L.copy() -> list : a shallow copy of L
- tuple=tuple(),()
    - T.count(value) -> integer : return number of occurrences of value
    - T.index(value [,start [,stop]]) -> integer : return first index of value.
- dict=dict(),{key:value,....}
    - D[key] = value : Add or Change an Item by [ key ]
    - D1.update(D2) : Combine two dict
    - D.clear() -> None : Remove all items from D.
    - D.keys() -> a set-like object providing a view on D's keys
    - D.values() -> an object providing a view on D's values
- set=set(),{v1,v2,v3}
    - S1&S2 or S1.intersection(S2) 
    - S1|S2 or S1.union(S2)
    - S1-S2 or S1.difference(S2)
    - S1^S2 or S1.symmetric_difference(S2)
    - S1<=S2 or S1.issubset(S2)
    - S1>=S2 or S1.issuperset(S2)
- del :del L[index],D[index]
- in : value in L,T,D,S
- sorted : sorted(L,T,D,S)
- len : len (L,T,D,S)

### ch4

- #: Comment with #
- \ : Continue Lines with \
- if,elif,else:
    ```python
    if expression :
        suite
    elif expression :
        suite
    else :
        suite
    ```
- comparison operators 
    - ==,!=,>,<,>=,<=,in
- while :Repeat with while
- break,continue:flow control
- for :Iterate with for
    ```
    Pythonic for
    >>> fruits=['apple','banana','orange']
    >>> for fruit in fruits:
    ...     print(fruit)
    ... 
    apple
    banana
    orange
    ```
    ```
    Iterating over a dictionary
    dict.key():return dict keys
    dict.values():return dict values
    dict.items():return dict (key,value) , type is tuple
    ```
- zip():Iterate Multiple Sequences with zip()
    ```python
    >>> a=[i for i in range(10)]
    >>> b=[i for i in range(11,20)]
    >>> c=[i+j for i,j in zip(a,b)]
    >>> a
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> b
    [11, 12, 13, 14, 15, 16, 17, 18, 19]
    >>> c
    [11, 13, 15, 17, 19, 21, 23, 25, 27]    
    ```
- range():Generate Number Sequences with range()
    ```
    range(start,stop,slice)
    ```
- Some pythonic comprehensions
    ```python
    >>> list=[i for i in range(10)]
    >>> list
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]    
    ```
    ```python
    >>> list=[i for i in range(10) if i%2==0]
    >>> list
    [0, 2, 4, 6, 8]
    ```
    ```python
    >>> list=[ (i,j) for i in range(3) for j in range(3) ]
    >>> list
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), 
     (1, 2), (2, 0), (2, 1), (2, 2)]
    ```
    ```python
    >>> word = 'letters'
    >>> letter_counts = {letter: word.count(letter) for letter in set(word)}
    >>> letter_counts
    {'t': 2, 'l': 1, 's': 1, 'r': 1, 'e': 2}
    ```
- Functions:Naming Conventions xxx_xxx separated by underscores
    ```python
    >>> def print_parameter(param):
    ...     print(param)
    ... 
    >>> print_parameter("Hello world")
    Hello world
    ```
    - Specify Default Parameter Values (very useful)
    ```python
    >>> def menu(wine, entree, dessert='pudding'):
    ... return {'wine': wine, 'entree': entree, 'dessert': dessert}
    ```
    
  