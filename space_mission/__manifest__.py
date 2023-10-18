{
    "name": "Odoo Space Mission",
    "summary": "App for logistic and management of Spaceships and crews",
    "description": "App for logistic and management of Spaceships and crews",
    "license": "OPL-1",
    "author": "Odoo Inc.",
    "website": "www.odoo.com",
    "data": [
        "security/space_mission_groups.xml",
        "security/ir.model.access.csv",
        "views/spaceship_views.xml",
        "views/mission_views.xml",
        "views/project_views.xml",
        "wizard/project_task_wizard_view.xml",
        "views/space_mission_menuitems.xml",
    ],
    "demo": [
        "demo/spaceship_demo.xml",
        "demo/mission_demo.xml",
    ],
    "depends": ["project"],
    "application": True,
}
