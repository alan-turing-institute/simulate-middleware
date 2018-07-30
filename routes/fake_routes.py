"""
Make some fake routes for testing purposes
"""

from flask_restful import Resource
from tests.create_osrc_case import clear_db, set_up_osrc_testdata


class TestData(Resource):
    """
    Class to be used for generating fake data
    """

    def post(self):
        """
        Create the default fake data
        """
        set_up_osrc_testdata()

    def delete(self):
        """
        Delete all the cases and jobs
        """
        clear_db()
