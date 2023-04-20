BOT_API_TOKEN = '5844664384:AAHvTFd9p8lCkOWT8kLZ5QAdxux_MUsnFyQ'
WEATHER_API_KEY = '71ce3060658c5a31015846dee04b01f9'

CURRENT_WEATHER_API_CALL = (
        'https://api.openweathermap.org/data/2.5/weather?'
        'lat={latitude}&lon={longitude}&'
        'appid=' + WEATHER_API_KEY + '&units=metric'
)
