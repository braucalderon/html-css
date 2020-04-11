//  this
// console.log(this);
// calculateAge(1985)

// function calculateAge(year){
//     console.log(2016 - year);
//     console.log(this);
    
// }
// An object 
let Jon ={
    name: 'John',
    year: 1990,
    calculateAge: function(){
        console.log(this);
        console.log(2016 - this.year);

        // function innerFunction(){
        //     console.log(this);
            
        // }
        // innerFunction()
        
        
    }
}
Jon.calculateAge()

let mike = {
    name:'mike',
    year: 1984
}

// borrowing functions
mike.calculateAge = Jon.calculateAge;
mike.calculateAge()