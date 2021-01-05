class Status:
    class Status200OK():
        CODE: int = 200
        MESSAGE: str = 'OK'

    class Status201Created():
        CODE: int = 201
        MESSAGE: str = 'Created'

    class Status204Deleted():
        CODE: int = 204
        MESSAGE: str = ''

    class Status400BadRequest():
        CODE: int = 400
        MESSAGE: str = 'Bad Request'

    class Status401Unauthorized():
        CODE: int = 401
        MESSAGE: str = 'Unauthorized'

    class Status403Forbidden():
        CODE: int = 403
        MESSAGE: str = 'Forbidden'

    class Status404NotFound():
        CODE: int = 404
        MESSAGE: str = 'Not Found'

    class Status409Conflict():
        CODE: int = 404
        MESSAGE: str = 'Conflict'

    class Status500InternalServerError():
        CODE: int = 500
        MESSAGE: str = 'Internal Server Error'

    class Status502BadGatewayError():
        CODE: int = 502
        MESSAGE: str = 'Bad Gateway Error'

    class Status503ServiceUnavailable():
        CODE: int = 503
        MESSAGE: str = 'Service Unavailable'
