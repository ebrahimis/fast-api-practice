from uuid import UUID

from dateutil import parser


def convert_to_datetime(value: str):
    """
    Try convert string to datetime.

    :return: Datetime object if conversion succeeded otherwise return none.
    """
    try:
        return parser.parse(value)
    except Exception:
        return None


def convert_to_uuid(value):
    """
    Try convert value to UUID.

    :return: UUID object if conversion succeeded otherwise return none.
    """
    try:
        return value if type(value) == UUID else UUID(value)
    except Exception:
        return None
