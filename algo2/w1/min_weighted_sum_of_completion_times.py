# def diff(weight, length):
#     return (weight, length, weight-length)

# def large_diff_first(job1, job2):
#     w1, length1 = job1
#     w2, length2 = job2
#     diff1 = w1 - length1
#     diff2 = w2 - length2
#     if diff1==diff2:

def larger_diff(job_attributes):
    weight, length = job_attributes
    return (weight-length, weight)

def run(input_file, sort_key):
    job_weights_and_lengths = []
    with open(input_file) as input:
        number_jobs = int(input.readline())
        line_seen = 0
        for line in input or line_seen!=number_jobs:
            weight, length = line.split()
            weight = int(weight)
            length = int(length)
            # job_weights_and_lengths.append(diff(weight, length))
            job_weights_and_lengths.append((weight, length))
            line_seen+=1
        print "{0} line seen".format(line_seen)
        job_weights_and_lengths.sort(key=sort_key, reverse=True)
    # print job_weights_and_lengths[:10]
    completion_time_so_far = 0
    weighted_sum = 0
    for job in job_weights_and_lengths:
        weight, length = job
        completion_time_so_far += length
        weighted_sum += weight*completion_time_so_far
    return weighted_sum

# job_weights_and_lengths = ["1 2", "2 3"]
job_weights_and_lengths = [(1,2), (2,3)]
job_weights_and_lengths.sort(key=larger_diff, reverse=True)
assert job_weights_and_lengths == [(2,3), (1,2)]
# print job_weights_and_lengths

# print (3, 2) > (1, 5)
assert run('./test.txt', larger_diff) == 23
print run('./jobs.txt', larger_diff)