/*
* CODING CHALLENGE 1
*/

/*
Mark and John are trying to compare their BMI (Body Mass Index), which is calculated
using the formula: BMI = mass / heigh^2 = mass / (height * height).
(mass in Kg and height in meter).

1. Store  Mark's and John's mass and height in variables
2. Calculated both their BMIs
3. Create a boolean variable contaning information about whether Mark has a heigher BMI than John.
4. Print a string to the console containing the variable from step 3. (Something like 'Is Mark's BMI higher
than John's'? true)
*/

var massMark, massJohn, markHeight,johnHeight, bmiMark, bmiJohn
markHeight = 1.80;
johnHeight = 1.78;
massJohn = 78;
massMark = 90;

bmiJohn = massJohn / johnHeight**2;
bmiMark = massMark / markHeight**2;

console.log('Is Mark BMI higher than Johns ?' + ' ' + (bmiJohn > bmiMark));

var firsName, age;
firsName = 'John';

age = 40;
switch(true){
    case age < 13:
        console.log(firstName + ' is a boy.');
        break;
    case age >= 13 && age < 20:
        console.log(firsName + ' is a teneger.');
        break;
    case age >= 20 && age < 30:
        console.log(firsName + ' is a young man.');
        break;
    default:
        console.log(firsName + ' is a man.');        
}

/*
* CODING CHALLENGE 2
*/

/*
Mark and John both play basketball in different teams. In the lastest 3 games, John's team scored 
89, 120, 103 points, while Mike's team scored 116, 94, and 123 points. 

1. Calculate the average score for each team
2. Decide which teams wins in average (highest average score), and print the winner to the console.
Also include the average score in the output.
3. Then change the scores to show different winners. Dont forget to take into account there might be a draw
(the same average score)

4.EXTRA: Mary also plays basketball, and her team scored 97, 134, and 105 points. like before, log the average
winner to the console. HINT: you will need the && operator to take the decision. If can't solve this on, just
watch the solution.

5. Like before, change the scores to generate different winners, keeping in mind there might be draws. 
*/

var mark, john, mary, mark_1, mark_2, mark_3, john_1, john_2, jonh_3, mary_1, mary_2, mary_3;

// game 1
mark_1 = 116;
john_1 = 89;
mary_1 = 97;

// game 2
mark_2 = 94;
john_2 = 120;
mary_2 = 134;

// game 3
jonh_3 = 103;
mark_3 = 123;
mary_3 = 105;

mark = (mark_1 + mark_2 + mark_3) / 3;
john = (john_1 + john_2 + jonh_3) / 3;
mary = (mary_1 + mary_2 + mary_3) / 3;

console.log(mark, john, mary);

switch(true){
    case mark > john && mark > mary:
        console.log('Mike won with the average of ' + mark + ' points');
        break;
    case john > mark && john > mary:
        console.log('John won with the average of ' + john + ' points');
        break;
    case mary > john && mary > mark:
        console.log('Mary won with the average of ' + mary + ' points');
        break;
    case mary === john:
        console.log('Mary and John got same scores ' + mary + ' , ' + john );
        break;
    case john === mark:
        console.log('John and Mike got same scores ' + john + ' , ' + mark);
        break;
    case mark === mary:
        console.log('Mike and Mary got same scores ' + mary + ' , ' + mark);
        break;
        
    default:
        console.log('No one won the game');
            
}

/*
Functions 
*/

function calculateAge(birthday){
    return 2018 - birthday;
}


var ageJohn = calculateAge(1990);
var ageMike = calculateAge(1948);
var ageJane = calculateAge(1969);

console.log(ageJohn, ageJane, ageMike);

function yearsUntilRetirement(birthday, firstName){

    var age = calculateAge(birthday);
    var retirement = 65 - age;
    if(retirement < 0){
        console.log(firstName + ' is already retired.');
        
    }
    else{
        console.log(firstName + ' retires in ' + retirement + ' years.');
    }
    
    
}

yearsUntilRetirement(1990, 'Lio');
yearsUntilRetirement(1948, 'Mike');
yearsUntilRetirement(1969, 'Jane');

/*
Function Statement and Expression
*/
// Function declaration
// function WhatDoYouDo(job, firstName){

// }

// Function expression
var whatDoYouDo = function(job, firstName){
    switch(job){
        case 'teacher':
            return firstName + ' teaches kids how to code';

        case 'driver':
            return firstName + ' drives an Uber car';

        case 'designer':
            return firstName + ' design beatiful websites';

        default:
            return firstName + ' does something else';
    }
}
console.log(whatDoYouDo('teacher', 'John'));
console.log(whatDoYouDo('driver', 'Mike'));
console.log(whatDoYouDo('designer', 'Jane'));
console.log(whatDoYouDo('security', 'Tim'));
 
/*
Arrays
*/

// Initialize new array
var names = ['John', 'Mark', 'Jane'];
var years = new Array(1990, 1969, 1948);

console.log(names[2]);
console.log(names.length);

// Mutate array data
names[1] = 'Ben';
names[names.length] = 'Mary';
console.log(names);

// Different data type
var john = ['John', 'Smith', 1990, 'teacher', false];
// push() will add the element at the end of the array
john.push('blue');
// unshift() will add the element at the begining of the array
john.unshift('Mr.');
// pop() remove the element from the end
john.pop();
john.pop();
// shift() remove the element from the begining of the array
john.shift();
console.log(john);

// if else statement
var isDesigner = john.indexOf('designer') === -1 ? 'John is NOT a designer': 'John IS a designer';
console.log(isDesigner);

console.log(john.indexOf(1990));

/*
* CODING CHALLENGE 3
*/

/*
John and his family went on a holiday and went to 3 different restaurants. The bills were $124, $48 and
$268.
To tip the waiter a fair amount, John created a smple tip calculator  (as a function). He likes to tip 20%
of the bill when the bill is less than $50, 15% when the bill is between $50 and $200, and 10% if the bill 
is more than $200.

In the end, John would like to have 2 arrays:
1. Contaning all three tips (one for each bill)
2. Contaning all three final paid amounts (bill + tip)

To calculate 20% of a value , simply multiply if with 20/100 = 0.2
*/

var bills = [124,48,268];
var tips = new Array();
var tipsPlusAmount = new Array();

var tipCalculator = function(bill, percentage){
    var tip = (percentage/100) * bill;
    tips.push(tip);
    console.log(tips);
    var total = tip + bill;
    tipsPlusAmount.push(total); 
    console.log(tipsPlusAmount);
        
}

var totalBill = function(bill){
    
    switch(true){
        case bill < 50:
            return tipCalculator(bill, 20);
        case bill >= 50 && bill < 200:
            return tipCalculator(bill, 15);
        case bill >= 200:
            return tipCalculator(bill, 10);
    }
}

console.log(totalBill(bills[0]));
console.log(totalBill(bills[1]));
console.log(totalBill(bills[2]));


/*
Objects and properties 
Objects with curly braces 
*/
 
var john = {
    firstName: 'John',
    lastName: 'Smith',
    birthYear: 1990,
    family: ['Jane', 'Mark', 'Bob' , 'Emily'],
    job: 'teacher',
    
};
// dot notation
console.log(john.firstName);
console.log(john['lastName']);
var x  = 'birthYear';
console.log(john[x]);

// Mutate to another description
// Adding another element into a array of objects 
john.job = 'designer';
john['isMarried'] = true;
console.log(john);

// creating an array object 
var jane = new Object();
jane.name = 'Jane';
jane.birthYear = 1996;
jane['lastName'] = 'Smith';
console.log(jane);
 

/*
Objects and methods
*/

var jona = {
    firstName: 'John',
    lastName: 'Smith',
    birthYear: 1990,
    family: ['Jane', 'Mark', 'Bob' , 'Emily'],
    job: 'teacher',
    isMarried: false,
    calcAge: function(){
        // this.age creates a new variable into the array and add the result
        this.age = 2018 - this.birthYear;
    }
    
};

// accessing a method from an array object
console.log(jona.calcAge());

// store the outcome from a method into an object
jona.calcAge();
console.log(jona);



























