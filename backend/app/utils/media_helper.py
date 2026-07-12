from pathlib import Path


MEDIA_ROOT = Path(__file__).resolve().parent.parent.parent / "media"


def get_script_folder(media_type: str, script_public_id: str) -> Path:
    """
    Example:
    media/images/<script_public_id>/
    media/audio/<script_public_id>/
    media/videos/<script_public_id>/
    """

    folder = MEDIA_ROOT / media_type / script_public_id

    folder.mkdir(
        parents=True,
        exist_ok=True,
    )

    return folder