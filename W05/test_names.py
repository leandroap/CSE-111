from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("Bruce", "Lee") == "Lee; Bruce"
    assert make_full_name("Marie", "Olivier-George") == "Olivier-George; Marie"
    assert make_full_name("George", "Washington") == "Washington; George"

def test_extract_family_name():
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Bruce; Lee") == "Bruce"
    assert extract_family_name("Olivier-George; Marie") == "Olivier-George"
    assert extract_family_name("Washington; George") == "Washington"

def test_extract_given_name():
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Bruce; Lee") == "Lee"
    assert extract_given_name("Olivier-George; Marie") == "Marie"
    assert extract_given_name("Washington; George") == "George"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])

