import discord
from discord.ext import commands
from discord import app_commands
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium

from backend import log, embed_template, error_template, get_books, get_classes, get_subjects, driver


class Example(commands.Cog):
    def __init__(self, client):
        self.client = client


    # Use @command.Cog.listener() for an event-listener (on_message, on_ready, etc.)
    @commands.Cog.listener()
    async def on_ready(self):
        print("helo")
        await self.client.tree.sync()


    @app_commands.command(name='textbook')
    @app_commands.autocomplete(grade=get_classes)
    @app_commands.autocomplete(subject=get_subjects)
    @app_commands.autocomplete(book=get_books)
    async def textbook(self, interaction, grade: str, subject: str, book: str):
            
        driver.get("https://ncert.nic.in/textbook.php")

        all_classes = selenium.webdriver.remote.webelement.WebElement = driver.find_element(By.NAME, "tclass")
        driver.execute_script(f'document.test.tclass.selectedIndex = {grade};')
        driver.execute_script('change();')

        all_subjects = selenium.webdriver.remote.webelement.WebElement = driver.find_element(By.NAME, "tsubject")
        driver.execute_script(f'document.test.tsubject.selectedIndex = {subject};')
        driver.execute_script('change1(document.test.tsubject.selectedIndex);')

        all_books = selenium.webdriver.remote.webelement.WebElement = driver.find_element(By.NAME, "tbook")
        driver.execute_script(f'document.test.tbook.selectedIndex = {book};')

        out = driver.execute_script('return document.test.tbook.options[document.test.tbook.options.selectedIndex].value;')
        print(out)
        


        await interaction.followup.send(out)

    
async def setup(client):
    # Here, `Example` is the name of the class
    await client.add_cog(Example(client))
