const notes = ['note 1', 'note 2', 'note 3']

notes[2] = 'This is noe the one note 3'

notes.forEach(function(item, index){
    const num = index + 1
    console.log(`${num}. ${item}`);
    
})
console.log(notes.length);
console.log(notes);

// counting
for(let count = 0; count <= 2; count++){
    console.log(count);
    
}
for (let count = notes.length -1; count >= 0; count--) {
    console.log(notes[count]);
    
}

// challenge
const todo = ['order cat food', 'clean kitchen', 'do work', 'exersice']

for (let index = 0; index < todo.length; index++) {
    const num = index + 1
    const tod = todo[index]
    console.log(`${num}. ${tod}`);
    
}

