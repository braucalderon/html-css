const notes = ['notes 1','notes 2', 'notes 3']

notes[2] = 'This is the new one'

notes.forEach(function(item, index){
    console.log(index);
    console.log(item);
    
})

console.log(notes.length);
console.log(notes);

const todo = ['order cat food', 'clean kitchen', 'do work', 'exersice']

todo.slice(2, 1)
todo.push('buy coffee')
todo.shift()

console.log(`You have ${todo.length} todo`);


// Challenge
// callback function (call fucntion into a fucntion)
todo.forEach(function(todo, index) {
    // to start with 1
    const num = index + 1
    console.log(`${num}. ${todo}`);
    
})
