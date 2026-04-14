from appium import webdriver
from appium.options.common import AppiumOptions
import time

def test_mobile_camera():
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": "AndroidDevice",
        "appPackage": "com.android.camera2", # Package name varies by OEM
        "appActivity": "com.android.camera.CameraLauncher"
    })

    driver = webdriver.Remote("http://localhost:4723", options=options)

    try:
        # Wait for camera to load
        time.sleep(2)
        
        # Locate the Shutter/Capture button (ID varies by device)
        shutter_button = driver.find_element(by="accessibility id", value="Shutter")
        shutter_button.click()
        print("Photo taken successfully!")
        
        time.sleep(2)
    finally:
        driver.quit()

# Note: Requires 'pip install Appium-Python-Client