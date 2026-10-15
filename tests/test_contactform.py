
from playwright.sync_api import expect
from pages.contact_page import ContactPage


def test_contactform(page):

    # Create the contact page object
    contact_page = ContactPage(page)

    # Open the portfolio website
    contact_page.open()

    # Verify the page title
    expect(page).to_have_title(contact_page.page_title)

    # Fill in the contact form
    contact_page.fill_contact_form()

    # Submit the form
    contact_page.submit_form()

    # Verify the success message
    expect(contact_page.success_message).to_be_visible()


def test_empty_contactform(page):
    # Create the contact page object
    contact_page = ContactPage(page)

    # Open the portfolio website
    contact_page.open()
  
    # Submit the empty form
    contact_page.submit_empty_form()

    # Verify that the validation messages are displayed for required fields
    expect(contact_page.name_error).to_have_text("Full name is required.")
    expect(contact_page.email_error).to_have_text("Email address is required.")
    expect(contact_page.message_error).to_have_text("Message is required.")
    expect(contact_page.success_message).not_to_be_visible()


def test_invalid_name_contactform(page):
    # Create the contact page object
    contact_page = ContactPage(page)

    # Open the portfolio website
    contact_page.open()

    # Fill all fields correctly except for a name below the minimum length
    contact_page.fill_contact_form(full_name="A")

    # Verify the application error and that submission was prevented
    contact_page.submit_form()
    expect(contact_page.name_length_error).to_have_text("Name must be at least 2 characters.")
    expect(contact_page.success_message).not_to_be_visible()


def test_invalid_email_contactform(page):
    # Create the contact page object
    contact_page = ContactPage(page)

    # Open the portfolio website
    contact_page.open()

    # Fill all fields correctly except for the email format
    contact_page.fill_contact_form(email="arpit123")

    # Verify the application error and that submission was prevented
    contact_page.submit_form()
    expect(contact_page.email_format_error).to_have_text("Enter a valid email address.")
    expect(contact_page.success_message).not_to_be_visible()


def test_empty_message_contactform(page):
    # Create the contact page object
    contact_page = ContactPage(page)

    # Open the portfolio website
    contact_page.open()

    # Fill the other fields correctly and leave the message empty
    contact_page.fill_contact_form(message="")

    # Verify the application error and that submission was prevented
    contact_page.submit_form()
    expect(contact_page.message_error).to_have_text("Message is required.")
    expect(contact_page.success_message).not_to_be_visible()