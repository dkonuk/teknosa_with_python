import pytest
from pages.HomePage import HomePage
import time


class TestHomePage():


    def test_home_page_title(self, fixtureSetup):
        driver = fixtureSetup
        home_page = HomePage(driver)
        time.sleep(5)
        print(home_page.get_page_title())
        assert "Teknosa" in home_page.get_page_title(), f"Expected 'Teknosa' in title, but got: {home_page.get_page_title()}"
        home_page.check_promotions_banner_text()
