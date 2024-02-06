if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    # Convert the map object to a list
    scores = list(arr)

    max_score = float('-inf')  
    runner_up_score = float('-inf')  

    # Iterate through the scores to find max_score and runner_up_score
    for score in scores:
        if score > max_score:
            runner_up_score = max_score
            max_score = score
        elif score > runner_up_score and score != max_score:
            runner_up_score = score

    # Print the runner-up score
    print(runner_up_score)
