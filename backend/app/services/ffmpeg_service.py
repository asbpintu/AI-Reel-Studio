import subprocess
from pathlib import Path


class FFmpegService:

    def create_scene_video(
        self,
        image_path: str,
        audio_path: str,
        output_path: str,
    ):

        Path(output_path).parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        command = [
            "ffmpeg",
            "-y",

            "-loop", "1",

            "-i", image_path,

            "-i", audio_path,

            "-c:v", "libx264",

            "-tune", "stillimage",

            "-c:a", "aac",

            "-b:a", "192k",

            "-pix_fmt", "yuv420p",

            "-shortest",

            output_path,
        ]

        subprocess.run(
            command,
            check=True,
        )

        return output_path