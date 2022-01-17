from autoscab.locators import Locator, Location
from selenium.webdriver.common.by import By


Starbucks_Locator = Locator(
    locations={
    # accept privacy agreement
    "privacy" : Location(
        By.XPATH,
         '//*[@id="dialogTemplate-dialogForm-StatementBeforeAuthentificationContent-ContinueButton"]',
        'click'
    ),  
    # click register as new candidate
    "newacct_button" : Location(
        By.XPATH,
         '//*[@id="dialogTemplate-dialogForm-login-register"]',
        'click'
    ),  
    # fill new candidate username
    "newacct_username" : Location(
        By.XPATH,
         '//*[@id="dialogTemplate-dialogForm-userName"]',
        'send_keys',
        "{username}"
    ),    
    # fill new candidate password
    "newacct_pass" : Location(
        By.XPATH,
         '//*[@id="dialogTemplate-dialogForm-password"]',
        'send_keys',
        '{password}'
    ),    
    # fill re-enter password
    "newacct_repass" : Location(
        By.XPATH,
         '//*[@id="dialogTemplate-dialogForm-passwordConfirm"]',
        'send_keys',
        '{password}'
    ),  
    # fill Personal Email Address
    "newacct_email" : Location(
        By.XPATH,
         '//*[@id="dialogTemplate-dialogForm-email"]',
        'send_keys',
        '{email}'
    ),  
    # fill Re-enter Personal Email Address
    "newacct_reemail" : Location(
        By.XPATH,
         '//*[@id="dialogTemplate-dialogForm-emailConfirm"]',
        'send_keys',
        '{password}'
    ),  
    # Register click button for next page
    "newacct_next1" : Location(
        By.XPATH,
         '//*[@id="dialogTemplate-dialogForm-defaultCmd"]',
        'click'
    ),  
    # # optional click import data from indeed
    # "#" : Location(
    #     By.XPATH,
    #      '//*[@id="editTemplateMultipart-editForm-content-ftf-gp-j_id_id16pc8-page_0-ResumeParsingBlock-UploadResumeBlock-IndeedRadio_7"]'
    # ),
    # # else optional click I want to upload a resume
    # "#newacct_resume" : Location(
    #     By.XPATH,
    #      '//*[@id="editTemplateMultipart-editForm-content-ftf-gp-j_id_id16pc8-page_0-ResumeParsingBlock-UploadResumeBlock-resumeUploadRadio_2"]'
    # ),
    # else click fill application manually
    "resume_manual" : Location(
        By.XPATH,
         '//*[@id="editTemplateMultipart-editForm-content-ftf-gp-j_id_id16pc8-page_0-ResumeParsingBlock-UploadResumeBlock-resumeSkipRadio_1"]',
        'click'
    ),  

    # //this fill application manually bubble is already clicked. Clicking it a second time seems to refresh the page.
    # Click continue to pg 1
    "resume_continue" : Location(
        By.XPATH,
         '//*[@id="editTemplateMultipart-editForm-content-ftf-saveContinueCmdBottom"]',
        'click'
    ),

    # ---------
    # fill Legal First Name
    "bio_first" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-cpi-cfrmsub-frm-dv_cs_candidate_personal_info_FirstName"]',
        'send_keys',
        'first_name'
    ),
    # fill last name
    "bio_last" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-cpi-cfrmsub-frm-dv_cs_candidate_personal_info_LastName"]',
        'send_keys',
        '{last_name}'
    ),  
    # fill Preferred First Name
    "bio_preffirst" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-cpi-cfrmsub-frm-dv_cs_candidate_personal_info_UDFCandidatePersonalInfo_Preferred_32_Name"]',
        'send_keys',
        '{first_name}'
    ),  
    # fill street address
    "bio_address" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-cpi-cfrmsub-frm-dv_cs_candidate_personal_info_Address"]',
        'send_keys',
        '{address}'
    ),  
    # fill city
    "bio_city" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-cpi-cfrmsub-frm-dv_cs_candidate_personal_info_City"]',
        'send_keys',
        '{city}'
    ),  
    # fill zip code
    "bio_zip" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-cpi-cfrmsub-frm-dv_cs_candidate_personal_info_ZipCode"]',
        'send_keys',
        '{zip}'
    ),  
    # drop down country
    "bio_country_us" : Location(
        By.XPATH,
         '/html/body/div[3]/form/span/span[2]/span[4]/table/tbody/tr/td[1]/span[4]/div/span/span/table/tbody/tr[4]/td[3]/span/fieldset/div[1]/select/option[2]',
        'click'
    ),  
    # drop down state
    "bio_state_or" : Location(
        By.XPATH,
         '/html/body/div[3]/form/span/span[2]/span[4]/table/tbody/tr/td[1]/span[4]/div/span/span/table/tbody/tr[4]/td[3]/span/fieldset/div[2]/select/option[41]',
        'click'
    ),  
    # drop down nearest major city
    "bio_city_eug" : Location(
        By.XPATH,
         '/html/body/div[3]/form/span/span[2]/span[4]/table/tbody/tr/td[1]/span[4]/div/span/span/table/tbody/tr[4]/td[3]/span/fieldset/div[3]/select/option[8]',
        'click'
    ),  
    # fill primary contact number
    "bio_phone" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-cpi-cfrmsub-frm-dv_cs_candidate_personal_info_HomePhone"]',
        'send_keys',
        '{phone}'
    ),
    # # fill personal email address
    # "" : Location(
    #     By.XPATH,
    #      '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-cpi-cfrmsub-frm-dv_cs_candidate_personal_info_EmailAddress"]'
    # ),

    # // must match one used to create login?
    # Drop down Have you ever been a Starbucks Partner or Contingent Worker?
    "bio_nopriors" : Location(
        By.XPATH,
         '/html/body/div[3]/form/span/span[2]/span[4]/table/tbody/tr/td[1]/span[4]/div/span/span/table/tbody/tr[6]/td[1]/span/span[1]/select/option[5]',
        'click'
    ),  
    # drop down driven by SCAP
    "bio_no_scap" : Location(
        By.XPATH,
         '/html/body/div[3]/form/span/span[2]/span[4]/table/tbody/tr/td[1]/span[5]/div/span/table/tbody/tr[2]/td[1]/span/select/option[2]',
        'click'
    ),  
    # drop down interest in SCAP
    "bio_no_scap_interest" : Location(
        By.XPATH,
         '/html/body/div[3]/form/span/span[2]/span[4]/table/tbody/tr/td[1]/span[5]/div/span/table/tbody/tr[3]/td[1]/span/select/option[2]',
        'click'
    ),  
    # click to continue to pg 2
    "bio_continue" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]',
        'click'
    ),  
    # check boxes for availability
    "" : Location(
        By.XPATH,
         '/html/body/div[3]/form/span/span[2]/span[4]/table/tbody/tr/td[1]/table/tbody/tr/td/span/span[2]/span/span/table/tbody/tr[2]/th[1]/span/a/span/span/span/span'
    ),  

    # // this one checks all boxes
    # drop down hours per week
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_1-careerSectionMultipleCustomForm-cfrm-cfrmsub-frm-dv_cs_workcondition_HoursPerWeekWilling"]'
    ),  
    # check box willing to work holidays
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_1-careerSectionMultipleCustomForm-cfrm-cfrmsub-frm:dv_cs_workcondition_IsAvailableHolidays"]'
    ),  
    # click to continue to pg 3
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]'
    ),  
    # fill work experience employer
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-we-wei-0-frm-dv_cs_experience_Employer"]'
    ),  
    # fill job title
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-we-wei-0-frm-dv_cs_experience_JobFunction"]'
    ),  

    # //both employer and job title turn into clickable dropdowns as the boxes are filled.
    # click opens selector employer in new page
    "" : Location(
        By.XPATH,
         '/html/body/div[3]/form/span/span[2]/span[4]/table/tbody/tr/td[1]/span[5]/fieldset/div/span/table/tbody/tr[1]/td[1]/span/fieldset/span/a/span/span/span/span'
    ),  
    # click opens selector job title in new page
    "" : Location(
        By.XPATH,
         '/html/body/div[3]/form/span/span[2]/span[4]/table/tbody/tr/td[1]/span[5]/fieldset/div/span/table/tbody/tr[1]/td[2]/span/fieldset/span/a/span/span/span/span'
    ),  

    # //optional
    # fill job duties
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-we-wei-0-frm-dv_cs_experience_Responsibility"]'
    ),  
    # click if current job
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-we-wei-0-frm:dv_cs_experience_CurrentEmployer"]'
    ),  
    # drop down employment status
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-we-wei-0-frm-dv_cs_experience_UDFExperience_wkexp_term"]'
    ),  
    # start date
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-we-wei-0-frm-fc61"]'
    ),  

    # //opens calendar with clickable dates
    # optional click add work experience
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-we-lblAddWorkExperience"]'
    ),  
    # drop down education level
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_1-csef-efi-0-frm-dv_cs_education_StudyLevel"]'
    ),  
    # fill school name
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_1-csef-efi-0-frm-dv_cs_education_Institution"]'
    ),  

    # //also turns into a drop down
    # fill field of study
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_1-csef-efi-0-frm-dv_cs_education_Program"]'
    ),  

    # // also turns into a drop down
    # drop down status
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_1-csef-efi-0-frm-dv_cs_education_UDFEducation_Education_32_Status"]'
    ),  
    # click select school name new page
    "" : Location(
        By.XPATH,
         '/html/body/div[3]/form/span/span[2]/span[4]/table/tbody/tr/td[1]/span[6]/fieldset/div/span/table/tbody/tr[3]/td[1]/span/fieldset/span/a/span/span/span/span'
    ),  
    # click select field new page
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_1-csef-efi-0-frm-fc39"]'
    ),  
    # click add education
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_1-csef-lblAddEducation"]'
    ),  
    # click to continue to pg 4
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]'
    ),  
    # click browse attach documents
    "" : Location(
        By.XPATH,
         '//*[@id="editTemplateMultipart-editForm-content-ftf-gp-j_id_id16pc8-page_0-AttachedFilesBlock-uploadedFile"]'
    ),  
    # fill comment about file
    "" : Location(
        By.XPATH,
         '//*[@id="editTemplateMultipart-editForm-content-ftf-gp-j_id_id16pc8-page_0-AttachedFilesBlock-comment"]'
    ),  
    # click attach
    "" : Location(
        By.XPATH,
         '//*[@id="editTemplateMultipart-editForm-content-ftf-gp-j_id_id16pc8-page_0-AttachedFilesBlock-attachFileCommand"]'
    ),  
    # click if file is relevant
    "" : Location(
        By.XPATH,
         '//*[@id="editTemplateMultipart-editForm-content-ftf-gp-j_id_id16pc8-page_0-AttachedFilesBlock-j_id_id34pc9:0:selectionid"]'
    ),  
    # click if file is resume
    "" : Location(
        By.XPATH,
         '//*[@id="editTemplateMultipart-editForm-content-ftf-gp-j_id_id16pc8-page_0-AttachedFilesBlock-j_id_id34pc9:0:resumeselectionid"]'
    ),  
    # click to delete file
    "" : Location(
        By.XPATH,
         '//*[@id="editTemplateMultipart-editForm-content-ftf-gp-j_id_id16pc8-page_0-AttachedFilesBlock-j_id_id34pc9-0-attachmentFileDelete"]'
    ),  
    # click sure you want to delete yes
    "" : Location(
        By.XPATH,
         '//*[@id="editTemplateMultipart-editForm-content-ftf-gp-j_id_id16pc8-page_0-AttachedFilesBlock-j_id_id4pc9-YesDeleteAttachedFileCommand"]'
    ),  
    # click to continue to pg 5
    "" : Location(
        By.XPATH,
         '//*[@id="editTemplateMultipart-editForm-content-ftf-saveContinueCmdBottom"]'
    ),  
    # click yes legally employable
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-preq-j_id_id7pc10-page__1-q-j_id_id2pc11-0-qr_com.taleo.functionalcomponent.prescreening.entity.question.PossibleAnswer__95901"]'
    ),  
    # click > 16
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-preq-j_id_id7pc10-page__1-q-j_id_id2pc11-1-qr_com.taleo.functionalcomponent.prescreening.entity.question.PossibleAnswer__138977"]'
    ),  
    # click yes dress code
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-preq-j_id_id7pc10-page__1-q-j_id_id2pc11-2-qr_com.taleo.functionalcomponent.prescreening.entity.question.PossibleAnswer__139014"]'
    ),  
    # click yes able to do job
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-preq-j_id_id7pc10-page__1-q-j_id_id2pc11-3-qr_com.taleo.functionalcomponent.prescreening.entity.question.PossibleAnswer__146937"]'
    ),  
    # click to continue to pg 6
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]'
    ),  
    # click yes a veteran
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-koq-j_id_id7pc10-page__1-q-j_id_id2pc11-0-qr_com.taleo.functionalcomponent.prescreening.entity.question.PossibleAnswer__140694"]'
    ),  
    # click not a veteran
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-koq-j_id_id7pc10-page__1-q-j_id_id2pc11-0-qr_com.taleo.functionalcomponent.prescreening.entity.question.PossibleAnswer__140695"]'
    ),  
    # click no answer veteran
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-koq-j_id_id7pc10-page__1-q-j_id_id2pc11-0-qr_com.taleo.functionalcomponent.prescreening.entity.question.PossibleAnswer__140696"]'
    ),  
    # click spouse is vet
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-koq-j_id_id7pc10-page__1-q-j_id_id2pc11-1-qr_com.taleo.functionalcomponent.prescreening.entity.question.PossibleAnswer__140677"]'
    ),  
    # click spouse not vet
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-koq-j_id_id7pc10-page__1-q-j_id_id2pc11-1-qr_com.taleo.functionalcomponent.prescreening.entity.question.PossibleAnswer__140678"]'
    ),  
    # click no answer spouse vet
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-koq-j_id_id7pc10-page__1-q-j_id_id2pc11-1-qr_com.taleo.functionalcomponent.prescreening.entity.question.PossibleAnswer__140679"]'
    ),  
    # click to continue to pg 7
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]'
    ),  
    # 4212 this bubble is labeled “Please select”
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-0-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__27060130812"]'
    ),  

    # //wtf?
    # Click 4212 applies yes
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-0-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__27160130812"]'
    ),  
    # click 4212 applies no
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-0-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__27260130812"]'
    ),  
    # gender this bubble is labeled “Please select”
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-1-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__22160130812"]'
    ),  

    # //wtf?
    # click gender female
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-1-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__22260130812"]'
    ),  
    # click gender male
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-1-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__22360130812"]'
    ),  
    # click gender won’t provide
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-1-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__22460130812"]'
    ),  
    # latino this bubble is labeled “Please select”
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-2-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__24160130812"]'
    ),  
    # click latino yes
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-2-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__24260130812"]'
    ),  
    # click latino no
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-2-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__24360130812"]'
    ),  
    # click latino won’t provide
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-2-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__24460130812"]'
    ),  
    # race this bubble is labeled “Please select”
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-3-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__26160130812"]'
    ),  
    # click race latino
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-3-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__26260130812"]'
    ),  
    # click race American Indian
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-3-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__26360130812"]'
    ),  
    # click race Asian
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-3-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__26460130812"]'
    ),  
    # click race Black
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-3-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__26660130812"]'
    ),  
    # click race Native Hawaiian
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-3-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__26560130812"]'
    ),  
    # click race White
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-3-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__26760130812"]'
    ),  
    # click race two or more
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-3-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__26860130812"]'
    ),  
    # click race won’t provide
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-3-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__26960130812"]'
    ),  
    # click continue to pg 8
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]'
    ),  
    # fill name self ID
    "" : Location(
        By.XPATH,
         '//*[@id="10046"]'
    ),  
    # fill today’s date
    "" : Location(
        By.XPATH,
         '//*[@id="10047"]'
    ),  
    # click have disability
    "" : Location(
        By.XPATH,
         '//*[@id="10048-shadow"]'
    ),  
    # click no disability
    "" : Location(
        By.XPATH,
         '//*[@id="10049-shadow"]'
    ),  
    # click don’t answer
    "" : Location(
        By.XPATH,
         '//*[@id="10050-shadow"]'
    ),  
    # click continue to pg 9
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]'
    ),  
    # click complete questionnaire in new window
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-extServBlock-outputText_takeNowInlineLink"]'
    ),  
    # click yes live with SNAP
    "" : Location(
        By.XPATH,
         '/html/body/form/div[4]/span/div[1]/div/div[1]/div/div/label[1]'
    ),  
    # click no live with SNAP
    "" : Location(
        By.XPATH,
         '/html/body/form/div[4]/span/div[1]/div/div[1]/div/div/label[2]'
    ),  
    # click yes live with TANF
    "" : Location(
        By.XPATH,
         '/html/body/form/div[4]/span/div[1]/div/div[2]/div/div/label[1]'
    ),  
    # click no live with TANF
    "" : Location(
        By.XPATH,
         '/html/body/form/div[4]/span/div[1]/div/div[2]/div/div/label[2]'
    ),  
    # click yes vet
    "" : Location(
        By.XPATH,
         '/html/body/form/div[4]/span/div[1]/div/div[2]/div/div/label[2]'
    ),  
    # click no vet
    "" : Location(
        By.XPATH,
         '/html/body/form/div[4]/span/div[1]/div/div[3]/div/div/label[2]'
    ),  
    # click yes disabled
    "" : Location(
        By.XPATH,
         '/html/body/form/div[4]/span/div[1]/div/div[4]/div/div/label[1]'
    ),  
    # click no disabled
    "" : Location(
        By.XPATH,
         '/html/body/form/div[4]/span/div[1]/div/div[4]/div/div/label[2]'
    ),  
    # click yes collecting unemployment
    "" : Location(
        By.XPATH,
         '/html/body/form/div[4]/span/div[1]/div/div[5]/div/div/label[1]'
    ),  
    # click no collecting unemployment
    "" : Location(
        By.XPATH,
         '/html/body/form/div[4]/span/div[1]/div/div[5]/div/div/label[2]'
    ),  
    # click rec’d unemployment
    "" : Location(
        By.XPATH,
         '/html/body/form/div[4]/span/div[1]/div/div[6]/div/div/label[1]'
    ),  
    # click not rec’d unemployment
    "" : Location(
        By.XPATH,
         '/html/body/form/div[4]/span/div[1]/div/div[6]/div/div/label[2]'
    ),  
    # click yes NA tribe
    "" : Location(
        By.XPATH,
         '/html/body/form/div[4]/span/div[1]/div/div[7]/div/div/label[1]'
    ),  
    # click no NA tribe
    "" : Location(
        By.XPATH,
         '/html/body/form/div[4]/span/div[1]/div/div[7]/div/div/label[2]'
    ),  
    # click next page
    "" : Location(
        By.XPATH,
         '//*[@id="SurveyControl_SurveySubmit"]'
    ),  

    # //directs to page about military service if veteran yes was selected

    # // missed an xpath copy to submit that whole questionnaire
    # click to continue to pg 11
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]'
    ),  
    # dropdown to confirm language
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-eSignatureBlock-selectOneMenu_language"]'
    ),  
    # fill full name
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-eSignatureBlock-cfrmsub-frm-dv_cs_esignature_FullName"]'
    ),  
    # click continue to pg 12
    "" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]'
    ),  
    # click submit final
    "" : Location(
        By.XPATH,
        
         '//*[@id="et-ef-content-ftf-submitCmdBottom"]'
    ),  
    }
)