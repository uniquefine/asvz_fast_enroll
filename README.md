# ASVZ fast enroll 

This is a small python script that enrolls you (a student of ETH) in asvz classes that requre registration (all of them as of summer 2020).

The code logs in before the start of the enrollment and then just posts the enrollment request. This should be faster than a pure selenium registration.

Please [get in touch](mailto:sleising@student.ethz.ch) if the script is broken or you need help. 

## Getting Started 
1. Install Selenium chromedriver or geckodriver [Selenium](http://www.seleniumhq.org/)
2. Install python requirements `pip -r install requirements.txt`
3. Save your netz username and password in a file `credentials.json` in the same folder ```{"username":"your_username", "password":"your_password"}```. Your credentials are only used to login with switch.
4. (Run test with `python3 test.py`)
5. Call `asvz\_register.py <lesson_id>` with find course on asvz, copy the lesson id from the url. 
   Example: for https://schalter.asvz.ch/tn/lessons/95699 `asvz\_register.py 95699`

The script will retrieve the enrollment time and wait for it to start before trying the login. The script must be running to enroll so keep it on a server or some other machine that is online until the enrollment starts.

## Acknowledgments

* Inspired by the code of [ChenChen](https://github.com/ChenchenYo/LoginCode)
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIK0Emk5gUznskkMH5Cf7DiJOf8iVjjk3INrHMDaatEni sleising@student.ethz.ch
