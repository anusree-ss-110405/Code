def main():
    import sys
    input = sys.stdin.read
    
    data = input().strip().split('\n')
    num_students = int(data[0])
    students = []

    # Read student names and scores
    for i in range(num_students):
        name = data[2 * i + 1]
        score = float(data[2 * i + 2])
        students.append([name, score])

    # Find unique scores and sort them
    scores = sorted(set([student[1] for student in students]))
    
    # Get the second lowest score
    if len(scores) > 1:
        second_lowest_score = scores[1]
    else:
        # Handle edge case where there's only one unique score
        print("Not enough unique scores to determine second lowest.")
        return

    # Find all names with the second lowest score
    names_with_second_lowest = [student[0] for student in students if student[1] == second_lowest_score]

    # Sort names alphabetically
    names_with_second_lowest.sort()

    # Print each name on a new line
    for name in names_with_second_lowest:
        print(name)

if __name__ == '__main__':
    main()
