import React from 'react';

// function


const info = (props) => {

    console.log(props.name)
    return(
        <div>
            <p onClick={props.clickInfo} >I am {props.name} and not {props.age} </p>
            <p>{props.children} </p>
            <input   type='text' onChange={props.changed} ></input>
        </div>
    )
};
export default info;