from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from uuid import UUID
from datetime import datetime

class User(BaseModel):
    id: Optional[UUID] = None
    created_at: Optional[datetime] = None
    supabase_user_id: Optional[UUID] = None
    email: Optional[str] = None

class ParsedLesson(BaseModel):
    id: Optional[UUID] = None
    user_id: UUID
    unit_title: Optional[str]
    content: Optional[Dict]
    created_at: Optional[datetime] = None

class AISuggestion(BaseModel):
    id: Optional[UUID] = None
    lesson_id: UUID
    type: str
    suggestion: str
    metadata: Optional[Dict]
    created_at: Optional[datetime] = None

class Feedback(BaseModel):
    id: Optional[UUID] = None
    suggestion_id: UUID
    feedback_type: str
    comments: Optional[str]
    created_at: Optional[datetime] = None

class LessonEmbedding(BaseModel):
    id: Optional[UUID] = None
    lesson_id: UUID
    content: str
    embedding: List[float]