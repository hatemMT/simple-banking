import random

from flask import request, jsonify, Response, abort
from sqlalchemy import or_, sql
from sqlalchemy.orm.exc import NoResultFound


QUESTIONS_PER_PAGE = 10


def register_controllers(app):
    pass # TODO register controllers
