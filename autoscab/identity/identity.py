import typing
from pathlib import Path
import random
from datetime import date
from math import floor
from random import randint
import warnings

import requests
from faker import Faker

from autoscab.identity.resume import make_resume
from autoscab.constants.agents import USER_AGENTS
from autoscab.utils import random_email
from autoscab.constants.resume import degrees, unis

import sys
if sys.version_info.minor >= 8:
    from typing import Literal
else:
    from typing_extensions import Literal

MAIL_SERVICES = Literal['guerilla', 'mailtm', 'random']

class Identity:
    def __init__(self, email_service:MAIL_SERVICES = 'random', age_range = (21,65), **kwargs):
        self.email_service = email_service

        self.faker = Faker()

        self.name = self.get_name()
        self.first_name, self.last_name = self.name[0], self.name[1]

        # Age
        self.dob = self.faker.date_of_birth(minimum_age=age_range[0], maximum_age=age_range[1]) # type: date
        self.age = floor((date.today() - self.dob).days / 365)

        self.username = f"{self.first_name}{self.last_name}{self.dob.year}_{randint(0,10000)}"


        password_kwargs = kwargs.get('password', {})
        self.password = self.faker.password(**password_kwargs)
        self.ssn = self.faker.ssn()
        phone = ''
        while len(phone)<1 or len(phone)>12:
            phone = self.faker.phone_number()
        self.phone = phone
        self.address = self.faker.street_address()
        self.city = self.faker.city()
        self.state = self.faker.state()
        self.zip = self.faker.zipcode()


        self.user_agent = random.choice(USER_AGENTS)

        email = self.get_email(self.email_service)
        self.email = email['email']
        self.email_sid = email['sid']

        self.university = random.choice(unis)
        self.degree = random.choice(degrees)
        self.company = self.faker.company()
        self.job = self.faker.job()

        self.resume = self.get_resume()




    def get_name(self) -> typing.List[str]:
        return [self.faker.first_name(), self.faker.last_name()]

    def get_email(self, service:MAIL_SERVICES='guerilla') -> typing.Dict[str,str]:
        if service == 'guerilla':
            response = requests.get('https://api.guerrillamail.com/ajax.php?f=get_email_address').json()
            fake_email = response.get('email_addr')
            mail_sid = response.get('sid_token')
        elif service == 'mailtm':
            fake_email = requests.post('https://api.mail.tm/accounts', data='{"address":"' + random_email(
                self.name[0] + ' ' + self.name[1]) + '","password":" "}',
                                       headers={'Content-Type': 'application/json'}).json().get('address')
            mail_sid = requests.post('https://api.mail.tm/token',
                                     data='{"address":"' + fake_email + '","password":" "}',
                                     headers={'Content-Type': 'application/json'}).json().get('token')
        elif service == "random":
            fake_email = self.faker.free_email()
            mail_sid = ''
        else:
            raise ValueError('Dont know what email service to use! try one of guerilla or mailtm')

        return {'email': fake_email, 'sid': mail_sid}

    def get_password(self) -> str:
        return self.faker.password()

    def get_resume(self) -> Path:
        return make_resume(
            name = " ".join(self.name),
            email = self.email,
            uni=self.university,
            degree=self.degree
        )

    def __del__(self):
        """
        On deletion, try to delete our resume
        """
        if hasattr(self, 'resume') and isinstance(self.resume, Path):
            if self.resume.exists():
                try:
                    self.resume.unlink()
                except Exception as e:
                    warnings.warn(f'Could not delete resume file, got exception: {e}')



