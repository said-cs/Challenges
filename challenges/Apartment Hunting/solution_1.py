def apartmentHunting(blocks, reqs):
    """
    Finds the optimal appartment based on the maximum distance to the required facilities

    Args:
        blocks (list of dicts): list of appartment blocks where each block is represented as a dictionnary.
            Each disctionnary contains information about the facilities in that block.
        reqs (list of str): List of required facilities

    Returns:
        int: Index of the optimal appartment block.

    Time Complexity:
        O(n^2 * m), where n is the number of blocks and m the number of facilities.

    Space Complexity:
        O(n), where n is the number of blocks

    Example:
        blocks = [
            {'gym': False, 'school': True, 'store': False},
            {'gym': True, 'school': False, 'store': False},
            {'gym': True, 'school': True, 'store': False},
            {'gym': False, 'school': True, 'store': False},
        ]
        reqs = ['gym', 'school', 'store']
        result = apartmentHunting(blocks, reqs)
        print(result)  # Output: 3
    """

    # Initialize an array to store the maximum distance at each block
    maxDistanceAtBlocks = [float("-inf") for block in blocks]

    # Iterate through each block
    for i in range(len(blocks)):
        # Iterate through each required facility
        for req in reqs:
            closestReqDistance = float("inf")

            # Find the closest block with the required facility
            for j in range(len(blocks)):
                if blocks[j][req]:
                    closestReqDistance = min(closestReqDistance, distanceBetween(i, j))
                
            # Update the maximum distance for the current block
            maxDistanceAtBlocks[i] = max(maxDistanceAtBlocks[i], closestReqDistance)

    # Return the index of the min max distance
    return getMinIdxValue(maxDistanceAtBlocks)


def distanceBetween(a, b):
    """
    Returns the distance between two indices

    Args:
        a (int): Index of the first block
        b (int): Index of the seond block

    Returns:
        int: Distance between two indices
    """
    return abs(a - b)

def getMinIdxValue(array):
    """
    Returns the idx of the min value in the array
    
    Args:
        array (list): List of numeric values

    Returns:
        int: Index of the min value
    """
    minValue = float("inf")
    minValueIdx = 0

    # Iterate through an index to find the minimun and its index
    for i in range(len(array)):
        if array[i] < minValue:
            minValue = array[i]
            minValueIdx = i

    return minValueIdx