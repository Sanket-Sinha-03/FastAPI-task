Install the packages in requirements.txt file
Copy all files to a desired location
Open terminal at this location and run the following commands
1.python myapi.py
2.uvicorn myapi:app --reload (This command sets up the server)
On correct execution the terminal prints the address and port at which the server is running copy this address and add "/docs" and run this address on the browser
You can now test the task.