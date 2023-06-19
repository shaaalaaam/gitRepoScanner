import React, { useState } from "react";
import axios from "axios";
import "./App.css";

interface Repository {
  name: string;
  url: string;
}

function App() {
  const [githubUrl, setGithubUrl] = useState("");
  const [repository, setRepository] = useState<Repository | null>(null);
  const [complexityScore, setComplexityScore] = useState<number | null>(null);

  const analyzeRepository = async (url: string) => {
    try {
      const response = await axios.post("http://localhost:5000/api/analyze", {
        url,
      });
      const { mostComplexRepository, complexityScore } = response.data;
      setRepository(mostComplexRepository);
      setComplexityScore(complexityScore);
    } catch (error) {
      console.error(error);
    }
  };

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    analyzeRepository(githubUrl);
  };

  return (
    <div className="container">
      <h1>GitHub Repository Analyzer</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="githubUrl">Enter GitHub URL:</label>
        <input
          type="text"
          id="githubUrl"
          placeholder="https://github.com/username/repository"
          value={githubUrl}
          onChange={(e) => setGithubUrl(e.target.value)}
        />
        <button type="submit">Analyze</button>
      </form>
      {repository && (
        <div id="resultContainer">
          <h2>Most Complex Repository:</h2>
          <p>Name: {repository.name}</p>
          <p>
            URL: <a href={repository.url}>{repository.url}</a>
          </p>
          <p>Complexity Score: {complexityScore}</p>
        </div>
      )}
    </div>
  );
}

export default App;
