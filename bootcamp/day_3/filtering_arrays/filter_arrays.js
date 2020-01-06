
// const todo = ['order cat food', 'clean kitchen', 'do work', 'exersice']

// todo.indexOf('do work')
// console.log(todo.indexOf('do'));

const todos = [{
    title: 'My next stop',
    body: 'zero body fat',
    completed: false
}, {
    title: 'bad habbits',
    body: ' bodr fat',
    completed: false
}, {
    title: 'Office hours',
    body: 'get a new diet',
    completed: true
}]

// const filter_notes = notes.filter(function(note, index){
//     const isTitleMatch = note.title.toLowerCase().includes('ne')
//     const isBodyMatch = note.body.toLowerCase().includes('ne')
//     return isTitleMatch || isBodyMatch
// })
// console.log(filter_notes);

// const findNotes = function(note, query){
//     return notes.filter(function(note, index) {
//         const isTitleMatch = note.title.toLowerCase().includes(query.toLowerCase())
//         const isBodyMatch = note.body.toLowerCase().includes(query.toLowerCase())
//         return isTitleMatch || isBodyMatch
//     })
    
// }
//  console.log(findNotes(notes, 'bad things'));
 
 const deleteTodos = function(todos, todoText){
     const index = todos.findIndex(function(todo){
         return todo.text === todoText
     })
     if (index > -1) {
         todos.splice(index, 1)
     }
 }

 const getThingsTodo = function(todos){
     return todos.filter(function(todo){
         return !todo.completed
     })
 }

 console.log(getThingsTodo(todos));
 


 
 
 

//  console.log(deleteTodos(todos, 1));
 
// const getThingsTodo = function(todos){
//     return todos.filter(function(todo){
//         return todos.completed === false
//     })
// }
// console.log(getThingsTodo(todos));

// const note = findNote(notes, 'some other office modification')
// console.log(note);

