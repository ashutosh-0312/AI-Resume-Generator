AI Resume & Cover Letter Generator
Project Overview
The "AI Resume & Cover Letter Generator" is a web-based application designed to streamline and enhance the process of creating professional resumes and cover letters. By leveraging advanced Large Language Models (LLMs) from Google Gemini, the application generates personalized and high-quality documents based on user-provided details such as skills, job role, experience, and career goals. This tool aims to significantly reduce the time and effort job seekers spend on crafting application materials, ensuring they are professional, tailored, and impactful.

Features
Personalized Document Generation: Creates custom resumes and cover letters based on specific user inputs.

AI-Powered Content: Utilizes the Google Gemini LLM (gemini-2.0-flash) for intelligent text generation.

Modern Resume Formatting: Generates resumes in a clean, well-structured plain text format with clear section headings and proper indentation.

Formal Cover Letter: Produces formal cover letters starting with a "Dear Hiring Manager," salutation and a professional closing.

Intuitive User Interface: A clean, responsive, and visually appealing web form for easy data input.

Real-time Feedback: Includes loading indicators and custom message boxes for a smooth user experience.

Robust Error Handling: Provides clear feedback for missing inputs or API communication issues.

Technology Stack
Frontend (Client-Side)
HTML5: For structuring the web page.

CSS3 (Tailwind CSS): For modern, responsive styling.

JavaScript (ES6+): For client-side logic and interaction with the backend.

Backend (Server-Side)
Python 3.x: The core programming language.

Flask Framework: A lightweight web framework for the API endpoint.

Requests Library: For making HTTP requests to the Gemini API.

Flask-CORS: To handle Cross-Origin Resource Sharing.

Artificial Intelligence
Google Gemini API (gemini-2.0-flash): The Large Language Model used for content generation.

System Architecture
The application follows a client-server architecture:

Frontend (Web Browser): Users interact with the index.html interface, inputting their details.

HTTP Request: Upon submission, JavaScript sends a JSON payload via a POST request to the Flask backend.

Flask Backend: Receives the request, constructs a detailed prompt using the user's data, and makes an authenticated POST request to the Google Gemini API.

Google Gemini API: Processes the prompt and generates the resume and cover letter content in a structured JSON format.

Backend Response: The Flask backend parses the AI's JSON response, extracts the generated text, and sends it back to the frontend.

Frontend Display: The JavaScript updates the output sections on the index.html page, displaying the generated documents to the user.

+-----------------+     HTTP(S) Request/Response     +-----------------+
|   Web Browser   |<-------------------------------->| Flask Backend   |
| (HTML, CSS, JS) |                                  | (Python)        |
+-----------------+                                  +-----------------+
                                                             |
                                                             | Google Gemini API Call (HTTP/S)
                                                             V
                                                       +-----------------+
                                                       | Google Gemini   |
                                                       | API (LLM)       |
                                                       +-----------------+

Setup and Deployment
To get the AI Resume & Cover Letter Generator running on your local system, follow these steps:

Prerequisites
Python 3.8+ installed.

Git installed.

A Google Gemini API Key. You can obtain one for free from Google AI Studio.

1. Clone the Repository
First, clone this GitHub repository to your local machine:

git clone https://github.com/ashutosh-0312/AI-Resume-Generator.git
cd AI-Resume-Generator

2. Project Structure
Ensure your local project directory is structured as follows:

AI-Resume-Generator/
├── backend/
│   └── app.py
└── frontend/
    └── index.html

3. Backend Setup
Navigate into the backend directory in your terminal:

cd backend

Install the required Python libraries:

pip install Flask Flask-Cors requests

Set your Gemini API Key as an environment variable (replace YOUR_ACTUAL_GEMINI_API_KEY_HERE with your key):

For Windows (Command Prompt):

set GEMINI_API_KEY=YOUR_ACTUAL_GEMINI_API_KEY_HERE

For macOS/Linux (Bash/Zsh Terminal):

export GEMINI_API_KEY="YOUR_ACTUAL_GEMINI_API_KEY_HERE"

Start the Flask backend server:

python app.py

Keep this terminal window open; the server must remain running for the application to function.

4. Frontend Access
Open a new terminal or simply navigate in your file explorer to the frontend directory:

cd ../frontend

Open the index.html file in your preferred web browser:

start index.html  # On Windows
open index.html   # On macOS
xdg-open index.html # On Linux (may vary)

Alternatively, you can simply double-click the index.html file in your file explorer.

Usage
Input Data: On the web interface, accurately fill in all the provided input fields with your personal and professional details.

Generate Documents: Click the "Generate Resume & Cover Letter" button. A loading message will appear.

Review Output: The generated Resume and Cover Letter will be displayed in separate boxes below the form.

Copy Content: Select and copy the text from the output boxes to use in your applications.

Iterate: Modify your inputs and regenerate the documents to fine-tune the output.

Future Enhancements
PDF Export Functionality: Allow users to download documents as PDFs.

Template Selection: Offer various resume and cover letter templates.

User Account Management & Document Persistence: Implement user authentication and database storage for saving profiles and generated documents.

In-Application Editing: Enable minor text edits directly within the output boxes.

Feedback & Iteration Loop: Create a mechanism for user feedback to improve AI generation.

Enhanced Input Validation: Implement more robust client-side and server-side input validation.

Job Description Analysis: Allow users to paste a job description for highly targeted content generation.