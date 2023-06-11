from src.services.user.enums import UserCategory


def validate_category_enum(enum: str):
    if hasattr(UserCategory, enum):
        return True
    raise ValueError(f"{enum} is not a valid category.")
