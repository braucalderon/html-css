import React, { Component } from 'react';
import './index.css'
import Input from './Input';
import Validation from './Validation';
import Char from './Char/Char';

class App extends Component {
  state = {
    st: ''
  }

  changeHandler = (event) =>{
      this.setState( {st: event.target.value});
      
  }

  deleteChatHandler = (index) => {
      const text = this.state.st.split('');
      text.splice(index, 1); // removed the character clicked from the array
      const updatedText = text.join(''); // join the remaining text together
      this.setState({st: updatedText}); // update the text without the empty space
  }


  render(){
    // maps each character or letter into Char.js components square box
    // map does not touch the original array, it duplicates the same array and 
    // store it into charList
    // to slip into each character use slip() and pass an empty string as an argument
    const charList = this.state.st.split('').map((ch,index) => {
      return <Char character={ch} 
              key={index}
              clicked={()=> this.deleteChatHandler(index)}
              />;
    });

    return(
      <div>
        <Input changed={this.changeHandler} p={this.state.st}></Input>
        
        <Validation len={this.state.st.length}/>
        {charList}
        
      </div>
      
    )

  }
}
export default App;
