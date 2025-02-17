# %%
import xmltodict
import random

file_path = "../drugbank_partial.xml"
output_file = "drugbank_partial_and_generated.xml"
def generate_random_drugs(file_path, output_file, no_drugs):
    with open(file_path, "r", encoding="utf-8") as file:
        data_dict = xmltodict.parse(file.read())

    drugs = data_dict["drugbank"]["drug"]

    with open(output_file, "w", encoding="utf-8") as file:
        file.write('<?xml version="1.0" encoding="utf-8"?>\n')
        file.write('<drugbank>\n')

        for drug in drugs:
            file.write(xmltodict.unparse({"drug": drug}, pretty=True, full_document=False))

        start_id = 101
        for i in range(no_drugs):
            base_drug = random.choice(drugs)
            synthetic_drug = base_drug.copy()
            synthetic_drug["drugbank-id"] = f"DB{str(start_id + i).zfill(5)}"

            file.write(xmltodict.unparse({"drug": synthetic_drug}, pretty=True, full_document=False))

        file.write('\n')
        file.write('</drugbank>\n')
        print(f"Database saved to {output_file}")

generate_random_drugs(file_path, output_file, 2000)


# %%
