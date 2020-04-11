import Link from 'next/link';
import styles from './Example.module.css'

const Footer = () => (
    <div>
        <div className={styles.footerContainer}>
        <Link href='/'>
            <p className={styles.footerContainer1} >NYC @copy, 2020, All Rights Reserved</p>
        </Link>
        </div>
        
    </div>
    

)

export default Footer;