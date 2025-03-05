# Enhanced openai_conversation for Home Assistant
This is an enhanced version of the openai_conversation component for Home Assistant. 
After replacing the original version, when adding a service, you can input the base_url freely, which is the API endpoint for your desired AI large model.

How to use?

-- Remove the openai_conversation from the components directory in Home Assistant, download the openai_conversation from this repository, and replace it with the entire directory.

For docker:
1. delete the old one:
docker rm  home-assistant:/usr/src/homeassistant/homeassistant/components/testtesttest

2. copy the new one:
docker cp openai_conversation/ home-assistant:/usr/src/homeassistant/homeassistant/components/

3. restart the docker
