def vowel_filter(function):

    def wrapper():
        # letters = function()
        return [ch for ch in function() if ch in "ieoua"]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())