""" Helper Functions """


def get_client_ip(request):
    """Get Client IP

    Arguments:
        request {dict}

    Returns:
        str
    """
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        request_ip = x_forwarded_for.split(",")[0]
    else:
        request_ip = request.META.get("REMOTE_ADDR")
    return request_ip
