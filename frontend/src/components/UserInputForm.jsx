// UserInputForm.jsx
import React, { useState, useEffect } from 'react';
import './UserInputForm.css'; // Import your CSS file

function UserInputForm() {
  const [userInput, setUserInput] = useState('');
  const [response, setResponse] = useState(null);
  const [error, setError] = useState(null);
  const [isTyping, setIsTyping] = useState(false);
  const [remainingTime, setRemainingTime] = useState(30);
  const [timer, setTimer] = useState(null);

  const handleChange = (event) => {
    setUserInput(event.target.value);
    if (!isTyping) {
      setIsTyping(true);
    }
  };

  const handleSubmit = async () => {
    clearTimeout(timer);
    setIsTyping(false);
    try {
      const response = await fetch(`http://127.0.0.1:5000/api/userInput`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input: userInput }),
        credentials: 'include',
      });
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      setResponse(data);
      setError(null);
    } catch (error) {
      console.error('Fetch error:', error);
      setError('An error occurred while fetching data');
      setResponse(null);
    }
  };

  useEffect(() => {
    if (isTyping) {
      const newTimer = setTimeout(() => {
        handleSubmit();
      }, remainingTime * 1000);
      setTimer(newTimer);

      return () => clearTimeout(newTimer);
    }
  }, [isTyping, userInput, remainingTime]);

  useEffect(() => {
    if (isTyping && remainingTime > 0) {
      const interval = setInterval(() => {
        setRemainingTime((prevTime) => prevTime - 1);
      }, 1000);

      return () => clearInterval(interval);
    }
  }, [isTyping, remainingTime]);

  return (
    <div className="user-input-form">
      <label>
        Enter Your Input:
        <input type="text" value={userInput} onChange={handleChange} />
      </label>
      <button onClick={handleSubmit}>Submit</button>

      {response && <p>Response: {JSON.stringify(response)}</p>}
      {error && <p>Error: {error}</p>}
      {isTyping && remainingTime > 0 && <p>Time left: {remainingTime} seconds</p>}
      {remainingTime === 0 && <p>Sent Submit due Time</p>}
    </div>
  );
}

export default UserInputForm;
