from odoo import http
from odoo.http import request


class Mission(http.Controller):
    @http.route("/missions/current", auth="public", website=True)
    def index(self, **kw):
        missions = request.env["space_mission.mission"].search(
            [["state", "in", ["scheduled", "in_progress", "done"]]],
            order="launch_date asc",
        )
        return http.request.render(
            "space_mission.current_missions", {"missions": missions}
        )
