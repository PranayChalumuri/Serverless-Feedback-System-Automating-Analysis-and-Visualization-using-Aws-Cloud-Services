import json
import boto3
import urllib.parse
import urllib3
import os

# Initialize clients
comprehend = boto3.client('comprehend')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('pranaybuklist3')
http = urllib3.PoolManager()

def lambda_handler(event, context):
    print(f"Received event: {json.dumps(event)}")
    
    # Get request details
    http_method = event.get('httpMethod', 'GET')
    path = event.get('path', '')
    query_params = event.get('queryStringParameters') or {}
    headers = event.get('headers', {})
    
    print(f"Method: {http_method}, Path: {path}, Query: {query_params}")
    
    # ===== API ENDPOINT - Returns JSON =====
    if path.endswith('/api/sentiments'):
        print("Serving API endpoint - returning JSON")
        return handle_api_proxy()
    
    # ===== DASHBOARD PAGE - Returns HTML =====
    elif path.endswith('/dashboard'):
        print("Serving dashboard page - returning HTML")
        return serve_html('success.html')
    
    # ===== STATIC HTML PAGES =====
    elif http_method == 'GET':
        # App selection page
        if query_params.get('page') == 'app_selection':
            print("Serving app selection page")
            return serve_html('app_selection.html')
        
        # Default - contact page
        else:
            print("Serving contact page")
            return serve_html('contactus.html')
    
    # ===== FORM SUBMISSIONS =====
    elif http_method == 'POST':
        try:
            # Parse form data
            body = event.get('body', '')
            if event.get('isBase64Encoded', False):
                import base64
                body = base64.b64decode(body).decode('utf-8')
            
            form_data = parse_form_data(body)
            print(f"Form data: {form_data}")
            
            # Analyze sentiment with Comprehend
            sentiment_response = comprehend.detect_sentiment(
                Text=form_data['message'],
                LanguageCode='en'
            )
            form_data['sentiment'] = sentiment_response['Sentiment']
            
            # Store in DynamoDB
            table.put_item(Item=form_data)
            
            # Return thank you page
            return serve_html('lasting.html')
            
        except Exception as e:
            print(f"Error processing form: {str(e)}")
            return error_response(f"Form processing error: {str(e)}")
    
    # ===== FALLBACK =====
    return serve_html('contactus.html')

def handle_api_proxy():
    """Fetch data from AppSync and return JSON"""
    try:
        api_url = 'https://xzeajhrezvecvohp3h52ing6i4.appsync-api.ap-south-1.amazonaws.com/graphql'
        api_key = 'da2-4mcqhrw4dzg3fat3djp5up7ksy'
        
        query = """
            query GetSentiments {
                getSentiments {
                    appName
                    sentiment
                }
            }
        """
        
        response = http.request(
            'POST',
            api_url,
            body=json.dumps({'query': query}),
            headers={
                'Content-Type': 'application/json',
                'x-api-key': api_key
            },
            timeout=10.0
        )
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': response.data.decode('utf-8')
        }
    except Exception as e:
        print(f"API Proxy Error: {str(e)}")
        return error_response(str(e))

def serve_html(filename):
    """Serve HTML files"""
    print(f"Attempting to serve: {filename}")
    try:
        # Try multiple possible paths
        possible_paths = [
            filename,
            f"./{filename}",
            f"/var/task/{filename}",
            f"/var/task/html/{filename}"
        ]
        
        html_content = None
        for path in possible_paths:
            try:
                with open(path, 'r', encoding='utf-8') as file:
                    html_content = file.read()
                    print(f"✓ Successfully loaded {filename} from {path}")
                    break
            except FileNotFoundError:
                print(f"✗ File not found at: {path}")
                continue
        
        if html_content is None:
            raise FileNotFoundError(f"Could not find {filename} in any location")
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/html; charset=utf-8',
                'Access-Control-Allow-Origin': '*'
            },
            'body': html_content
        }
    except Exception as e:
        print(f"Error serving {filename}: {str(e)}")
        return error_response(f'Could not load {filename}: {str(e)}')

def parse_form_data(body):
    """Parse URL-encoded form data"""
    # Remove any leading/trailing whitespace
    body = body.strip()
    
    # URL decode
    decoded = urllib.parse.unquote(body)
    
    # Parse key-value pairs
    data = {}
    for pair in decoded.split('&'):
        if '=' in pair:
            key, value = pair.split('=', 1)
            data[key] = value
    
    return data

def error_response(message):
    """Return error response"""
    return {
        'statusCode': 500,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({'error': message})
    }
