class BrowserStacks:
    def __init__(self):
        self.backstack = []  # Stack for backward navigation history
        self.forwardstack = []  # Stack for forward navigation history
        self.current_url = None  # Current URL

    def navigate_to(self, url):
        if self.current_url:
            self.backstack.append(self.current_url)
            self.forwardstack = []  # Clear the forward stack when navigating to a new URL
        self.current_url = url

    def go_back(self):
        if not self.backstack:
            print("Can't go BACKWARD. Backward history is EMPTY.")
            return
        self.forwardstack.append(self.current_url)
        self.current_url = self.backstack.pop()

    def go_forward(self):
        if not self.forwardstack:
            print("Can't go FORWARD. Forward history is EMPTY.")
            return
        self.backstack.append(self.current_url)
        self.current_url = self.forwardstack.pop()

    def current_page(self):
        return self.current_url

    def print_history(self):
        print("Backward History:", self.backstack)
        print("Forward History:", self.forwardstack)


# Example usage:
browser = BrowserStacks()

browser.navigate_to("https://www.microsoft.com")
browser.navigate_to("https://www.geeksforgeeks.orgs")
browser.navigate_to("https://www.openai.com")

browser.print_history()  # Print navigation history

print("Current Page:", browser.current_page())  # Print the current page

browser.go_back()
print("Current Page (after going backward):", browser.current_page())

browser.go_forward()
print("Current Page (after going forward):", browser.current_page())

browser.print_history()  # Print updated navigation history
