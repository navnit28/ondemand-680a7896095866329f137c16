
import requests

# Replace these with your actual values
API_KEY = "<replace_api_key>"
EXTERNAL_USER_ID = "<replace_external_user_id>"
QUERY = "Put your query here"

# Create Chat Session
create_session_url = "https://api.on-demand.io/chat/v1/sessions"
create_session_headers = {
    "apikey": API_KEY
}
create_session_body = {
    "agentIds": [],
    "externalUserId": EXTERNAL_USER_ID
}

create_session_response = requests.post(create_session_url, headers=create_session_headers, json=create_session_body)

if create_session_response.status_code == 201:
    session_id = create_session_response.json().get('data', {}).get('id')
    print(f"Session created with ID: {session_id}")

    # Submit Query
    submit_query_url = f"https://api.on-demand.io/chat/v1/sessions/{session_id}/query"
    submit_query_headers = {
        "apikey": API_KEY
    }
    submit_query_body = {
        "endpointId": "predefined-openai-gpt4.1",
        "query": QUERY,
        "agentIds": [
            "plugin-1713962163", "plugin-1745475776", "plugin-1730662083",
            "plugin-1722260873", "plugin-1713954536", "plugin-1713958591",
            "plugin-1713958830", "plugin-1713961903", "plugin-1713967141"
        ],
        "responseMode": "sync",
        "reasoningMode": "medium"
    }

    submit_query_response = requests.post(submit_query_url, headers=submit_query_headers, json=submit_query_body)

    if submit_query_response.status_code == 200:
        print("Query submitted successfully.")
        print("Response:", submit_query_response.json())
    else:
        print(f"Failed to submit query. Status Code: {submit_query_response.status_code}")
else:
    print(f"Failed to create session. Status Code: {create_session_response.status_code}")
