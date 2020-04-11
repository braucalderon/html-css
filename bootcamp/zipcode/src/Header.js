import React, { Component } from 'react';
// import './App.css';
// import ZipCode from './ZipCode';
// import Info from './Info';
// import Input from './Input';



// main code
class Header extends Component{
    
    constructor(props){
        super(props);
        this.state = {
            items:[],
            zipcode: ' ',
            city: ' '
        }
        // this.state = {zipcode: ''}

    }//end constructor

   

    // componentDidMount(){
    //     fetch(`http://ctp-zip-api.herokuapp.com/zip/${this.state.zipcode}`)

    //     .then(results => results.json())
    //     .then(json => {this.setState({items: json})})
    // }


    //  functions
   
    fetchDataZip(){
        fetch(`http://ctp-zip-api.herokuapp.com/zip/${this.state.zipcode}`)
        .then(results => results.json())
        .then(json => {this.setState({items: json})})
        
    }
    SubmitHandler = (event) => {
        event.preventDefault();
        // this.setState({zipcode:event.target.value})
        this.fetchDataZip()
    }

    ChangeHandler = (event) => {
        this.setState({zipcode:event.target.value})
    }

    // swicthHandler = (event) => {
    //     event.preventDefault();

    //     // console.log("test");
    //     // this is an array
    //     this.setState = ({
    //         info:[
    //             {name: event.target.value, age:27},
    //             {information: 'too'}
    //         ]
    //     })
       
    // }

    render(){

       

        return(
            <section id='container'>
                <div id="container-header" >
                <form id="header-form" onSubmit = {this.SubmitHandler} >

                    <p>Enter the Zipcode:  </p>
                    <input id="header-text" type="text" onChange = {this.ChangeHandler} ></input>
                    <input id="submit-header" type="submit" onSubmit={this.SubmitHandler}></input>
                    
                </form>

                </div>

            
               
                <div id='container-result'>
                {/* Button */}
                {/* transfer a property from one function to another */}
                {/* <button onClick={this.swicthHandler}>Transfer</button>
                <ZipCode name ='cosa'></ZipCode>
                <Info name={this.state.info[0].name} age ={this.state.info.name} clickInfo={this.swicthHandler.bind(this,"To")}
                changed={this.swicthHandler} >My Hobbies: Racing</Info> */}

                {/* <ZipCode name={this.state.username}  ></ZipCode>
                <Input changed={this.usernameChangeHandler}></Input> */}
                <p id='title' >Cities by ZipCode</p>
                {this.state.items.map(item => (
                     
                    <ul>
                       
                        <br/>
                        <li key={item.RecordNumber}>{item.City} <br/> 
                        <p className='subtitle' >State: {item.State} </p>
                        <p className='subtitle' >LocationType: {item.LocationType} </p>
                        <p className='subtitle' >ZipCodeType: {item.ZipCodeType} </p>
                        <p className='subtitle' >Location: {item.Location} </p>
                        </li>
                    </ul>
                    
                    

                ))}

                </div>
            </section>
        ) //end return
    } //end render

} //end class
export default Header;
