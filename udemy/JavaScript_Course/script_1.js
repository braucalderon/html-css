/*
* CODING CHALLENGE 4
*/

/*
Implement the same functionality with objects and methods.
1. For each of them, create an object with propertiesfor their
full name, mass, and height
2. Then, add a method to each object to calculate the BMI. Save
the BMI to the object and also return it from the method.
3. In the end, log to the console who has the heighest BMI. Don't
forget they might have the same BMI.

BMI = mass / height^2 = mass / (height * height). (mass in kg and height
    in metter).
*/

// Objects with a method 
var mike = {
    firstName: 'Mike',
    lastName: 'Smith',
    height: 1.70,
    mass: 98,
    calBMI:function(){
        this.bmi = this.mass / (this.height * this.height);
        return this.bmi;
    }
};

var jana = {
    firstName: 'Jana',
    lastName: 'Garcia',
    height: 1.77,
    mass: 96,
    calBMI:function(){
        this.bmi = this.mass / (this.height * this.height);
        return this.bmi;
    }
};

if(mike.calBMI() > jana.calBMI()){
    console.log(mike.firstName +' '+ mike.lastName +' has the heighest BMI with ' + mike.bmi);
    
}else if(jana.bmi > mike.bmi){
    console.log(jana.firstName +' '+ jana.lastName +' has the heighest BMI with ' + jana.bmi);
}else{
    console.log('They both have the same BMI');
    
}

console.log(mike,jana);

/**
 * Loops ansd iterations 
 */
// for(var i = 0; i < 10; i+=2){
//     console.log(i);
    
// }

var john = ['John', 'Smith', 1990, 'designer', false];

// for(var i = 0; i < john.length; i++){
//     console.log(john[i]);
    
// }

// var i = 0;
// while(i < john.length){
//     console.log(john[i]);
//     i ++
    
// }

// continue ans breaks statemtents 
for(var i = 0; i < john.length; i++){
    // it will get only strings in the array
    if (typeof john[i] !== 'string') continue;
    console.log(john[i]);
    
}

for(var i = 0; i < john.length; i++){
    // it breaks from the loop after the a non string element
    if (typeof john[i] !== 'string') break;
    console.log(john[i]);
    
}

for(var i = john.length-1; i >= 0; i--){
    console.log(john[i]);
    
}

/*
* CODING CHALLENGE 5
*/

/*
Tip calculator, lets create a more advance version using everything we learned!
This time, John snd his family went to 5 different restaurants. The bills were $124, $48,
$268, $180 and $42

John likes to tip 20 percent of the bill when the bill is less than $50, 15 percent when the bill 
is between $50 and $200, and 10 percent of the bill is more than $200

Implement a tip calculator using objects and loops:
1. Create an object with an array for the bill values 
2. Add a method to calculate the tip
3. This method should include a loop to iterate over all the paid bills and do the tip calculations
4. As an output, create 1) a new array containing all tips, 2) an array containing final paid amounts
(bill + tips). HINT: start with two empty arrays [] as properties and then fill them up in the loop.

Extra: Mark's family also went on a holiday, going to 4 different restaurants. The bills were $77, 
$375, $110, and $45.
Mark likes to tip 20 percent  of the bill when the bill is less than $100, 10 percent when the bill is
between $100 and $300, and 25 percent if the bill is more than $300

5. Implement the same functionality as before, this time using Mark's tipping rules
6. Create a function (not a method) to calculate the average of a given array of tips. HINT: Loop 
over the array, and in each iteration store the current sum in a variable (starting from 0). After
you have the sum of the array, divide it by the number of elements in it ( that's how you calculate the average)
7. Calculate the average tip for each family 
8. Log to the console which family paid the heighest tips on average. 
*/



var averTips = new Array();

var mike = {
    bills: [124, 48, 268, 180, 42],
    totalTips: [],
    tipsBills: [],
    calcTips: function(){
        for(var i = 0; i < this.bills.length; i++){
            var totalB, totalT;
            if(this.bills[i] < 50){
                totalT = this.bills[i] * (20/100);
                totalB = totalT + this.bills[i];
                // console.log(totalTips, tipsBills);
                
            }else if(this.bills[i] >= 50 && this.bills[i] < 200){
                totalT = this.bills[i] * (15/100);
                totalB = totalT + this.bills[i];
                // console.log(totalTips, tipsBills);

            }else {
                if(this.bills[i] >= 200){
                    totalT = this.bills[i] * (20/100);
                    totalB = totalT + this.bills[i];
                    // console.log(totalTips, tipsBills);
                }
            }
            this.totalTips.push(totalT);
            this.tipsBills.push(totalB);
            averTips.push(totalT); 
        }
    }
};

var mark = {
    bills: [77, 375, 110, 45],
    totalTips: [],
    tipsBills: [],
    calcTips: function(){
        for(var i = 0; i < this.bills.length; i++){
            var totalB, totalT;

            if(this.bills[i] < 100){
                totalT = this.bills[i] * (20/100);
                totalB = totalT + this.bills[i];
                // console.log(totalTips, tipsBills);
                
            }else if(this.bills[i] >= 100 && this.bills[i] < 300){
                totalT = this.bills[i] * (15/100);
                totalB = totalT + this.bills[i];
                // console.log(totalTips, tipsBills);

            }else {
                if(this.bills[i] >= 300){
                    totalT = this.bills[i] * (25/100);
                    totalB = totalT + this.bills[i];
                    // console.log(totalTips, tipsBills);
                }
            }
            this.totalTips.push(totalT);
            this.tipsBills.push(totalB);
            averTips.push(totalT);
        }
    }
    
};

mike.calcTips();
mark.calcTips();

console.log(mike.totalTips);
console.log(mike.tipsBills);
console.log(mark.totalTips);
console.log(mark.tipsBills);
console.log(averTips);


// function expression 

function calAverage(array){
    var total = 0;
    // var average = 0;
    for(var i = 0; i < array.length; i ++){
        total += array[i];
        // console.log(total);
    }
    average = total / array.length;
    return average;
}

   
// creates a variable in the object 
mike.average = calAverage(mike.totalTips);
mark.average = calAverage(mark.totalTips);
console.log(mike, mark);


if (mike.average > mark.average){
    console.log('Mike paid the highest tip with an average of $' + mike.average);
    
}else if(mark.average > mike.average){
    console.log('Mark paid the highest tips with the average of $' + mark.average);
    
}else {
    console.log('Both families paid the same amount of tips with the sum of $' + mike.average);
    
}

console.log('The total average of tips overall is $' + calAverage(averTips));

// console.log(averageTips(mike.totalTips));






