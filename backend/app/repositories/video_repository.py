from sqlalchemy.orm import Session

from app.models.video import Video


class VideoRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_script(self, script_id: int):

        return (
            self.db.query(Video)
            .filter(Video.script_id == script_id)
            .first()
        )

    def create(self, video: Video):

        self.db.add(video)
        self.db.flush()
        self.db.refresh(video)

        return video

    def update(self, video: Video):

        self.db.add(video)
        self.db.flush()
        self.db.refresh(video)

        return video