This Python script calculates the average marks of a student from a list of student records.  
It demonstrates how to:
- Read and process user input
- Store data using dictionaries
- Calculate mean using the `statistics` module
- Format output to two decimal places using f-strings



if __name__ == '__main__':
    
    import statistics
    
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    average = statistics.mean(student_marks[query_name]) 
    print(f"{average:.2f}")
