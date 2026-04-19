package com.demo;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.support.ui.ExpectedConditions;

import java.time.Duration;

public class App {

    public static void main(String[] args) {

        WebDriver driver = null;
        boolean testPassed = true;

        try {
            System.out.println("===== TEST STARTED =====");

            // Step 1: Launch Browser
            driver = new ChromeDriver();
            driver.manage().window().maximize();
            System.out.println("STEP 1: Browser Launched - PASS");

            // Step 2: Open Google
            driver.get("https://www.google.com");
            System.out.println("STEP 2: Google Opened - PASS");

            WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));

            // Step 3: Locate Search Box
            WebElement searchBox = wait.until(
                    ExpectedConditions.visibilityOfElementLocated(By.name("q")));
            System.out.println("STEP 3: Search Box Found - PASS");

            // Step 4: Enter Text
            searchBox.sendKeys("Selenium Testing");
            searchBox.submit();
            System.out.println("STEP 4: Search Performed - PASS");

            // Step 5: Verify Title
            wait.until(ExpectedConditions.titleContains("Selenium"));

            String title = driver.getTitle();

            if (title.contains("Selenium")) {
                System.out.println("STEP 5: Title Verification - PASS");
            } else {
                System.out.println("STEP 5: Title Verification - FAIL");
                testPassed = false;
            }

        } catch (Exception e) {
            testPassed = false;
            System.out.println("ERROR OCCURRED: " + e.getMessage());
            e.printStackTrace();
        } finally {

            if (driver != null) {
                driver.quit();
                System.out.println("Browser Closed");
            }

            System.out.println("===== FINAL RESULT =====");

            if (testPassed) {
                System.out.println("TEST RESULT: PASS");
            } else {
                System.out.println("TEST RESULT: FAIL");
            }
        }
    }
}