# carnatic-ragas-2
This repository contains all the data and templates which have been corrected after the Expert Review process
The article generation process and steps such as generating XML and rendering remain same.
However, the key changes to be done during this expert review process:
1. [This](https://iiitaphyd-my.sharepoint.com/:x:/g/personal/v_a_lalitha_research_iiit_ac_in/EQOrTEPmzNZGsps-bSrw8lYBBqnvUkr4lY6MzSS7xG74IA) is sheet shared with subject matter experts for correction of the raga name, arohana, avarohana, etc. Green cells indicate corrected ones, yellow cells indicate ragas with multiple possible arohanas and avarohanas (to be handled separately in the template), and red indicates no resources found for that particular raga  
2. When all the rows are done in the above sheet, get the songs, kritis and varnams in those ragas from ragakb_raw.csv and share it with Ms.Vibha for correction of language level errors in the names of those  
3. Once both subject and language errors are corrected, run is_vakra.py to mark the vakta ragas as 1 and others 0 (Adding a new attribute)
4. Based on yellow cells discussed in step 1, take the sheet containing ragas with multiple arohanas and avarohanas from subject experts, and create new attributes called **alternate_arohana** and **alternate_avarohana**. This will remain NULL for the other ragas which have only one arohana and avarohana
5. Once arohana and avarohana are ready, generate images of the swaras on keyboard following the steps in the [original repository](https://github.com/nikhilpriyatam/wiki_ragas/)  
6. Once all the data is collected, use the updated template (ragas_new.j2) and generate the output XML following the standard procedure for bot generation of articles
7. Send the output XML along with the generated images of keyboard arohana and avarohana for uploading 
