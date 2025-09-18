'use client';

import { useEffect, useState } from 'react';

interface ChatResponse {
  response?: string;
  timestamp?: string;
  status?: string;
  error?: string;
}

const Chat = () => {
  const [data, setData] = useState<ChatResponse | null>(null);
  const [message, setMessage] = useState('');
  const [loading, setLoading] = useState(false);
  
  const sendReq = async () => {
    setLoading(true);
    try {
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message: message
        })
      });
      const res = await response.json();
      setData(res);
    } catch (error) {
      console.error('Error sending message:', error);
      setData({ error: 'Failed to send message' });
    } finally {
      setLoading(false);
    }
  };

  const testHealthEndpoint = async () => {
    try {
      const response = await fetch('/api/health');
      const res = await response.json();
      setData(res);
    } catch (error) {
      console.error('Error fetching health:', error);
    }
  };

  useEffect(() => {
    // You can call testHealthEndpoint here if you want to fetch data on component mount
    // testHealthEndpoint();
  }, []);
  
  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Chat Component</h1>
      
      <div className="mb-4">
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type your message here..."
          className="border p-2 mr-2 w-64 text-red-500"
        />
        <button 
          onClick={sendReq} 
          disabled={loading || !message.trim()}
          className="bg-blue-500 text-red-500 px-4 py-2 rounded disabled:bg-gray-300"
        >
          {loading ? 'Sending...' : 'Send Message'}
        </button>
      </div>

      <button 
        onClick={testHealthEndpoint}
        className="bg-green-500 text-red-500 px-4 py-2 rounded mr-2 mb-4"
      >
        Test Health Endpoint
      </button>
      
      {data && (
        <div className="mt-4">
          <h3 className="font-bold">Response:</h3>
          <pre className="bg-gray-900 p-4 rounded">{JSON.stringify(data, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default Chat