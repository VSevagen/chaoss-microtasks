## Microtask-2

Execute micro-mordred to collect, enrich and visualize data from Git repositories.

### Steps

1. Run **docker-compose up** to start Kibiter and ElasticSearch.
2. Run **micro.py --raw --enrich --cfg ./setup.cfg --backends git** as shown in the Getting-Started file.
3. Run **micro.py --panels --cfg ./setup.cfg**

## Issues Faced

1. Run into the empty index issue. Solved it by disabling **latest_items** as shown in the Getting-Started file
2. Ran into [Issue#274](https://github.com/chaoss/grimoirelab/issues/274) and used the solution provided.

Here is a demo

![MicroMordred Demo](MicroMordred.gif)
