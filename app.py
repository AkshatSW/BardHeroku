import google.generativeai as genai

# Store your API key directly as a string (replace with your actual key)
YOUR_API_KEY = "XXX"

# Configure the API connection with your key
genai.configure(api_key=YOUR_API_KEY)

# Load the Gemini Pro model
model = genai.GenerativeModel('gemini-pro')

# Send a request to Gemini Pro
response = model.generate_content("write me a poem about rain in 2 lines")
print(response.text)

