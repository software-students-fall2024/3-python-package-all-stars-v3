import pytest
from src.pyroasts import roasts

class Tests:

    #
    # Test functions
    #

    def test_sanity_check(self):
        """
        Test debugging... making sure that we can run a simple test that always passes.
        Note the use of the example_fixture in the parameter list - any setup and teardown in that fixture will be run before and after this test function executes.
        """
        expected = True
        actual = True
        assert actual == expected, "Expected True to be equal to True!"
        
    #-----------------------------------------------------------------------------------------------------------------------------------

    # Tests for `personal_roast` function
    def test_personal_roast_valid_severity(self):
        assert roasts.personal_roast("alIce", 1) == "Alice, you're like a Monday morning — nobody likes you, we put up with you."
        assert roasts.personal_roast("CHARLIE", 2) == "Charlie, if you were any more average, you'd be a mean."
        assert roasts.personal_roast("bob", 3) == "Bob, I'd explain how awful you are, but it's more fun to watch you figure it out."
        assert roasts.personal_roast("DIanA", 4) == "Diana, you're the reason we can't have nice things."
        assert roasts.personal_roast("eVan", 5) == "Evan, even your reflection is disappointed when it sees you."
        
    def test_personal_roast_invalid_severity(self):
        assert roasts.personal_roast("Charlie", 6) == "Charlie, you're so bland that even a salt shaker thinks you're boring."
        assert roasts.personal_roast("David", 0) == "David, you're so bland that even a salt shaker thinks you're boring."
        assert roasts.personal_roast("Evan", "hello world") == "Evan, you're so bland that even a salt shaker thinks you're boring."
        
    def test_personal_roast_edge_cases(self):
        assert roasts.personal_roast("", 1) == ", you're like a Monday morning — nobody likes you, we put up with you."
        assert roasts.personal_roast("Eve", -1) == "Eve, you're so bland that even a salt shaker thinks you're boring."

    #-----------------------------------------------------------------------------------------------------------------------------------

    # Tests for `skill_roast` function
    def test_skill_roast_valid_sarcasm_level(self):
        assert roasts.skill_roast("cooking", 1) == "Your cooking skills are like a WiFi signal in the middle of nowhere — nonexistent."
        assert roasts.skill_roast("wRiTiNg", 2) == "Writing... You're joking right?"
        assert roasts.skill_roast("DANCING", 3) == "I've seen toddlers with better dancing skills than you... and they can't even talk."

    def test_skill_roast_invalid_sarcasm_level(self):
        assert roasts.skill_roast("singing", 5) == "Your singing skills are a whole new level of disappointment."
        assert roasts.skill_roast("coding", 0) == "Your coding skills are a whole new level of disappointment."
        assert roasts.skill_roast("driving", "hello world") == "Your driving skills are a whole new level of disappointment."
        
    def test_skill_roast_edge_cases(self):
        assert roasts.skill_roast("", 2) == "... You're joking right?"
        assert roasts.skill_roast("painting", -1) == "Your painting skills are a whole new level of disappointment."

    #-----------------------------------------------------------------------------------------------------------------------------------

    # Tests for `comparison_roast` function
    def test_comparison_roast_valid_input(self):
        result = roasts.comparison_roast("mac", "windows")
        assert result in [
            "Mac instead of windows? I'd rather sit on a cactus.",
            "Mac over windows? I'd rather star in a documentary called 'How Far Can the Human Body be Stretched'.",
            "Mac over windows? I'd rather step on a LEGO."
        ]

    def test_comparison_roast_capitalized_input(self):
        result = roasts.comparison_roast("APPLES", "ORANGES")
        assert result in [
            "Apples instead of oranges? I'd rather sit on a cactus.",
            "Apples over oranges? I'd rather star in a documentary called 'How Far Can the Human Body be Stretched'.",
            "Apples over oranges? I'd rather step on a LEGO."
        ]

    def test_comparison_roast_empty_strings(self):
        result = roasts.comparison_roast("", "")
        assert result in [
            " instead of ? I'd rather sit on a cactus.",
            " over ? I'd rather star in a documentary called 'How Far Can the Human Body be Stretched'.",
            " over ? I'd rather step on a LEGO."
        ]

    #-----------------------------------------------------------------------------------------------------------------------------------

    # Tests for `advice_roast` function
    def test_advice_roast_valid_sarcasm_level(self):
        assert roasts.advice_roast("skydiving", 1) == "Trying to learn skydiving? Just keep doing the bare minimum, I'm sure it'll work out... somehow."
        assert roasts.advice_roast("dRivING", 2) == "Your attempt at driving is so inspiring, it's a shame nobody's watching."
        assert roasts.advice_roast("EXERCISING", 3) == "Maybe if you spent half as much time on exercising as you do scrolling on social media, you'd actually get somewhere."

    def test_advice_roast_invalid_sarcasm_level(self):
        assert roasts.advice_roast("cooking", 4) == "You call that effort in cooking? I've seen potatoes put in more work."
        assert roasts.advice_roast("writing", 0) == "You call that effort in writing? I've seen potatoes put in more work."
        assert roasts.advice_roast("biking", "hello_world") == "You call that effort in biking? I've seen potatoes put in more work."
        
    def test_advice_roast_edge_cases(self):
        assert roasts.advice_roast("", 2) == "Your attempt at  is so inspiring, it's a shame nobody's watching."
        assert roasts.advice_roast("gardening", -1) == "You call that effort in gardening? I've seen potatoes put in more work."