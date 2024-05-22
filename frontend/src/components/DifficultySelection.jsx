import React, { useState, useEffect, useCallback } from 'react';

function DifficultySelection({ setPrompt }) {
  const [difficulty, setDifficulty] = useState('easy');

  const handleDifficultyChange = (event) => {
    setDifficulty(event.target.value);
  };

  const fetchPrompt = useCallback(async () => {
    try {
      const response = await fetch(`http://127.0.0.1:5000/api/difficulty/${difficulty}`);
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      console.log(data);
      setPrompt(data.prompt);
    } catch (error) {
      console.error('Fetch error:', error);
      setPrompt('Error fetching prompt.');
    }
  }, [difficulty, setPrompt]);

  useEffect(() => {
    fetchPrompt();
  }, [fetchPrompt]);

  return (
    <div>
      <h2>Select Difficulty:</h2>
      <select value={difficulty} onChange={handleDifficultyChange}>
        <option value="easy">Easy</option>
        <option value="medium">Medium</option>
        <option value="hard">Hard</option>
      </select>
    </div>
  );
}

export default DifficultySelection;
