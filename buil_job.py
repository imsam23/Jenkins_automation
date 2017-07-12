#!/usr/bin/python
import jenkins
import sys
import time
import os
#For remotely build the jib , we need build token
# Arguments:
# 1 - jenkins url
# 2 - Job path
# 3 - Build token

print('jenkins url', sys.argv[1])
print('Job path', sys.argv[2])
print('Build token', sys.argv[3])

def waitJob2Complete(job_name, job_number) :
    while True:
        time.sleep(5)
        job_info = server.get_job_info(job_name)
        print('Wait for job_number:'+str(job_number) +' to completion ... [lastCompletedBuild:'+ str(job_info['lastCompletedBuild']['number'])+']')
        if job_info['lastCompletedBuild']['number'] >= job_number :
            break;
        elif job_info['color'] != 'blue_anime' and job_info['lastCompletedBuild']['number'] >= job_number :
            break;

# logging jenkins
server = jenkins.Jenkins(sys.argv[1], username="username", password="passowrd")
print('We logged in jenkins')

# trigger job
print('We are going to trigger the job')
server.build_job(sys.argv[2], parameters=None, token=sys.argv[3])
print('We are done')

job_info = server.get_job_info(sys.argv[2])
jobNumber = job_info['nextBuildNumber']

print('Trigger job_number:'+str(jobNumber))

waitJob2Complete(sys.argv[2],jobNumber)

print('\nConsole output:')
print server.get_build_console_output(sys.argv[2], jobNumber).encode('ascii', 'ignore')

build_info = server.get_build_info(sys.argv[2], jobNumber)
print('Build result: '+build_info['result'])

if build_info['result'] != "SUCCESS" :
        sys.exit(1)
