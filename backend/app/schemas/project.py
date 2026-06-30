from pydantic import BaseModel, ConfigDict, Field


class ProjectCreate(BaseModel):
    project_name: str = Field(min_length=3, max_length=200)
    description: str | None = None


class ProjectUpdate(BaseModel):
    project_name: str | None = None
    description: str | None = None


class ProjectResponse(BaseModel):
    public_id: str
    project_name: str
    description: str | None

    model_config = ConfigDict(from_attributes=True)