import time
import random
import datetime
from datetime import date
import pdb
from autoscab.deployments.deployment import Deployment
from autoscab.locators.fredmeyer import FredMeyerLocator
from autoscab.constants.common import NOS, NAS
from autoscab.postbot import PostBot
from autoscab.constants.location import load_cities
from pprint import pformat


class FredMeyerPostbot(PostBot):

    def __postinit__(self):
        # get some random location info
        cities = load_cities()
        oregon = cities[cities['state_id'] == 'OR']
        row = oregon.sample(1)
        self.identity.city = row.city.values[0]
        self.identity.state = 'Oregon'
        self.identity.zip = random.choice(row.zips.values.tolist()[0].split(' '))
        self.logger.info(f'Applying for job with identity:\n{pformat(self.identity.__dict__)}')

    def apply(self):
        self.choose_position()
        self.make_account()
        self.fill_application()

    def choose_position(self):
        self.positions.click()
        time.sleep(2)
        # stash current window handle
        current_window = self.browser.current_window_handle
        self.apply_button.click()
        time.sleep(5)
        # this opens a new tab.
        for handle in self.browser.window_handles:
            if handle != current_window:
                self.browser.switch_to.window(handle)
                break
        self.logger.success('Position chosen, making account')


    def make_account(self):
        # "make new account"
        self.new_account.click()
        self.random_sleep(3,5)

        # fill in form fields
        self.newacct_email.send_keys(self.identity.email)
        self.random_sleep()
        self.newacct_email_conf.send_keys(self.identity.email)
        self.random_sleep()
        self.newacct_pass.send_keys(self.identity.password)
        self.random_sleep()
        self.newacct_pass_conf.send_keys(self.identity.password)
        self.random_sleep()
        self.newacct_first.send_keys(self.identity.name[0])
        self.random_sleep()
        self.newacct_last.send_keys(self.identity.name[1])
        self.random_sleep()
        self.newacct_us.click()
        self.random_sleep()

        # click privacy waiver dialogue
        self.newacct_privacy.click()
        self.random_sleep()
        self.newacct_privacy_accept.click()
        self.random_sleep()

        # make account
        self.newacct_create.click()
        self.logger.success('Account created, waiting up to 45s for application to load')
        self.random_sleep(5,6)
        # long sleep, their backend is slow.
        self.sleep_until_clickable('app_upload_resume', timeout=45)
        # self.random_sleep(15,20)
        self.logger.success('Application Loaded, filling...')

    def fill_application(self):
        # upload documents
        self.app_upload_resume.click()
        self.random_sleep()
        self._tracebacks = False
        self.app_file_input.send_keys(str(self.identity.resume))
        self.random_sleep(2,3)
        self._tracebacks = True
        self.app_phone.send_keys(self.identity.phone)
        self.random_sleep()
        self.app_state_or.click()
        self.random_sleep()
        self.app_address.send_keys(self.identity.address)
        self.random_sleep()
        self.app_city.send_keys(self.identity.city)
        self.random_sleep()
        self.app_zip.send_keys(self.identity.zip)
        self.random_sleep()

        self.app_ssn.send_keys(self.identity.ssn)

        # fuck it click all the rest of the buttons
        for anattr in [
            "app_heard_other",
            "app_no_education",
            "app_high_school",
            "app_not_related",
            "app_notvet",
            "app_yes18",
            "app_notobacco",
            "app_preference1",
            "app_preference2",
            "app_evenings",
            "app_weekends",
            "app_holidays",
            "app_parttime",
            "app_callanytime",
            "available_sunday",
            "available_monday",
            "available_tues",
            "available_weds",
            "available_thurs",
            "available_fri",
            "available_sat",
            "notfired",
            "nostealing",
            "app_nocrime",
            "app_emergency_other",
            "app_sig_acknowledge",
            "app_am18",
            "app_am19",
            "app_am21",
            "app_legaltowork",
            "app_bgcheck",
            "app_workovernight"]:
            button = getattr(self, anattr)
            button.click()
            self.random_sleep(0, 0.5)

        # give a random day int he future as a start date
        futuredate = datetime.date.today() + datetime.timedelta(days=random.randint(1,14))
        datestr = futuredate.strftime('%m/%d/%Y')
        self.app_available.send_keys(datestr)
        self.random_sleep()

        self.previous_kroger.send_keys(random.choice(NAS))
        self.random_sleep()
        self.previous_retail.send_keys(random.choice(NOS))
        self.random_sleep()

        self.app_crime_signature.send_keys(' '.join(self.identity.name))

        # fake emergency contact
        self.app_emergency_lname.send_keys(self.identity.faker.first_name())
        self.random_sleep()
        self.app_emergency_fname.send_keys(self.identity.faker.last_name())
        self.random_sleep()
        self.app_emergency_phone.send_keys(self.identity.faker.phone_number())
        self.random_sleep()

        self.app_sig.send_keys(' '.join(self.identity.name))

        self.random_sleep()
        self.submit_application.click()
        self.random_sleep(10,15)
        self.logger.success("Completed Application!")



FredMeyerDeployment = Deployment(
    name="fredmeyer",
    urls=['https://kroger.eightfold.ai/careers?query=1976116&domain=kroger.com&location_distance_km=100&messenger=email'],
    locators=dict(FredMeyerLocator.__dict__),
    postbot=FredMeyerPostbot,
    active_dates=(date(2021,12,1), date(2021,12,31))
)