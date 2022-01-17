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
        '{email}'
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
        '{first_name}'
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
    ## availability
    'availability_panel': Location(
        By.CSS_SELECTOR,
        '#dayPanel',
        'manual'
    ),


    # always available
    "availability_all" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-shiftAvailabilityBlock-AllShift"]',
        'click'
    ),

    'available_fulltime' : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_1-careerSectionMultipleCustomForm-cfrm-cfrmsub-frm-dv_cs_workcondition_HoursPerWeekWilling"]/option[6]',
        'click'
    ),

    # # check box willing to work holidays
    "available_holidays" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_1-careerSectionMultipleCustomForm-cfrm-cfrmsub-frm:dv_cs_workcondition_IsAvailableHolidays"]',
        'click'
    ),
    # # click to continue to pg 3
    "available_continue" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]',
        'click'
    ),
    # # fill work experience employer
    "exp_employer" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-we-wei-0-frm-dv_cs_experience_Employer"]',
        'manual'
    ),
    # # fill job title
    "exp_job" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-we-wei-0-frm-dv_cs_experience_JobFunction"]',
        'manual'
    ),

    'exp_quit': Location(
        By.XPATH,
        '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-we-wei-0-frm-dv_cs_experience_UDFExperience_wkexp_term"]/option[2]',
        'manual'
    ),


    'exp_start': Location(
        By.XPATH,
        '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-we-wei-0-frm-dv_cs_experience_BeginDate.display"]',
        'manual'
    ),
    'exp_end': Location(
        By.XPATH,
        '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-we-wei-0-frm-dv_cs_experience_EndDate.display"]',
        'manual'
    ),
    'exp_year_back': Location(
        By.XPATH,
        '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-we-wei-0-frm-dv_cs_experience_BeginDate-prev-year"]',
        'manual'
    ),
    'exp_month_back': Location(
        By.XPATH,
        '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-we-wei-0-frm-dv_cs_experience_BeginDate-prev-month"]',
        'manual'
    ),
    'exp_days': Location(
        By.XPATH,
        '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-we-wei-0-frm-dv_cs_experience_BeginDate-table"]',
        'manual'
    ),
    'exp_stillemployed': Location(
        By.XPATH,
        '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-we-wei-0-frm-dv_cs_experience_UDFExperience_wkexp_term"]/option[4]',
        'click'
    ),
    'exp_current': Location(
        By.XPATH,
        '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-we-wei-0-frm:dv_cs_experience_CurrentEmployer"]',
        'click'
    ),
    'exp_college': Location(
        By.XPATH,
        '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_1-csef-efi-0-frm-dv_cs_education_StudyLevel"]/option[7]',
        'click'
    ),

    # # fill school name
    "exp_college_name" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_1-csef-efi-0-frm-dv_cs_education_Institution"]',
        'send_keys',
        '{university}'
    ),
    #
    # # //also turns into a drop down
    # # fill field of study
    "exp_field" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_1-csef-efi-0-frm-dv_cs_education_Program"]',
        'send_keys',
        '{degree}'
    ),
    'exp_incollege': Location(
        By.XPATH,
        '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_1-csef-efi-0-frm-dv_cs_education_UDFEducation_Education_32_Status"]/option[2]',
        'click'
    ),
    'exp_graduated': Location(
        By.XPATH,
        '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_1-csef-efi-0-frm-dv_cs_education_UDFEducation_Education_32_Status"]/option[4]',
        'click'
    ),
    #
    # # // also turns into a drop down

    # # click to continue to pg 4
    "exp_continue" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]',
        'click'
    ),
    # # click browse attach documents
    "docs_upload" : Location(
        By.XPATH,
         '//*[@id="editTemplateMultipart-editForm-content-ftf-gp-j_id_id16pc8-page_0-AttachedFilesBlock-uploadedFile"]',
        'manual'
    ),
    # # fill comment about file
    "docs_describe" : Location(
        By.XPATH,
         '//*[@id="editTemplateMultipart-editForm-content-ftf-gp-j_id_id16pc8-page_0-AttachedFilesBlock-comment"]',
        'manual'
    ),
    # # click attach
    "docs_attach" : Location(
        By.XPATH,
         '//*[@id="editTemplateMultipart-editForm-content-ftf-gp-j_id_id16pc8-page_0-AttachedFilesBlock-attachFileCommand"]',
        'click'
    ),

    # # click if file is relevant
    # "" : Location(
    #     By.XPATH,
    #      '//*[@id="editTemplateMultipart-editForm-content-ftf-gp-j_id_id16pc8-page_0-AttachedFilesBlock-j_id_id34pc9:0:selectionid"]'
    # ),
    # # click if file is resume
    # "" : Location(
    #     By.XPATH,
    #      '//*[@id="editTemplateMultipart-editForm-content-ftf-gp-j_id_id16pc8-page_0-AttachedFilesBlock-j_id_id34pc9:0:resumeselectionid"]'
    # ),
    # # click to delete file
    # "" : Location(
    #     By.XPATH,
    #      '//*[@id="editTemplateMultipart-editForm-content-ftf-gp-j_id_id16pc8-page_0-AttachedFilesBlock-j_id_id34pc9-0-attachmentFileDelete"]'
    # ),
    # # click sure you want to delete yes
    # "" : Location(
    #     By.XPATH,
    #      '//*[@id="editTemplateMultipart-editForm-content-ftf-gp-j_id_id16pc8-page_0-AttachedFilesBlock-j_id_id4pc9-YesDeleteAttachedFileCommand"]'
    # ),
    # # click to continue to pg 5
    "docs_continue" : Location(
        By.XPATH,
         '//*[@id="editTemplateMultipart-editForm-content-ftf-saveContinueCmdBottom"]',
        'click'
    ),
    # # click yes legally employable
    "q_legal" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-preq-j_id_id7pc10-page__1-q-j_id_id2pc11-0-qr_com.taleo.functionalcomponent.prescreening.entity.question.PossibleAnswer__95901"]',
        'click'
    ),
    # # click > 16
    "q_16" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-preq-j_id_id7pc10-page__1-q-j_id_id2pc11-1-qr_com.taleo.functionalcomponent.prescreening.entity.question.PossibleAnswer__138977"]',
        'click'
    ),
    # # click yes dress code
    "q_dress" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-preq-j_id_id7pc10-page__1-q-j_id_id2pc11-2-qr_com.taleo.functionalcomponent.prescreening.entity.question.PossibleAnswer__139014"]',
        'click'
    ),
    # # click yes able to do job
    "q_able" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-preq-j_id_id7pc10-page__1-q-j_id_id2pc11-3-qr_com.taleo.functionalcomponent.prescreening.entity.question.PossibleAnswer__146937"]',
        'click'
    ),
    # # click to continue to pg 6
    "q_continue" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]',
        'click'
    ),
    # # click yes a veteran
    # "" : Location(
    #     By.XPATH,
    #      '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-koq-j_id_id7pc10-page__1-q-j_id_id2pc11-0-qr_com.taleo.functionalcomponent.prescreening.entity.question.PossibleAnswer__140694"]'
    # ),
    # # click not a veteran
    "vet_no" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-koq-j_id_id7pc10-page__1-q-j_id_id2pc11-0-qr_com.taleo.functionalcomponent.prescreening.entity.question.PossibleAnswer__140695"]',
        'click'
    ),
    # # click no answer veteran
    # "" : Location(
    #     By.XPATH,
    #      '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-koq-j_id_id7pc10-page__1-q-j_id_id2pc11-0-qr_com.taleo.functionalcomponent.prescreening.entity.question.PossibleAnswer__140696"]'
    # ),
    # # click spouse is vet
    # "" : Location(
    #     By.XPATH,
    #      '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-koq-j_id_id7pc10-page__1-q-j_id_id2pc11-1-qr_com.taleo.functionalcomponent.prescreening.entity.question.PossibleAnswer__140677"]'
    # ),
    # # click spouse not vet
    "vet_no_spouse" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-koq-j_id_id7pc10-page__1-q-j_id_id2pc11-1-qr_com.taleo.functionalcomponent.prescreening.entity.question.PossibleAnswer__140678"]',
        'click'
    ),
    # # click no answer spouse vet
    "vet_no_answer_spouse" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-koq-j_id_id7pc10-page__1-q-j_id_id2pc11-1-qr_com.taleo.functionalcomponent.prescreening.entity.question.PossibleAnswer__140679"]',
        'click'
    ),
    # # click to continue to pg 7
    "vet_continue" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]',
        'click'
    ),
    'eeo_no_protected' : Location(
        By.XPATH,
        '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-0-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__27260130812"]',
        'click'
    ),
    'eeo_female': Location(
        By.XPATH,
        '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-1-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__22260130812"]',
        'click'
    ),
    'eeo_male':  Location(
        By.XPATH,
        '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-1-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__22360130812"]',
        'click'
    ),
    'eeo_nogender':  Location(
        By.XPATH,
        '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-1-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__22460130812"]',
        'click'
    ),

    # # click latino yes
    "eeo_latino" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-2-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__24260130812"]',
        'click'
    ),
    # # click latino no
    "eeo_nolatino" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-2-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__24360130812"]',
        'click'
    ),
    # # click latino won’t provide
    "eeo_noinfolatino" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-2-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__24460130812"]',
        'click'
    ),
    # # race this bubble is labeled “Please select”
    # "" : Location(
    #     By.XPATH,
    #      '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-3-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__26160130812"]'
    # ),
    # # click race latino
    "eeo_race_latino" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-3-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__26260130812"]',
        'click'
    ),
    # # click race American Indian
    # "" : Location(
    #     By.XPATH,
    #      '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-3-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__26360130812"]'
    # ),
    # # click race Asian
    # "" : Location(
    #     By.XPATH,
    #      '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-3-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__26460130812"]'
    # ),
    # # click race Black
    # "" : Location(
    #     By.XPATH,
    #      '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-3-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__26660130812"]'
    # ),
    # # click race Native Hawaiian
    # "" : Location(
    #     By.XPATH,
    #      '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-3-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__26560130812"]'
    # ),
    # # click race White
    "eeo_race_white" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-3-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__26760130812"]',
        'click'

    ),
    # # click race two or more
    # "" : Location(
    #     By.XPATH,
    #      '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-3-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__26860130812"]'
    # ),
    # # click race won’t provide
    # "" : Location(
    #     By.XPATH,
    #      '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-diversityBlock-j_id_id11pc10-0-j_id_id14pc10-3-questionRadio_com.taleo.systemcomponent.question.entity.RegulationPossibleAnswer__26960130812"]'
    # ),
    # # click continue to pg 8
    "eeo_continue" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]',
        'click'
    ),
    # # fill name self ID
    "dis_name" : Location(
        By.XPATH,
         '//*[@id="10046"]',
        'send_keys',
        '{name}'
    ),
    # # fill today’s date
    "dis_date" : Location(
        By.XPATH,
         '//*[@id="10047"]',
        'send_keys',
        ''
    ),
    # # click have disability
    # "" : Location(
    #     By.XPATH,
    #      '//*[@id="10048-shadow"]'
    # ),
    # # click no disability
    "dis_no" : Location(
        By.XPATH,
         '//*[@id="10049-shadow"]',
        'click'
    ),
    # # click don’t answer
    "dis_no_answer" : Location(
        By.XPATH,
         '//*[@id="10050-shadow"]',
        'click'
    ),
    # # click continue to pg 9
    "dis_continue" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]',
        'click'
    ),
    # # click complete questionnaire in new window
    "tax_open" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-extServBlock-outputText_takeNowInlineLink"]',
        'click'
    ),
    # # click yes live with SNAP
    # "" : Location(
    #     By.XPATH,
    #      '/html/body/form/div[4]/span/div[1]/div/div[1]/div/div/label[1]'
    # ),
    # # click no live with SNAP
    "tax_nosnap" : Location(
        By.XPATH,
         '/html/body/form/div[4]/span/div[1]/div/div[1]/div/div/label[2]',
        'click'
    ),

    # # click no live with TANF
    "tax_notanf" : Location(
        By.XPATH,
         '/html/body/form/div[4]/span/div[1]/div/div[2]/div/div/label[2]',
        'click'
    ),

    # # click no vet
    "tax_novet" : Location(
        By.XPATH,
         '/html/body/form/div[4]/span/div[1]/div/div[3]/div/div/label[2]',
        'click'
    ),
    # # click no disabled
    "tax_nodisable" : Location(
        By.XPATH,
         '/html/body/form/div[4]/span/div[1]/div/div[4]/div/div/label[2]',
        'click'
    ),

    # # click no collecting unemployment
    "tax_nounemploy" : Location(
        By.XPATH,
         '/html/body/form/div[4]/span/div[1]/div/div[5]/div/div/label[2]',
        'click'
    ),
    # # click rec’d unemployment
    "tax_noapply" : Location(
        By.XPATH,
         '/html/body/form/div[4]/span/div[1]/div/div[6]/div/div/label[2]',
        'click'
    ),
    # # click not rec’d unemployment

    # # click no NA tribe
    "tax_nonnative" : Location(
        By.XPATH,
         '/html/body/form/div[4]/span/div[1]/div/div[7]/div/div/label[2]',
        'click'
    ),
    # # click next page
    "tax_next" : Location(
        By.XPATH,
         '//*[@id="SurveyControl_SurveySubmit"]',
        'click'
    ),
    'tax_submit': Location(
        By.XPATH,
        '//*[@id="SurveyControl_SurveySubmit"]',
        'click'
    ),
    #
    # # //directs to page about military service if veteran yes was selected
    #
    # # // missed an xpath copy to submit that whole questionnaire
    # # click to continue to pg 11
    # "" : Location(
    #     By.XPATH,
    #      '//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]'
    # ),
    # # dropdown to confirm language
    # "" : Location(
    #     By.XPATH,
    #      '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-eSignatureBlock-selectOneMenu_language"]'
    # ),
    # # fill full name
    "conf_name" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-gp-j_id_id16pc9-page_0-eSignatureBlock-cfrmsub-frm-dv_cs_esignature_FullName"]',
        'send_keys',
        '{name}'
    ),
    # # click continue to pg 12
    "conf_continue" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-saveContinueCmdBottom"]',
        'click'
    ),
    # # click submit final
    "submit_app" : Location(
        By.XPATH,
         '//*[@id="et-ef-content-ftf-submitCmdBottom"]',
        'click'
    ),
    'completed': Location(
        By.XPATH,
        '//*[@id="et-ef-content-flowTemplate-gp-j_id_id16pc9-page_0-thankYouBlock-tyTitle"]',
        'manual'
    )
    }
)