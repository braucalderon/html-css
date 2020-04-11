import Link from 'next/link';
import fetch from 'isomorphic-unfetch';
import { Component } from 'react';
import axios from 'axios';


class Index extends Component{
    static async getInitialProps() {

        const axios = await fetch('https://api/tvmaze.com/search/shows?q=batman');
        const data = await res.json();
  
        console.log(`Show data fetch. Count: ${data.length}`);

        return {

            shows: data.map(entry => entry.show)
            }

    }
}
// const Index = props => (

//     <Layout>
//       <h1>Batman TV Shows</h1>
//       <ul>
//         {props.shows.map(show => (
//           <li key={show.id}>
//             <Link href='/p/[id]' as={`/p/${show.id}`}>
//               <a>{show.name} </a>
//             </Link>
//           </li>
//         ))}
//       </ul>
//     </Layout>
//   );


//  Index.getInitialProps =  static async function(){
  
    // const config = { httpsAgent: new HttpsProxyAgent(process.env.https_proxy)
    // }
    // const res = await axios.get('https://api/tvmaze.com/search/shows?q=batman')
    // const data = await res.join();
    
   
//     const res = await fetch('https://api/tvmaze.com/search/shows?q=batman');
//     const data = await res.json();
  
//     console.log(`Show data fetch. Count: ${data.length}`);
  
//     return {
//       shows: data.map(entry => entry.show)
//     }
    
//   }



export default Index;