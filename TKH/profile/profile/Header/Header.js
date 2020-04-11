import Link from 'next/link'
import style from './header.module.css'



const Header = () => (
    <div className={style.header} >
        
        <div className={style.headerOne}>
           
            <div className={style.container} >
                <p className={style.letter_b}>B</p>
                <p className={style.letter_c}>C</p>
            </div>
            
        </div>
        <div className={style.headerOne_}>
            <div className={style.headerTwo} >
                    <Link href='/'>
                    <a className={style.act} >Home</a></Link>
                    
            </div>    

            <div className={style.headerThree}>
                <Link href='/profile/Profile'>
                <a className={style.act} >Profile</a>
                </Link>
                
            </div>

            <div className={style.headerFour}>
                <Link href='/projects/Projects'>
                <a>Portfolio</a>     
                </Link>
                
            </div>
        </div>
        
    </div>
    

)
export default Header;