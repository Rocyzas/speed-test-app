// components/UserInputForm.jsx
import React, { useState } from 'react';

function UserInputForm() {
  const [userInput, setUserInput] = useState('');
  const [response, setResponse] = useState(null); // State to store response from backend
  const [error, setError] = useState(null); // State to store error message

  const handleChange = (event) => {
    setUserInput(event.target.value);
  };

  const handleSubmit = async () => {
    try {
      const response = await fetch(`http://127.0.0.1:5000/api/userInput`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input: userInput }), // Include user input in the request body
      });
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json(); // Parse response JSON
      setResponse(data); // Update state with response from backend
      setError(null); // Clear any previous error
    } catch (error) {
      console.error('Fetch error:', error);
      setError('An error occurred while fetching data'); // Set error state
      setResponse(null); // Clear any previous response
    }
  };

  return (
    <div>
      <label>
        Enter Your Input:
        <input type="text" value={userInput} onChange={handleChange} />
      </label>
      <button onClick={handleSubmit}>Submit</button>

      {response && <p>Response: {JSON.stringify(response)}</p>}
      {error && <p>Error: {error}</p>}
    </div>
  );
}

export default UserInputForm;
