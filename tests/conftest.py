import  pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options as OptionsEdge


@pytest.fixture()
def fixtureSetup():
    driver = None
    options = Options()
    options_edge = OptionsEdge()
    #options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--dns-prefetch-disable')
    options.add_argument("--disable-gpu")
    options.add_argument("--enable-cdp-events")
    #driver = webdriver.Edge(options=options)
    driver = webdriver.Chrome(options=options)
    return driver
