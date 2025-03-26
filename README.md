# Tobias - Tavion's Original But Intelligent Artificial System

Tobias is a simple AI assistant built in Python that processes requests through the terminal and responds vocally. It is designed to handle various predefined "skills" that provide information such as time, date, weather, and more.

## Skills

Tobias can respond to the following requests:

- Current Time: Announces the current time.
- Current Date: Provides the current date.
- Version Information: States its current version.
- Name Inquiry: States its name.
- Creator Information: Mentions its creator's name.
- Birthday: Reveals its birthday.
- Age Inquiry: Tells how old it is.
- Weather Information: Reports the weather for a specified location.
  - If no location is specified in the query, Tobias uses the location in config.txt.
    - If config.txt does not contain a location, the default is Washington, DC.
- Joke Telling: Tells a random joke.

## Usage

Run Tobias using the following command:

`python3 main.py`

Then, enter a command in the terminal to interact with Tobias.

## How to Ask a Question

To interact with Tobias, ensure that every query includes the word "Tobias", similar to a wake word like Siri or Alexa. For example:

"Tobias, what’s the weather like today?"

"Tobias, tell me a joke."

"Tobias, what time is it?"

## Skill Query Dictionary

To trigger each skill, include the corresponding keyword(s) in your query:

- Current Time: Include "time" (e.g., "Tobias, what time is it?").

- Current Date: Include "date" (e.g., "Tobias, what’s today’s date?").

- Version Information: Include "version" (e.g., "Tobias, what’s your version?").

- Name Inquiry: Include "your name" (e.g., "Tobias, what’s your name?").

- Creator Information: Include "creator" (e.g., "Tobias, who created you?").

- Birthday: Include "birthday" (e.g., "Tobias, when is your birthday?").

- Age Inquiry: Include "age" (e.g., "Tobias, how old are you?").

- Weather Information for Config.txt/Default Location: Include "weather" (e.g., "Tobias, what’s the weather like today?").

- Weather Information for a Specific Location: Include "weather" and "in" followed by the location (e.g., "Tobias, what’s the weather in Los Angeles?").

- Joke Telling: Include "joke" (e.g., "Tobias, tell me a joke.").

## Acknowledgements

Tobias uses the following APIs:

- [OpenWeatherMap](https://openweathermap.org/api): Provides real-time weather information for the weather-related skills.
- [Official Joke API](https://github.com/15Dkatz/official_joke_api): Fetches random jokes for the joke-telling skill.

## Future Improvements

- Implement a GUI or web-based interface.

- Expand skillset to include reminders, news updates, and more.
