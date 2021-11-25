{
    'name': "Ks Project Scrum",

    'summary': '',
    'description': """
        Ksolves,
        Ksolves India Private Limited,
        Ksolves India Pvt. Ltd.
        Ksolves India Private Limited odoo apps,
        Ksolves India Pvt. Ltd. odoo apps,
        Ksolves odoo apps,
        Ksolves apps,
        Ksolves odoo,
        Ksolves odoo themes,
        Ksolves themes,
        Ksolves odoo app, 
        odoo apps,
    """,

    'author': "Ksolves India Ltd.",
    'website': "https://www.ksolves.com",
    'license': 'OPL-1',
    'currency': '',
    'price': '',
    'version': '14.0.1.0.0',
    'support': 'sales@ksolves.com',
    'depends': ['website_helpdesk_support_ticket', 'project_scrum_portal', 'hr_holidays', 'project'],
    'data': [
        'security/ir.model.access.csv',
        'static/ir.model.access.csv',
        'views/assets.xml',
        'views/ks_project_scrum_release_view.xml',
        'views/ks_project_scrum_view.xml',
        'views/ks_helpdesk_support.xml',
        'views/ks_scrum_portal.xml',
        'views/project_scrum_role_view.xml',
        'views/project_scrum_devteam_view.xml',
        'views/hr_employee_view.xml',
        'views/project_scrum_release_view.xml',
        'views/ks_project_type.xml',
        'data/ks_project_type_data.xml',
        'views/project_project_view.xml',
        'views/ks_project_sprint_checklist.xml',
        'views/project_task_view.xml',
        'views/email/build_ready_reminder_email.xml',
        'views/email/sprint_delivery_reminder_email_template.xml',
        'views/email/sprint_uat_email.xml',
        'views/email/client_delivery_reminder_email_template.xml',
        'views/ir_cron.xml',
    ],
    "application": True,
    "installable": True,
}
