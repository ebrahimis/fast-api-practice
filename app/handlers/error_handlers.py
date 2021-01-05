import logging

from app.handlers.response_handler import ResponseHandler
from app.handlers.errors import NotExistError
from requests.exceptions import ConnectionError
from sqlalchemy.exc import DataError


class ErrorHandlers:
    """
    Register global error handlers in app.

    :param app: app.
    :param app: The application object.
    """


    @app.errorhandler(NotExistError)
    def handle_app_not_exist_error(error: NotExistError):
        """
        Global error handler that handle app not exist error.

        :param error: Not exist error.
        :return: Response tuple with 404 status code and error message.
        """
        return ResponseHandler.get_not_found_404(error.description)


    @app.errorhandler(DataError)
    def handle_sqlalchemy_data_error(error: DataError):
        """
        Global error handler that handle sqlalchemy data error.

        :param error: Sqlalchemy data error.
        :return: Response tuple with 404 status code and error message.
        """
        return ResponseHandler.get_bad_request_400({
            'key': 'InvalidValue',
            'message': 'Please check your input',
        })


    @app.errorhandler(ConnectionError)
    def handle_connection_error(error: ConnectionError):
        """
        Global error handler that handle requests connection error.

        :param error: Connection error.
        :return: Error response tuple.
        """
        return ResponseHandler.get_service_unavailable_503('External service unavailable')


    @app.errorhandler(ValueError)
    def handle_value_error(error: ValueError):
        """
        Global error handler that handle value error.

        :param error: Value error.
        :return: Response tuple with 404 status code and error message.
        """
        return ResponseHandler.get_not_found_404()


    @app.errorhandler(Exception)
    def handle_internal_server_error(error: Exception):
        """
        Global error handler that handle any unhandled exception.

        :param error: Instance of exception.
        :return: Response tuple with 500 status code.
        """
        logging.exception(error)
        return ResponseHandler.get_internal_server_error_500()
