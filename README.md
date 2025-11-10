# Case 3: End-to-End Mini Project 
Creating an automated system for providing department recommendations based on input regarding gender, age, and symptoms
**[Github]([https://aistudio.google.com/](https://github.com/aisyahaini/pretest))** 


# How To Run This APP

## 1. Install Dependencies
`pip install fastapi uvicorn langchain langchain-google-genai pydantic
`

## 2. Set API KEY from Google AI Studio

**a. Open [Google AI Studio](https://aistudio.google.com/)**  
**b. Create API Key**  
**c. Then Copy the API Key**  
Example of API Key: `AIzaSyDimyUkjlwT92QRkAImfflrVv_d25trpNc`
  
## 3. Create a `main.py` File
After create a `main.py`, input API Key to `os.environ["GOOGLE_API_KEY"] = "API_KEY"`

## 4. Running the FastAPI Server

#### - Running the server using commands on terminal: `uvicorn main:app --reload`

#### - After the server is running:
a. Open http://127.0.0.1:8000/docs to open Swagger UI  
b. Select the POST /recommend endpoint  
c. Click 'Try it out'  
d. Enter the following JSON input example:
`{
  "gender": "female",
  "age": 30,
  "symptoms": ["sakit kepala", "mual", "sulit berjalan"]
}`  
e. Click 'Execute'  
f. Output:   
`{
  "recommended_department": "Neurology"
}
`

## 5. Output:
The system can guess from gender, age, and symptoms entered for department recommendations. 

![Output](image.png)

