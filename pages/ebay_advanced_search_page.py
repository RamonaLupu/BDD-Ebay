import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import BasePage


class AdvancedSearchPage(BasePage):
    ADVANCED_SEARCH_LINK = (By.ID, 'gh-as-td')
    ENTER_KEYWORDS_OR_ITEM_NUMBER = (By.ID, '_nkw')
    KEYWORD_OPTIONS = (By.XPATH, '//*[@id="s0-1-17-4[0]-7[1]-_in_kw"]')
    EXCLUDE_WORDS_FROM_SEARCH = (By.ID,'_ex_kw')
    SEARCH_CATEGORIES = (By.XPATH,'//*[@id="s0-1-17-4[0]-7[3]-_sacat"]')
    SEARCH_BUTTON = (By.XPATH, '/html/body/div[3]/div/main/form/fieldset[1]/div[5]/button')

    def click_on_the_advance_link(self):
        self.chrom.find_element(*self.ADVANCED_SEARCH_LINK).click()


    def enter_keywords_or_item_number(self):
        self.chrom.find_element(*self.ENTER_KEYWORDS_OR_ITEM_NUMBER).send_keys('pampers')

    def select_keyword_options(self):
        category_options = Select(self.chrom.find_element(*self.KEYWORD_OPTIONS))
        category_options.select_by_visible_text('Exact words, exact order')

    def select_search_category(self):
        category_search = Select(self.chrom.find_element(*self.SEARCH_CATEGORIES))
        category_search.select_by_visible_text('Baby')

    def exclude_words_from_search(self):
        pass
        # TO BE IMPLEMENTED

    def click_search_button(self):
        self.chrom.find_element(*self.SEARCH_BUTTON).click()
