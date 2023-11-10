def apartmentHunting(blocks, reqs):
    """
    Finds the optimal appartment based on the maximum distance to the required facilities.

    Args:
        blocks (list of dicts): List of appartment blocks where each block is representes as a dictionnary.
            Each dictionnary contains information about facilities in that block.
        reqs (list of str): list of required facilities.

    Returns:
        int: Index of the optimal apartment block.

    Time Complexity:
        O(n * m), where n is the number of blocks and m is the number of required facilities.

    Space Complexity:
        O(n * m), where n is the number of blocks and m is the number of required facilities.

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
    # Calculate the minimum distances from each block to each required facility
    minDistancesFromBlocks = list(map(lambda req: getMinDistances(blocks, req), reqs))

    # Calculate maximum distances at each block by considering all required facilities
    maxDistanceAtBlocks = getMaxDistances(blocks, minDistancesFromBlocks)

    # Returns the index of the block with the minimum maximum distance
    return getMinIdxValue(maxDistanceAtBlocks)


def getMinDistances(blocks, req):
    """
    Calculate the minimum distances from each block to a specific required facility.

    Args:
        blocks (list of dicts): List of appartment blocks where each block is representes as a dictionnary.
            Each dictionnary contains information about facilities in that block.
        req (str): The required facilitie.

    Returns:
        list: Minimum distances from each block to the specified required facility 
    """
    minDistances = [0] * len(blocks)
    closestReqIdx = float("inf")

    # Forward pass: Finds the closest block with the required facility
    for i in range(len(blocks)):
        if blocks[i][req]:
            closestReqIdx = i
        minDistances[i] = distanceBetween(i, closestReqIdx)

    # Backward pass: Find the closest block with the required facility
    for i in reversed(range(len(blocks))):
        if blocks[i][req]:
            closestReqIdx = i
        minDistances[i] = min(minDistances[i], distanceBetween(i, closestReqIdx))

    return minDistances


def distanceBetween(a, b):
    """
    Returns the distance between two indices.

    Args:
        a (int): Index of the first block.
        b (int): Index of the second block.

    Returns:
        int: Distance between the two indices.
    """
    return abs(a - b)

def getMaxDistances(blocks, minDistancesFromBlocks):
    """
    Calculates the maximum distances at each block by considering all required facilities.

    Args:
        blocks (list of dicts): List of apartment blocks.
        minDistancesFromBlocks (list of lists): Minimum distances from each block to each required facility.

    Returns:
        list: Maximum distances at each block.
    """
    maxDistanceAtBlocks = [0 for block in blocks]

    for i in range(len(blocks)):
        # Get the minimum distances for the current block from all required facilities
        minDistanceAtBlock = list(map(lambda distances: distances[i], minDistancesFromBlocks))

        # Update the maximum distance at the current block
        maxDistanceAtBlocks[i] = max(minDistanceAtBlock)

    return maxDistanceAtBlocks

def getMinIdxValue(array):
    """
    Returns the index of the minimum value in the array.

    Args:
        array (list): List of numeric values.

    Returns:
        int: Index of the minimum value.
    """
    minValue = float("inf")
    minValueIdx = 0

    # Iterate through the array to find the minimum value and its index
    for i in range(len(array)):
        if array[i] < minValue:
            minValue = array[i]
            minValueIdx = i

    return minValueIdx