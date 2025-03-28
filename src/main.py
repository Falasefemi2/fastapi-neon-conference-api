from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import models, schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/speakers/", response_model=schemas.Speaker)
def create_speaker(speaker: schemas.SpeakerCreate, db: Session = Depends(get_db)):
    db_speaker = models.Speaker(**speaker.dict())
    db.add(db_speaker)
    db.commit()
    db.refresh(db_speaker)
    return db_speaker

@app.get("/speakers/", response_model=List[schemas.Speaker])
def read_speakers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    speakers = db.query(models.Speaker).offset(skip).limit(limit).all()
    return speakers

@app.get("/speakers/{speaker_id}", response_model=schemas.SpeakerWithTalks)
def read_speaker(speaker_id: int, db: Session = Depends(get_db)):
    db_speaker = db.query(models.Speaker).filter(models.Speaker.id == speaker_id).first()
    if db_speaker is None:
        raise HTTPException(status_code=404, detail="Speaker not found")
    return db_speaker

@app.post("/talks/", response_model=schemas.Talk)
def create_talk(talk: schemas.TalkCreate, db: Session = Depends(get_db)):
    db_talk = models.Talk(**talk.dict())
    db.add(db_talk)
    db.commit()
    db.refresh(db_talk)
    return db_talk

@app.get("/talks/", response_model=List[schemas.Talk])
def read_talks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    talks = db.query(models.Talk).offset(skip).limit(limit).all()
    return talks

@app.get("/talks/{talk_id}", response_model=schemas.Talk)
def read_talk(talk_id: int, db: Session = Depends(get_db)):
    db_talk = db.query(models.Talk).filter(models.Talk.id == talk_id).first()
    if db_talk is None:
        raise HTTPException(status_code=404, detail="Talk not found")
    return db_talk