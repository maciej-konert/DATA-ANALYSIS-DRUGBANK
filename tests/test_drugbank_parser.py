import xmltodict
import pytest
from Main import (
    get_id,
    get_food_interactions,
    get_synonyms,
    get_no_pathways,
    get_targets,
    get_genatlas_id,
    parse_drug_status,
    parse_drug_data,
    parse_drug_interactions,
    parse_gene_drug_product,
)

# Sample XML data for testing
sample_drug_xml = """
<drugbank>
    <drug>
        <drugbank-id primary="true">DB00001</drugbank-id>
        <food-interactions>
            <interaction>Avoid alcohol.</interaction>
            <interaction>Take with food.</interaction>
        </food-interactions>
        <synonyms>
            <synonym>Acetylsalicylic Acid</synonym>
            <synonym>Aspirin</synonym>
        </synonyms>
        <pathways>
            <pathway>
                <name>Metabolism Pathway</name>
            </pathway>
            <pathway>
                <name>Inflammation Pathway</name>
            </pathway>
        </pathways>
        <targets>
            <target>
                <name>COX-1</name>
            </target>
            <target>
                <name>COX-2</name>
            </target>
        </targets>
        <external-identifiers>
            <external-identifier>
                <resource>GenAtlas</resource>
                <identifier>GA12345</identifier>
            </external-identifier>
        </external-identifiers>
        <groups>
            <group>approved</group>
            <group>investigational</group>
        </groups>
    </drug>
</drugbank>
"""

@pytest.fixture
def parsed_sample_drug():
    """Parse the sample XML and return the drug dictionary."""
    data_dict = xmltodict.parse(sample_drug_xml)
    return data_dict["drugbank"]["drug"]

def test_get_id(parsed_sample_drug):
    assert get_id(parsed_sample_drug) == "DB00001"

def test_get_food_interactions(parsed_sample_drug):
    assert get_food_interactions(parsed_sample_drug) == [
        ["Avoid alcohol.",
        "Take with food."]
    ]

def test_get_synonyms(parsed_sample_drug):
    assert get_synonyms(parsed_sample_drug) == ["Acetylsalicylic Acid", "Aspirin"]

def test_get_no_pathways(parsed_sample_drug):
    assert get_no_pathways(parsed_sample_drug) == 2

def test_get_targets(parsed_sample_drug):
    targets = get_targets(parsed_sample_drug)
    assert len(targets) == 2
    assert targets[0]["name"] == "COX-1"
    assert targets[1]["name"] == "COX-2"

def test_get_genatlas_id(parsed_sample_drug):
    external_ids = parsed_sample_drug["external-identifiers"]
    assert get_genatlas_id(external_ids) == "GA12345"

def test_parse_drug_status():
    """Test drug status parsing with different cases."""
    drugs = [
        {"groups": {"group": ["approved", "withdrawn"]}},
        {"groups": {"group": ["approved"]}},
        {"groups": {"group": ["investigational"]}},
        {"groups": {"group": ["experimental", "approved"]}},
        {"groups": {"group": "vet_approved"}},
        {"groups": {}},
    ]
    statuses, approved_not_withdrawn = parse_drug_status(drugs)

    assert statuses["approved"] == 3
    assert statuses["withdrawn"] == 1
    assert statuses["experimental"] == 1
    assert statuses["investigational"] == 1
    assert statuses["vet_approved"] == 1
    assert approved_not_withdrawn == 2
