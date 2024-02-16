import json
import sys

markdown_file = sys.argv[1]

with open(markdown_file, 'r') as file:
    markdown = file.read()

markdown = markdown.replace("|", "").strip()
sections = markdown.split("\n### ")

json_object = {}
json_object["config"] = {}

for section in sections:
    lines = section.split("\n")
    title = lines[0].strip("# ").strip()
    content = "\n".join(lines[1:]).strip()

    if title == "Environment to export":
        json_object["config"]["environmentToExport"] = content
    elif title == "Export all Integrations":
        json_object["config"]["exportAllIntegrations"] = content.lower() == "yes"
    elif title == "Error handling":
        json_object["config"]["errorHandling"] = content.lower() == "yes"
    elif title == "Revert on error":
        json_object["config"]["revertOnError"] = content.lower() == "yes"
    elif title == "Revert release":
        json_object["config"]["revertRelease"] = content
    elif title == "Environment to deploy":   
        json_object["config"]["environmentToDeploy"] = content
    elif title == "Repository releases":
        json_object["config"]["repositoryReleases"] = content
    elif title == "Environment to release":   
        json_object["config"]["environmentToRelease"] = content    
    elif title == "Configuration":
        # Parse the content as a JSON object
        integrations_start = content.find('"integrations":')
        atp_start = content.find('"atp":')

        integrations_end = content.find(']', integrations_start) + 1
        atp_end = content.find(']', atp_start) + 1

        integrations_json = content[integrations_start:integrations_end]
        atp_json = content[atp_start:atp_end]

        integrations_json = "{" + integrations_json + "}"
        atp_json = "{" + atp_json + "}"

        integrations = json.loads(integrations_json)
        atp = json.loads(atp_json)

        json_object["integrations"] = integrations["integrations"]
        json_object["atp"] = atp["atp"]

print(json.dumps(json_object, indent=2))