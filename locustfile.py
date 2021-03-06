import logging
import random

import zmq
from httprunner.exceptions import MyBaseError, MyBaseFailure
from httprunner.loader import load_locust_tests
from httprunner.runner import Runner
from locust import HttpLocust, TaskSet, task
from locust.events import request_failure

logging.getLogger().setLevel(logging.CRITICAL)
logging.getLogger('locust.main').setLevel(logging.INFO)
logging.getLogger('locust.runners').setLevel(logging.INFO)


class WebPageTasks(TaskSet):
    def on_start(self):
        self.test_runner = Runner(self.locust.config, self.client)
        self.testcases = load_locust_tests(self.locust.file_path)

    @task(weight=1)
    def test_any(self):
        teststeps = random.choice(self.locust.tests)
        for teststep in teststeps:
            try:
                self.test_runner.run_test(teststep)
            except (MyBaseError, MyBaseFailure) as ex:
                request_failure.fire(
                    request_type=teststep.get("request", {}).get("method"),
                    name=teststep.get("name"),
                    response_time=0,
                    exception=ex
                )


class WebPageUser(HttpLocust):
    task_set = WebPageTasks
    min_wait = 10
    max_wait = 30

    file_path = "/opt/ApiAutoProjectNEW/STL/logs/httprunner.json"
    locust_tests = load_locust_tests(file_path)
    config = locust_tests["config"]
    tests = locust_tests["tests"]

    host = config.get('request', {}).get('base_url', '')
