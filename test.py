import datetime
import json
import unittest

import requests

from asvz_register import login, get_enrollment_time, register, enroll, error_msgs, load_credentials


class RegisterTests(unittest.TestCase):
    def testGetEnrollmentTime(self):
        fr, to = get_enrollment_time(95699)
        assert fr == datetime.datetime(2020, 7, 6, 13, 5, tzinfo=datetime.timezone(datetime.timedelta(seconds=7200)))
        assert to == datetime.datetime(2020, 7, 7, 13, 5, tzinfo=datetime.timezone(datetime.timedelta(seconds=7200)))

    def testLoginAndEnroll(self):
        """
            Get an up too date lesson_id where login is no longer possible.
        """
        req = requests.get("https://asvz.ch/asvz_api/event_search?_format=json&limit=60")
        lessons = json.loads(req.content.decode())['results']
        no_free_places = [l for l in lessons if l['places_free'] == 0]
        assert len(no_free_places) > 0
        usernameStr, passwordStr = load_credentials()
        lesson_id = no_free_places[0]['url'].split("/")[-1]
        headers = login(usernameStr, passwordStr)
        assert 'Authorization' in headers
        err, val = enroll(headers, lesson_id) # Anmeldefrist vorbei -> 422
        if err:
            assert err in error_msgs


if __name__ == '__main__':
    unittest.main()
