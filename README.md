# GitRepoScanner
This repository will contain Backend and Frontend for the Git Repository Scanner.

## Backend
##

# GitHub Repository Complexity Analyzer

This repository contains a Python Flask API that allows users to analyze the complexity of GitHub repositories. By providing a GitHub repository URL, the API fetches the repositories of the user, preprocesses the code, uses a GPT-2 model to generate a response, calculates the complexity score, and returns the most complex repository and its complexity score.

## Features

- Analyze the complexity of GitHub repositories.
- Fetch user repositories using the GitHub API.
- Use a GPT-2 model to generate a response based on the code.
- Calculate complexity score based on tokenized code.
- Return the most complex repository and its complexity score.

## Technologies Used

- Python
- Flask
- Transformers (Hugging Face)
- React (for the frontend, not included in this repository)

## Setup and Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/github-repo-complexity-analyzer.git

2. Navigate to the project directory:
   ```bash
   cd github-repo-complexity-analyzer

3. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   
4. Start the Flask server:
   ```bash
   python app.py
6. Ensure the Flask server is running on port 5001 (adjust the port if needed).

7. Integrate the API with your React project by sending a POST request to http://localhost:5001/api/analyze with the following JSON payload:

   {
     "url": "https://github.com/user/repository"
   }
The API will respond with a JSON object containing the most complex repository and its complexity score.

Example API Response
{
  "mostComplexRepository": {
    "name": "repository-name",
    "url": "https://github.com/user/repository"
  },
  "complexityScore": 1000
}
## Frontend
##

# Complexity Analyzer - GitHub Repository Analyzer

This project is a GitHub Repository Analyzer built using React. It allows users to enter a GitHub repository URL and analyze its technical complexity. The analyzer makes use of a backend API to fetch the repository information and calculate the complexity score.

## Prerequisites

- Node.js and npm installed on your machine.

## Getting Started

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the dependencies by running the following command:

   ```bash
   npm install

4. Start the development server:
 
    ```bash
    npm start
    ```
 
 5. Open your web browser and visit http://localhost:3000 to access the Complexity Analyzer.
 
 ## Usage
 
 1. Enter the GitHub repository URL in the input field. The URL should be in the format https://github.com/username/repository.
 2. Click the "Analyze" button to initiate the analysis.
 3. The application will communicate with the backend API to fetch the repository information and calculate the complexity score.
 4. Once the analysis is complete, the most complex repository and its complexity score will be displayed on the screen.
 
 ## Technologies Used 
    React: A JavaScript library for building user interfaces.   
    Axios: A library for making HTTP requests.
    CSS: Cascading Style Sheets for styling the application.
    
 ## Backend API
 
    The frontend application communicates with a backend API to perform the analysis. Make sure the backend API is running and    accessible    at http://localhost:5000/api/analyze or update the API URL in the analyzeRepository function inside the App component.
 
 ## Contributing
 Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.
 
 ## License
 
 This project is licensed under the MIT License. See the LICENSE file for details.
 
 ## Acknowledgements
 
 The GitHub Repository Analyzer is inspired by the concept of code complexity analysis. The project utilizes the power of React and various open-source libraries to provide a user-friendly interface for analyzing GitHub repositories.


