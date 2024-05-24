import React, { useState } from 'react';
import './App.css';
import TextDisplay from './components/TextDisplay';
import DifficultySelection from './components/DifficultySelection';
import UserInputForm from './components/UserInputForm';

function App() {
  const [prompt, setPrompt] = useState('');

  return (
    <div className="app-container">
      <DifficultySelection setPrompt={setPrompt} />
      <TextDisplay text={prompt} />
      <UserInputForm />
    </div>
  );
}

export default App;
