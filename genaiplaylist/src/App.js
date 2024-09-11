import React, { useState } from 'react';
import './App.css';

function App() {
    const [data, setData] = useState([{}]);
    const [search, setSearch] = useState("");
    const [loading, setLoading] = useState(false);

    // Function to handle the search button click
    const handleSearch = () => {
        if (search.trim() === "") {
            // Don't trigger search for empty input
            return;
        }
        setLoading(true); // Start loading
        fetch(`/home?search=${encodeURIComponent(search)}`)
            .then(res => res.json())
            .then(data => {
                setData(data);
                setLoading(false); // Stop loading after data fetch
            })
            .catch(error => {
                console.error("Error fetching data:", error);
                setLoading(false); // Stop loading if there's an error
            });
    };

    // Allow search on "Enter" key
    const handleKeyDown = (event) => {
        if (event.key === "Enter") {
            handleSearch();
        }
    };

    return (
        <div className="app-container">
            <section className="hero-section">
                <h1 className="main-title">Discover Amazing Content on YouTube</h1>
                <p className="subtitle">Explore tutorials, how-tos, and more with a simple search.</p>

                {/* Search Bar */}
                <div className="search-container">
                    <input
                        className="search-input"
                        type="text"
                        value={search}
                        onChange={(e) => setSearch(e.target.value)}
                        onKeyDown={handleKeyDown} // Trigger search on "Enter"
                        placeholder="Enter a search query"
                    />
                    <button className="search-button" onClick={handleSearch}>
                        Search
                    </button>
                </div>
            </section>

            {/* Display YouTube Thumbnails or Loading */}
            <main className="video-section">
                <div className="videos-container">
                    {loading ? (
                        <div className="loading-spinner"></div> // Show spinner when loading
                    ) : (
                        data.home && data.home.length > 0 && data.home.map((item, i) => {
                            const videoId = item.split("v=")[1];
                            const thumbnailUrl = `https://img.youtube.com/vi/${videoId}/0.jpg`;

                            return (
                                <div className="video-card" key={i}>
                                    <a href={item} target="_blank" rel="noopener noreferrer">
                                        <img
                                            className="video-thumbnail"
                                            src={thumbnailUrl}
                                            alt={`Video ${i}`}
                                        />
                                    </a>
                                </div>
                            );
                        })
                    )}
                </div>
            </main>
        </div>
    );
}

export default App;
