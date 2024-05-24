import React, { useState, useEffect, useCallback } from 'react';
import './DifficultySelection.css';

function DifficultySelection({ setPrompt }) {
  const [difficulty, setDifficulty] = useState('easy');

  const handleDifficultyChange = async (newDifficulty) => {
    setDifficulty(newDifficulty);
    await fetchPrompt(newDifficulty);
  };

  const fetchPrompt = useCallback(async (difficulty) => {
    try {
      const response = await fetch(`http://127.0.0.1:5000/api/difficulty/${difficulty}`, {
        credentials: 'include'
      });
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
  }, [setPrompt]);

  useEffect(() => {
    fetchPrompt(difficulty);
  }, [fetchPrompt, difficulty]);

  return (
    <div className="difficulty-selection">
      <h2>Select Difficulty:</h2>
      <div className="difficulty-buttons">
        <button onClick={() => handleDifficultyChange('easy')}>Easy</button>
        <button onClick={() => handleDifficultyChange('medium')}>Medium</button>
        <button onClick={() => handleDifficultyChange('hard')}>Hard</button>
      </div>
    </div>
  );
}

export default DifficultySelection;
