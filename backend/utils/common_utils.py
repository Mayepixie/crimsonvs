

def validate_id(id_to_check):
    """ Checks if id_to_check is a integer """
    try:
        int(id_to_check)
    except Exception:
        raise ValueError("id must be a integer!")
