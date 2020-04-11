// Hoisting 

// functions 
// hoisting works with function 
calculateAge(1967)

function calculateAge(year){
    console.log(2016 - year);
    
}

// functions expressions 
// hoisting does not work with functions expressions 

let retirement = function(year){
    console.log(65 - (2016-year));
    
}
retirement(1998)

// variables 

let age = 23
console.log(age);


function foo(){
    let age = 65
    console.log(age);

    
}
foo()
console.log(age);


// scoping chain
// lexicol scope 
// function
let a = 'Hello'
first()
function first(){
    let b = 'Hi'
    second()

    function second(){
        let c = 'Hey!'
        third()
        
    }
}
function third(){
    let d = 'John'
    console.log(a + d)
    
}




