
const axios = require('axios');
const https = require('https');

const API_KEY = '<replace_api_key>';
const EXTERNAL_USER_ID = '<replace_external_user_id>';
const AGENT_IDS = [
  'agent-1713962163',
  'agent-1745475776',
  'agent-1730662083',
  'agent-1722260873',
  'agent-1713954536',
  'agent-1713958591',
  'agent-1713958830',
  'agent-1713961903',
  'agent-1713967141'
];

async function createChatSession() {
  const url = 'https://api.on-demand.io/chat/v1/sessions';
  const headers = {
    'apikey': API_KEY,
    'Content-Type': 'application/json'
  };
  const body = {
    agentIds: [],
    externalUserId: EXTERNAL_USER_ID
  };
  const response = await axios.post(url, body, { headers });
  return response.data.data.id;
}

async function submitQuery(sessionId, query) {
  const url = `https://api.on-demand.io/chat/v1/sessions/${sessionId}/query`;
  const headers = {
    'apikey': API_KEY,
    'Content-Type': 'application/json'
  };
  const body = {
    endpointId: 'predefined-openai-gpt4.1',
    query: query,
    agentIds: AGENT_IDS,
    responseMode: 'sync',
    reasoningMode: 'medium'
  };
  const response = await axios.post(url, body, { headers });
  return response.data;
}

(async () => {
  try {
    const sessionId = await createChatSession();
    const query = 'Put your query here';
    const result = await submitQuery(sessionId, query);
    console.log(result);
  } catch (error) {
    if (error.response) {
      console.error('Error:', error.response.status, error.response.data);
    } else {
      console.error('Error:', error.message);
    }
  }
})();
