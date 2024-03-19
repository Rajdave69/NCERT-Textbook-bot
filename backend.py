import configparser
import sys
import discord
import logging
from discord.ext import commands
from colorlog import ColoredFormatter
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
intents = discord.Intents.default()


# Initializing the logger
def colorlogger(name: str = 'my-discord-bot') -> logging.log:
    logger = logging.getLogger(name)
    stream = logging.StreamHandler()

    stream.setFormatter(ColoredFormatter("%(reset)s%(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s"))
    logger.addHandler(stream)
    return logger  # Return the logger


log = colorlogger()

# Loading config.ini
config = configparser.ConfigParser()

try:
    config.read('./data/config.ini')
except Exception as e:
    log.critical("Error reading the config.ini file. Error: " + str(e))
    sys.exit()

# Getting variables from config.ini
try:
    # Getting the variables from `[general]`
    log_level: str = config.get('general', 'log_level')
    presence: str = config.get('general', 'presence')

    # Getting the variables from `[secret]`
    discord_token: str = config.get('secret', 'discord_token')

    # Getting the variables from `[discord]`
    embed_footer: str = config.get('discord', 'embed_footer')
    embed_color: int = int(config.get('discord', 'embed_color'), base=16)
    embed_url: str = config.get('discord', 'embed_url')


except Exception as err:
    log.critical("Error getting variables from the config file. Error: " + str(err))
    sys.exit()

# Set the logger's log level to the one in the config file
if log_level.upper().strip() in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
    log.setLevel(log_level.upper().strip())
else:
    log.setLevel("INFO")
    log.warning(f"Invalid log level `{log_level.upper().strip()}`. Defaulting to INFO.")

# Initializing the client
client = commands.Bot(intents=intents, command_prefix="!")  # Setting prefix

_embed_template = discord.Embed(
    title="Error!",
    color=embed_color,
    url=embed_url
)
_embed_template.set_footer(text=embed_footer)

embed_template = lambda: _embed_template.copy()


def error_template(description: str) -> discord.Embed:
    _error_template = discord.Embed(
        title="Error!",
        description=description,
        color=0xff0000,
        url=embed_url
    )
    _error_template.set_footer(text=embed_footer)

    return _error_template.copy()



driver = webdriver.Firefox()
driver.get("https://ncert.nic.in/textbook.php")


async def get_classes(interaction: discord.Interaction, current) -> list[discord.app_commands.Choice[str]]:
    print(interaction, current)
    # get the current textbox (discord option)'s value
    # current = interaction.data['options'][0]['value'].lower()
    print("1")

    print("2")
    all_classes = selenium.webdriver.remote.webelement.WebElement = driver.find_element(By.NAME, "tclass")
    all_classes = all_classes.text.splitlines()
    all_classes.pop(0)
    print("3")

    print(all_classes)

    e = [discord.app_commands.Choice(name=all_classes[i], value=str(i)) for i in range(all_classes)]
    print(e)
    return list({discord.app_commands.Choice(name=all_classes[i], value=str(i)) for i in range(all_classes)})


async def get_subjects(interaction: discord.Interaction, current) -> list[discord.app_commands.Choice[str]]:
    print(interaction, current)
    # get the current textbox (discord option)'s value
    # current = interaction.data['options'][0]['value'].lower()
    class_index = int(interaction.data['options'][0]['value'].lower())


    driver.execute_script(f'document.test.tclass.selectedIndex = {class_index};')
    driver.execute_script('change();')

    all_subjects = selenium.webdriver.remote.webelement.WebElement = driver.find_element(By.NAME, "tsubject")

    return list({discord.app_commands.Choice(name=all_subjects[i], value=str(i)) for i in range(all_subjects)})


async def get_books(interaction: discord.Interaction, current) -> list[discord.app_commands.Choice[str]]:
    print(interaction, current)
    # get the current textbox (discord option)'s value
    # current = interaction.data['options'][0]['value'].lower()
    subject_index = int(interaction.data['options'][1]['value'].lower())

    driver.execute_script(f'document.test.tsubject.selectedIndex = {subject_index};')
    driver.execute_script('change1(document.test.tsubject.selectedIndex);')

    all_books = selenium.webdriver.remote.webelement.WebElement = driver.find_element(By.NAME, "tbook")

    return list({discord.app_commands.Choice(name=all_books[i], value=str(i)) for i in range(all_books)})






