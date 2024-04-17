# string-similarity-arraylist

Finds degree of similarity in list of array of objects , array of strings and two stings  based on Dice's Coefficient which is way better than Levenshtein distance.

## Installation

### For Node Js 

```bash
npm install string-similarity-arraylist --save
```

Once the package is installed, you can import the library using import or require approach:

## Usage

```js

const {

    getSimilarityofArrayOfObjects,
    getSimilarityScaleofArrayOfObjects
    getSimilarityOfArrayOfStrings,
    getSimilarityOfTwoString,
    
    } = require('string-similarity-arraylist')

```

or

```js

import { 
    
    getSimilarityofArrayOfObjects ,
    getSimilarityScaleofArrayOfObjects ,
    getSimilarityOfArrayOfStrings,
    getSimilarityOfTwoString 
    
    } from 'string-similarity-arraylist'

```

### For browser apps

Include   ``<script src="//cdn.jsdelivr.net/npm/string-similarity-arraylist/index.min.js"></script>`` to get the latest version.

Or ``<script src="//cdn.jsdelivr.net/npm/string-similarity-arraylist@1.0.1/index.min.js"></script>`` to get a specific version (1.0.1) in this case.

##### This exposes a global variable called getSimilarityofArrayOfObjects , getSimilarityScaleofArrayOfObjects , getSimilarityOfArrayOfStrings , getSimilarityOfTwoString  which you can start using.


```js

    <script>

     const data = getSimilarityofArrayOfObjects({

                             data: Array Of Objects,
                             rawText: String,
                             objectMatchingKeys: Array of Object key,
                             similarityScale: Scale of Similarity (0 - 1)
                             sortingOrder: default None ,
                             itemsToBeRendered: Number of Items Return,
                             callback: Return Best Match
            
                         });

      console.log(data)    // All Filtered Lists             

    </script>

```

## API

The package contains Four methods:


### getSimilarityofArrayOfObjects({ data:Array , rawText:String , objectMatchingKeys:Array , similarityScale:Number , sortingOrder:Number , itemsToBeRendered:Number , callback:Function })

Returns All Items whose fraction between 0 and 1, which indicates the degree of similarity of your word with mentioned objects keys of array items as per similarityScale value . 0 indicates completely different object item , 1 indicates identical object item . The comparison is case-sensitive.


##### Arguments


1. data : Array Of object 
2. rawText : The string that you waana match
3. objectMatchingKeys : Array of keys of an object
4. similarityScale : Number or fraction value from finding start                 ->  Default 0
5. sortingOrder : Number                                                ->  1 for DESC and 0 for ASC , Default None
6. itemsToBeRendered : Number Of Items Return                        ->   Default all items
7. callback: Function                                        ->  Return Best Matched Item and Index of that matched item from Given List


#### Examples

```js

const array1 = [
    { name: "John", age: 25, city: "New York" },
    { name: "Alice", age: 30, city: "Los Angeles" },
    { name: "Bob", age: 28, city: "Chicago" }
];

 const datavalue =   getSimilarityofArrayOfObjects({
    data:array1,
    similarityScale:0,
    rawText:'find john in the list',
    objectMatchingKeys:['name'],
    sortingOrder:1,
    itemsToBeRendered:2
})


console.log(datavalue)  

// Return Item

[
  {
    item: { name: 'John', age: 25, city: 'New York' },
    similarityScale: { name: 0.3157894736842105 },        // describe each key similarityScale
    averageSimilarityScale: 0.3157894736842105            // describe average similarityScale of all mentioned key of an object
  },
  {
    item: { name: 'Alice', age: 30, city: 'Los Angeles' },
    similarityScale: { name: 0.1 },
    averageSimilarityScale: 0.1
  }
]


// callback Item

{
  bestMatch: {
    item: { name: 'John', age: 25, city: 'New York' },
    similarityScale: { name: 0.3157894736842105 },
    averageSimilarityScale: 0.3157894736842105
  },
  bestMatchIndex: 0
}


```


### getSimilarityScaleofArrayOfObjects({ data:Array , rawText:String , objectMatchingKeys:Array , sortingOrder:Number , itemsToBeRendered:Number })

Returns all Items whose fraction between 0 and 1, which indicates the degree of similarity of your word with mentioned objects keys of array items. 0 indicates completely different object item , 1 indicates identical object item . The comparison is case-sensitive.


##### Arguments


1. data : Array Of object 
2. rawText : The string that you waana match
3. objectMatchingKeys : Array of keys of an object
4. sortingOrder : Number                                                ->  1 for DESC and 0 for ASC , Default None
5. itemsToBeRendered : Number Of Items Return                           ->  Default All Item


#### Examples

```js

const array1 = [
    { name: "John", age: 25, city: "New York" },
    { name: "Alice", age: 30, city: "Los Angeles" },
    { name: "Bob", age: 28, city: "Chicago" }
];

 const datavalue =   getSimilarityScaleofArrayOfObjects({
    data:array1,
    rawText:'find john in the list',
    objectMatchingKeys:['name'],
})


console.log(datavalue)  

// Return All Items

[
 {
    item: { name: 'John', age: 25, city: 'New York' },
    similarityScale: { name: 0.3157894736842105 },        // describe each key similarityScale
    averageSimilarityScale: 0.3157894736842105            // describe average similarityScale of all mentioned key of an object
  },
  {
    item: { name: 'Alice', age: 30, city: 'Los Angeles' },
    similarityScale: { name: 0.1 },
    averageSimilarityScale: 0.1
  },
  {
    item: { name: 'Bob', age: 28, city: 'Chicago' },
    similarityScale: { name: 0 },
    averageSimilarityScale: 0
  }
]


```


### getSimilarityOfArrayOfStrings({ data:Array of String , rawText:String , sortingOrder:Number , itemsToBeRendered:Number , callback:Function})

Returns all Items whose fraction between 0 and 1, which indicates the degree of similarity of your word with mentioned Array of strings. 0 indicates completely different strings , 1 indicates identical string. The comparison is case-sensitive.


##### Arguments


1. data : Array Of Strings 
2. rawText : The string that you waana match
3. sortingOrder : Number                                                ->  1 for DESC and 0 for ASC , Default None
4. itemsToBeRendered : Number Of Items Return                        ->   Default all items
5. callback: Function                                        ->  Return Best Matched Item and Index of that matched item from Given List


#### Examples

```js

const array1 = [
  "The quick brown fox jumps over the lazy dog.",
  "She sells seashells by the seashore.",
  "The sun rises in the east and sets in the west.",
  "Coding is a valuable skill in the modern world.",
  "Learning new things is a lifelong journey."
]

 const datavalue =   getSimilarityOfArrayOfStrings({
    arrayOfStrings:array1,
    rawText:'sun is getting rises in east'
})


console.log(datavalue)  

// Return All Items

[
  {
    targetString: 'The quick brown fox jumps over the lazy dog.',
    similarityScale: 0
  },
  {
    targetString: 'She sells seashells by the seashore.',
    similarityScale: 0.15384615384615385
  },
  {
    targetString: 'The sun rises in the east and sets in the west.',
    similarityScale: 0.4482758620689655                                               // describe similarityScale of string
  },
  {
    targetString: 'Coding is a valuable skill in the modern world.',
    similarityScale: 0.16666666666666666
  },
  {
    targetString: 'Learning new things is a lifelong journey.',
    similarityScale: 0.2807017543859649
  }
]


// callback Item

{
  bestMatch: {
    targetString: 'The sun rises in the east and sets in the west.',
    similarityScale: 0.4482758620689655
  },
  bestMatchIndex: 2
}


```


### getSimilarityOfTwoString(string1,string2)

Returns fraction between 0 and 1, which indicates the degree of similarity of your two strings. 0 indicates completely different strings , 1 indicates identical string. The comparison is case-sensitive.


##### Arguments


1. string1 : First String
2. string2 : Second String


#### Examples

```js


var datavalue = getSimilarityOfTwoString('She enjoys reading books in her free time.','She loves reading books during her leisure hours.');

console.log(datavalue)


// Return similarityScale of your both strings

{ similarityScale: 0.48 }


```


# Documentation of Api Content

Here we mentioned our default value of Parameter of an Api's .

The general structure of api's as follows:


| Property  | Value  | Default Value |
| :------------ |:---------------:| -----:|
| data      | Array Of Object | Blank Array |
| rawText      | String        | Blank String |
| similarityScale | Number or Fractional Value        | Zero  |
| objectMatchingKeys | Array of Object Keys        | Blank Array |
| sortingOrder | Number ( 0 - 1 )       | null |
| itemsToBeRendered | Number ( 0 - Array Length   )     | Array Length |
| callback | Function        | Function |
| string1 | string        | null |
| string2 | string        | null |



# Release Notes


> **Version 1.0.2**  : Released  getSimilarityOfArrayOfStrings and  getSimilarityOfTwoString .

> **Version 1.0.1**  : Released  getSimilarityofArrayOfObjects and  getSimilarityScaleofArrayOfObjects .


# Resourses 

> Spacy.js

> TensorFlow.js

> NLU