import styles from './projects.module.css'
import React, { useState } from 'react'
import Card from '../../card/Card'
import Header from '../../Header/Header'



const Projects = props => {
    const [cardFrontState, setCardFront] = useState({
        card:[
            // Database
            {img:'/img/database_panel.png', title:'Database Application',
            github:'https://github.com/braucalderon/Database', 
            title_back:'Description',
            info:'Develop a detailed system customizing an overnight policy.',
            info1:'The application allows the user to perform standard CRUD operation.',
            info2:'Increase efficiency by 70% overall by decreasing the number of steps.',
            id: 'card_1'},
            // Android Development
            {img:'/img/score_counter1.gif', title:'Android Mobile Application Development',
            github:'https://github.com/braucalderon/andriod_class',
            title_back:'Objectives',
            info:'Create user interface, activities and handle events, work with threads and files.',
            info1:'Work with menus, tabs, preference and settings, use themes, layout and styles.',
            info2:'Store data using SQLite database.',
            id: 'card_2'},
            // HTML & CSS
            {img:'/img/hotel_1.gif', title:'Comprehensive course on HTML & CSS',
            github:'https://github.com/braucalderon/html-css',
            title_back:'Fundamentals',
            info:'Non-semantics elements and new semantics elements in HTML 5.',
            info1:'Responsive Design, Flexbox & CSS Grid.',
            info2:'Sticky Menus, Overlays, Form Styling, Sass CSS Pre-compiler & Landing pages.',
            id: 'card_3'}

        ]
        
    })
    
    return(

        <div>
            <Header/>
            <div className={styles.general} >
                
                {cardFrontState.card.map(card => {
                    return <Card
                    // front
                    img={card.img}
                    title={card.title}
                    //back
                    project_link={card.github}
                    title_back={card.title_back}
                    info={card.info}
                    info1={card.info1}
                    info2={card.info2}
                    key={card.id} />

                })}
                
                {/* <Card 
                // front
                img={cardFrontState.card[0].img} 
                title={cardFrontState.card[0].title} 
                // back
                project_link={cardBackState.card[0].github}
                title_back={cardBackState.card[0].title_back}
                info={cardBackState.card[0].info}
                info1={cardBackState.card[0].info1}
                info2={cardBackState.card[0].info2}
                /> */}
                
            </div>
            
        </div>
    )
        
}
export default Projects;