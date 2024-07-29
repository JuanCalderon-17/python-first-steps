// Online Java Compiler
// Use this editor to write, compile and run your Java code online
class Queue {
    constructor() {
        this.items = [];
    }
    
    enqueue(item) {
        this.items.push(item);
    }
    
    dequeue() {
        return this.items.shift();
    }
    
    size() {
        return this.items.length;
    }
    
    peek() {
        return this.items[0];
    }
}

const myQueue = new Queue();
myQueue.enqueue(5); 
myQueue.enqueue(4);
myQueue.enqueue(8);
myQueue.enqueue(1);

console.log(myQueue.peek())
console.log(myQueue.dequeue())
console.log(myQueue.peek())
console.log(myQueue.size())
