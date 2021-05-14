# Project for the course 02806 Social Data Analysis and Visualization


This project is the final project for the course 02806 Social Data Analysis and Visualization on DTU.
The topic of the project is *Visualizing child welfare in Barcelona*.

This repo contains all file used throughout the project, as well as notebooks for the data analysis.
The main notebook is the `main_explainer.ipynb`, which goes through the project, how the data was treated, 
how the plots created, and why we did the choices we did. 

## USEFUL LINKS

- [Website](https://barcelona-social-data.netlify.app/)
- [Main notebook](https://barcelona-social-data.netlify.app/main-explainer.html)
- [Website source code](https://github.com/peterampazzo/dtu-02806-website)
- [Dataset](https://opendata-ajuntament.barcelona.cat/data/en/dataset/ebsib-bcn-enquesta-benestar-subjectiu-infancia#fieldDescription)

## DIRECTORY STRUCTURE

```
├── TODO
├── HANDBOOK          
├── README.md                          <- The top-level README for developers using this project
├── main_explainer.ipynb               <- Explainer Notebook
├── data
|   ├── 2017_ebsib_bcn_enquesta_benestar_subjectiu_infancia_barcelona.csv    <- Survey Data (BCN OPEN DATA)
│   ├── zona-urban-audit.geojson                                             <- Neigbourhoods Data (BCN OPEN DATA)
│   └── ...                   <- TBC
├── docs
|   ├── survey-cat.pdf                 <- Original Survey (in catalan)
|   ├── survey-eng.pdf                 <- Translated Survey (in english)
|   ├── Notes-ideas.ipynb              <- Ideas and notes not to forget during analysis (to remove before submission)
│   └── ...   
├── src
│   ├── analysis                       <- Scripts to create exploratory and results
│   └── data                           <- Scripts to download or generate data
│
└── requirements.txt                   <- The requirements file for reproducing the analysis environment
                                        e.g. generated with `pip freeze > requirements.txt`
```


Project collaborators:

- Pietro Rampazzo
- Silvia De Sojo
- Stefan Petrovic
