# Kairon-deep-research-project
this is the assignment project given by kairon

```
conda create -n kairon-venv python=3.10 -y
```
```
conda activate kairon-venv
```

```
pip install -r requirements.txt
```

# To use this make .env file and put some of the key in it
```
GOOGLE_API_KEY = ""
TAVILY_API_KEY = ""
```


### Now lets understand the project<br>
research-system/
├── .env file    
├── app.py                   
├── graph.ipynb         
├── main.py
├── README.md                     
└── requirements.txt   
<br>

### first of all i have using a langchain , langgraph and tavilysearch tool to make this project 
### first of all i have created a research agent these will seach the whole internet to find the useful information regarding to our Query and give top 5 answer also i have added to prompt template named reseach_prompt to make sure taht our llm take the user query and give the structured output ( create_tool_calling_agent is used to bind llm , tool and prompt_template)

### Now we have a drafter, which mainly draft the comming data from the agent 1 or reseach agent and make it in proper format that we have given in the class ReseachState and for that i make the Simple chain of llm and draft_prompt 

### one import thing is that we got output in the format of class ResearchState

### Now i have make the different function for both of the Agent's (reseach and draft)

### And with the help of langgraph, make the node of the functions and joined the edge between them ( to know how the edges joined please check graph.ipynb file)

### At the end make the process_question which will take the input and give the output 

### additinlly i have created a streamlit frontend for these with little bit of my knowledge and llm 
<img src="Screenshot 2025-03-05 002948.png"  width="300" />