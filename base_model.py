import datetime
from sqlalchemy import Column, DateTime, String, Boolean
from sqlalchemy.orm import declarative_base

from exceptions import DatabaseError
from app.utils.responses import m_return
import app.utils.responses as resp
import logging
from flask import jsonify, make_response


class BaseModel(object):
    """Base model class

    Args:
        object (_type_): class to hold repetative fields and methods
    """

    __abstract__ = True

    date_created = Column(
        DateTime(timezone=True), nullable=False, default=datetime.datetime.now
    )
    date_updated = Column(
        DateTime(timezone=True), nullable=False, default=datetime.datetime.now
    )
    created_by = Column(String(100), nullable=False, default="SYSTEM")
    active = Column(Boolean, nullable=False, default=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    def save(self, session):
        session.add(self)
        session.commit()
     
    def set_model_dict(self, model_dict):
        for k, v in model_dict.items():
            getattr(self, k, setattr(self, k, v))

    def get_all(self, session):
        items = session.query(self).all()
        return items

    def get_one(self, id, session):


        try:
            items = session.query(self).get(id)

            if items:

                return items
        
            return items

        except Exception as why:

            logging.info("User doesn't exist" + str(why))

            return m_return(http_code=resp.USER_DOES_NOT_EXIST['http_code'], message=resp.USER_DOES_NOT_EXIST['message'],
                            code=resp.USER_DOES_NOT_EXIST['code'])

        


Base = declarative_base(cls=BaseModel)
