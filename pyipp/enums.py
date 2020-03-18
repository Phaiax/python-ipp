"""Enumerators for IPP."""
from enum import IntEnum


class IppStatus(IntEnum):
    """Represent the ENUMs of a status response."""

    CUPS_INVALID = -1
    OK = 0x0000
    OK_IGNORED_OR_SUBSTITUTED = 0x0001
    OK_CONFLICTING = 0x0002
    OK_IGNORED_SUBSCRIPTIONS = 0x0003
    OK_IGNORED_NOTIFICATIONS = 0x0004
    OK_TOO_MANY_EVENTS = 0x0005
    OK_BUT_CANCEL_SUBSCRIPTION = 0x0006
    OK_EVENTS_COMPLETE = 0x0007
    REDIRECTION_OTHER_SITE = 0x0200
    CUPS_SEE_OTHER = 0x0280
    ERROR_BAD_REQUEST = 0x0400
    ERROR_FORBIDDEN = 0x0401
    ERROR_NOT_AUTHENTICATED = 0x0402
    ERROR_NOT_AUTHORIZED = 0x0403
    ERROR_NOT_POSSIBLE = 0x0404
    ERROR_TIMEOUT = 0x0405
    ERROR_NOT_FOUND = 0x0406
    ERROR_GONE = 0x0407
    ERROR_REQUEST_ENTITY = 0x0408
    ERROR_REQUEST_VALUE = 0x0409
    ERROR_DOCUMENT_FORMAT_NOT_SUPPORTED = 0x040A
    ERROR_ATTRIBUTES_OR_VALUES = 0x040B
    ERROR_URI_SCHEME = 0x040C
    ERROR_CHARSET = 0x040D
    ERROR_CONFLICTING = 0x040E
    ERROR_COMPRESSION_ERROR = 0x040F
    ERROR_DOCUMENT_FORMAT_ERROR = 0x0410
    ERROR_DOCUMENT_ACCESS = 0x0411
    ERROR_ATTRIBUTES_NOT_SETTABLE = 0x0412
    ERROR_IGNORED_ALL_SUBSCRIPTIONS = 0x0413
    ERROR_TOO_MANY_SUBSCRIPTIONS = 0x0414
    ERROR_IGNORED_ALL_NOTIFICATIONS = 0x0415
    ERROR_PRINT_SUPPORT_FILE_NOT_FOUND = 0x0416
    ERROR_DOCUMENT_PASSWORD = 0x0417
    ERROR_DOCUMENT_PERMISSION = 0x0418
    ERROR_DOCUMENT_SECURITY = 0x0419
    ERROR_DOCUMENT_UNPRINTABLE = 0x041A
    ERROR_ACCOUNT_INFO_NEEDED = 0x041B
    ERROR_ACCOUNT_CLOSED = 0x041C
    ERROR_ACCOUNT_LIMIT_REACHED = 0x041D
    ERROR_ACCOUNT_AUTHORIZATION_FAILED = 0x041E
    ERROR_NOT_FETCHABLE = 0x041F
    ERROR_CUPS_ACCOUNT_INFO_NEEDED = 0x049C
    ERROR_CUPS_ACCOUNT_CLOSED = 0x049D
    ERROR_CUPS_ACCOUNT_LIMIT_REACHED = 0x049E
    ERROR_CUPS_ACCOUNT_AUTHORIZATION_FAILED = 0x049F
    ERROR_INTERNAL = 0x0500
    ERROR_OPERATION_NOT_SUPPORTED = 0x0501
    ERROR_SERVICE_UNAVAILABLE = 0x0502
    ERROR_VERSION_NOT_SUPPORTED = 0x0503
    ERROR_DEVICE = 0x0504
    ERROR_TEMPORARY = 0x0505
    ERROR_NOT_ACCEPTING_JOBS = 0x0506
    ERROR_BUSY = 0x0507
    ERROR_JOB_CANCELED = 0x0508
    ERROR_MULTIPLE_JOBS_NOT_SUPPORTED = 0x0509
    ERROR_PRINTER_IS_DEACTIVATED = 0x050A
    ERROR_TOO_MANY_JOBS = 0x050B
    ERROR_TOO_MANY_DOCUMENTS = 0x050C
    ERROR_CUPS_AUTHENTICATION_CANCELED = 0x1000
    ERROR_CUPS_PKI = 0x1001
    ERROR_CUPS_UPGRADE_REQUIRED = 0x1002


class IppOperation(IntEnum):
    """Represent the ENUMs of an operation."""

    CUPS_INVALID = -0x0001
    CUPS_NONE = 0x0000
    PRINT_JOB = 0x0002
    PRINT_URI = 0x0003
    VALIDATE_JOB = 0x0004
    CREATE_JOB = 0x0005
    SEND_DOCUMENT = 0x0006
    SEND_URI = 0x0007
    CANCEL_JOB = 0x0008
    GET_JOB_ATTRIBUTES = 0x0009
    GET_JOBS = 0x000A
    GET_PRINTER_ATTRIBUTES = 0x000B
    HOLD_JOB = 0x000C
    RELEASE_JOB = 0x000D
    RESTART_JOB = 0x000E
    PAUSE_PRINTER = 0x0010
    RESUME_PRINTER = 0x0011
    PURGE_JOBS = 0x0012
    SET_PRINTER_ATTRIBUTES = 0x0013
    SET_JOB_ATTRIBUTES = 0x0014
    GET_PRINTER_SUPPORTED_VALUES = 0x0015
    CREATE_PRINTER_SUBSCRIPTIONS = 0x0016
    CREATE_JOB_SUBSCRIPTIONS = 0x0017
    GET_SUBSCRIPTION_ATTRIBUTES = 0x0018
    GET_SUBSCRIPTIONS = 0x0019
    RENEW_SUBSCRIPTION = 0x001A
    CANCEL_SUBSCRIPTION = 0x001B
    GET_NOTIFICATIONS = 0x001C
    SEND_NOTIFICATIONS = 0x001D
    GET_RESOURCE_ATTRIBUTES = 0x001E
    GET_RESOURCE_DATA = 0x001F
    GET_RESOURCES = 0x0020
    GET_PRINT_SUPPORT_FILES = 0x0021
    ENABLE_PRINTER = 0x0022
    DISABLE_PRINTER = 0x0023
    PAUSE_PRINTER_AFTER_CURRENT_JOB = 0x0024
    HOLD_NEW_JOBS = 0x0025
    RELEASE_HELD_NEW_JOBS = 0x0026
    DEACTIVATE_PRINTER = 0x0027
    ACTIVATE_PRINTER = 0x0028
    RESTART_PRINTER = 0x0029
    SHUTDOWN_PRINTER = 0x002A
    STARTUP_PRINTER = 0x002B
    REPROCESS_JOB = 0x002C
    CANCEL_CURRENT_JOB = 0x002D
    SUSPEND_CURRENT_JOB = 0x002E
    RESUME_JOB = 0x002F
    PROMOTE_JOB = 0x0030
    SCHEDULE_JOB_AFTER = 0x0031
    CANCEL_DOCUMENT = 0x0033
    GET_DOCUMENT_ATTRIBUTES = 0x0034
    GET_DOCUMENTS = 0x0035
    DELETE_DOCUMENT = 0x0036
    SET_DOCUMENT_ATTRIBUTES = 0x0037
    CANCEL_JOBS = 0x0038
    CANCEL_MY_JOBS = 0x0039
    RESUBMIT_JOB = 0x003A
    CLOSE_JOB = 0x003B
    IDENTIFY_PRINTER = 0x003C
    VALIDATE_DOCUMENT = 0x003D
    ADD_DOCUMENT_IMAGES = 0x003E
    ACKNOWLEDGE_DOCUMENT = 0x003F
    ACKNOWLEDGE_IDENTIFY_PRINTER = 0x0040
    ACKNOWLEDGE_JOB = 0x0041
    FETCH_DOCUMENT = 0x0042
    FETCH_JOB = 0x0043
    GET_OUTPUT_DEVICE_ATTRIBUTES = 0x0044
    UPDATE_ACTIVE_JOBS = 0x0045
    DEREGISTER_OUTPUT_DEVICE = 0x0046
    UPDATE_DOCUMENT_STATUS = 0x0047
    UPDATE_JOB_STATUS = 0x0048
    UPDATE_OUTPUT_DEVICE_ATTRIBUTES = 0x0049
    GET_NEXT_DOCUMENT_DATA = 0x004A
    ALLOCATE_PRINTER_RESOURCES = 0x004B
    CREATE_PRINTER = 0x004C
    DEALLOCATE_PRINTER_RESOURCES = 0x004D
    DELETE_PRINTER = 0x004E
    GET_PRINTERS = 0x004F
    SHUTDOWN_ONE_PRINTER = 0x0050
    STARTUP_ONE_PRINTER = 0x0051
    CANCEL_RESOURCE = 0x0052
    CREATE_RESOURCE = 0x0053
    INSTALL_RESOURCE = 0x0054
    SEND_RESOURCE_DATA = 0x0055
    SET_RESOURCE_ATTRIBUTES = 0x0056
    CREATE_RESOURCE_SUBSCRIPTIONS = 0x0057
    CREATE_SYSTEM_SUBSCRIPTIONS = 0x0058
    DISABLE_ALL_PRINTERS = 0x0059
    ENABLE_ALL_PRINTERS = 0x005A
    GET_SYSTEM_ATTRIBUTES = 0x005B
    GET_SYSTEM_SUPPORTED_VALUES = 0x005C
    PAUSE_ALL_PRINTERS = 0x005D
    PAUSE_ALL_PRINTERS_AFTER_CURRENT_JOB = 0x005E
    REGISTER_OUTPUT_DEVICE = 0x005F
    RESTART_SYSTEM = 0x0060
    RESUME_ALL_PRINTERS = 0x0061
    SET_SYSTEM_ATTRIBUTES = 0x0062
    SHUTDOWN_ALL_PRINTER = 0x0063
    STARTUP_ALL_PRINTERS = 0x0064
    PRIVATE = 0x4000
    CUPS_GET_DEFAULT = 0x4001
    CUPS_GET_PRINTERS = 0x4002
    CUPS_ADD_MODIFY_PRINTER = 0x4003
    CUPS_DELETE_PRINTER = 0x4004
    CUPS_GET_CLASSES = 0x4005
    CUPS_ADD_MODIFY_CLASS = 0x4006
    CUPS_DELETE_CLASS = 0x4007
    CUPS_ACCEPT_JOBS = 0x4008
    CUPS_REJECT_JOBS = 0x4009
    CUPS_SET_DEFAULT = 0x400A
    CUPS_GET_DEVICES = 0x400B
    CUPS_GET_PPDS = 0x400C
    CUPS_MOVE_JOB = 0x400D
    CUPS_AUTHENTICATE_JOB = 0x400E
    CUPS_GET_PPD = 0x400F
    CUPS_GET_DOCUMENT = 0x4027
    CUPS_CREATE_LOCAL_PRINTER = 0x4028


class IppTag(IntEnum):
    """Represent the ENUMs of a tag."""

    CUPS_INVALID = -1
    ZERO = 0x00
    OPERATION = 0x01
    JOB = 0x02
    END = 0x03
    PRINTER = 0x04
    UNSUPPORTED_GROUP = 0x05
    SUBSCRIPTION = 0x06
    EVENT_NOTIFICATION = 0x07
    RESOURCE = 0x08
    DOCUMENT = 0x09
    SYSTEM = 0x0A
    UNSUPPORTED_VALUE = 0x10
    DEFAULT = 0x11
    UNKNOWN = 0x12
    NO_VALUE = 0x013
    NOT_SETTABLE = 0x15
    DELETE_ATTR = 0x16
    ADMIN_DEFINE = 0x17
    INTEGER = 0x21
    BOOLEAN = 0x22
    ENUM = 0x23
    STRING = 0x30
    DATE = 0x31
    RESOLUTION = 0x32
    RANGE = 0x33
    BEGIN_COLLECTION = 0x34
    TEXT_LANG = 0x35
    NAME_LANG = 0x36
    END_COLLECTION = 0x37
    TEXT = 0x41
    NAME = 0x42
    RESERVED_STRING = 0x43
    KEYWORD = 0x44
    URI = 0x45
    URI_SCHEME = 0x46
    CHARSET = 0x47
    LANGUAGE = 0x48
    MIME_TYPE = 0x49
    MEMBER_NAME = 0x4A
    EXTENSION = 0x7F
    CUPS_MASK = 0x7FFFFFFF
    CUPS_CONST = -0x7FFFFFFF - 1


class IppJobState(IntEnum):
    """Represent the ENUMs of the state of a print job."""

    PENDING = 0x03
    HELD = 0x04
    PROCESSING = 0x05
    STOPPED = 0x06
    CANCELED = 0x07
    ABORTED = 0x08
    COMPLETED = 0x09


class IppDocumentState(IntEnum):
    """Represent the ENUMs of the state of a document."""

    PENDING = 0x03
    PROCESSING = 0x05
    CANCELED = 0x07
    ABORTED = 0x08
    COMPLETED = 0x08


class IppPrinterState(IntEnum):
    """Represent the ENUMs of the state of a printer."""

    IDLE = 0x0003
    PROCESSING = 0x0004
    STOPPED = 0x0005