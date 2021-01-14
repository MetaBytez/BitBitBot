from pydantic import BaseModel


class TwitchTags(BaseModel):
    display_name: str
    color: str
    user_id: str
    mod: str
    subscriber: str
