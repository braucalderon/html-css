import React from 'react';
import '../index.css'

const char = (props) => {
    
    return(
        // component that draws a square for each character
        <div className='char' onClick={props.clicked}>
            {props.character}
        </div>
    )
};
export default char;