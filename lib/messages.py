"""Definitions of messages sent/received by clients and servers."""


def error(msg=""):
    """Construct message used for sending error messages

    :param msg: Optional error details.
    :type msg: string
    :returns: Constructed error dict, ready to be sent over the wire.

    """
    return {"type": "error", "msg": msg}


def ping_req():
    """Construct message used when sending pings.

    :returns: Constructed ping_req dict, ready to be sent over the wire.

    """
    return {"type": "ping_req"}


def ping_reply():
    """Construct message used when replying to pings.

    :returns: Constructed ping_reply dict, ready to be sent over the wire.

    """
    return {"type": "ping_reply"}


def list_req():
    """Construct message used when sending list requests to CtrlServer.

    By 'list', we mean 'give me all the callable methods on your systems'.

    :returns: Constructed list_req dict, ready to be sent over the wire.

    """
    return {"type": "list_req"}


def list_reply(objects):
    """Construct message used by CtrlServer when replying to list requests.

    By 'list', we mean 'give me all the callable methods on your systems'.

    :param objects: Dict of subsystem object names to their callable methods.
    :type objects: dict
    :returns: Constructed list_reply dict, ready to be sent over the wire.

    """
    return {"type": "list_reply", "objects": objects}


def call_req(obj_name, method, params):
    """Construct message used when sending API calls to CtrlServer.

    :param obj_name: Name of API-exported system that owns the given method.
    :type obj_name: string
    :param method: API-exported method to call on the given object.
    :type method: string
    :param params: Params to pass to the given method.
    :type params: dict
    :returns: Constructed call_req dict, ready to be sent over the wire.

    """
    return {
        "type": "call_req",
        "obj_name": obj_name,
        "method": method,
        "params": params
    }


def call_reply(msg, call_return):
    """Construct message used by CtrlServer when replying to API calls.

    :param msg: Description of API call.
    :type msg: string
    :param call_return: Return value of API call.
    :type call_return: string
    :returns: Constructed call_reply dict, ready to be sent over the wire.

    """
    return {"type": "call_reply", "msg": msg, "call_return": call_return}


def exit_req():
    """Construct message used when asking CtrlServer to exit.

    :returns: Constructed exit_req dict, ready to be sent over the wire.

    """
    return {"type": "exit_req"}


def exit_reply():
    """Construct message used when replying to an exit_req message.

    :returns: Constructed exit_reply dict, ready to be sent over the wire.

    """
    return {"type": "exit_reply"}
