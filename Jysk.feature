Feature: Checking search
Scenario: Check count of search results
Given website "http://www.jysk.ua"
Then set text for search 'RYSLINGE'
Then push search button
Then check count of results = '8'

Scenario: Check header after first of search result is clicked
Given website "http://www.jysk.ua"
Then set text for search 'RYSLINGE'
Then push search button
Then click first search item
Then check if header equals clicked search item 'Стіл RYSLINGE + 4 стільці RYSLINGE'

Scenario: Check page description
Given website page Stilci
Then check that description text equals 'в комплекті з 2 додатковими "крилами"'

Scenario: Check feedback count
Given website page Stilci
Then check feedback count equals '4 відгуків'

Scenario: Check feedback count on Feedback tab
Given website page Stilci
When I click Feedback tab
Then feedback count should also equal '4 відгуків'

Scenario: Create feedback
Given website page Stilci
When I click Feedback tab
Then I want to send feedback
Then I set rating
Then I set title 'test title'
Then I set feedback 'It is a test feedback'
Then I set my name 'Myroslava'
Then I set my age '25-34'
Then I set my sex 'Жінка'
Then I set City 'Chernivtsi'
Then I set my email 'test@email.com'
When all fields are filled I click button Send Feedback
Then I need to check that Feedback window is not closed
And required checkbox for agreements is red