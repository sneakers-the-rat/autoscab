import time
import random
import datetime
import pdb
from autoscab.deployments.deployment import Deployment
from autoscab.locators.starbucks import Starbucks_Locator
from autoscab.constants.common import NOS, NAS
from autoscab.postbot import PostBot
from autoscab.constants.location import load_cities
from pprint import pformat
from datetime import date


class StarbucksPostBot(PostBot):

    def __postinit__(self):
        # get some random location info
        cities = load_cities()
        oregon = cities[cities['state_id'] == 'OR']
        oregon = oregon[oregon['city'] == "Eugene"]
        row = oregon.sample(1)
        self.identity.city = row.city.values[0]
        self.identity.state = 'Oregon'
        self.identity.zip = random.choice(row.zips.values.tolist()[0].split(' '))
        self.logger.info(f'Applying for job with identity:\n{pformat(self.identity.__dict__)}')

    def apply(self):
        self.make_account()


    def make_account(self):
        # agree to privacy policy
        self.privacy.click()

        # wait until next field loaded
        self.sleep_until_clickable('newacct_button', timeout=10)
        # click new candidate
        self.newacct_button.click()

        # wait until user page loaded
        actions = ['newacct_username', "newacct_pass", "newacct_repass", "newacct_email", "newacct_reemail", "newacct_next1" ]

        # wait for new page to be loaded
        self.sleep_until_clickable('resume_manual')
        actions2 = ['resume_manual', 'resume_continue']

        self.sleep_until_clickable('bio_first')

    def fill_bio(self):

        # page 2
        actions = [
            'bio_first', 'bio_last', 'bio_preffirst',
            'bio_address', 'bio_city', 'bio_zip', 'bio_country_us', 'bio_state_or', 'bio_city_eug',
            'bio_phone', 'bio_nopriors', 'bio_no_scap', 'bio_no_scap_interest', 'bio_continue'
        ]








StarbucksDeployment = Deployment(
    name="starbucks",
    urls=['https://starbucks.taleo.net/careersection/application.jss?lang=en&type=1&csNo=10900&portal=34100010236&reqNo=1337403&iniurl.src=CWS-13040&isOnLogoutPage=true'],
    locators=Starbucks_Locator,
    postbot=StarbucksPostbot,
    active_dates=(date(2022, 1, 16),None)
)