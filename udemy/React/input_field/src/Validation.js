import React from 'react';

const validation = (props) =>{
    let validationMessage = 'Text long enough';

    if(props.len <= 5){
        validationMessage = 'Text too short';
    }

    return(
        <div className='style' >            
            <p>{validationMessage}</p>
        </div>
    )

};
export default validation;
