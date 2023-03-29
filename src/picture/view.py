from typing import Optional

from fastapi import APIRouter, Depends, UploadFile, status, File
from starlette.responses import Response, FileResponse

from src.core.utils import get_db
from .service import *
from .model import Picture

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
async def root(response: Response, db: Session = Depends(get_db),
               limit: Optional[int] = None,
               offset: Optional[int] = None,
               ):

    # All records by default
    query = db.query(Picture).all()
    files_in_db = get_files_from_db_limit_offset(db, query, limit, offset)

    if len(files_in_db) == 0:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message': 'No results =('}

    response.status_code = status.HTTP_200_OK
    return files_in_db


@router.post("/", status_code=status.HTTP_200_OK)
async def upload_or_update_file(
                        response: Response,
                        pk: int,
                        title: Optional[str] = None,
                        user: Optional[str] = None,
                        file: UploadFile = File(...),
                        db: Session = Depends(get_db)
                    ):

    # Format new filename
    full_title = format_filename(file, title)

    # Save file
    await save_file_to_uploads(file, full_title)

    # Get file size
    size = get_file_size(full_title)

    # Get info from DB
    file_info_from_db = get_file_from_db(db, pk)

    # Add to DB
    if not file_info_from_db:
        response.status_code = status.HTTP_201_CREATED
        return add_file_to_db(
                                db,
                                title=full_title,
                                size=size,
                                user=user,
                            )

    # Update in DB
    if file_info_from_db:
        # Delete file from uploads
        delete_file_from_uploads(file_info_from_db.title)

        response.status_code = status.HTTP_201_CREATED
        return update_file_in_db(
                                    db,
                                    id=pk,
                                    title=full_title,
                                    size=size,
                                )


@router.get("/{pk}", status_code=status.HTTP_200_OK)
async def download_file(
                        response: Response,
                        pk: int,
                        db: Session = Depends(get_db)
                    ):
    file_info_from_db = get_file_from_db(db, pk)

    if file_info_from_db:
        file_resp = FileResponse(UPLOADED_FILES_PATH + file_info_from_db.title)
        response.status_code = status.HTTP_200_OK
        return file_resp
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'msg': 'File not found'}


@router.delete("/{pk}")
async def delete_file(
                        response: Response,
                        pk: int,
                        db: Session = Depends(get_db)
                    ):
    file_info_from_db = get_file_from_db(db, pk)

    if file_info_from_db:
        # Delete file from DB
        delete_file_from_db(db, file_info_from_db)

        # Delete file from uploads
        delete_file_from_uploads(file_info_from_db.title)

        response.status_code = status.HTTP_200_OK
        return {'msg': f'File {file_info_from_db.title} successfully deleted'}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'msg': f'File does not exist'}

