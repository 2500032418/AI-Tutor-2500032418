from fastapi import FastAPI
klu=FastAPI(title="AI Tutor",
            description="AI Tutor pbl project",
            version="1.0.0")
@klu.get("/")
def home():
    return {"message":"welcome to AI Tutor project"}

@klu.get("/demo")
def demo():
    return {"message":"kl University"}

@klu.get("/askquestion")

def ask():
    return {"message":"what is LLM","Answer":"Large Language Model"}

@klu.get("/student")
def student():
    return {"id": 1, "name": "Ram","gender":"male","course":"DSA"}

@klu.get("/students")
def getstudents():
    return [{"id": 1, "name": "Ram","gender":"male","course":"DSA"},
            {"id": 2, "name": "sita","gender":"female","course":"DSA"},
            {"id": 3, "name": "klu","gender":"female","course":"DSA"}
            ]
