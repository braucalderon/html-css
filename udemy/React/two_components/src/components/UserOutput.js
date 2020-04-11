import React from 'react';
import './userOutput.css';


const userOutput = (props) => {

    return(
        <div className="output" >
            <p> {props.user} did a cruise ship evacuation: Another 99 cases have been confirmed aboard the quarantined Diamond Princess cruise ship in Japan.</p>
            <p>The man behind all this {props.user}, who was diagnosed before his wife, flew on Hawaiian Airlines flight HA265 from Kahului, Hawaii, to Honolulu on Feb. 3, 
            in addition to flying home on Delta flight 611 from Honolulu to Nagoya on Feb. 6 with his wife.</p>
        </div>
    )
}

export default userOutput;