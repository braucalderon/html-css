import React from 'react';
import './index.css';

const input_  = (props) => {
    return (
        <div className='style'>
            <p>{props.p} {props.len}</p>
            <input type='text' onChange={props.changed} value={props.text}/>
        </div>
    )

}
export default input_;