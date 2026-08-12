"""Central exception hierarchy — every error the app raises intentionally should live here.

TODO, mirroring your usual Node ApiError pattern:

class ApiError(Exception):
    # base: statusCode + message

class ValidationError(ApiError):
    # 400, carries errors: list[{field, message}]

class NotFoundError(ApiError):
    # 404

class SQLSafetyError(ApiError):
    # 400 — validation agent blocked a dangerous or out-of-scope generated query

class PermissionScopeError(ApiError):
    # 403 — user asked for data outside their permitted scope
"""
