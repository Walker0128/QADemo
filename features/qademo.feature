Feature: QA Demo
  Idea from this short test is
  to develop the understanding of technical abilities of the candidate
  such as framework design, framework creation, reporting etc.

  Scenario: search on google
    Given search keyword on google
    Then we should get result on ZDnet

  Scenario Outline: list of cloud platform on ZDNet
    Given list of cloud platform on ZDNet
    When we check the list
    Then we should find <name>
    Examples: CloudPlatform
      | name                  | |
      | Amazon Web Services   | |
      | Microsoft Azure       | |
      | Google Cloud Platform | |

  Scenario: view the AWS page
    Given click on View now at AWS button
    Then it opens up a new tab within the same browser
    And it opens up AWS page
    And it lands to the page which shows AWS title
