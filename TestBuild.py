import jenkins
import sys

username = 'charles.whaples'
password = 'placeholder'

test_name = sys.argv[1]
test_suite = sys.argv[2]

job_name = "SlaveTestBuild"

jenkins_url = "http://10.8.32.144"

build_token = "thynicemouseswing"

j = jenkins.Jenkins(jenkins_url,username,password)
j.build_job(job_name,{"TEST_SUITE":test_suite,"TEST_NAME":test_name},token=build_token)
