This simple repo uses allbonds.py script to create an interface with OpenBB for the accompanying allbonds.csv. The 

1) create a python environment for OpenBB. Start the environment
3) within the environment enter: "install pip install openbb-platform-api"
4) whilst in the allbonds folder launch the api by running the following command in the terminal  "openbb-api --app allbonds.py --port 8000"
5) this will generate the widgets.json and serve it to Workspace.
6) check that the api is running, returning the local address & port number (8000)
7) this will look something like this:
      To access this data from OpenBB Workspace, use the link displayed after the application startup completes.
      Chrome is the recommended browser. Other browsers may conflict or require additional configuration.
      Documentation is available at /docs.
      
      INFO:     Started server process [41002]
      INFO:     Waiting for application startup.
      INFO:     Application startup complete.
      INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
      Successfully read 80505 rows from ${{ github.workspace }}/allbonds.csv
      INFO:     127.0.0.1:57403 - "GET /get_all_bonds HTTP/1.1" 200 OK
      INFO:     127.0.0.1:57562 - "OPTIONS /get_all_bonds HTTP/1.1" 200 OK
9) copy the API endpoint (in this case http://127.0.0.1:8000 ) & enter it into OpenBB Apps connection, being sure to name the connection and test it.
10) open the widget by searching for 'allbonds' in the 'widget' repository in OpenBB
