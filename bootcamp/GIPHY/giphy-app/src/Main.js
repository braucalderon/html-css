import React, {Component} from 'react';
import Images from './Images';
// import './App.css';
// import Logo from './logo.png';

class Main extends Component{
    constructor(props){
        super(props);

        this.state={
            items:[],
            search: '',
            key: 'jrw5ouPx80uapcJddCsjJiOwiB2yh9FD',
            count: 7

        }
        // this.displayItems = this.displayItems.bind(this);


    }
    // componentDidMount(){
    //     console.log(this.state.key);
        
    //     fetch(`https://api.giphy.com/v1/gifs/search?api_key=${this.state.key}&limit=5`)
    //     .then(results => results.json())
    //     .then(json =>{
    //         // this.setState({items: json})
    //         // meta status 200, server check
    //         // console.log(json.data);
    //         // console.log('META', json.meta);
            
            
    //     })
    //     .catch(err => {
    //         console.error(err);
            
            
    //     })
    // }

    // functions
    fetchDataSearch(){
        // console.log(this.state.key);
        // console.log(this.state.search);
        
        fetch(`https://api.giphy.com/v1/gifs/search?q=${this.state.search}&api_key=${this.state.key}&limit=${this.state.count}`)
        .then(results => results.json())
        .then(jsonResult =>{
            
            // meta status 200, server check
           // console.log(jsonResult.data);
            //console.log('META', jsonResult.meta);
            this.setState({items: jsonResult.data})
            console.log(this.state.items);
            
            
            
        })
        .catch(err => {
            console.error(err);
            
            
        })
        
        
    }
    // functions
    submitHandler = (event) =>{
        event.preventDefault();
        this.fetchDataSearch();
        
   
    }
    changeHandler = (event) =>{
        this.setState({search:event.target.value})
    }
    


    // displayItems = () => {
    
    //    return(

    //         this.state.items.map(item =>(

    //             <div>
    //             <img src={item.images.original.url} alt=''/>
    //             </div>  
    //         ))
    //    ) 
            
    // }
//     displayItems = () => {
//         /* this.state.items.data.map(item =>
//              <ul>
//                  <li>{item.url} </li>
//              </ul>
//     )*/
//    console.log(this.state.items.data)
//     if (this.state.items.data) {
//         console.log(this.state.items.data) 
//     this.state.items.data.map(function (item){
//         console.log(item.url);
//         return (
//           <div>
//             <h1>{item.url}</h1>
//           </div>
//         );
//     });

//         //console.log(this.state.items.data)
//         //return <h1>hola</h1>

//         //
    
//     }
    
// }

    render(){
        return(
            <div className='container'>
                <div className='header'>
                    <form className='header-search' onSubmit={this.submitHandler}>
                        <p>Enter Giph Name:</p>
                        <input className='header-text' type='text' value={this.state.search} onChange={this.changeHandler}></input>
                        <button className='submit-search' type='submit'>Submit</button>
                    </form>
                </div>
                <div className='result'>

                    {/* {this.displayItems()} */}
                    {/* {this.displayItems()} */}
                    <Images items={this.state.items}></Images>

                </div>
                
            </div>
        );
    }// end render
}// end class

export default Main;
