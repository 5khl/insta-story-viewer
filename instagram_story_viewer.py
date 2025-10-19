import requests

def get_instagram_stories(access_token):
    url = "https://graph.instagram.com/me/stories"
    params = {
        'access_token': access_token
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        stories = response.json()
        return stories
    else:
        print(f"Error retrieving stories: {response.status_code}")
        return None

# Example usage
if __name__ == "__main__":
    access_token = "YOUR_ACCESS_TOKEN"  # Replace with your access token
    stories = get_instagram_stories(access_token)
    if stories:
        print("Retrieved stories:", stories)