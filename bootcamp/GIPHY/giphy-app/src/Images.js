import React from 'react';

const images = (props) =>{
    const result = props.items
    return(
        result.map(item => (
            <div className='container-image'>
                <div key={item.id} className='image-result'>
                <br/>
                <p className='image-title'>{item.title}</p>
                <br/>
                <img  className='image' src={item.images.original.url} alt='' height='250' width='250'/>
                </div>
         
            </div>
        ))
            

    )
    
        
        
    
}
export default images;