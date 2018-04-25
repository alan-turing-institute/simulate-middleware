"""
Make some fake routes for testing purposes
"""

from flask_restful import Resource
from tests.create_and_mint_case_using_stores import set_up_test_database
from tests.create_damBreak_case import setup_dambreak_testdata


class TestData(Resource):
    """
    Class to be used for generating fake data
    """

    def post(self):
        """
        Create the default fake data
        """
#        set_up_test_database()
        setup_dambreak_testdata()
