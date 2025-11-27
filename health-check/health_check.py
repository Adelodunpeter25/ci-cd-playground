import requests
import sys

def check_health():
    api_endpoint = "https://content-hub-api.vercel.app/health"
    
    try:
        response = requests.get(api_endpoint, timeout=30)
        if response.status_code == 200:
            print(f"✅ Health check passed: {api_endpoint}")
            return True
        else:
            print(f"❌ Health check failed: {api_endpoint} returned {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Health check failed: {api_endpoint} - {str(e)}")
        return False

if __name__ == "__main__":
    if not check_health():
        sys.exit(1)
