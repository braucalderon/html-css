import React, { useState } from 'react';
import './App.css';
import Person from './Person/Person';

// React Hooks

const hooks = props => {

  const [personsState, setPerson ] =  useState({
    persons: [
      {name:'Max', age:28},
      {name: 'Manu', age:29},
      {name:'Stephanie', age:32}
    ],
    // otherState: 'some other value'
  });

  const[otherState, setOtherState] = useState('some other value')
  console.log(personsState, otherState);


  const switchHandler = () =>{
    // console.log('was clicked');
    setPerson({
      persons:[
        {name:'Tomas', age:28},
        {name: 'Manu', age:29},
        {name:'Stephanie', age:41}
      ],
      // otherState: personsState.otherState 
    })
  }
  
    return (
      <div className="App">
        <h1>Hi, I am a React App</h1>
        <p>This is working</p>
        <button onClick={switchHandler} >Switch Name</button>
        <Person name={personsState.persons[0].name} age={personsState.persons[0].age}> </Person>
        <Person name={personsState.persons[1].name} age={personsState.persons[1].age}>My Hobbies: Racing</Person>
        <Person name={personsState.persons[2].name} age={personsState.persons[2].age}/>
        
      </div>
    );
    // return React.createElement('div', {className :'App'} ,React.createElement('h1',null,'Does this work now?'))
  }


export default hooks;



