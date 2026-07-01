from fastapi import FastAPI,Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import joblib as jb 
import numpy as np
import pandas as pd

app = FastAPI()

templates = Jinja2Templates(directory='templates')
app.mount("/static",StaticFiles(directory='static'),name="static")

model = jb.load('Models/RandomForest_Tuned.pkl')

@app.get("/",response_class = HTMLResponse)
def home(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

class verify(BaseModel):
    age : int
    gender : str
    cgpa : float
    branch : str
    tier : str
    internships : int
    projects : int
    certifications : int
    coding : float
    aptitude : float
    communication : float
    logical: float
    hackathons : int
    github : int
    linkedin : int
    mock : float
    attendance : float
    backlogs : int
    extra : float
    leadership : float
    volunteer : str
    sleep : int
    study : int

@app.post('/predict')
def predict(data:verify):
    features = pd.DataFrame([{
    "age": data.age,
    "gender": data.gender,
    "cgpa": data.cgpa,
    "branch": data.branch,
    "college_tier": data.tier,
    "internships_count": data.internships,
    "projects_count": data.projects,
    "certifications_count": data.certifications,
    "coding_skill_score": data.coding,
    "aptitude_score": data.aptitude,
    "communication_skill_score": data.communication,
    "logical_reasoning_score": data.logical,
    "hackathons_participated": data.hackathons,
    "github_repos": data.github,
    "linkedin_connections": data.linkedin,
    "mock_interview_score": data.mock,
    "attendance_percentage": data.attendance,
    "backlogs": data.backlogs,
    "extracurricular_score": data.extra,
    "leadership_score": data.leadership,
    "volunteer_experience": data.volunteer,
    "sleep_hours": data.sleep,
    "study_hours_per_day": data.study
    }])
    prediction = model.predict(features)
    if prediction == 1:
        result = "Placed"
    else:
        result = "Not Placed"

    return {
    "prediction": result
    }
    
