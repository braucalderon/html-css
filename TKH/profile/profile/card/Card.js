import Link from 'next/link'
import styles from './card.module.css'

const card = (props) => (
    <div className={styles.card} >
    <style jsx>{`
       a {
           color: white;
           margin-left: 1.5rem;
           margin-right: 1.5rem;
           margin-bottom: 1rem;
           font-size: 2.5rem;

       }
       a:hover{
           font-size: 2.6rem;
           color: rgb(50, 55, 63);
       }
       @media (max-width: 750px) {
        a{
            font-size: 2rem;
        }
    }
      
    `}</style>
    <script src="https://kit.fontawesome.com/9d6c6e6009.js" crossOrigin="anonymous"></script>
    <div className={styles.inner_card}>
        {/* Front of the card */}
        <div className={styles.front}>
            <img className={styles.img} src={props.img} alt='project'/>
            <p className={styles.p_title}>{props.title}</p>
            
        </div>
        {/* Back of the card */}
        <div className={styles.back}>
            <p className={styles.p_titleBack}>{props.title_back}</p>
            <p className={styles.p}>{props.info}</p>
            <p className={styles.p}>{props.info1}</p>
            <p className={styles.p}>{props.info2}</p>
                
            <div className={styles.align_icon} >
                <p className={styles.p_moreInfo} >Click for more info</p>
                <div className={styles.icons}>
                   
                    <a href='https://www.linkedin.com/in/brauliocalderon18/' target="_blank" className='fab fa-linkedin-in'></a>
                    
                    
                    <a href={props.project_link} target="_blank" className='fab fa-github'></a>
                </div>
                
            </div>
                
            
        </div>
    </div>
    </div>
)
export default card;