from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
import selenium.webdriver as webdriver
from time import sleep
import webbrowser
import pyttsx3

class ActionStoreURLs(Action):
    def name(self) -> Text:
        return "action_store_urls"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Define URLs directly within the action
        urls = [
            "https://bhuvan.nrsc.gov.in",
            "https://bhuvan-app3.nrsc.gov.in/aadhaar/",
            "https://bhuvan-app2.nrsc.gov.in/mgnrega/mgnrega_phase2.php",
            "https://bhuvan-app3.nrsc.gov.in/data/",
            "https://bhuvan-app1.nrsc.gov.in/bhuvan2d/bhuvan/bhuvan2d.php",
            "https://bhuvan.nrsc.gov.in/home/index.php",
            "https://bhuvan-app1.nrsc.gov.in/api/",
            "https://bhuvan-app1.nrsc.gov.in/hfa/housing_for_all.php",
            "https://bhuvan-app1.nrsc.gov.in/apshcl",
            "https://bhuvan-app1.nrsc.gov.in/ntr",
            "https://bhuvan.nrsc.gov.in/forum",
            "https://bhuvan-wbis.nrsc.gov.in/",
            "https://bhuvan.nrsc.gov.in/geonetwork/",
            "https://bhuvan-app2.nrsc.gov.in/planner/",
            "https://bhuvan-app1.nrsc.gov.in/globe/3d.php",
            "https://bhuvan-app1.nrsc.gov.in/mhrd_rusa/",
            "https://bhuvan-app1.nrsc.gov.in/geographicalindication/index.php",
            "https://bhuvan-app1.nrsc.gov.in/flycatchers/flycatchers.php",
            "https://bhuvan-app1.nrsc.gov.in/mhrd_ncert",
            "https://bhuvan-app1.nrsc.gov.in/nabard",
            "https://bhuvan-app1.nrsc.gov.in/iwmp",
            "https://bhuvan-app1.nrsc.gov.in/tourism/tourism.php",
            "https://bhuvan-app1.nrsc.gov.in/hp_forest",
            "https://bhuvan-app1.nrsc.gov.in/disaster/disaster.php",
            "https://bhuvan-app1.nrsc.gov.in/thematic/thematic/index.php",
            "https://bhuvan-app1.nrsc.gov.in/imd/",
            "https://bhuvan-app1.nrsc.gov.in/pdmc/",
            "https://bhuvan-app1.nrsc.gov.in/heatwave/",
            "https://bhuvan-app1.nrsc.gov.in/mowr_ganga/",
            "https://bhuvan-app1.nrsc.gov.in/ts_forest/",
            "https://bhuvan-app1.nrsc.gov.in/pb_forest/",
            "https://bhuvan-app1.nrsc.gov.in/narl/",
            "https://bhuvan-app1.nrsc.gov.in/ka_forest",
            "https://bhuvan-app1.nrsc.gov.in/state/HR",
            "https://bhuvan-app1.nrsc.gov.in/saraswati/",
            "https://bhuvan-app1.nrsc.gov.in/web_view/index.php",
            "https://bhuvan-app1.nrsc.gov.in/pmjvk",
            "https://bhuvan-app1.nrsc.gov.in/anganwadi/",
            "https://bhuvan-app2.nrsc.gov.in/mgnregatpv/",
            "https://bhuvan-app3.nrsc.gov.in/corona/",
            "https://bhuvan-app1.nrsc.gov.in/moef_cris",
            "https://bhuvan-app1.nrsc.gov.in/2dresources/bhuvanstore.php",
            "https://bhuvan-app1.nrsc.gov.in/rbi",
            "https://bhuvan-app1.nrsc.gov.in/sitemap",
            "https://bhuvan-app1.nrsc.gov.in/mhrd_ncert/sb/sb.php",
            "https://bhuvan-app1.nrsc.gov.in/tourism/tourism.php?tourismid=1",
            "https://bhuvan-app1.nrsc.gov.in/tr_forest/",
            "https://bhuvan-app1.nrsc.gov.in/municipal/municipal.php",
            "https://bhuvan-app1.nrsc.gov.in/toll/morth_nhai.php",
            "https://bhuvan-app1.nrsc.gov.in/walamtari/walamtari.php",
            "https://bhuvan-app1.nrsc.gov.in/mines/mines.php",
            "https://bhuvan-app1.nrsc.gov.in/agriculture/agri.php",
            "https://bhuvan-app1.nrsc.gov.in/deltas/index.php",
            "https://bhuvan-app1.nrsc.gov.in/cdma/index.php",
            "https://bhuvan-app1.nrsc.gov.in/state/AP",
            "https://bhuvan-mapper1.nrsc.gov.in/twris",
            "https://bhuvan-app1.nrsc.gov.in/multilingual",
            "https://bhuvan-app1.nrsc.gov.in/disaster/disaster.php?id=fire",
            "https://bhuvan-app1.nrsc.gov.in/shipping",
            "https://bhuvan-app1.nrsc.gov.in/rkvy/index.php",
            "https://bhuvan-app1.nrsc.gov.in/aibp/aibp.php",
            "https://bhuvan-app1.nrsc.gov.in/mwrds/index.php",
            "https://bhuvan-app1.nrsc.gov.in/pmgsy/home/index.php",
            "https://bhuvan-app1.nrsc.gov.in/collaboration/"
        ]

        current_urls = tracker.get_slot('urls')

        if urls:
            current_urls.extend(urls)
            dispatcher.utter_message(f"Stored {len(urls)} URLs.")
        else:
            dispatcher.utter_message("No URLs provided.")

        return [SlotSet("urls", current_urls)]

class ActionProvideInfo(Action):
    def name(self) -> Text:
        return "action_provide_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        recognized_intent = tracker.latest_message['intent'].get('name')

        if recognized_intent == 'provide_url_bhuvan':
            dispatcher.utter_message("Sure! Bhuvan is a geoportal that provides satellite imagery and geospatial data of India. "
                                     "You can explore it further at [Bhuvan Portal](https://bhuvan.nrsc.gov.in).")
            webbrowser.open("https://bhuvan.nrsc.gov.in")
        elif recognized_intent == 'provide_url_housing':
            dispatcher.utter_message("This URL leads to information about housing for all. For more details, please visit "
                                     "[Housing for All](https://bhuvan-app1.nrsc.gov.in/hfa/housing_for_all.php).")
        elif recognized_intent == 'provide_url_forum':
            dispatcher.utter_message("The provided URL leads to the Bhuvan Forum. You can participate in discussions and "
                                     "get more information at [Bhuvan Forum](https://bhuvan.nrsc.gov.in/forum).")
        elif recognized_intent == 'provide_url_aadhaar':
            dispatcher.utter_message("The provided URL might be related to Aadhaar, the unique identification system in India. "
                                     "For more details, you can visit [Aadhaar](https://bhuvan-app3.nrsc.gov.in/aadhaar/).")
        elif recognized_intent == 'provide_url_apshcl':
            dispatcher.utter_message("The provided URL leads to Bhuvan data. You can explore more at [Bhuvan Data](https://bhuvan-app3.nrsc.gov.in/data/).")
        elif recognized_intent == 'provide_url_ntr':
            dispatcher.utter_message("The provided URL leads to Bhuvan data. You can explore more at [Bhuvan Data](https://bhuvan-app3.nrsc.gov.in/data/).")
        elif recognized_intent == 'provide_url_forum':
            dispatcher.utter_message("The provided URL leads to Bhuvan data. You can explore more at [Bhuvan Data](https://bhuvan-app3.nrsc.gov.in/data/).")    
        elif recognized_intent == 'provide_url_geonetwork':
            dispatcher.utter_message("The provided URL leads to Bhuvan data. You can explore more at [Bhuvan Data](https://bhuvan-app3.nrsc.gov.in/data/).")
        elif recognized_intent == 'provide_url_planner':
            dispatcher.utter_message("The provided URL leads to Bhuvan data. You can explore more at [Bhuvan Data](https://bhuvan-app3.nrsc.gov.in/data/).")
        elif recognized_intent == 'provide_url_globe':
            dispatcher.utter_message("The provided URL leads to Bhuvan data. You can explore more at [Bhuvan Data](https://bhuvan-app3.nrsc.gov.in/data/).")
        elif recognized_intent == 'provide_url_mhrd_rusa':
            dispatcher.utter_message("The provided URL leads to Bhuvan data. You can explore more at [Bhuvan Data](https://bhuvan-app3.nrsc.gov.in/data/).")
        elif recognized_intent == 'provide_url_geographicalindication':
            dispatcher.utter_message("The provided URL leads to Bhuvan data. You can explore more at [Bhuvan Data](https://bhuvan-app3.nrsc.gov.in/data/).")
        elif recognized_intent == ' provide_url_flycatchers':
            dispatcher.utter_message("The provided URL leads to Bhuvan data. You can explore more at [Bhuvan Data](https://bhuvan-app3.nrsc.gov.in/data/).")
        elif recognized_intent == ' provide_url_mhrd_ncert':
            dispatcher.utter_message("The provided URL leads to Bhuvan data. You can explore more at [Bhuvan Data](https://bhuvan-app3.nrsc.gov.in/data/).")
        elif recognized_intent == 'provide_url_nabard':
            dispatcher.utter_message("The provided URL leads to Bhuvan data. You can explore more at [Bhuvan Data](https://bhuvan-app3.nrsc.gov.in/data/).")
        elif recognized_intent == 'provide_url_iwmp':
            dispatcher.utter_message("The provided URL leads to Bhuvan data. You can explore more at [Bhuvan Data](https://bhuvan-app3.nrsc.gov.in/data/).")
                                                                                                                                                                               
        return []

# class ActionSpeak(Action):
#     def name(self) -> Text:
#         return "action_speak"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain) -> list:
#         # Access conversation history
#         conversation_history = tracker.events

#         # Initialize the TTS engine
#         engine = pyttsx3.init()

#         # Iterate over the events in conversation history
#         for event in conversation_history:
#             if 'text' in event:
#                 # Access the text of the user's message
#                 user_message = event['text']
#                 dispatcher.utter_message(f"User said: {user_message}")

#                 # Use pyttsx3 to speak the user's message
#                 engine.say(user_message)
#                 engine.runAndWait()

#         # Your custom logic here...

#         return []

class ActionPerformWebAutomation(Action):
    def name(self) -> Text:
        return "action_perform_web_automation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/120.0.0.0'
        driver_path = r"C:\Users\offic\OneDrive\Desktop\msedgedriver.exe"
        edge_service = EdgeService(driver_path)
        edge_options = EdgeOptions()

        # If you don't want to showcase the automation on the webpage
        edge_options.add_argument('--headless')

        edge_options.add_argument(f'user-agent={user_agent}')

        url = "https://bhuvan-app3.nrsc.gov.in/aadhaar/"

        # Create an Edge WebDriver instance with specified options
        browser = webdriver.Edge(service=edge_service, options=edge_options)

        try:
            search_query = 'Chandigarh'
            # Open the URL in the browser
            browser.get(url)

            # Wait for the search field to be present
            search_field = WebDriverWait(browser, 20).until(
                EC.element_to_be_clickable((By.ID, "Val"))
            )

            # Clear the search field (optional, depending on your use case)
            search_field.clear()

            # Enter the search query into the search field
            search_field.send_keys(search_query)

            # Wait for the table to update (you may adjust the wait time)
            sleep(2)

            # Assuming the table has an ID, locate the table element
            table_element = WebDriverWait(browser, 20).until(
                EC.presence_of_element_located((By.ID, "ga"))
            )

            # Extract information from the table (adjust based on your table structure)
            rows = table_element.find_elements(By.TAG_NAME, "tr")

            # Extract row data and respond back to the user
            table_data = []
            for i, row in enumerate(rows, start=1):
                columns = row.find_elements(By.TAG_NAME, "td")
                row_data = [column.text for column in columns]
                formatted_row = f"{i}. {', '.join(row_data)}"
                table_data.append(formatted_row)

            # Send the formatted list as a response to the user
            dispatcher.utter_message(text="\n".join(table_data))



        finally:
            browser.quit()

        return []
    
    
    