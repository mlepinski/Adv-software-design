You are to code an API that provides a Bin Packing algorithm. It is not important that your Bin Packing algorithm do a good job, only that it operates correctly.

You can find information about the general Bin Packing problem here.
- [Wikipedia Page]([https://en.wikipedia.org/wiki/Pente](https://en.wikipedia.org/wiki/Bin_packing_problem)

For this particular version of the Bin Packing problem, all bins have a 100 units of space (capacity) and each item has an integer size.
The goal is to pack a series of items using as few bins as possible. 

Note: This is the 'online' version of the problem where the algorithm doing the packing only gets to see one item at time. 

---

## State Encoding

A set of partially packed bins are encoded as follows:

  ##binOneItems#binTwoItems#binThreeItems# ... ##

That is, the set of bins is an arbitrarily long sequence of substrings separated by the # symbol where each substring encodes a bin.

Each of the substrings (e.g., binTwoItems) should be encoded as follows:
  sizeOne!sizeTwo!sizeThree! ... 

That is, the bin is a sequence of item sizes (for items currently in the bin) separated by a ! symbol

As an example, the following string encodes a set of three bins where:
- The first bin has items of sizes 1, 2, and 3
- The second bin has a single item of size 44
- The third bin has found itmes of sizes 5, 6, 7, and 8

  ##1!2!3#44#5!6!7!8##

Recall that each bin has a capacity of 100. Therefore, an encoding is invalid if the sum of the sizes in any bin exceed 100.

## API Endpoint - New Problem

Recall that your API is essentially implementing a bin packing algorithm. You are presented with items and need to decide which bin they go into. 
You don't need to make smart decisions, but you need to make valid decisions.

/newproblem/

Input: There is no input for this API endpoint

Output is a JSON Object:

  {
  'ID': problemID
  'bins' : binEncoding
  }

The **problemID** should be an integer that can be used to reference a particular set of bins that are being packed.

The **binEncoding** for a new (fresh) instance of bin packing should be an empty set containing no bins. 

## API Endpoint - Place Item

/placeitem/problemID/size

Input: 
-- **problemID** is the unique ID that was associated with the problem instance when it was created (see above). 
-- **size** is the size of the new item to be placed in a bin.

Your algorithm must choose which bin to place the item in and then provide an encoding of the bins with the new item now placed within a bin.

*IMPORTANT*: Your algorithm is not allowed to move items that have already been placed!

Output is a JSON Object:

  {
  'ID': problemID
  'size' : new_item_size
  'loc' : bin_number
  'bins' : new_bin_encoding
  }

The **problemID** should be the same as was provided in the input

**new_item_size** should be the size of the newly placed item 

**bin_number** should be the number of the bin where the new item was placed. (Please number the first bin as 1)

The **new_bin_encoding** should be a string encoding the set of bins with the new itemed placed.

## API Endpoint - End Problem

/endproblem/problemID

Input: 
-- **problemID** is the unique ID that was associated with the problem instance when it was created (see above). 

Your algorithm should end the current problem instance. Any further attempts to add items to this problem instance should fail.

You should then return the following information about the problem instance.

Output is a JSON Object:

  {
  'ID': problemID
  'size' : total_size
  'items' : num_items
  'count' : num_bins
  'wasted' : wasted_space
  'bins' : bin_encoding
  }

The **problemID** should be the same as was provided in the input

**total_size** should be the total size of all of the items

**num_items** should be the number of items placed in the collection of bins

**num_bins** should be the number of bins used to store the items

**wasted_space** should be the capacity of all of the bins minus the total size of the items

The **bin_encoding** should be a string encoding of the final set of packed bins.

## Submission

You should create a GitHub repository that includes your code. Please make your code as clear and easy to read as possible. 

It would be helpful to include some test cases. I have provided skeleton test code that might be useful.
