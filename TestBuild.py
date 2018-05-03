import jenkins
import sys

username = 'charles.whaples'
password = 'placeholder'

parameter_name = "testcase_name"
parameter_value = "test_name"

job_name = "job_name"

jenkins_url = "http://jenkins.orasi.com"

build_token = "custom_token"

j = jenkins.Jenkins(jenkins_url,username,password)
j.build_job(job_name,{parameter_name:parameter_value},token=build_token)

