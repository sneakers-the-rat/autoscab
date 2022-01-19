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
from selenium.common.exceptions import ElementNotInteractableException


class StarbucksPostBot(PostBot):

    identity_args = {
        'password': {
            'special_chars': False
        }
    }

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

    def apply(self) -> bool:
        self.make_account()
        self.fill_bio()
        self.fill_availability()
        self.fill_experience()
        self.fill_resume()
        self.fill_aboutme()
        self.fill_disability()
        self.fill_tax()
        self.fill_confirm()

        self.sleep_until_clickable('completed')
        success = self.confirm()
        self.print_feedback(success)
        return success


    def make_account(self):
        # agree to privacy policy
        self.privacy.click()

        # wait until next field loaded
        self.sleep_until_clickable('newacct_button', timeout=10)
        # click new candidate
        self.newacct_button.click()

        # wait until user page loaded
        actions = ['newacct_username', "newacct_pass", "newacct_repass", "newacct_email", "newacct_reemail", "newacct_next1" ]
        self.execute(actions)
        # wait for new page to be loaded
        self.sleep_until_clickable('resume_manual')
        actions2 = ['resume_manual', 'resume_continue']
        self.execute(actions2)
        self.sleep_until_clickable('bio_first')

    def fill_bio(self):

        # page 2
        actions = [
            'bio_first', 'bio_last', 'bio_preffirst',
            'bio_address', 'bio_city', 'bio_zip', 'bio_country_us', 'bio_state_or', 'bio_city_eug',
            'bio_phone', 'bio_nopriors', 'bio_no_scap', 'bio_no_scap_interest', 'bio_continue'
        ]
        self.execute(actions)
        self.sleep_until_clickable('availability_all')

    def fill_availability(self):
        # sometimes you do get ppl that just are available at any time..
        if random.random()<0.05:
            self.availability_all.click()
        else:
            # get all checkboxes
            checkboxes = self.availability_panel.find_elements_by_tag_name('input')
            # introduce a lil entropy... be a morning or night person
            morning_person = False
            if random.random()>0.5:
                morning_person = True
            weekends=True
            if random.random()>0.8:
                weekends = False

            # randomly choose some checkboxes
            if morning_person:
                to_check = [box for box in checkboxes if 'Overnight' not in box.get_attribute('class') and random.random()<0.9]
            else:
                to_check = [box for box in checkboxes if
                            'EarlyMorning' not in box.get_attribute('class') and random.random() < 0.9]

            if not weekends:
                to_check = [box for box in to_check if 'Sunday' not in box.get_attribute('class') and 'Saturday' not in box.get_attribute('class')]

            # check the boxes
            for box in to_check:
                box.click()

        # hours wiilling to work & work holidays
        self.available_fulltime.click()
        self.available_holidays.click()
        self.available_continue.click()
        self.sleep_until_clickable('exp_employer')

    def fill_experience(self):

        # fill one prior job...
        self.exp_employer.send_keys(self.identity.company)
        self.exp_job.send_keys(self.identity.job)
        self.exp_stillemployed.click()
        self.exp_current.click()

        # years and months ago we worked there
        years_start = random.randint(1,5)
        months_start = random.randint(0,12)

        self.exp_start.click()
        for i in range(years_start):
            self.exp_year_back.click()
        for i in range(months_start):
            self.exp_month_back.click()

        # choose a random day
        days = self.exp_days.find_elements_by_class_name('day')
        day = random.choice(days)
        try:
            day.click()
        except ElementNotInteractableException:
            self.logger.debug('not interactable :(')

        ## Education
        # say we're in college...
        self.exp_college.click()
        # give us a, say 75% change we went to uo
        if random.random()<0.75:
            college = "University of Oregon"
            self.identity.university = college
        else:
            college = self.identity.university

        self.exp_college_name.send_keys(college)
        self.exp_field.send_keys(self.identity.degree)

        # if we're younger, we might still be in college
        if self.identity.age < 24:
            self.exp_incollege.click()
        else:
            self.exp_graduated.click()

        self.exp_continue.click()
        self.sleep_until_clickable('docs_continue')

    def fill_resume(self):

        # only submit resume sometimes
        # apparently can't upload for security reasons. oh well
        # if random.random()>0.5:
        #     # get another resume bc we may have changed universities
        #     resume = self.identity.get_resume()
        #     self.docs_upload.send_keys(str(resume))
        #     self.docs_describe.send_keys(
        #         random.choice([
        #             'resume', 'Resume', "my resume", "My Resume", "My Resume Is Attached", 'CV', 'cv', 'C/V', "Cv", "curriculum vitae", 'Curriculum Vitae'
        #         ])
        #     )
        #     self.docs_attach.click()

        self.docs_continue.click()
        self.sleep_until_clickable('q_legal')

    def fill_aboutme(self):
        actions = ['q_legal', 'q_16', 'q_dress', 'q_able', 'q_continue']
        self.execute(actions)

        self.vet_no.click()
        if random.random()>0.5:
            self.vet_no_spouse.click()
        else:
            self.vet_no_answer_spouse.click()
        self.vet_continue.click()
        self.sleep_until_clickable('eeo_no_protected')

        # EEO
        self.eeo_no_protected.click()
        random.choice([self.eeo_female, self.eeo_male, self.eeo_nogender]).click()

        latino = random.choice([self.eeo_latino, self.eeo_nolatino, self.eeo_noinfolatino])
        latino.click()

        if latino == self.eeo_latino:
            self.eeo_race_latino.click()
        else:
            # just bc i don't want to enter all the locators
            self.eeo_race_white.click()

        self.eeo_continue.click()
        self.sleep_until_clickable('dis_name')

    def fill_disability(self):

        self.dis_name.send_keys(" ".join(self.identity.name))
        self.dis_date.send_keys(date.today().strftime('%m/%d/%y'))
        random.choice([self.dis_no, self.dis_no_answer]).click()
        self.dis_continue.click()
        self.sleep_until_clickable('tax_open')

    def fill_tax(self):

        self.tax_open.click()

        self.sleep_until_clickable('tax_nosnap', 30)
        self.tax_nosnap.click()
        self.tax_notanf.click()
        self.tax_novet.click()
        self.tax_nodisable.click()
        self.tax_nounemploy.click()
        self.tax_noapply.click()
        self.tax_nonnative.click()
        self.tax_next.click()
        self.sleep_until_clickable('tax_submit')
        self.tax_submit.click()

    def fill_confirm(self):
        self.sleep_until_clickable('conf_name')
        self.conf_name.send_keys(" ".join(self.identity.name))
        self.conf_continue.click()
        self.sleep_until_clickable('submit_app')
        self.submit_app.click()

    def confirm(self) -> bool:
        return self.completed.text == "Process completed"










StarbucksDeployment = Deployment(
    name="starbucks",
    urls=['https://starbucks.taleo.net/careersection/application.jss?lang=en&type=1&csNo=10900&portal=34100010236&reqNo=1337403&iniurl.src=CWS-13040&isOnLogoutPage=true'],
    locators=Starbucks_Locator,
    postbot=StarbucksPostBot,
    active_dates=(date(2022, 1, 16),None),
)