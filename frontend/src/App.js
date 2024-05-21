import React, { useState } from 'react';

function App() {
  const [difficulty, setDifficulty] = useState('easy');

  const fetchPrompt = async () => {
    const response = await fetch(`http://127.0.0.1:5000/api/difficulty/${difficulty}`);
    const data = await response.json();
    console.log(data.prompt);
  };

  return (
    <div>
      <select value={difficulty} onChange={(e) => setDifficulty(e.target.value)}>
        <option value="easy">Easy</option>
        <option value="medium">Medium</option>
        <option value="hard">Hard</option>
      </select>
      <button onClick={fetchPrompt}>Get Prompt</button>
    </div>
  );
}

export default App;