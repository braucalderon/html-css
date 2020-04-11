import Link from 'next/link';
import styles from './Example.module.css'


const Header = () =>(
    <div className={styles.headerContainer1} >
    <link src="https://kit.fontawesome.com/9d6c6e6009.js" crossorigin="anonymous"></link>
        <Link href='/'>
            <a className={styles.headerContainer2}>Home</a>
        </Link>
       
    </div>
)

export default Header;