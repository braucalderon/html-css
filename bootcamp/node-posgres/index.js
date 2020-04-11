

// let tableName = 'person'

// const {Pool, Client} = require('pg')
// const connectionString = 'postgres://postgres:Totomalo123!@localhost:5432/postgres';

// const pool = new Pool({connectionString: connectionString});

// // pool.query('select now()', (err, res) => {
// //     console.log(err, res);
// //     pool.end();
    
// // });
// const client = new Client ({connectionString: connectionString});
// client.connect();

// console.log('');
// const query = {
//     text: `INSERT INTO ${tableName}(name, material, height, tool) VALUE`,
//     values: ['brian', 'brian.m.calson', 'none', 7, false]
// };

// client.query(`select * from ${tableName}`, (err, res) =>{
//     if(err){
//         console.log(err.stack);
        
//     }else{
//         res.rows.forEach(row => {
//             console.log(row);
            
//         })
//     }
// })

let Sequelize = require('sequelize');
let sequelize = new Sequelize('postgres://postgres:Totomalo123!@localhost:5432/postgres')

// tabble name

let table = 'person'
let Person = sequelize.define('person', {
    name:Sequelize.STRING,
    material: Sequelize.STRING,
    height: Sequelize.INTEGER,
    brim: Sequelize.BOOLEAN

});

Person
.sync()
.then(function(){
    console.log();
    console.log('The table people created for use');
     
})

Person.create({
    name:'brain',
    material: 'felt',
    height: 5,
    brim: false
});

// New Table Users

let Users = sequelize.define('users', {
    name:Sequelize.STRING,
    material: Sequelize.STRING,
    height: Sequelize.INTEGER,
    brim: Sequelize.BOOLEAN

});
Users
.sync()
.then(function(){
    console.log();
    console.log('The table users created for use');
     
})

// New Table Posts

let Posts = sequelize.define('posts', {
    name:Sequelize.STRING,
    material: Sequelize.STRING,
    height: Sequelize.INTEGER,
    brim: Sequelize.BOOLEAN

});
Posts
.sync()
.then(function(){
    console.log();
    console.log('The table posts created for use');
     
})

