from fastapi import APIRouter, HTTPException
from models import (
    add_translation,
    update_translation,
    delete_translation,
    get_translation_by_banglish,
    get_translation_by_id,
    get_all_translations,
)
from schemas import TranslationRequest, TranslationResponse
from utils import transliterate_to_bangla
from typing import List


router = APIRouter(
    prefix="/translations", 
    tags=["Translations"]
)

@router.post("/add")
def add_translation_route(translation: TranslationRequest):
    bangla = transliterate_to_bangla(translation.banglish)
    add_translation(translation.banglish, bangla)
    return {"banglish": translation.banglish, "bangla": bangla}

@router.get("/translate/{banglish}", response_model=TranslationResponse)
def translate(banglish: str):
    result = get_translation_by_banglish(banglish)
    if result:
        return {"id": result[0], "banglish": result[1], "bangla": result[2]}
    else:
        bangla = transliterate_to_bangla(banglish)
        return {"banglish": banglish, "bangla": bangla}

@router.put("/update/{id}")
def update_translation_route(id: int, translation: TranslationRequest):
    if not get_translation_by_id(id):
        raise HTTPException(status_code=404, detail="Translation with this ID not found")
    bangla = transliterate_to_bangla(translation.banglish)
    update_translation(id, translation.banglish, bangla)
    return {"message": "Translation updated successfully"}

@router.delete("/delete/{id}")
def delete_translation_route(id: int):
    if not get_translation_by_id(id):
        raise HTTPException(status_code=404, detail="Translation with this ID not found")
    delete_translation(id)
    return {"message": "Translation deleted successfully"}

@router.get("/", response_model=List[TranslationResponse])
def get_all_translations_route():
    return get_all_translations()
