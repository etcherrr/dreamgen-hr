{
    "name": "BOSNET Employee Database",
    "author": "Mohamad Fhatir",
    "website": "https://bosnetdis.com",
    "version": "1.0.0",
    "depends": [
        "hr",
        "hr_recruitment",
        "website_hr_recruitment",
        "mail",
    ],
    "data": [
        "data/cron.xml",
        "data/mail.xml",
        "views/res_config_settings_views.xml",
        "views/recruitment_form.xml",
        "views/employee_form.xml",
        "views/form_website.xml",
    ],
    "license": "LGPL-3",
    "installable": True,
    'auto_install': False,
    'application': True
}