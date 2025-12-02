import data
import helpers


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        # Check if the Urban Routes server is reachable
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        # Add in S8
        print("Function created: set_route")
        pass

    def test_select_plan(self):
        # Add in S8
        print("Function created: select_plan")
        pass

    def test_fill_phone_number(self):
        # Add in S8
        print("Function created: fill_phone_number")
        pass

    def test_fill_card(self):
        # Add in S8
        print("Function created: fill_card")
        pass

    def test_comment_for_driver(self):
        # Add in S8
        print("Function created: comment_for_driver")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        print("Function created: order_blanket_and_handkerchiefs")
        pass

    def test_order_2_ice_creams(self):
        """
        Tests ordering two ice creams in the Urban Routes app.
        Implementation will be added in Sprint 8.
        """

        number_of_ice_creams = 2

        for _ in range(number_of_ice_creams):
            # Add in S8
            pass

        print("Function created: order_2_ice_creams")

    def test_car_search_model_appears(self):
        # Add in S8
        print("Function created: car_search_model_appears")
        pass
