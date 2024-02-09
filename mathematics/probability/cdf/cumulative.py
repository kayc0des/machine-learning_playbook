# Cumulative Distribution Function (CFD)
# It's a function that gives the probability that a random variable X is less than or equal to a certain value x.

""" Understanding Percentiles """

def pencentile_rank(scores, your_score):
    """Determine the percentile from a list of scores w.r.t a certain score"""

    count = 0

    for score in scores:
        if score <= your_score:
            count += 1

    percentile = 100 * count / len(scores)
    return percentile


""" Using percentile rank to determine the Score """

def Percentile2(scores, percentile_rank):
    scores.sort()
    index = percentile_rank * (len(scores)-1) / 100
    return scores[index]


""" --- Cumulative Distribution Function (CFD) --- """
def EvalCdf(t, x):
    count = 0.0
    for value in t:
        if value <= x:
            count += 1

    prob = count / len(t)
    return prob