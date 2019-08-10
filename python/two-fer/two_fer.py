# parameter 'name' has a default argument 'you'
def two_fer(name="you"):
    # using str.format()
    return "One for {}, one for me.".format(name)
    # using f-string
    # return f"One for {name}, one for me."
