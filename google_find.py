from selene.support.shared import browser
from selene import be, have


def test_positive(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Селена - Википедия'))


def test_negative(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.no.text('Fail - Википедия'))
