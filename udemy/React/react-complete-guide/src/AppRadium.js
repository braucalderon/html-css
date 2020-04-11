import React, { Component } from 'react';
import './App.css';
import Radium, { StyleRoot} from 'radium';
import Person from './Person/Person'



class App extends Component{
    state = {
        persons:[
            {id: 'nae1', name:'Thomas', age: 24},
            {id: 'nam2', name: 'Nicolas', age: 21},
            {id: 'nar3', name: 'Max', age: 20}
        ],
        otherState: 'some other state',
        showPersons: false
    }


    
    changeHandler = (event ,id) => {
        // it will execute findIndex() on each element of the array
        // find the index of the element of the array
        const personIndex = this.state.persons.findIndex( p => {
            return p.id === id
        }); 
        // working with copies 
        const person = {
            ...this.state.persons[personIndex] // creates a new a copy of the new object 
        };
        
        person.name = event.target.value;

        const persons = [...this.state.persons];
        persons[personIndex] = person;


        this.setState( {persons: persons}); // update with a copy 

        // alternative to create another object 
        // const person = Object.assign({}, this.state.persons[personIndex]);

        // this.setState({
        //     persons: [
        //         {name: 'Thomas', age: 28},
        //         {name: 'Nicolas', age: 21},
        //         {name: event.target.value, age: 20}
        //     ]
        // })
    }

    //  remove one person from the array persons
    deletePersonHandler = (personIndex) => {
        // const persons = this.state.persons;
        const persons = [...this.state.persons] // adds a new array from the old array
        // do not change the array from the original array
        persons.splice(personIndex, 1) //remove one element from the array
        this.setState({persons: persons});
        // adding a key property to keep track of what has been deleted. 

    }

    togglePersonHandler = () =>{
        const doesShow = this.state.showPersons;
        this.setState({showPersons: !doesShow})

    }

    render() {
        // styling the button
        const style = {
            backgroundColor: 'white',
            font: 'inherit',
            border: '1x solid blue',
            padding: '8px',
            cursor: 'pointer',
            // figures using the radium dependency
            ':hover': {
                backgroundColor: 'lightgreen',
                color:'black'
            }
        }


        // this is the prefer way to put conditional content in the render section
        let persons = null;
        if(this.state.showPersons){
            persons = (
                <div >
                {this.state.persons.map((person, index) => {
                    // map into a <Person component
                    return <Person
                    // remove elements
                    click={() => this.deletePersonHandler(index)}
                    name={person.name}
                    age={person.age}
                    key={person.id}
                    changed={(event) => this.changeHandler(event, person.id)}
                    />
                })}
                

                </div> 
            );
        }

         // different way to style in react
         // overwrite the hov style
         style.backgroundColor = 'red';
         style[':hover'] = {
             backgroundColor:'salmon',
             color:'black'
         }
         
    

         const classes = [];
        //  adding dynamic nature to the code above
        if(this.state.persons.length <= 2){
            classes.push('red');  // classes = ['red']
        }
        if(this.state.persons.length <= 1){
            classes.push('bold'); // classes=['red', 'bold']
        }



        return(
            <StyleRoot>
            <div className='App'>
                <h1>Hi, I am a React App</h1>
                <p className={classes.join(' ')}>This is really working</p>
                <button 
                style={style}
                onClick={this.togglePersonHandler}>Switch Name</button>
                
                {persons}
                
            </div>
            </StyleRoot>

        )
    }
}

export default Radium(App);
// radium is a new dependency u must add "yarn add radium" or "npm install --save radium"
// radium helps to add more figures from css into js files 

//----------------------------------------------------------------------------------------


// from the Person.js component
// create a component is just an function that returns something 
import React from  'react';
import './Person.css';
import Radium from 'radium';

const person = (props) => {
    // using the dependency radium 
    const style = {
        '@media (min-width: 500px)':{
            width: '450px'
        }
    };
    return (
        <div className="Person" style={style} >
            <p onClick={props.click} >I'm {props.name} and I am {props.age} years old!</p>
            <p>{props.children}</p>
            <input type='text' onChange={props.changed} value={props.name} />
        </div>
    )
}

export default Radium(person);
// radium is a new dependency u must add "yarn add radium" or "yarn install --save radium"
// radium helps to add more figures from css into js files 


