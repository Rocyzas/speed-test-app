// src/App.js
import React, { useState } from 'react';
import TextDisplay from './components/TextDisplay';
import DifficultySelection from './components/DifficultySelection';
import UserInputForm from './components/UserInputForm';

function App() {
  const [prompt, setPrompt] = useState('');

  return (
    <div>
      <DifficultySelection setPrompt={setPrompt} />
      <TextDisplay text={prompt} />
      <UserInputForm />
      
    </div>
  );
}

export default App;
