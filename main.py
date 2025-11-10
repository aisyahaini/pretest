# Import Library
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import os

app = FastAPI()

# Set API KEY from Google AI Studio
os.environ["GOOGLE_API_KEY"] = "AIzaSyDimyUkjlwT92QRkAImfflrVv_d25trpNc"

# Initializing LangChain LLM with Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.2,
    max_output_tokens=150,
    google_api_key=os.environ["GOOGLE_API_KEY"]  
)

# Schema JSON input
class PatientInfo(BaseModel):
    gender: str
    age: int
    symptoms: list[str]

# Endpoint JSON
@app.post("/recommend")
async def recommend_department(patient: PatientInfo):
    prompt = f"""
    Patient gender  {patient.gender}, age {patient.age} years old,
    with symptoms: {', '.join(patient.symptoms)}.
    Determine the most appropriate specialist department.
    Options: ["Neurology", "Cardiology", "Gastroenterology", "Orthopedics", "ENT", "Psychiatry", "Dermatology"].
    Answer with only one department name.
    """

    try:
        result = llm.invoke([HumanMessage(content=prompt)])
        recommendation = result.content.strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while invoking LLM: {str(e)}")

    return {"recommended_department": recommendation}
