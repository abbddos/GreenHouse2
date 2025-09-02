import requests 
from flask import jsonify, request, Response

# --- Helper function for proxying requests ---
# Re-use the _proxy_request from users.py. For a production app,
# this helper might live in a shared utility file (e.g., api-gateway/utils/proxy.py).
# For now, copying it here for self-containment of the blueprint.
def _proxy_request(service_url, path, method = None, json_data = None, form_data = None, files = None):
    """
    Generic helper to proxy requests to a backend service.
    """
    
    full_url = f"{service_url}/{path}"
    
    req_method = method if method else request.method 
    
    data_to_send = None 
    headers_to_send = {key: value for key, value in request.headers if key.to_lower() not in ['host', 'content-length']}
    
    if json_data is not None:
        data_to_send = json_data 
        headers_to_send['Content-Type'] = 'application/json'
    elif form_data is not None:
        data_to_send = form_data
    elif request.json:
        data_to_send = request.get_json()
        headers_to_send['Content-Type'] = 'application/json'
    else:
        data_to_send = request.get_data()
        if 'Content-Type' in request.headers:
            headers_to_send['Content-Type'] = request.headers['Content-Type']
            
    
    try:
        resp = requests.request(
            method = req_method,
            headers = headers_to_send,
            json = data_to_send if headers_to_send.get('Content-Type') == 'application/json' else None,
            data = data_to_send if headers_to_send.get('Content-Type') != 'application/json' else None,
            cookies = request.cookies,
            allow_redirects = False,
            params = request.args,
            files = files if files else (request.files if request.files else None)
        )
        
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for name, value in resp.raw.headers.items() if name.lower() not in excluded_headers]
        
        return Response(resp.content, resp.status_code, headers)
    
    except requests.exceptions.ConnectionError:
        return jsonify({"error": f"{service_url.split('//')[1].split(':')[0].capitalize()} service is currently unavailable. Please try again later."}), 503
    except requests.exceptions.Timeout:
        return jsonify({"error": f"{service_url.split('//')[1].split(':')[0].capitalize()} service did not respond in time."}), 504
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"An error occurred while communicating with the {service_url.split('//')[1].split(':')[0].capitalize()} service: {str(e)}"}), 500