def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    """
    Finds available time slots in the schedule of two individuals.

    Args:
        calendar1 (list): list of existing appoitntments for individual 1.
        dailyBounds1 (list): Daily schedule bounds for individual 1.
        calendar2 (list): list of existing appoitntments for individual 2.
        dailyBounds2 (list): Daily schedule bounds for individual 2.
        meetingDuration (duration): Duration of the meeting in minutes.

    Returns:
        list: List of available slots for the meeting in [hh:mm] format.

    O(c1 + c2) Time Complexity | O(c1 + c2) Space complexity, where c1 and c2 are the lengths of calendar1 and calendar2.
    """
    # Update clandars with daily bounds, merge them, flatten, and find avaliable time slots.
    updatedCal1 = updateCal(calendar1, dailyBounds1)
    updatedCal2 = updateCal(calendar2, dailyBounds2)
    mergedCals = mergeCals(updatedCal1, updatedCal2)
    flattenedCal = flattenCal(mergedCals)
    return getMatchingAvaliabilities(flattenedCal, meetingDuration)


def updateCal(cal, dailyBound):
    """
    Updates the calendar with the daily bounds.

    Args:
        cal (list): List of existing appointments.
        dailyBound (list): Daily schedule bounds.

    Returns:
        list: Updated calendar with daily bounds in minutes.
    """
    updated = cal[:]
    updated.insert(0, ["0:00", dailyBound[0]])
    updated.append([dailyBound[1], "23:59"])
    return list(map(lambda m: [timeToMin(m[0]), timeToMin(m[1])], updated))

def mergeCals(cal1, cal2):
    """
    Merge two Calendars while maintaining chronological order.

    Args:
        cal1 (list): Calendar of individual 1.
        cal2 (list): Calendar of individual 2.

    Returns:
        list: Merged calendar in chronological order.
    """
    merged = []
    i, j = 0, 0
    while i < len(cal1) and j < len(cal2):
        meeting1 = cal1[i]
        meeting2 = cal2[j]
        if meeting1[0] < meeting2[0]:
            merged.append(meeting1)
            i += 1
        else:
            merged.append(meeting2)
            j += 1

    while i < len(cal1):
        merged.append(cal1[i])
        i += 1

    while j < len(cal2):
        merged.append(cal2[j])
        j += 1

    return merged

def flattenCal(cal):
    """
    Combines overlapping time slots in th calendar.

    Args:
        cal (list): calendar with overlapping time slots.

    Returns: 
        list: Flattened calendar with non-overlapping time slots.
    """
    flattened = [cal[0]]
    for i in range(1, len(cal)):
        previousStart, previousEnd = flattened[-1]
        currentStart, currentEnd = cal[i]

        if previousEnd >= currentStart:
            flattened[-1] = [previousStart, max(previousEnd, currentEnd)]
        else:
            flattened.append([currentStart, currentEnd])

    return flattened

def getMatchingAvaliabilities(cal, duration):
    """
    Finds available time slots for the specified meeting duration.

    Args:
        cal (list): Flattened calendar with non-overlapping time slots.
        duration (int): Duration of the meeting in minutes

    Returns:
        list: Avaliable time slots for the meeting in minutes. 
    """
    avaliabilities = []
    for i in range(1, len(cal)):
        end = cal[i][0]
        start = cal[i-1][1]
        avaliability = end - start
        if avaliability >= duration:
            avaliabilities.append([start, end])
    
    return list(map(lambda m : [minToTime(m[0]), minToTime(m[1])], avaliabilities))

def timeToMin(time):
    """
    Convert the time form the format [hh:mm] to minutes.

    Args: 
        time (str): time in "hh:mm" format

    Returns:
        int: Time in minutes
    """
    hours, mins = list(map(int, time.split(":")))
    return hours * 60 + mins

def minToTime(time):
    """
    Convert the time from from minutes to the format "hh:mm"

    Args:
        time (int): Time in minutes.

    Returns:
        string: Time in "hh:mm" format.
    """
    hours = time // 60
    mins = time % 60
    hoursString = str(hours)
    minsString = "0" + str(mins) if mins < 10 else str(mins)
    return hoursString + ":" + minsString
