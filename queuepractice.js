// This exercise is on a JavaScript Compiler

// Define the Queue class
class Queue {
    constructor() {
        // Initialize an empty array to store queue items
        this.items = [];
    }
    
    // Method to add an item to the end of the queue
    enqueue(item) {
        this.items.push(item);
    }
    
    // Method to remove and return the item from the front of the queue
    dequeue() {
        return this.items.shift();
    }
    
    // Method to return the number of items in the queue
    size() {
        return this.items.length;
    }
    
    // Method to return the item at the front of the queue without removing it
    peek() {
        return this.items[0];
    }
}

// Create an instance of the Queue class
const myQueue = new Queue();

// Add items to the queue
myQueue.enqueue(5); 
myQueue.enqueue(4);
myQueue.enqueue(8);
myQueue.enqueue(1);

// Print the item at the front of the queue (should be 5)
console.log(myQueue.peek())

// Remove and print the item at the front of the queue (should be 5)
console.log(myQueue.dequeue())

// Print the new item at the front of the queue (should be 4 after dequeue)
console.log(myQueue.peek())

// Print the number of items remaining in the queue (should be 3 after dequeue)
console.log(myQueue.size())

