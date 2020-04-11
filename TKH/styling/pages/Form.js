
import styles from './Contact.module.css'
import Link from 'next/link'

const form = props => {

    

    return (
        <div className={styles.container_form} >
            
            <div className={styles.container_form1} >
                <p className={styles.p} >First Name</p>
                <input type='text' 
                className={styles.input} 
                value={props.first}
                />
                <p className={styles.p} >Last Name</p>
                <input type='text' className={styles.input}
                value={props.last}
                />
                {/* <p className={styles.p} >Company Name</p>
                <input type='text' className={styles.input}
                value={props}
                /> */}
                <p className={styles.p} >Address</p>
                <input type='text' className={styles.input}
                value={props.address}
                />
                <p className={styles.p} >City</p>
                <input type='text' className={styles.input}
                value={props.city}
                />
                <p className={styles.p} >State</p>
                <input type='text' className={styles.input}
                value={props.state}
                />
                <p className={styles.p} >Zip Code</p>
                <input type='text' className={styles.input}
                value={props.zipcode}
                />
            </div>

            
        </div>
    )
}
export default form;