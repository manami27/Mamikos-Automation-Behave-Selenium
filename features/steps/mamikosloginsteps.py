from behave import *
from selenium import webdriver
from time import sleep

@given('launch chrome browser')
def launchBrowser(context):
    context.driver=webdriver.Chrome()
    context.driver.maximize_window()

@when('open Mamikos homepage')
def openHomepage(context):
    context.driver.get('https://mamikos.com/')
    sleep(5)

@when('click on Masuk button')
def clickMasuk(context):
    context.driver.find_element_by_xpath('//*[@id="globalNavbar"]/div/button').click()
    sleep(3)

@when('click on Pencari Kos button')
def clickPencariKos(context):
    context.driver.find_element_by_xpath('//*[@id="loginModal"]/div/div/div[2]/div/div[2]/div/div[1]/p').click()
    sleep(3)

@when('Enter nohp "{nohp}" and password "{pwd}"')
def enterLoginInfo(context,nohp,pwd):
    context.driver.find_element_by_xpath('//*[@id="loginModal"]/div/div/div[2]/div/div[3]/div/p').is_displayed()
    context.driver.find_element_by_xpath('//*[@id="loginModal"]/div/div/div[2]/div/div[3]/div/form/fieldset/div[1]/input').send_keys(nohp)
    context.driver.find_element_by_xpath('//*[@id="loginModal"]/div/div/div[2]/div/div[3]/div/form/fieldset/div[2]/input').send_keys(pwd)

@when('click on Login button')
def clickLogin(context):
    context.driver.find_element_by_xpath('//*[@id="loginModal"]/div/div/div[2]/div/div[3]/div/form/fieldset/button').click()
    sleep(5)
    status=context.driver.find_element_by_xpath('//*[@id="globalNavbar"]/ul/div[3]/div[1]/div/img').is_displayed()
    assert status is True
    
@when('open room detail page')
def openRoomDetailPage(context):
    context.driver.get('https://mamikos.com/room/kost-kabupaten-simeulue-kost-campur-eksklusif-kos-agen-duo-tenant-1#/date')
    sleep(3)

@when('select mulai kos and cara bayar')
def selectMulai(context):
    context.driver.find_element_by_xpath('//*[@id="priceCard"]/div/section[1]/div[2]/section/div[1]').click()
    sleep(5)
    context.driver.find_element_by_xpath('//*[@id="app"]/div/section/div[4]/div/div/div[1]/div[2]/span[6]').click()
    sleep(3)
    context.driver.find_element_by_xpath('//*[@id="app"]/div/section/div[4]/div/div/div[2]/button').click()
    sleep(3)
    context.driver.find_element_by_xpath('//*[@id="priceCard"]/div/section[1]/div[2]/section/div[2]/section[2]/div/div/div[2]/div/div/div[2]/div[22]').click()
    sleep(3)
    context.driver.find_element_by_xpath('//*[@id="priceCard"]/div/section[1]/div[2]/div/div/div/div/div').click()
    showPembayaran=context.driver.find_element_by_xpath('//*[@id="priceCard"]/div/section[2]/div/div/div[2]/p[1]/a').is_displayed()
    assert showPembayaran is True

@when('click on Ajukan Sewa button')
def ajukanSewa(context):
    context.driver.find_element_by_xpath('//*[@id="priceCard"]/div/section[2]/button').click()
    sleep(5)
    nextpage=context.driver.find_element_by_xpath('//*[@id="bookingContainer"]/div[1]/div/div[1]/div[2]/div[1]/h1[1]').is_displayed()
    assert nextpage is True

@when('next to booking summary page')
def bookingSummary(context):
    context.driver.find_element_by_xpath('//*[@id="bookingSummary"]/div[2]/div/div/label/span').click()
    sleep(3)
    context.driver.find_element_by_xpath('//*[@id="bookingSummary"]/div[2]/button').click()
    sleep(5)

@then('booking success confirmation')
def bookingSuccess(context):
    succses=context.driver.find_element_by_xpath('//*[@id="bookingContainer"]/div[3]/div/h4').is_displayed()
    assert succses is True
    sleep(5)
    context.driver.close()


