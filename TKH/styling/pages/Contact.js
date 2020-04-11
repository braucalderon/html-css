
import React, {useState} from 'react'
import Link from 'next/link'
import Header from '../components/Header'
import Form from './Form'
import styles from './Contact.module.css'



export default function Contact() {

    const [formState] = useState ({
        form_info: [
            {first: ' '},
            {last: ' '},
            {address: ' '},
            {state: ' '},
            {county: ' '},
            {zipcode: ' '}
            
        ],
    })

    return(
        <div>

        <style global jsx>{` 

                body {
                    padding: 0;
                    margin: 0;
                }         
                a {
                    text-decoration: none;
                }
        `}
        </style>


        <Header />
        {/* <p> This is contact page</p> */}
            <div className={styles.col} >

                <div className={styles.container_contact} >
                        
                        <section className={styles.front} >
                            <section className={styles.inner}>
                                <section className={styles.p}>
                                    <a className={styles.contact_center} >click here for the form</a>
                                </section>
                            </section>
                            
                        </section>
                        <section className={styles.back}>
                            <section className={styles.inner}>
                                <section className={styles.p}>
                                    <p>
                                        <Form
                                            first={formState.form_info[0].first}
                                            last={formState.form_info[0].last}
                                            address={formState.form_info[0].address}
                                            city={formState.form_info[0].city}
                                            state={formState.form_info[0].state}
                                            zipcode={formState.form_info[0].zipcode}>
                                            
                                        </Form>
                                    </p>
                                    
                                </section>
                                
                            </section>
                        </section>

                </div>
            </div>          
        </div>
    )
}

