from fastapi import FastAPI
from config.db import user_collection
from fastapi.middleware.cors import CORSMiddleware 
from routes.realestate import realestateRouter
from routes.users import userRouter
from auth import authRouter
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=False,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(realestateRouter)
app.include_router(userRouter)
app.include_router(authRouter)


