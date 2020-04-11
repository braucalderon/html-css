import React, { useState } from 'react';

import UserOutput from './components/UserOutput';
import UserInput from './components/UserInput';

const App = (props) => {
  const [userState, setUser] = useState({
    user:[
      {username: 'Tom'}
    ],
  })


  const changeHandler = (event) => {
    setUser({
      user:[
        {username: event.target.value}
      ]
    })
  }

  return (
    <div>
      <UserInput changed={changeHandler}
      name={userState.user[0].username}></UserInput>
      {/* <button onClick={changeHandler}>Submit</button> */}
      <UserOutput user={userState.user[0].username} ></UserOutput>
      <UserOutput user={userState.user[0].username} ></UserOutput>
    </div>
  )

}
export default App;
