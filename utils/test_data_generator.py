from datetime import datetime
import uuid


def generate_unique_email():

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    unique_id = uuid.uuid4().hex[:6]

    return (
        f"playwright_{timestamp}_{unique_id}"
        "@example.com"
    )