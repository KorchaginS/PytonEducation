def solution(string, ending):

    if len(ending) == 0 : return True
    return True if string[-len(ending):] == ending else False


print(solution('abcde', ''))