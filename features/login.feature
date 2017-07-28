Feature: Login

Background:
Given I am on Login Page

Scenario:  Assert Home Screen Title
    When I fill the email "tonho@mail.com"
    When I fill the fill password "tonhotonho"
    When I click on login button
