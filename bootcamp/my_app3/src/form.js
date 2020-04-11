import React,{Component} from 'react';
// import ReactDOM from 'react-dom';
// import logo from './logo.svg';
import './App.css';

class Form extends Component{
  constructor(props){
    super(props);
    this.state = {username: ''}
    
  }

  myChangeHandler = (event) =>{
    this.setState({username: event.target.value})
  }
  mySubmitHandler = (event) =>{
      event.preventDefault();
      // alert(`username:  ${this.state.username}`)
      this.setState({username: event.target.value})
      
  }
  
  render(){
     return (
       <form onSubmit = {this.mySubmitHandler} >
           <h1> hello I cannot read any information</h1>
           <p>Please enter your name</p>
           <input type="text"  onChange = {this.myChangeHandler} ></input>
            <h3>This is you name: </h3>
            <input type="submit" ></input>

            

            {/* {this.state.username} */}

            <div>
              <h1> {this.state.username} </h1>
            </div>

       </form>

       
      

     ); 
  }
}

export default Form;