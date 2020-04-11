// getters and setters

let car = {
    make: 'toyota',
    model: 'camory',
    plateNumber: 'fertg123',
    owner: 'joe camper',
    makeYear: 2020,

    set setModel(m){
        this.model = m
    }
}
let model = car.setModel = 'Tacoma'
console.log(model);

