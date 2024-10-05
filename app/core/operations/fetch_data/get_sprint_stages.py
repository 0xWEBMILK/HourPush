from typing import List, Dict


async def get_sprint_stages(bitrix_model, bitrix_sprint_id: str) -> List[Dict]:
    """
    Retrieves the stages for a given sprint from the Bitrix model, excluding the first and last stages.

    Args:
        bitrix_model: The Bitrix model instance used to fetch the stages.
        bitrix_sprint_id (str): The ID of the sprint for which stages are being retrieved.

    Returns:
        List[Dict]: A list of stages for the specified sprint, excluding the first and last stage.
    """
    result = await bitrix_model.get_stages(bitrix_sprint_id)

    # Exclude the first and last stages
    return result['result'][1:-1]
