# Enhanced openai_conversation for Home Assistant
This is an enhanced version of the openai_conversation component for Home Assistant. 

After replacing the original version, when adding a service, you can input the base_url freely, which is the API endpoint for your desired AI large model.



How to use?

-- Remove the openai_conversation from the components directory in Home Assistant, download the openai_conversation from this repository, and replace it with the entire directory.

For docker:
1. delete the old one:
   a. enter into the docker:

   docker exec -it <Docker's name or ID> bash
   
   rm  -rf /usr/src/homeassistant/homeassistant/components/openai_conversation


3. exit from the docker bash, copy the new one:
   
   docker cp openai_conversation/ <Docker's name or ID>:/usr/src/homeassistant/homeassistant/components/


4. restart the docker
