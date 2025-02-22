from aiogram.filters.callback_data import CallbackData

from src.entities.enums.lang_enum import LanguageEnum
from src.entities.enums.profile_action_type_enum import ProfileActionTypeEnum


class ProfileMenu(CallbackData, prefix="prf"):
    action_type: ProfileActionTypeEnum


class SelectChangeLanguage(ProfileMenu, prefix="prf"):
    select_language: LanguageEnum


class SelectLanguageConfirm(SelectChangeLanguage, prefix="prf"):
    confirm_language: str = "t"
