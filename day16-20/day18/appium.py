from appium import webdriver

desired_caps = {}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='4.2'
desired_caps['deviceName']='Android Emulator'
desired_caps['appPackage']='com.android.calculator2'
desired_caps['appActivity']='.Calculator'

driver= webdriver.Remote('http://loaclhost:4723/wd/hub',desired_caps)