from brownie import AdvancedCollectible, network
from scripts.helpful_scripts import get_breed
from metadata.sample_metadata import metadata_template
from pathlib import Path
import json

def main():
    advanced_collectible = AdvancedCollectible[-1]
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(f"You have created {number_of_advanced_collectibles} collectibles")
    for token_id in range(number_of_advanced_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        metadata_file_name = (
            f".metadata/{network.show_active()}/{token_id}-{breed}.json"
        )
        collectible_metadata = metadata_template
        print(metadata_file_name)
        if Path(metadata_file_name).exists():
            print(f"Metadata file {metadata_file_name} already exists! Delete it to overwrite it.")
        else:
            print(f"Creating metadata file {metadata_file_name}")
            collectible_metadata["name"] = breed
            collectible_metadata["description"] = f"An adorable {breed} pup!"
            image_path = "./img/" + breed.lower().replace("_", "-") + ".png"
            collectible_metadata["image"] = image_uri
            with open(metadata_file_name, "w") as file:
                json.dump(collectible_metadata, file)

def upload_to_ipfs():
    with Path(filepath).open("rb") as fp: # Open the file 'filepath' in binary mode. We want to open it in binary mode because we want to read the bytes of the file.
        image_binary = fp.read() # Read the contents of the file into a string