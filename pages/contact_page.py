
from playwright.sync_api import Page


class ContactPage:

    def __init__(self, page: Page):
        # Store the browser page for this object
        self.page = page

        # Website URL
        self.url = ("https://portfolio-sepia-one-6j5rl6ugp7.vercel.app/")

        # Browser tab / document title
        self.page_title = "Arpit Dhiman | QA Automation Engineer & Quality Assurance Specialist"

        # Contact form locators
        self.full_name = page.get_by_role("textbox", name="Full name")
        self.email = page.get_by_role("textbox", name="Email Address")
        self.country_code = page.get_by_role("combobox", name="Country code")
        self.phone_number = page.get_by_role("textbox", name="Phone number")
        self.message = page.get_by_role("textbox", name="Write your message")
        self.send_button = page.get_by_role("button", name="Send Message")
        self.success_message = page.get_by_text("Thanks! Your message was sent successfully.")

        # Validation message locators
        self.name_error = page.get_by_role("alert").filter(has_text="Full name is required.")
        self.name_length_error = page.get_by_role("alert").filter(
            has_text="Name must be at least 2 characters."
        )
        self.email_error = page.get_by_role("alert").filter(has_text="Email address is required.")
        self.email_format_error = page.get_by_role("alert").filter(
            has_text="Enter a valid email address."
        )
        self.message_error = page.get_by_role("alert").filter(has_text="Message is required.")

    def open(self):
        # Open the portfolio website
        self.page.goto(self.url)

    # Test 1: Valid Data Submission
    def fill_contact_form(
        self,
        full_name="Automation Testing",
        email="testuser2506@gmail.com",
        message="Automation Testing",
    ):
        # Enter contact form details
        self.full_name.fill(full_name)
        self.email.fill(email)
        self.country_code.select_option(value="Canada (+1)")
        self.phone_number.fill("8968628515")
        self.message.fill(message)

    def submit_form(self):
        # Click the Send Message button
        self.send_button.click()
    

    # Test 2: Empty Form Submission
    def submit_empty_form(self):
        self.send_button.click()
    