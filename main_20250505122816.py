
import requests

# Replace with your actual API key and external user ID
API_KEY = "<replace_api_key>"
EXTERNAL_USER_ID = "<replace_external_user_id>"

# Create Chat Session
def create_chat_session():
    url = "https://api.on-demand.io/chat/v1/sessions"
    headers = {
        "apikey": API_KEY
    }
    body = {
        "agentIds": [],
        "externalUserId": EXTERNAL_USER_ID
    }
    
    response = requests.post(url, headers=headers, json=body)
    
    if response.status_code == 201:
        session_id = response.json().get('data', {}).get('id')
        return session_id
    else:
        raise Exception(f"Failed to create chat session: {response.status_code} {response.text}")

# Submit Query
def submit_query(session_id, query):
    url = f"https://api.on-demand.io/chat/v1/sessions/{session_id}/query"
    headers = {
        "apikey": API_KEY
    }
    body = {
        "endpointId": "predefined-openai-gpt4.1",
        "query": query,
        "agentIds": [
            "plugin-1713962163", "plugin-1745475776", "plugin-1730662083",
            "plugin-1722260873", "plugin-1713954536", "plugin-1713958591",
            "plugin-1713958830", "plugin-1713961903", "plugin-1713967141"
        ],
        "responseMode": "sync",
        "reasoningMode": "medium"
    }
    
    response = requests.post(url, headers=headers, json=body)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to submit query: {response.status_code} {response.text}")

# Example usage
try:
    session_id = create_chat_session()
    print(f"Session ID: {session_id}")
    
    query = "Put your query here"
    response = submit_query(session_id, query)
    print("Query Response:", response)
except Exception as e:
    print(e)
