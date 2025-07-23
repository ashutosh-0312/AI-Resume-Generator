# Import necessary Flask modules and other libraries
from flask import Flask, request, jsonify
from flask_cors import CORS # Used to handle Cross-Origin Resource Sharing, important for frontend-backend communication
import json # To parse JSON data
import os # To access environment variables (for API key, if needed)
import requests # To make HTTP requests to the Gemini API

# Initialize the Flask application
app = Flask(__name__)
# Enable CORS for all routes, allowing the frontend to make requests
CORS(app)

# Define the API key for the Gemini API.
# In a real-world scenario, you would load this from environment variables
# or a secure configuration management system.
# For this example, we'll leave it as an empty string, assuming the Canvas environment
# will inject it.
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "") # You can set this in your environment or directly here

@app.route('/generate', methods=['POST'])
def generate_resume_and_cover_letter():
    """
    Handles POST requests to generate a resume and cover letter using the Gemini LLM.
    It expects JSON input containing user details.
    """
    try:
        # Get JSON data from the request body
        data = request.get_json()

        # Extract user input from the request data
        name = data.get('name', '').strip()
        contact = data.get('contact', '').strip()
        job_role = data.get('jobRole', '').strip()
        skills = data.get('skills', '').strip()
        experience = data.get('experience', '').strip()
        education = data.get('education', '').strip()
        career_goals = data.get('careerGoals', '').strip()

        # Validate essential inputs
        if not all([name, job_role, skills, experience]):
            return jsonify({"error": "Please fill in at least your Name, Target Job Role, Skills, and Work Experience."}), 400

        # Construct the prompt for the LLM based on user input
        # --- UPDATED PROMPT FOR MODERN FORMAT AND QUALITY ---
        prompt = f"""Generate a professional resume and a formal cover letter in JSON format based on the following information.

        For the Resume:
        - Use a modern, clean, and highly readable plain text format suitable for today's job market.
        - Structure the resume with clear, capitalized section headings (e.g., "CONTACT INFORMATION", "SUMMARY", "WORK EXPERIENCE", "EDUCATION", "SKILLS").
        - Use consistent line breaks and indentation to separate information within sections and between different sections.
        - For Work Experience, use strong action verbs and quantify achievements where possible. Each point should be concise and impactful, starting on a new line.
        - Ensure the language is professional and concise.
        - DO NOT use any Markdown formatting like bold (**), italics (*), or bullet points with asterisks (*). Use plain text, new lines, and spaces for structure.

        For the Cover Letter:
        - Start the letter with a formal salutation: "Dear Hiring Manager,".
        - Clearly state the job role you are applying for in the opening paragraph.
        - Highlight how the user's skills and experience directly align with the job role.
        - Express enthusiasm for the role and the company.
        - Maintain a professional and persuasive tone.
        - End with a formal closing like "Sincerely," followed by the user's name.
        - DO NOT use any Markdown formatting like bold (**), italics (*), or bullet points with asterisks (*). Use plain text.

        User Information:
        Name: {name}
        Contact Information: {contact}
        Target Job Role: {job_role}
        Skills: {skills}
        Work Experience: {experience}
        Education: {education}
        Career Goals: {career_goals}

        Please ensure the output is a valid JSON object with two keys: "resume" and "coverLetter".
        Example JSON Format:
        {{
          "resume": "...",
          "coverLetter": "..."
        }}"""
        # --- END OF UPDATED PROMPT ---

        # Prepare the payload for the Gemini API request
        chat_history = [{"role": "user", "parts": [{"text": prompt}]}]
        payload = {
            "contents": chat_history,
            "generationConfig": {
                "responseMimeType": "application/json",
                "responseSchema": {
                    "type": "OBJECT",
                    "properties": {
                        "resume": {"type": "STRING"},
                        "coverLetter": {"type": "STRING"}
                    },
                    "propertyOrdering": ["resume", "coverLetter"]
                }
            }
        }

        # Define the Gemini API URL
        api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

        # Make the POST request to the Gemini API
        response = requests.post(api_url, headers={'Content-Type': 'application/json'}, json=payload)
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)

        # Parse the JSON response from the Gemini API
        result = response.json()

        # Extract the generated resume and cover letter from the API response
        if result.get('candidates') and len(result['candidates']) > 0 and \
           result['candidates'][0].get('content') and result['candidates'][0]['content'].get('parts') and \
           len(result['candidates'][0]['content']['parts']) > 0:
            
            json_string = result['candidates'][0]['content']['parts'][0]['text']
            parsed_json = json.loads(json_string) # Use json.loads to parse the string into a Python dict

            resume_text = parsed_json.get('resume', "Could not generate resume. Please try again.")
            cover_letter_text = parsed_json.get('coverLetter', "Could not generate coverLetter. Please try again.")

            # Return the generated content as JSON
            return jsonify({"resume": resume_text, "coverLetter": cover_letter_text})
        else:
            # Handle cases where the API response structure is unexpected
            return jsonify({"error": "Unexpected API response structure or no content generated."}), 500

    except requests.exceptions.RequestException as e:
        # Catch network-related errors or bad HTTP responses from the API
        print(f"API request error: {e}")
        return jsonify({"error": f"Failed to connect to the AI service: {e}"}), 500
    except json.JSONDecodeError as e:
        # Catch errors if the API response is not valid JSON
        print(f"JSON decoding error: {e}")
        return jsonify({"error": f"Failed to parse AI response: {e}"}), 500
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return jsonify({"error": f"An internal server error occurred: {e}"}), 500

# Run the Flask app
# This will run on http://127.0.0.1:5000/ by default
if __name__ == '__main__':
    app.run(debug=True) # debug=True enables auto-reloading and better error messages
