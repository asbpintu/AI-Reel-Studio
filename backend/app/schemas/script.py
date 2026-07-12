from pydantic import BaseModel, ConfigDict


class ScriptCreate(BaseModel):
    prompt: str
    keywords: str | None = None
    duration_seconds: int | None = None
    language: str | None = None
    reel_type: str | None = None
    voice_type: str | None = None
    style: str | None = None


class ScriptUpdate(BaseModel):
    prompt: str | None = None
    keywords: str | None = None
    duration_seconds: int | None = None
    language: str | None = None
    reel_type: str | None = None
    voice_type: str | None = None
    style: str | None = None
    generated_script: str | None = None
    status: str | None = None


class ScriptResponse(BaseModel):
    public_id: str
    prompt: str
    keywords: str | None = None
    duration_seconds: int | None = None
    language: str | None = None
    reel_type: str | None = None
    voice_type: str | None = None
    style: str | None = None
    generated_script: str | None
    status: str

    model_config = ConfigDict(from_attributes=True)