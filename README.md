Lang Chain is a open source framework for building application powered by LLMs. 

## Lang Chain Components:
### Model: 
- **Why:** Since there are many LLMs available and each of them provide slightly different API structure for calling. **No standard way of APIs**
- **Solution:** Common/Standard Interface. 
- **Def:** Core Interface through which application interact with AI (LLMs).
- Different API -> Different Interface/Code
- **Standard Interface and code.** 
![Architecture Diagram](assets\LangChain_model.png)

#### Code: 
1. Closed Source LLMs: 
	1. API keys (load_dotenv). 
	2. Initialization (Use prebuild class in langchain). 
	3. Invoke
	4. Response.content 
2. Hugging face Open Source models - Locally run or using API
	1. API key (load_dotenv).
	2. Hugging Face interface - HuggingFaceEndpoint
	3. Initialize the model - ChatHuggingFace
	4. Invoke
	5. Response

### Prompt: 
- Prompt Template: 
	- A **PromptTemplate** in LangChain is a structured way to create prompts dynamically by inserting variables into predefined templates, Instead of hardcoding prompts. 
	- PromptTemplate allows you to define placeholder that can be filled in *runtime* with different input. 
	- Why to use it: 
		- Default validation 
		- Reusable - Create separate python file for **PromptTemplate** and **save in json**
		- LangChain Ecosystem - Can be used with **chains**
- Topics: 
	- Messages - **SystemMessage, AImessage, HumanMessage.**

![Prompts Langchain](assets\LangChain_prompts.png)

#### Code : 
1. Create Template using **PromptTemplate()**
2. Fill the placeholder using **template.invoke()**
3. This two steps will first set the template along with the placeholders and invoke will give the prompt. 
4. Pass the prompt to **model.invoke(prompt)**

#### Why we need: 
1. **PromptTemplates:** To make the prompt dynamic and also some extra features such as: Reuseable, Validation and Align with the langChain Ecosystem. 
2. **ChatPromptTemplates**: To have a history of Chat, while specifying which message is sent by whom. 
### Output Structure: 
- System to system communication, useful in AI agents systems
-  **with_structured_output** ->Data format specify. Dataformats are: 
	- TypeDict - help\suggest the datatype.
	- Pydantic - Type Validation.
	- json_schema
1. Pydantic - 
	1. Pydantic Normal - Inherit from **BaseModel**
	2. Pydantic **Optional** with initialized value.
	3. Coerce try to understand the datatype, and perform conversion if needed. 
	4. Field Functions and Email_address validator

#### Code : 
- with_structured_output(**Dataformats**)
- Data formats = TypedDict, Pydantic, Json


### Output Parsers: 
Help to convert **raw LLM responses** into **structured format** like JSON, CSV, Pydantic model, and more.  
1 **StrOutput parser:**  Output --> String

![Output Langchain](assets\LangChain_output_str.png)

### Chains: 
- Application is made up of small small steps
- Executing them individually is lengthy and time consuming. 
- Through chains we can create pipelines. 