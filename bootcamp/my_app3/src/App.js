import React,{Component} from 'react';
// import ReactDOM from 'react-dom';
// import logo from './logo.svg';
import './App.css';

class Car extends Component{
  constructor(props){
    super(props);
    this.state = {color:'red',
  make:'toyota', year: 2020, brand: ''}
    
  }
  changeColor = () =>{
    this.setState({color:'blue'})
  }
  render(){
     return (
       <div>
       <h1>I am a {this.state.color} {this.state.make} {this.state.year - 3} car</h1> 
       <button type="button" onClick = {this.changeColor} >Change Color</button>
       </div>
      

     ); 
  }
}

export default Car;

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }


