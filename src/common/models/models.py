from elasticsearch_dsl import DocType, String, Integer, Date
from datetime import datetime
from src.common.constants.backendconstatants import *

class Task(DocType):
    date_created = String(default=datetime.now())
    task = String(index=ANALYSER)
    tags = String(index=ANALYSER)
    status = String(index=ANALYSER)

    class Meta:
        index=INDEX
        doc_type = DOC_TYPE

