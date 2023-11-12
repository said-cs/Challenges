from solution import calendarMatching, updateCal, mergeCals, flattenCal, getMatchingAvaliabilities, timeToMin, minToTime

# Test cases
def run_tests():
    # Test 1
    calendar1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
    dailyBounds1 = ["9:00", "20:00"]
    calendar2 = [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]]
    dailyBounds2 = ["10:00", "18:30"]
    meetingDuration = 30
    result = calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration)
    print("Test 1 Result:", result)

    # Test 2
    calendar1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
    dailyBounds1 = ["9:00", "20:00"]
    calendar2 = [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]]
    dailyBounds2 = ["10:00", "18:30"]
    meetingDuration = 60
    result = calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration)
    print("Test 2 Result:", result)


if __name__ == "__main__":
    run_tests()
