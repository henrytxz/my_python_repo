import numpy as np

def SJF(jobs, job_position):
    #implment Shortest Job First
    print jobs
    print job_position
    my_job = jobs[job_position]
    indices_of_my_job_before_sort = np.where(np.array(jobs) == my_job)[0]
    which_job = list(indices_of_my_job_before_sort).index(job_position)
    jobs.sort()
    print 'jobs now sorted: {0}'.format(jobs)
    indices_of_my_job_after_sort = np.where(np.array(jobs) == my_job)[0]
    return sum(jobs[:indices_of_my_job_after_sort[which_job]+1])    # all the jobs that are quicker and will be run before + my job runs

# assert SJF([3,10,20,1,2], 0) == 6
# assert SJF([3, 10, 10, 20, 1, 2], 1) == 16
# assert SJF([3, 10, 10, 20, 1, 2], 2) == 26
# print SJF([20, 9, 15, 17, 11, 17, 9, 9, 12, 12], 2)
# assert SJF([20, 9, 15, 17, 11, 17, 9, 9, 12, 12], 2) == 27
print SJF([8, 3, 20, 18, 5, 3, 9, 11, 9, 7], 0)

# values = np.array([1,2,3,1,2,4,5,6,3,2,1])
# searchval = 3
# ii = np.where(values == searchval)[0]
# print ii