# -*- coding: utf-8 -*-
#/src/controllers/HomeController.py

"""
                        Home Service
    ------------------------------------------------------------------------
                            API
    ------------------------------------------------------------------------
    
"""
from flask import request, Blueprint, json, Response

home_api = Blueprint('home_api', __name__)


@home_api.route('/', methods=['POST'])
def create():
  """
  Create post message
  ---
  """
  try:
    req_data = request.get_json() 
    return custom_response(req_data, 200)
  except Exception as error:
    return custom_response(str(error), 500)


@home_api.route('/<int:home_id>', methods=['GET'])
def get_one(home_id):
  """
  Get A Home
  ---
  """
  try:
    return custom_response({"message":"Ok", "id":home_id}, 200)
  except Exception as error:
    return custom_response(str(error), 500)

@home_api.route('/<int:home_id>', methods=['PUT'])
def update(home_id):
  """
  Update A About
  ---
  """
  try:
    return custom_response({"message":"Updated", "id":home_id}, 200)
  except Exception as error:
    return custom_response(str(error), 500)


@home_api.route('/<int:home_id>', methods=['DELETE'])
def delete(home_id):
  """
  Delete A About
  ---
  """
  try:
    return custom_response({"message":"deleted", "id":home_id}, 200)
  except Exception as error:
    return custom_response(str(error), 500)


def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )
