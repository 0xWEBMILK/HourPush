async def get_active_sprint(bitrix_model) -> str:
    """
    Retrieves the current sprint ID from the Bitrix model.

    Args:
        bitrix_model: The Bitrix model instance used to fetch the sprint data.

    Returns:
        str: The ID of the current sprint.
    """
    result = await bitrix_model.get_sprint()

    # Return the ID of the first sprint in the result
    return result['result'][0]['id']
