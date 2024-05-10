def jobScheduling(jobs):
    # Sort jobs by deadline and profit in descending order
    jobs.sort(key=lambda x: (-x[1], x[0]))
    
    sequence, total_profit = [], 0  # Initialize variables for sequence of jobs and total profit
    
    for job in jobs:
        time_slot = job[0]  # Get the deadline of the current job
        # Find the time slot for the current job
        while sequence and sequence[-1][1] > time_slot:
            time_slot = sequence[-1][1] + 1
        # Add the job to the sequence and update total profit
        sequence.append((job[0], time_slot, job[2]))
        total_profit += job[2]
    
    return sequence, total_profit  # Return the sequence of jobs and total profit

# Define the jobs with their deadlines and profits
jobs = [(1, 4, 20), (2, 2, 100), (3, 1, 40), (4, 3, 35)]

# Call the jobScheduling function with the list of jobs
sequence, total_profit = jobScheduling(jobs)

# Print the maximum profit sequence of jobs and total profit
print("Following is maximum profit sequence of jobs:")
for job in sequence:
    print(job[0], end=" ")  # Print job IDs
print("\nTotal Profit:", total_profit)  # Print total profit
