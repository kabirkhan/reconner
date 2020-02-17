import pytest
from nersights.validation import fix_annotations_format


@pytest.fixture()
def messy_data():
    return [
        {
            "text": "Denver is a city.",
            "spans": [
                {
                    "start": 0,
                    "end": 6,
                    "label": "GPE"
                }
            ],
            "meta": "Cities Data"
        }
    ] 

def test_fix_annotations_format(messy_data):
    fixed_data = fix_annotations_format(messy_data)

    assert fixed_data[0]["spans"][0]['text'] == "Denver"
    assert fixed_data[0]["meta"] == {
        "source": "Cities Data"
    }
