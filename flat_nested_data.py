def flat_nested_data(formatted_data=None, data=None, parent_key=None):
    """
    it is used to flat dictionary document
    :param formatted_data: it is data dictionary flat data
    :param data: nested data that have to flatten
    :param parent_key: key on which fields have to set in flat data
    :return:
    """
    if not formatted_data:
        formatted_data = {}
    for key, val in data.items():
        if isinstance(val, dict):
            if parent_key:
                flat_nested_data(formatted_data, data=val, parent_key=parent_key + "." + key)
            else:
                flat_nested_data(formatted_data, data=val, parent_key=key)
        else:
            if parent_key:
                formatted_data[parent_key + "." + key] = val
            else:
                formatted_data[key] = val
    return formatted_data
