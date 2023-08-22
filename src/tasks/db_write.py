import time

from src.core.db import get_actual_session
from src.models import ResultModel
from src.worker import celery


# ----------------------------------------------------------------
@celery.task(name='add_result_db')
def add_result_db(result_struct: dict):
    """
    Task to add result to database

    Params:
        - result_struct: dictionary with validated result data
    """
    time.sleep(10)
    session = get_actual_session()
    try:
        result_model = ResultModel(**result_struct)
        duplicate = session.query(ResultModel).filter(ResultModel.offer_id == result_model.offer_id).first()
        if not duplicate:
            session.add(result_model)
            session.commit()
    except Exception as e:
        session.rollback()
        raise e
