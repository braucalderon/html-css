import React, { Component } from 'react';
import './App.css';
import Person from './Person/Person'


class App extends Component{
    state = {
        persons:[
            {name:'Thomas', age: 24},
            {name: 'Nicolas', age: 21},
            {name: 'Max', age: 20}
        ],
        otherState: 'some other state',
        showPersons: false
    }

    // switchHandler = (newName) => {
    //     this.setState({
    //         persons: [
    //             {name: newName, age: 40},
    //             {name: 'Nicolas', age: 21},
    //             {name: 'Max', age: 40}
    //         ]
    //     })
    // }

    changeHandler = (event) => {
        this.setState({
            persons: [
                {name: 'Thomas', age: 28},
                {name: 'Nicolas', age: 21},
                {name: event.target.value, age: 20}
            ]
        })
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
            cursor: 'pointer'
        }

        // this is the prefer way to put conditional content in the render section
        let persons = null;
        if(this.state.showPersons){
            persons = (
                <div >
                {this.state.persons.map(person => {
                    {/* map into a <Person component */}
                    return <Person
                    name={person.name}
                    age={person.age}/>
                })}
                {/* not very efficient way to put data */}
                    {/* <Person
                    name={this.state.persons[0].name}
                    age={this.state.persons[0].age}/>
                    <Person
                    name={this.state.persons[1].name}
                    age={this.state.persons[1].age}/>
                    <Person
                    name={this.state.persons[2].name}
                    age={this.state.persons[2].age}
                    // passing the function as a reference 
                    click={this.switchHandler.bind(this, 'Max')} 
                    change={this.changeHandler}>My hobbies: Racing</Person> */}

                </div> 
            );
        }
        return(
            <div className='App'>
                <h1>Hi, I am a React App</h1>
                <p>This is really working</p>
                <button 
                style={style}
                onClick={this.togglePersonHandler}>Switch Name</button>
                
                {persons}
                
            </div>

        )
    }
}

export default App;


