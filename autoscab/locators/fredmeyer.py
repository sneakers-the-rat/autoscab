from selenium.webdriver.common.by import By
from autoscab.locators import Locator

class FredMeyerLocator:
    # login stuff
    positions = (By.CLASS_NAME, 'position-card')
    apply_button = (By.CLASS_NAME, 'position-apply-button')
    new_account = (By.CSS_SELECTOR, '.bottomLink > a')

    newacct_email = (By.ID, 'fbclc_userName')
    newacct_email_conf = (By.ID, 'fbclc_emailConf')
    newacct_pass = (By.ID, 'fbclc_pwd')
    newacct_pass_conf = (By.ID, 'fbclc_pwdConf')
    newacct_first = (By.ID, 'fbclc_fName')
    newacct_last = (By.ID, 'fbclc_lName')
    newacct_country = (By.ID, 'fbclc_country')
    newacct_us = (By.CSS_SELECTOR, '#fbclc_country > option[value=US]')
    newacct_create = (By.ID, 'fbclc_createAccountButton')
    newacct_privacy = (By.ID, 'dataPrivacyId')
    newacct_privacy_accept = (By.CSS_SELECTOR, '.modal-footer .globalPrimaryButton')

    apply_email = (By.ID, 'username')
    apply_password = (By.ID, 'password')

    # click these to open the 'upload from device' menu
    app_upload_resume = (By.XPATH, '//form/div[3]/div/div[1]/div[9]/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/div[6]/span[1]')
    app_upload_cover_letter = (By.ID, '54:_attachIcon')

    # this finds all the 'upload from device' input buttons for resume, cover letter
    app_file_input = (By.CSS_SELECTOR, '#sfOverlayMgr input')

    # profile
    app_phone = (By.CSS_SELECTOR, 'input[name="cellPhone"]')
    app_state_or = (By.CSS_SELECTOR, 'select[name="state"] > option[value="58"]')
    app_address = (By.CSS_SELECTOR, 'input[name="address"]')
    app_city  = (By.CSS_SELECTOR, 'input[name="city"]')
    app_zip  = (By.CSS_SELECTOR, 'input[name="zip"]')

    app_work_history_bar = (By.ID, '646:topBar')
    app_job_info_bar = (By.ID, '1130:topBar')

    app_ssn = (By.CSS_SELECTOR, 'input[name="ssn"]')
    app_heard_other = (By.CSS_SELECTOR, 'select[name="referralSourceExternal"] > option[value="55705"]')
    app_no_education = (By.CSS_SELECTOR, 'select[name="app_EdHighestLevelDiscipline"] > option[value="344"]')
    app_high_school = (By.CSS_SELECTOR, 'select[name="app_EdHighestLevel"] > option[value="449"]')
    app_not_related = (By.CSS_SELECTOR, 'select[name="app_ACERelatives"] > option[value="344"]')
    app_notvet = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[1]/div/div/div[19]/div/div/span/select/option[2]')
    app_yes18 = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[1]/div/div/div[21]/div/div/span/select/option[3]')
    app_notobacco = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[1]/div/div/div[23]/div/div/span/select/option[2]')
    app_preference1 = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[1]/div/div/div[27]/div/div/span/select/option[2]')
    app_preference2 = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[1]/div/div/div[29]/div/div/span/select/option[2]')

    app_available = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[1]/div/div/div[35]/div/div/span[1]/span/input')
    app_evenings = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[1]/div/div/div[37]/div/div/span/select/option[3]')
    app_weekends = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[1]/div/div/div[39]/div/div/span/select/option[3]')
    app_holidays = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[1]/div/div/div[41]/div/div/span/select/option[3]')
    app_parttime = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[1]/div/div/div[43]/div/div/span/select/option[4]')
    app_callanytime = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[1]/div/div/div[45]/div/div/span/select/option[3]')

    available_sunday = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[1]/div/div/div[49]/div/div/span/select/option[2]')
    available_monday = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[1]/div/div/div[51]/div/div/span/select/option[2]')
    available_tues = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[1]/div/div/div[53]/div/div/span/select/option[2]')
    available_weds = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[1]/div/div/div[55]/div/div/span/select/option[2]')
    available_thurs = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[1]/div/div/div[57]/div/div/span/select/option[2]')
    available_fri = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[1]/div/div/div[59]/div/div/span/select/option[2]')
    available_sat = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[1]/div/div/div[61]/div/div/span/select/option[2]')

    previous_kroger = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[1]/div/div/div[65]/div[2]/div/span/textarea')
    previous_retail = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[1]/div/div/div[67]/div[2]/div/span/textarea')
    notfired = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[1]/div/div/div[69]/div/div/span/select/option[2]')
    nostealing = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[1]/div/div/div[73]/div/div/span/select/option[2]')

    app_crime_signature = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[1]/div/div/div[81]/div/div/div[1]/input')
    app_nocrime = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[1]/div/div/div[83]/div/div/span/select/option[2]')

    app_emergency_fname = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[1]/div/div/div[89]/div/div/div[1]/input')
    app_emergency_lname = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[1]/div/div/div[93]/div/div/div[1]/input')
    app_emergency_other = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[1]/div/div/div[95]/div/div/span/select/option[6]')
    app_emergency_phone = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[1]/div/div/div[97]/div/div/div[1]/input')

    app_sig_acknowledge = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[1]/div/div/div[107]/div/div/span/select/option[2]')
    app_sig = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[1]/div/div/div[109]/div/div/div[1]/input')

    app_am18 = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[2]/div/div/div[1]/div[2]/div/div[1]/div[1]/span/a')
    app_am19 = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[1]/span/a')
    app_am21 = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[2]/div/div/div[3]/div[2]/div/div[1]/div[1]/span/a')
    app_legaltowork = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[2]/div/div/div[4]/div[2]/div/div[1]/div[1]/span/a')
    app_bgcheck = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[2]/div/div/div[5]/div[2]/div/div[1]/div[1]/span/a')
    app_workovernight = (By.XPATH, '//form/div[3]/div/div[1]/div[14]/div/div[2]/div/div/div[6]/div[2]/div/div[1]/div[1]/span/a')

    submit_application = (By.XPATH, '//form/div[3]/div/div[1]/div[16]/div/span[2]')