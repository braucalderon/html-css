
// const todo = ['order cat food', 'clean kitchen', 'do work', 'exersice']

// todo.indexOf('do work')
// console.log(todo.indexOf('do'));

const notes = [{
    title: 'My next stop',
    body: 'zero body fat'
}, {
    title: 'bad habbits',
    body: ' bodr fat'
}, {
    title: 'Office hours',
    body: 'get a new diet'
}]

console.log(notes.length);
console.log(notes);

const index = notes.findIndex(function(note, index){
    return notes.title === 'Office hours'
    
})
console.log(index);



