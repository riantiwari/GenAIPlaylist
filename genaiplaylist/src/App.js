import React, { useState, useEffect } from 'react';
import './App.css'; // Add this to import your CSS file

function App() {
  const [data, setData] = useState([{}]);

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

  // Extract video ID from YouTube link
  const extractVideoId = (url) => {
    const urlObj = new URL(url);
    return urlObj.searchParams.get("v");
  };

  return (
    <div className="app">
      {typeof data.home === 'undefined' ? (
        <p>Loading...</p>
      ) : (
        <div className="playlist-container">
          {data.home.map((item, i) => {
            const videoId = extractVideoId(item);
            return (
              <div className="playlist-item" key={i}>
                <a href={item} target="_blank" rel="noopener noreferrer">
                  <img
                    className="thumbnail"
                    src={`https://img.youtube.com/vi/${videoId}/hqdefault.jpg`}
                    alt={`Thumbnail of ${item}`}
                  />
                  <p>{item}</p>
                </a>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}

export default App;
