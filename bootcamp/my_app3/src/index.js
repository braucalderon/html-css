import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Car from './App'
import Form from './form'
// import App from './App';
import * as serviceWorker from './serviceWorker';

// class Person extends Component{
//     constructor(){
//         super();
//         this.state = {name: 'Tinda',
//     age: 80, email: 'gmail' }
//     }
//     render(){
//         return <h2>I am {this.state.name} {this.state.age} {this.state.email} </h2>
//     }
// }
ReactDOM.render(<Car color='blue' />, document.getElementById('root'));
ReactDOM.render(<Form/>,document.getElementById('root1'))
// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
