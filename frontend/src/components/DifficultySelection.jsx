import React, { useState, useEffect } from 'react';

function DifficultySelection() {
  const [difficulty, setDifficulty] = useState(null);
  const [prompt, setPrompt] = useState(null);

  const handleDifficultyChange = (event) => {
    setDifficulty(event.target.value);
  };

  const fetchPrompt = async () => {
    if (difficulty) {
      const response = await fetch(`/api/difficulty/${difficulty}`);
      const data = await response.json();
      setPrompt(data.prompt);
    }
  };

  useEffect(() => {
    fetchPrompt();
  }, [difficulty]);

  return (
    <div>
      <h2>Select Difficulty:</h2>
      <select value={difficulty} onChange={handleDifficultyChange}>
        <option value="easy">Easy</option>
        <option value="medium">Medium</option>
        <option value="hard">Hard</option>
      </select>
      <br />
      {prompt && <p>Prompt: {prompt}</p>}
    </div>
  );
}

export default DifficultySelection;
