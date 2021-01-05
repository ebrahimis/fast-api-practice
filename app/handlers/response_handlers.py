from app.settings.status import Status
from fastapi.responses import JSONResponse


class ResponseHandler():

    @staticmethod
    def get_bad_request_400(errors, message=Status.Status400BadRequest.MESSAGE):
        """
        Generete bad request response with provided errors and message.

        :param errors: Dict contains response error.
        :param message: Response message.
        :return: Bad request response tuple.
        """
        return ResponseHandler.get_response(code=Status.Status400BadRequest.CODE, message=message, errors=errors)


    @staticmethod
    def get_created_201(data, message=Status.Status201Created.MESSAGE):
        """
        Generete created response with provided data and message.

        :param data: Dict contains response data.
        :param message: Response message.
        :return: Created response tuple.
        """
        return ResponseHandler.get_response(code=Status.Status201Created.CODE, message=message, data=data)


    @staticmethod
    def get_deleted_204():
        """
        Generate deleted response without any data just status code

        :return: Deleted response tuple
        """
        return ResponseHandler.get_response(code=Status.Status204Deleted.CODE)


    @staticmethod
    def get_internal_server_error_500(message=Status.Status500InternalServerError.MESSAGE):
        """
        Generete internal server error response with provided message.

        :param message: Response message.
        :return: Internal server error response tuple.
        """
        return ResponseHandler.get_response(
            code=Status.Status500InternalServerError.CODE,
            message=message
        )


    @staticmethod
    def get_not_found_404(message=Status.Status404NotFound.MESSAGE):
        """
        Generete not found response with provided message.

        :param message: Response message.
        :return: Not found tuple.
        """
        return ResponseHandler.get_response(code=Status.Status404NotFound.CODE, message=message)


    @staticmethod
    def get_ok_200(data, message=Status.Status200OK.MESSAGE):
        """
        Generete ok response with provided data and message.

        :param data: Dict contains response data.
        :param message: Response message.
        :return: Ok tuple.
        """
        return ResponseHandler.get_response(code=Status.Status200OK.CODE, message=message, data=data)


    @staticmethod
    def get_ok_200_paginated(paginated_data, message=Status.Status200OK.MESSAGE):
        """
        Generete ok response with provided paginated data and message.

        :param paginated_data: Dict contains response pagination data.
        :param message: Response message.
        :return: Ok response tuple.
        """
        return ResponseHandler.get_response(code=Status.Status200OK.CODE, message=message, **paginated_data)


    @staticmethod
    def get_response(code: int, **kwargs):
        """
        Generete flask restx response according to provided code and kwargs.

        :param code: Response http status code.
        :param kwargs: Dict contains response data.
        :return: Response tuple.
        """
        if code == 204:
            return JSONResponse(status_code=code)
        
        response = {'code': code}
        for key, value in kwargs.items():
            if value or isinstance(value, list) or value == 0 or value is False:
                response[key] = value

        return JSONResponse({'content': response, 'status_code': code})


    @staticmethod
    def get_service_unavailable_503(message=Status.Status503ServiceUnavailable.MESSAGE):
        """
        Generete service unavailable response with provided message.

        :param message: Response message.
        :return: Ok response tuple.
        """
        return ResponseHandler.get_response(code=Status.Status503ServiceUnavailable.CODE, message=message)


    @staticmethod
    def get_unauthorized_401(message=Status.Status401Unauthorized.MESSAGE):
        """
        Generete unauthorized response with provided message.

        :param message: Response message.
        :return: Ok response tuple.
        """
        return ResponseHandler.get_response(code=Status.Status401Unauthorized.CODE, message=message)
