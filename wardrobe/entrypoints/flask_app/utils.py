import re
from urllib.parse import urlsplit, urlunsplit, unquote

from flask import url_for, request


def make_safe_url(url):
    parts = list(urlsplit(url))
    parts[0] = ""
    parts[1] = ""
    safe_url = urlunsplit(parts)

    return safe_url


def get_endpoint_url(endpoint):
    return url_for(endpoint) if endpoint else "/"


def get_safe_next_url(param_name, default_endpoint):
    if param_name in request.args:
        safe_next_url = make_safe_url(unquote(request.args[param_name]))
    else:
        safe_next_url = get_endpoint_url(default_endpoint)

    return safe_next_url


def is_valid_phone_no(phone_no):
    return any(
        [re.match("^01\d-\d{3,4}-\d{4}$", phone_no), re.match("^01\d{8,9}$", phone_no)]
    )
