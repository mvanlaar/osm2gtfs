# coding=utf-8

from creators.routes_creator import RoutesCreator


class RoutesCreatorMedellinmetro(RoutesCreator):

    def add_routes_to_schedule(self, schedule, data):

        # Get routes information
        data.get_routes()
        return

