import os
import uuid


class VideoService:

    UPLOAD_FOLDER = "uploads"

    @classmethod
    def save_video(cls, uploaded_file, progress_bar=None):

        os.makedirs(cls.UPLOAD_FOLDER, exist_ok=True)

        extension = os.path.splitext(uploaded_file.name)[1]
        filename = f"{uuid.uuid4()}{extension}"

        filepath = os.path.join(
            cls.UPLOAD_FOLDER,
            filename
        )

        uploaded_file.seek(0)

        total_size = uploaded_file.size
        bytes_written = 0
        chunk_size = 1024 * 1024  # 1 MB

        with open(filepath, "wb") as f:

            while True:

                chunk = uploaded_file.read(chunk_size)

                if not chunk:
                    break

                f.write(chunk)

                bytes_written += len(chunk)

                if progress_bar:

                    progress = min(
                        bytes_written / total_size,
                        1.0
                    )

                    progress_bar.progress(progress)

        uploaded_file.seek(0)

        return filepath

    @classmethod
    def list_videos(cls):

        os.makedirs(cls.UPLOAD_FOLDER, exist_ok=True)

        return sorted(os.listdir(cls.UPLOAD_FOLDER))

    @classmethod
    def delete_video(cls, filename):

        filepath = os.path.join(
            cls.UPLOAD_FOLDER,
            filename
        )

        if os.path.exists(filepath):
            os.remove(filepath)
            return True

        return False