"""
This file is the framework for generating multiple Streamlit applications 
through an object oriented framework. 
"""

# Import necessary libraries 
import streamlit as st


class Page:

    def __init__(self, title, icon, func):

        self.title = title

        if icon is None:
            icon = '📄'

        self.icon = icon
        self.run = func

# Define the multipage class to manage the multiple apps in our program 
class MultiPage: 
    """Framework for combining multiple streamlit applications."""

    def __init__(self) -> None:
        """Constructor class to generate a list which will store all our applications as an instance variable."""
        self.pages = {}
        self.page_order = []
        self.current_page = None
    
    def add_page(self, name, title, icon, func) -> None: 
        """Class Method to Add pages to the project
        Args:
            title ([str]): The title of page which we are adding to the list of apps 
            
            func: Python function to render this page in Streamlit
        """

        if name not in self.pages:
            self.pages[name] = Page(title, icon, func)
            self.page_order.append(name)

            if self.current_page == None:
                self.current_page = 0

        else:
            raise KeyError('A page with this name already exists')

    def run(self):

        # Sidebar config
        st.sidebar.title('Pages')

        # Buttons for all the pages
        buttons = []

        for i in self.page_order:
            page = self.pages[i]
            page_type = 'secondary'

            if i == self.page_order[self.current_page]:
                page_type = 'primary'

            button = st.sidebar.button(f'{page.icon} {page.title}', type=page_type, use_container_width=True)
            buttons.append(button)

        # More sidebar
        st.sidebar.divider()
        st.session_state.authenticator.logout('Logout', 'sidebar')

        for i in range(len(buttons)):
            if buttons[i] == True:

                # Button corresponding to page i in order triggered
                self.current_page = i

                # Rerun to load new page
                st.experimental_rerun()

        # Run the current page
        self.pages[self.page_order[self.current_page]].run()


