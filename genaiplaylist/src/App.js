import React, {useState, useEffect} from 'react'

function App() {
  
  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("/home")
        .then(res => {
            console.log("Response:", res); // Log the response to see what you are getting
            return res.json();
        })
        .then(data => {
            setData(data);
            console.log(data);
        })
        .catch(error => console.error("Error fetching data:", error));
}, []);

return (
  <div>
    {typeof data.home === 'undefined' ? (
      <p>Loading...</p>
    ) : (
      data.home.map((item, i) => (
        <p key={i}>{item}</p>  // Display the items as expected
      ))
    )}
  </div>
);
}

export default App