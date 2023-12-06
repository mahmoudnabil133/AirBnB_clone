#!/usr/bin/python3
"storage to link baseModule class with fileStorage class"
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
