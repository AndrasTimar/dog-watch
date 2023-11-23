import React from 'react';
import './App.css';

function App() {
  const handleClick = async () => {

    try {
      const response = await fetch('http://raspberrypi.local:8080', {
        method: 'POST',
      });

      if (!response.ok) {
        throw new Error(`Error! status: ${response.status}`);
      } else {
        console.log("SUCCESS");
      }
    } catch (err) {
      console.log(err);
    }
  };
  return (
    <div className="App">
      <header>
	    <img className="main-image" src="/smaller.jpg"/>
      <button  type="button" value="Click Me" onClick={handleClick} >Refresh</button>
      </header>
    </div>
  );
}

export default App;
