from pydantic import BaseModel, ConfigDict


class ScriptCreate(BaseModel):
    prompt: str


class ScriptUpdate(BaseModel):
    prompt: str | None = None
    generated_script: str | None = None
    status: str | None = None


class ScriptResponse(BaseModel):
    public_id: str
    prompt: str
    generated_script: str | None
    status: str

    model_config = ConfigDict(from_attributes=True)