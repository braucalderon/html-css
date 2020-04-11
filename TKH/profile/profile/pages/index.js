import Link from 'next/link'
import style from './index.module.css'

const Home = () => {
  return(
    <div>
      <style global jsx>{`
        body {
          padding: 0;
          margin: 0;
          background: black;
          
        }
        h1 {
          color: white;
          font-size: 3rem;
          opacity: .4;
        
        }
        @media (max-width: 750px){
          h1{
            font-size: 1.8rem
          }
          
        }
      `} </style>


      
      <div className={style.home_page}>
        <div className={style.h1}></div>
        <Link href='/projects/Projects'>
          <h1 className={style.linkup} >Software Developer</h1>
        </Link>
        
        
        
        
      </div>
      
      


    </div>
  )
}
export default Home;
